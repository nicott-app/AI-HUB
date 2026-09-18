import os
import requests
import streamlit as st

class AuthService:
    """Servicio de autenticación mediante la API REST de Firebase Identity Toolkit."""
    
    _BASE_URL = "https://identitytoolkit.googleapis.com/v1/accounts"
    
    def __init__(self):
        # 1. Intentar desde st.secrets
        self.api_key = None
        try:
            self.api_key = st.secrets.get("FIREBASE_WEB_API_KEY")
        except Exception:
            pass
            
        # 2. Fallback a variable de entorno
        if not self.api_key:
            self.api_key = os.getenv("FIREBASE_WEB_API_KEY")
            
        # 3. Fallback directo (Web API Key es pública por diseño en Firebase)
        if not self.api_key:
            self.api_key = "AIzaSyD8ZFp_ooUO7vY-sTXdX3vccMh7QNPyrUI"
            
        if not self.api_key:
            raise ValueError("No se ha encontrado FIREBASE_WEB_API_KEY en la configuración.")

    def _make_request(self, endpoint: str, payload: dict) -> dict:
        url = f"{self._BASE_URL}:{endpoint}?key={self.api_key}"
        response = requests.post(url, json=payload)
        data = response.json()
        
        if not response.ok:
            error_msg = data.get("error", {}).get("message", "Error desconocido de autenticación")
            raise Exception(self._translate_firebase_error(error_msg))
            
        return data

    def sign_in(self, email: str, password: str) -> dict:
        """Inicia sesión con correo y contraseña. Devuelve info del usuario."""
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        data = self._make_request("signInWithPassword", payload)
        
        # Guardar en sesión
        st.session_state.user = {
            "uid": data["localId"],
            "email": data["email"],
            "token": data["idToken"]
        }
        return st.session_state.user

    def sign_up(self, email: str, password: str) -> dict:
        """Registra un nuevo usuario con correo y contraseña."""
        payload = {
            "email": email,
            "password": password,
            "returnSecureToken": True
        }
        data = self._make_request("signUp", payload)
        
        st.session_state.user = {
            "uid": data["localId"],
            "email": data["email"],
            "token": data["idToken"]
        }
        return st.session_state.user

    def log_out(self):
        """Cierra sesión eliminando el usuario del estado."""
        if "user" in st.session_state:
            del st.session_state["user"]

    def _translate_firebase_error(self, error_msg: str) -> str:
        """Traduce errores comunes de Firebase al español."""
        translations = {
            "EMAIL_NOT_FOUND": "No existe ninguna cuenta con este correo.",
            "INVALID_PASSWORD": "La contraseña es incorrecta.",
            "USER_DISABLED": "Esta cuenta ha sido deshabilitada.",
            "EMAIL_EXISTS": "Ya existe una cuenta con este correo.",
            "WEAK_PASSWORD": "La contraseña debe tener al menos 6 caracteres.",
            "INVALID_EMAIL": "El formato del correo electrónico no es válido."
        }
        if "INVALID_LOGIN_CREDENTIALS" in error_msg:
            return "Credenciales incorrectas. Revisa el correo o la contraseña."
            
        for key, value in translations.items():
            if key in error_msg:
                return value
        return error_msg
