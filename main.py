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
            font-size: 1.4rem;
            font-weight: 800;
            background: linear-gradient(135deg, #5a6fd6 0%, #8b5cf6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -0.5px;
            line-height: 1.1;
        }
        .nav-subtitle {
            font-size: 0.65rem;
            color: #9ca3af;
            margin-top: 3px;
            letter-spacing: 1px;
            text-transform: uppercase;
            font-weight: 600;
        }


        /* Sección label */
        .nav-section-label {
            padding: 1rem 1.5rem 0.4rem;
            font-size: 0.65rem;
            color: #9ca3af;
            letter-spacing: 1.5px;
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
        
        /* HOME PAGE STYLES */
        .home-container {
            text-align: center;
            padding: 2rem 0 4rem;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }
        .home-title {
            font-size: 3.5rem;
            font-weight: 800;
            background: linear-gradient(90deg, #7c3aed, #ea580c);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
            line-height: 1.2;
        }
        .home-subtitle {
            font-size: 1.2rem;
            color: #4b5563;
            margin-bottom: 3.5rem;
            font-weight: 400;
        }
        .cards-container {
            display: flex;
            gap: 2.5rem;
            justify-content: center;
            flex-wrap: wrap;
        }
        .tool-card {
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
            width: 45%;
            min-width: 320px;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .tool-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        .card-content {
            padding: 3rem 2.5rem;
            flex-grow: 1;
            text-align: center;
        }
        .card-icon {
            font-size: 4rem;
            margin-bottom: 1.5rem;
        }
        .card-title {
            font-size: 1.6rem;
            font-weight: 700;
            margin-bottom: 1.2rem;
            margin-top: 0;
        }
        .title-purple { color: #7c3aed; }
        .title-orange { color: #ea580c; }
        .card-desc {
            color: #1f2937;
            font-size: 1.05rem;
            line-height: 1.5;
            text-align: left;
            margin: 0;
        }
        .card-footer {
            background: #f9fafb;
            border-top: 1px solid #e5e7eb;
            padding: 1.2rem;
            font-size: 0.85rem;
            color: #6b7280;
            text-align: center;
            font-weight: 500;
        }
        </style>
    """, unsafe_allow_html=True)


def render_sidebar() -> str:
    """Renderiza la navegación lateral y devuelve la página seleccionada."""
    with st.sidebar:
        # Cabecera con logo circular ⚡
        st.markdown("""
            <div class="nav-header">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 2px;">
                    <div style="background: linear-gradient(135deg, #7c3aed, #ea580c); border-radius: 50%; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 800; font-size: 1.2rem; flex-shrink: 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">⚡</div>
                    <div>
                        <div class="nav-logo">Pragma AI Hub</div>
                        <div class="nav-subtitle">Intelligent Agile Tooling</div>
                    </div>
                </div>
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


import textwrap

def render_home():
    html_content = textwrap.dedent("""
        <div class="home-container">
            <h1 class="home-title">Bienvenido a Pragma AI Hub</h1>
            <p class="home-subtitle">Tu espacio de trabajo para la gestión ágil potenciada por Inteligencia Artificial.</p>
            
            <div class="cards-container">
                <div class="tool-card">
                    <div class="card-content">
                        <div class="card-icon" style="color: #7c3aed;">🪓</div>
                        <h2 class="card-title title-purple">Troceador de Épicas</h2>
                        <p class="card-desc">Describe una épica y deja que Llama 3 la descomponga automáticamente en historias de usuario listas para el Sprint, con criterios de aceptación y story points estimados.</p>
                    </div>
                    <div class="card-footer">Tecnología: Groq · Llama 3.3 70B</div>
                </div>
                
                <div class="tool-card">
                    <div class="card-content">
                        <div class="card-icon" style="color: #ea580c;">📊</div>
                        <h2 class="card-title title-orange">Priorizador Multipropósito</h2>
                        <p class="card-desc">Evalúa tu backlog con los frameworks más usados en la industria: RICE, WSJF, MoSCoW, Kano y la Matriz Valor vs. Complejidad, con scores calculados por IA.</p>
                    </div>
                    <div class="card-footer">Tecnología: Groq · Firebase Firestore</div>
                </div>
            </div>
        </div>
    """)
    st.markdown(html_content, unsafe_allow_html=True)


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
