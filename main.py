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
    "🧠 Generador de Casos de Uso IA": "ai_usecase",
    "📋 Canvas de Proyecto IA": "ai_canvas",
    "🎯 Generador de OKRs": "okr",
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
        
        /* ─── ESTILOS DEL MENÚ DE NAVEGACIÓN (st.radio) ─── */
        /* Ocultar el círculo nativo del radio button */
        div[data-testid="stRadio"] div[role="radiogroup"] label > div:first-child {
            display: none !important;
        }
        /* Estilo base para las opciones del menú */
        div[data-testid="stRadio"] div[role="radiogroup"] label {
            padding: 0.6rem 1rem;
            border-radius: 8px;
            margin-bottom: 0.2rem;
            background-color: transparent;
            transition: all 0.2s ease;
            cursor: pointer;
        }
        /* Efecto hover */
        div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
            background-color: #f3f4f6;
        }
        /* Estilo para la opción activa (usando :has) */
        div[data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) {
            background-color: #f3e8ff;
        }
        div[data-testid="stRadio"] div[role="radiogroup"] label:has(input:checked) p {
            color: #7c3aed !important;
            font-weight: 700 !important;
        }

        /* ─── ESTILO BOTONES PRINCIPALES ─── */
        button[kind="primary"] {
            background: linear-gradient(90deg, #7c3aed, #ea580c) !important;
            border: none !important;
            border-radius: 8px !important;
            color: white !important;
            font-weight: 600 !important;
            transition: opacity 0.2s !important;
        }
        button[kind="primary"]:hover {
            opacity: 0.9 !important;
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
            width: 100%;
            height: 310px; /* ALTURA FIJA ESTRICTA */
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
            padding: 1.8rem 1.5rem;
            flex-grow: 1;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            height: 100%;
        }
        .card-icon {
            font-size: 3rem;
            margin-bottom: 0.5rem;
        }
        .card-title {
            font-size: 1.25rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            margin-top: 0;
            height: 3.5rem; /* ALTURA FIJA: para 2 líneas */
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .title-purple { color: #7c3aed; }
        .title-orange { color: #ea580c; }
        .card-desc {
            color: #1f2937;
            font-size: 0.92rem;
            line-height: 1.4;
            text-align: left;
            margin: 0;
            height: 5.5rem; /* ALTURA FIJA: para 4 líneas */
            overflow: hidden;
        }
        .card-footer {
            background: #f9fafb;
            border-top: 1px solid #e5e7eb;
            padding: 1rem;
            font-size: 0.85rem;
            color: #6b7280;
            text-align: center;
            font-weight: 500;
            margin-top: auto;
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

        # Inicializar estado si no existe
        page_keys = list(PAGES.keys())
        if "current_page" not in st.session_state:
            st.session_state.current_page = page_keys[0]

        try:
            current_idx = page_keys.index(st.session_state.current_page)
        except ValueError:
            current_idx = 0

        # Navegación con radio buttons (sin atarlo directamente a la sesión)
        selected_page = st.radio(
            label="",
            options=page_keys,
            index=current_idx,
            label_visibility="collapsed"
        )

        if selected_page != st.session_state.current_page:
            st.session_state.current_page = selected_page
            st.rerun()

        st.markdown('<hr class="nav-divider">', unsafe_allow_html=True)

    return PAGES[st.session_state.current_page]


def change_page(new_page: str):
    st.session_state.current_page = new_page

def render_home():
    # Renderizamos solo la cabecera en un string HTML
    html_header = """<div class="home-container" style="padding-bottom: 0;">
<h1 class="home-title">Bienvenido a Pragma AI Hub</h1>
<p class="home-subtitle" style="margin-bottom: 1.5rem;">Tu espacio de trabajo para la gestión ágil potenciada por Inteligencia Artificial.</p>
</div>"""
    st.markdown(html_header, unsafe_allow_html=True)
    
    # Renderizamos las tarjetas en filas (ordenadas lógicamente)
    # Fila 1: Ideación, Definición y Estrategia
    c1, c2, c_okr = st.columns(3, gap="medium")
    with c1:
        st.markdown("""<div class="tool-card" style="width: 100%; min-width: auto; margin-bottom: 1rem;">
<div class="card-content">
<div class="card-icon" style="color: #059669;">🧠</div>
<h2 class="card-title" style="color: #059669; font-size:1.3rem;">Generador de Casos de Uso IA</h2>
<p class="card-desc" style="font-size:0.95rem;">Obtén una lista priorizada de oportunidades de IA, evaluadas por impacto y esfuerzo.</p>
</div>
<div class="card-footer">Ideación Estratégica</div>
</div>""", unsafe_allow_html=True)
        st.button(
            "Abrir Casos de Uso", 
            use_container_width=True, 
            type="primary", 
            on_click=change_page, 
            args=("🧠 Generador de Casos de Uso IA",)
        )
            
    with c2:
        st.markdown("""<div class="tool-card" style="width: 100%; min-width: auto; margin-bottom: 1rem;">
<div class="card-content">
<div class="card-icon" style="color: #2563eb;">📋</div>
<h2 class="card-title" style="color: #2563eb; font-size:1.3rem;">Canvas de Proyecto IA</h2>
<p class="card-desc" style="font-size:0.95rem;">Define un proyecto de IA completo. Genera un documento ejecutivo con métricas, roadmap y ROI.</p>
</div>
<div class="card-footer">Definición Ejecutiva</div>
</div>""", unsafe_allow_html=True)
        st.button(
            "Abrir Canvas", 
            use_container_width=True, 
            type="primary", 
            on_click=change_page, 
            args=("📋 Canvas de Proyecto IA",)
        )

    with c_okr:
        st.markdown("""<div class="tool-card" style="width: 100%; min-width: auto; margin-bottom: 1rem;">
<div class="card-content">
<div class="card-icon" style="color: #db2777;">🎯</div>
<h2 class="card-title" style="color: #db2777; font-size:1.3rem;">Generador de OKRs</h2>
<p class="card-desc" style="font-size:0.95rem;">Traduce tu visión en Objetivos inspiracionales y Key Results medibles y accionables.</p>
</div>
<div class="card-footer">Alineación Estratégica</div>
</div>""", unsafe_allow_html=True)
        st.button(
            "Abrir Generador OKRs", 
            use_container_width=True, 
            type="primary", 
            on_click=change_page, 
            args=("🎯 Generador de OKRs",)
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Fila 2: Desglose y Priorización
    c3, c4 = st.columns(2, gap="large")
    with c3:
        st.markdown("""<div class="tool-card" style="width: 100%; min-width: auto; margin-bottom: 1rem;">
<div class="card-content">
<div class="card-icon" style="color: #7c3aed;">🪓</div>
<h2 class="card-title title-purple">Troceador de Épicas</h2>
<p class="card-desc">Describe una épica y deja que la IA la descomponga automáticamente en historias de usuario listas para el Sprint, con criterios de aceptación.</p>
</div>
<div class="card-footer">Desglose Ágil</div>
</div>""", unsafe_allow_html=True)
        st.button(
            "Abrir Troceador de Épicas", 
            key="btn_breaker",
            use_container_width=True, 
            type="primary", 
            on_click=change_page, 
            args=("🪓 Troceador de Épicas",)
        )
            
    with c4:
        st.markdown("""<div class="tool-card" style="width: 100%; min-width: auto; margin-bottom: 1rem;">
<div class="card-content">
<div class="card-icon" style="color: #ea580c;">📊</div>
<h2 class="card-title title-orange">Priorizador Multipropósito</h2>
<p class="card-desc">Evalúa tu backlog con los frameworks más usados en la industria: RICE, WSJF, MoSCoW, Kano y la Matriz Valor vs. Complejidad.</p>
</div>
<div class="card-footer">Priorización y Estimación</div>
</div>""", unsafe_allow_html=True)
        st.button(
            "Abrir Priorizador Multipropósito", 
            key="btn_prioritizer",
            use_container_width=True, 
            type="primary", 
            on_click=change_page, 
            args=("📊 Priorizador Multipropósito",)
        )


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
    elif page == "ai_usecase":
        from src.ui.ai_usecase_view import render_ai_usecase_generator
        render_ai_usecase_generator()
    elif page == "ai_canvas":
        from src.ui.ai_canvas_view import render_ai_canvas
        render_ai_canvas()
    elif page == "okr":
        from src.ui.okr_view import render_okr_generator
        render_okr_generator()

    # Footer fijo al fondo de la página
    st.markdown(
        '<div class="app-footer">⚡ Pragma AI Hub · v0.5.0 · Powered by Qwen 3 · Firebase Firestore</div>',
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
