import streamlit as st
from src.services.auth_service import AuthService

def render_auth_view():
    # Ocultar sidebar y ajustar padding superior
    st.markdown("""<style>
section[data-testid="stSidebar"] { display: none !important; }
footer { display: none !important; }
header { display: none !important; }
.block-container { padding-top: 2rem !important; padding-bottom: 0rem !important; }
div[data-testid="stForm"] { border: none !important; padding: 0 !important; }
</style>""", unsafe_allow_html=True)

    # ── Fila 1: Logo + Título ──
    _, logo_col, _ = st.columns([1.5, 1, 1.5])
    with logo_col:
        st.markdown("""
<div style="text-align: center;">
<div style="display: inline-flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #7c3aed, #ea580c); border-radius: 16px; width: 56px; height: 56px; margin-bottom: 1rem; box-shadow: 0 4px 12px rgba(124, 58, 237, 0.3);">
<span style="font-size: 1.8rem; color: white;">⚡</span>
</div>
<h1 style="font-size: 1.8rem; font-weight: 800; color: #0f172a; margin: 0 0 0.25rem 0; letter-spacing: -0.02em;">Sprinto AI Hub</h1>
<p style="color: #64748b; font-size: 0.95rem; margin: 0; margin-bottom: 1.5rem;">Gestión ágil potenciada por IA</p>
</div>
""", unsafe_allow_html=True)

    # ── Fila 2: Formulario centrado ──
    _, form_col, _ = st.columns([1.3, 1.4, 1.3])
    with form_col:
        tab_login, tab_register = st.tabs(["Iniciar Sesión", "Crear Cuenta"])
        auth = AuthService()

        with tab_login:
            with st.form("login_form", border=False):
                st.text_input("Correo electrónico", placeholder="tu@empresa.com", key="login_email")
                st.text_input("Contraseña", type="password", placeholder="••••••••", key="login_pass")
                
                if st.form_submit_button("Iniciar Sesión", type="primary", use_container_width=True):
                    email = st.session_state.login_email
                    pwd = st.session_state.login_pass
                    if not email or not pwd:
                        st.error("Rellena todos los campos.")
                    else:
                        try:
                            auth.sign_in(email, pwd)
                            st.rerun()
                        except Exception as e:
                            st.error(str(e))

        with tab_register:
            with st.form("signup_form", border=False):
                st.text_input("Correo electrónico", placeholder="tu@empresa.com", key="reg_email")
                st.text_input("Contraseña", type="password", placeholder="Mín. 6 caracteres", key="reg_pass")
                st.text_input("Confirmar contraseña", type="password", placeholder="••••••••", key="reg_pass2")
                
                if st.form_submit_button("Crear Cuenta", type="primary", use_container_width=True):
                    email = st.session_state.reg_email
                    pwd = st.session_state.reg_pass
                    pwd2 = st.session_state.reg_pass2
                    if not email or not pwd:
                        st.error("Rellena todos los campos.")
                    elif pwd != pwd2:
                        st.error("Las contraseñas no coinciden.")
                    elif len(pwd) < 6:
                        st.error("La contraseña debe tener al menos 6 caracteres.")
                    else:
                        try:
                            auth.sign_up(email, pwd)
                            st.rerun()
                        except Exception as e:
                            st.error(str(e))

    # ── Fila 3: Features ──
    _, feat_col, _ = st.columns([1.2, 1.6, 1.2])
    with feat_col:
        st.divider()
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown("##### 🚀")
            st.caption("Desglose de Épicas")
        with c2:
            st.markdown("##### 📝")
            st.caption("QA & Release Notes")
        with c3:
            st.markdown("##### 🎯")
            st.caption("OKRs & Canvas")
        with c4:
            st.markdown("##### 🔒")
            st.caption("Workspace seguro")
