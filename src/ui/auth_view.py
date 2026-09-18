import streamlit as st
from src.services.auth_service import AuthService

def render_auth_view():
    st.markdown("""
        <style>
        .auth-container {
            max-width: 400px;
            margin: 0 auto;
            padding: 2rem;
            background: white;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            text-align: center;
        }
        .auth-title {
            font-size: 2rem;
            font-weight: 800;
            background: linear-gradient(90deg, #7c3aed, #ea580c);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }
        .auth-subtitle {
            color: #6b7280;
            margin-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    st.markdown('<div class="auth-title">AI Hub</div>', unsafe_allow_html=True)
    st.markdown('<div class="auth-subtitle">Inicia sesión para acceder a tus proyectos</div>', unsafe_allow_html=True)
    
    # We use a container to visually group the form
    with st.container():
        tab1, tab2 = st.tabs(["Iniciar Sesión", "Registrarse"])
        
        auth_service = AuthService()
        
        with tab1:
            with st.form("login_form"):
                email = st.text_input("Correo electrónico", placeholder="ejemplo@empresa.com")
                password = st.text_input("Contraseña", type="password")
                submitted = st.form_submit_button("Entrar", type="primary", use_container_width=True)
                
                if submitted:
                    if not email or not password:
                        st.error("Por favor, rellena todos los campos.")
                    else:
                        try:
                            auth_service.sign_in(email, password)
                            st.rerun()
                        except Exception as e:
                            st.error(str(e))
                            
        with tab2:
            with st.form("signup_form"):
                reg_email = st.text_input("Correo electrónico", placeholder="ejemplo@empresa.com")
                reg_password = st.text_input("Contraseña", type="password", help="Mínimo 6 caracteres")
                reg_password_confirm = st.text_input("Confirmar Contraseña", type="password")
                reg_submitted = st.form_submit_button("Crear cuenta", type="primary", use_container_width=True)
                
                if reg_submitted:
                    if not reg_email or not reg_password:
                        st.error("Por favor, rellena todos los campos.")
                    elif reg_password != reg_password_confirm:
                        st.error("Las contraseñas no coinciden.")
                    elif len(reg_password) < 6:
                        st.error("La contraseña debe tener al menos 6 caracteres.")
                    else:
                        try:
                            auth_service.sign_up(reg_email, reg_password)
                            st.rerun()
                        except Exception as e:
                            st.error(str(e))
                            
    st.markdown('</div>', unsafe_allow_html=True)
