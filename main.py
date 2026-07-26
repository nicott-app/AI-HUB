"""
Punto de entrada principal para la aplicación Streamlit 'Pragma AI Hub'.
"""
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# ─── Páginas disponibles ───────────────────────────────────────────────────────
PAGES = {
    "🏠 Inicio": "home",
    "🪓 Troceador de Épicas": "epic_breaker",
    "📊 Priorizador Multipropósito": "prioritizer",
}

def inject_nav_css():
    st.markdown("""
        <style>
        /* Ocultar elementos nativos innecesarios */
        #MainMenu, footer, header { visibility: hidden; }

        /* Sidebar — fondo claro con borde derecho sutil */
        section[data-testid="stSidebar"] > div:first-child {
            background: #f8f9ff;
            border-right: 1px solid #e2e5f1;
            padding: 0;
        }

        /* Cabecera del sidebar */
        .nav-header {
            padding: 2rem 1.5rem 1.5rem;
            border-bottom: 1px solid #e2e5f1;
            margin-bottom: 0.5rem;
        }
        .nav-logo {
            font-size: 1.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #5a6fd6 0%, #8b5cf6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -0.5px;
        }
        .nav-subtitle {
            font-size: 0.7rem;
            color: #9ca3af;
            margin-top: 3px;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            font-weight: 600;
        }


        /* Sección label */
        .nav-section-label {
            padding: 1rem 1.5rem 0.4rem;
            font-size: 0.65rem;
            color: #9ca3af;
            letter-spacing: 2px;
            text-transform: uppercase;
            font-weight: 700;
        }

        /* Divisor decorativo en el sidebar */
        .nav-divider {
            margin: 1rem 1.5rem 0;
            border: none;
            border-top: 1px solid #e2e5f1;
        }

        /* Footer fijo al fondo de la ventana */
        .app-footer {
            position: fixed;
            bottom: 0;
            left: 0; right: 0;
            padding: 5px 1.5rem;
            font-size: 0.65rem;
            color: #9ca3af;
            text-align: center;
            background: rgba(255,255,255,0.85);
            backdrop-filter: blur(4px);
            border-top: 1px solid #e2e5f1;
            z-index: 999;
        }

        /* Área principal */
        .block-container {
            padding-top: 2rem !important;
            max-width: 1200px;
            padding-bottom: 2rem !important;
        }
        </style>
    """, unsafe_allow_html=True)


def render_sidebar() -> str:
    """Renderiza la navegación lateral y devuelve la página seleccionada."""
    with st.sidebar:
        # Cabecera
        st.markdown("""
            <div class="nav-header">
                <div class="nav-logo">⚡ Pragma AI Hub</div>
                <div class="nav-subtitle">Intelligent Agile Tooling</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="nav-section-label">Herramientas</div>', unsafe_allow_html=True)

        # Navegación con radio buttons estilizados
        page = st.radio(
            label="",
            options=list(PAGES.keys()),
            label_visibility="collapsed",
        )

        st.markdown('<hr class="nav-divider">', unsafe_allow_html=True)

    return PAGES[page]


def render_home():
    st.markdown("## Bienvenido a Pragma AI Hub ⚡")
    st.markdown("Tu espacio de trabajo para la gestión ágil potenciada por Inteligencia Artificial.")
    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="large")
    with c1:
        with st.container(border=True):
            st.markdown("#### 🪓 Troceador de Épicas")
            st.markdown("Describe una épica y deja que Llama 3 la descomponga automáticamente en historias de usuario listas para el Sprint, con criterios de aceptación y story points estimados.")
            st.markdown("**Tecnología:** Groq · Llama 3.3 70B")
    with c2:
        with st.container(border=True):
            st.markdown("#### 📊 Priorizador Multipropósito")
            st.markdown("Evalúa tu backlog con los frameworks más usados en la industria: **RICE, WSJF, MoSCoW, Kano** y la **Matriz Valor vs. Complejidad**, con scores calculados por IA.")
            st.markdown("**Tecnología:** Groq · Firebase Firestore")


def main() -> None:
    st.set_page_config(
        page_title="Pragma AI Hub",
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    inject_nav_css()
    page = render_sidebar()

    if page == "home":
        render_home()
    elif page == "epic_breaker":
        from src.ui.epic_breaker_view import render_epic_breaker
        render_epic_breaker()
    elif page == "prioritizer":
        from src.ui.prioritizer_view import render_prioritizer
        render_prioritizer()

    # Footer fijo al fondo de la página
    st.markdown(
        '<div class="app-footer">⚡ Pragma AI Hub · v0.3.0 · Powered by Llama 3.3 70B · Firebase Firestore</div>',
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
