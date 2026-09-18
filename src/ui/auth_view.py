import streamlit as st
from src.services.auth_service import AuthService

def render_auth_view():
    # CSS mínimo: solo estilos visuales, SIN intentar modificar layout de Streamlit
    st.markdown("""<style>
section[data-testid="stSidebar"] { display: none !important; }
footer { display: none !important; }
.auth-card {
    background: white;
    border-radius: 16px;
    padding: 2rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    border: 1px solid #f1f5f9;
}
.auth-card h3 { text-align: center; font-weight: 800; color: #0f172a; margin-bottom: 0.25rem; }
.auth-card p { text-align: center; color: #64748b; font-size: 0.95rem; }
div[data-testid="stForm"] { border: none !important; padding: 0 !important; }
input {
    border-radius: 8px !important;
    background-color: #f8fafc !important;
    border: 1px solid #e2e8f0 !important;
}
input:focus { background-color: #fff !important; border-color: #7c3aed !important; }
</style>""", unsafe_allow_html=True)

    # Cabecera con Streamlit nativo
    _, col_center, _ = st.columns([1, 2, 1])
    with col_center:
        st.markdown("""
<div style="text-align: center; padding-top: 1rem; padding-bottom: 1rem;">
<div style="display: inline-block; padding: 0.25rem 0.75rem; background: #f3e8ff; color: #7c3aed; border-radius: 9999px; font-size: 0.85rem; font-weight: 600; margin-bottom: 0.75rem;">✨ Suite de Herramientas AI</div>
<h1 style="font-size: 2.8rem; font-weight: 900; line-height: 1.1; color: #0f172a; margin: 0 0 0.5rem 0;">Sprinto <span style="background: linear-gradient(135deg, #7c3aed, #ea580c); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">AI Hub</span></h1>
<p style="font-size: 1.1rem; color: #475569; margin: 0;">Potencia a tu equipo ágil con Inteligencia Artificial</p>
</div>
""", unsafe_allow_html=True)

    # Formulario centrado
    _, col_form, _ = st.columns([1.2, 1.5, 1.2])
    with col_form:
        st.markdown("""
<div class="auth-card">
<h3>Bienvenido de nuevo</h3>
<p>Ingresa tus credenciales para continuar</p>
</div>
""", unsafe_allow_html=True)
    
        tab1, tab2 = st.tabs(["Iniciar Sesión", "Registrarse"])
        auth_service = AuthService()
        
        with tab1:
            with st.form("login_form", border=False):
                email = st.text_input("Correo electrónico", placeholder="ejemplo@empresa.com")
                password = st.text_input("Contraseña", type="password", placeholder="••••••••")
                submitted = st.form_submit_button("Entrar al Hub", type="primary", use_container_width=True)
                
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
            with st.form("signup_form", border=False):
                reg_email = st.text_input("Correo electrónico", placeholder="ejemplo@empresa.com")
                reg_password = st.text_input("Contraseña", type="password", placeholder="Mínimo 6 caracteres")
                reg_password_confirm = st.text_input("Confirmar Contraseña", type="password", placeholder="••••••••")
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

    # Features debajo del formulario
    _, col_feat, _ = st.columns([1, 2, 1])
    with col_feat:
        st.markdown("---")
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown("🚀 **Épicas**")
            st.caption("Desglose automático")
        with c2:
            st.markdown("📝 **QA & Docs**")
            st.caption("Generación inteligente")
        with c3:
            st.markdown("🎯 **OKRs**")
            st.caption("Definición asistida")
        with c4:
            st.markdown("🔒 **Seguro**")
            st.caption("Datos sincronizados")
