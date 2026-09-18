import streamlit as st
from src.services.auth_service import AuthService

def render_auth_view():
    st.markdown("""
        <style>
        /* Ocultar elementos de Streamlit SIN DEJAR HUECO */
        #MainMenu {display: none !important;}
        header {display: none !important;}
        footer {display: none !important;}
        div[data-testid="stHeader"] {display: none !important;}
        div[data-testid="stToolbar"] {display: none !important;}
        div[data-testid="stDecoration"] {display: none !important;}
        
        /* Eliminar todo el padding superior de Streamlit */
        .block-container,
        div[data-testid="stAppViewBlockContainer"],
        div.stMainBlockContainer,
        section[data-testid="stMain"] > div {
            padding-top: 1rem !important;
            margin-top: 0 !important;
            padding-bottom: 0 !important;
            max-width: 1100px !important;
        }
        
        /* Fondo de la página */
        .stApp {
            background-color: #f8fafc;
            background-image: radial-gradient(#e2e8f0 1px, transparent 1px);
            background-size: 20px 20px;
        }
        
        /* Ocultar la sidebar en la landing */
        section[data-testid="stSidebar"] {display: none !important;}

        /* Estilos de la parte de marca (izquierda) */
        .brand-section {
            padding-right: 2rem;
            padding-top: 3rem;
        }
        .brand-badge {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            background: #f3e8ff;
            color: #7c3aed;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 600;
            margin-bottom: 1.5rem;
        }
        .brand-title {
            font-size: 3.2rem;
            font-weight: 900;
            line-height: 1.1;
            color: #0f172a;
            margin-bottom: 1rem;
        }
        .brand-title span {
            background: linear-gradient(135deg, #7c3aed, #ea580c);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .brand-subtitle {
            font-size: 1.15rem;
            color: #475569;
            margin-bottom: 2rem;
            line-height: 1.5;
        }
        .feature-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .feature-list li {
            display: flex;
            align-items: center;
            margin-bottom: 1rem;
            color: #334155;
            font-size: 1.05rem;
            font-weight: 500;
        }
        .feature-icon {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 2rem;
            height: 2rem;
            background: #fff;
            border-radius: 50%;
            margin-right: 1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            color: #7c3aed;
        }

        /* Estilos de la tarjeta de Auth (derecha) */
        .auth-card {
            background: white;
            border-radius: 20px;
            padding: 2.5rem 2rem 2rem 2rem;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01);
            border: 1px solid #f1f5f9;
            margin-top: 2rem;
        }
        
        .auth-header {
            text-align: center;
            margin-bottom: 1rem;
        }
        .auth-header h3 {
            font-size: 1.5rem;
            font-weight: 800;
            color: #0f172a;
            margin: 0 0 0.5rem 0;
        }
        .auth-header p {
            color: #64748b;
            margin: 0;
            font-size: 0.95rem;
        }
        
        /* Refinar inputs y botones de Streamlit */
        div[data-testid="stForm"] {
            border: none !important;
            padding: 0 !important;
        }
        
        div[data-baseweb="tab-list"] {
            gap: 1rem;
            margin-bottom: 1rem;
            justify-content: center;
        }
        div[data-baseweb="tab-list"] button {
            padding-left: 1rem;
            padding-right: 1rem;
            font-weight: 600;
        }
        
        input {
            border-radius: 8px !important;
            background-color: #f8fafc !important;
            padding: 0.75rem 1rem !important;
            border: 1px solid #e2e8f0 !important;
        }
        input:focus {
            background-color: #ffffff !important;
            border-color: #7c3aed !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Layout directo con columnas de Streamlit (sin wrapper div)
    col_brand, col_form = st.columns([1.1, 0.9], gap="large")
    
    with col_brand:
        st.markdown("""
<div class="brand-section">
<div class="brand-badge">✨ Suite de Herramientas AI</div>
<h1 class="brand-title">Sprinto <span>AI Hub</span></h1>
<p class="brand-subtitle">
Transforma tu manera de gestionar el ciclo de vida del software.
Potencia a tu equipo ágil con Inteligencia Artificial.
</p>
<ul class="feature-list">
<li><span class="feature-icon">🚀</span> Desglose automático de Épicas</li>
<li><span class="feature-icon">📝</span> Generación de Casos de QA y Release Notes</li>
<li><span class="feature-icon">🎯</span> Definición de OKRs y Canvas</li>
<li><span class="feature-icon">🔒</span> Sincronización segura con tu Workspace</li>
</ul>
</div>
        """, unsafe_allow_html=True)
        
    with col_form:
        st.markdown("""
<div class="auth-card">
<div class="auth-header">
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
                            
        st.markdown('</div>', unsafe_allow_html=True)
