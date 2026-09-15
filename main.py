"""
Punto de entrada principal para la aplicación Streamlit 'Sprinto AI Hub'.
"""
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# ─── Módulos y Páginas disponibles ─────────────────────────────────────────────
MODULES = {
    "🚀 Sprinto Strategy": [
        {"name": "🏠 Inicio", "id": "home", "icon": "🏠", "desc": "Panel principal y visión general", "status": "active"},
        {"name": "🧠 Generador de Casos de Uso IA", "id": "ai_usecase", "icon": "🧠", "desc": "Obtén una lista priorizada de oportunidades de IA", "status": "active"},
        {"name": "📋 Canvas de Proyecto IA", "id": "ai_canvas", "icon": "📋", "desc": "Define un proyecto de IA completo", "status": "active"},
        {"name": "🎯 Generador de OKRs", "id": "okr", "icon": "🎯", "desc": "Traduce tu visión en OKRs accionables", "status": "active"},
    ],
    "🛠️ Sprinto Delivery": [
        {"name": "🪓 Troceador de Épicas", "id": "epic_breaker", "icon": "🪓", "desc": "Descompón épicas en historias de usuario", "status": "active"},
        {"name": "📊 Priorizador Multipropósito", "id": "prioritizer", "icon": "📊", "desc": "Evalúa tu backlog con frameworks (RICE, WSJF...)", "status": "active"},
        {"name": "🃏 AI Planning Poker", "id": "planning_poker", "icon": "🃏", "desc": "Estima el esfuerzo de las tareas con IA", "status": "active"},
    ],
    "🩺 Sprinto Ops & Quality": [
        {"name": "🩺 Dashboard de Salud", "id": "health_dash", "icon": "🩺", "desc": "Diagnóstico del Sprint en tiempo real", "status": "active"},
        {"name": "🧪 Generador de Pruebas", "id": "qa_gen", "icon": "🧪", "desc": "Gherkin a partir de historias", "status": "active"},
        {"name": "📚 Documentación Automática", "id": "docs_gen", "icon": "📚", "desc": "Redacta Release Notes y manuales", "status": "pending"},
    ]
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
        
        /* ─── ESTILO BOTONES PRINCIPALES Y NAVEGACIÓN ─── */
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
        
        /* Botón de navegación ACTIVO (Primary) en el sidebar - Color tenue */
        section[data-testid="stSidebar"] button[kind="primary"] {
            background: #f3e8ff !important; /* Morado muy claro/tenue */
            color: #7c3aed !important;      /* Texto morado corporativo */
            border: none !important;
            box-shadow: none !important;
            justify-content: flex-start !important;
            padding-left: 1rem !important;
            font-weight: 700 !important;
            min-height: 2.2rem !important;
            padding-top: 0.1rem !important;
            padding-bottom: 0.1rem !important;
        }

        /* Botones de navegación INACTIVOS (Secondary) en el sidebar sin bordes y más compactos */
        section[data-testid="stSidebar"] button[kind="secondary"] {
            border: none !important;
            background: transparent !important;
            box-shadow: none !important;
            justify-content: flex-start !important;
            padding-left: 1rem !important;
            color: #4b5563 !important;
            font-weight: 500 !important;
            min-height: 2.2rem !important;
            padding-top: 0.1rem !important;
            padding-bottom: 0.1rem !important;
        }
        section[data-testid="stSidebar"] div.stButton {
            margin-bottom: -0.5rem !important; /* Reduce el espacio vertical entre botones */
        }
        section[data-testid="stSidebar"] button[kind="secondary"]:hover {
            background: #f3f4f6 !important;
            color: #111827 !important;
        }
        
        /* Eliminar bordes de los expanders (secciones) en el sidebar */
        section[data-testid="stSidebar"] [data-testid="stExpander"] {
            border: none !important;
            box-shadow: none !important;
            background: transparent !important;
        }
        section[data-testid="stSidebar"] [data-testid="stExpander"] > details {
            border: none !important;
        }
        /* Añadir borde de color sutil (estilo ribbon) al título de las secciones */
        section[data-testid="stSidebar"] [data-testid="stExpander"] details summary {
            border-left: 3px solid #7c3aed !important;
            padding-left: 0.75rem !important;
            margin-bottom: 0.2rem !important;
            border-radius: 0 !important;
        }
        
        /* HOME PAGE STYLES */
        .home-container {
            text-align: center;
            padding: 2rem 0 2rem;
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
            margin-bottom: 2rem;
            font-weight: 400;
        }
        .tool-card {
            background: white;
            border: none;
            border-radius: 12px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
            width: 100%;
            height: 250px;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            transition: transform 0.2s, box-shadow 0.2s;
            margin-bottom: 1rem;
        }
        .tool-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        .card-content {
            padding: 1.5rem 1.5rem;
            flex-grow: 1;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            height: 100%;
        }
        .card-icon {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }
        .card-title {
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
            margin-top: 0;
            height: 3rem;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #1f2937;
        }
        .card-desc {
            color: #4b5563;
            font-size: 0.85rem;
            line-height: 1.4;
            text-align: center;
            margin: 0;
            height: 4rem;
            overflow: hidden;
        }
        .card-pending {
            opacity: 0.6;
            background: #f9fafb;
        }
        .badge-pending {
            background: #e5e7eb;
            color: #4b5563;
            font-size: 0.7rem;
            padding: 2px 8px;
            border-radius: 10px;
            font-weight: 600;
            text-transform: uppercase;
            margin-bottom: 5px;
        }
        </style>
    """, unsafe_allow_html=True)


def change_page(new_page: str):
    st.session_state.current_page = new_page

def render_sidebar() -> str:
    """Renderiza la navegación lateral dividida en módulos."""
    with st.sidebar:
        # Cabecera con logo circular ⚡
        st.markdown("""
            <div class="nav-header">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 2px;">
                    <div style="background: linear-gradient(135deg, #7c3aed, #ea580c); border-radius: 50%; width: 34px; height: 34px; display: flex; align-items: center; justify-content: center; color: white; font-weight: 800; font-size: 1.2rem; flex-shrink: 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">⚡</div>
                    <div>
                        <div class="nav-logo">Sprinto AI Hub</div>
                        <div class="nav-subtitle">Intelligent Agile Tooling</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        if "current_page" not in st.session_state:
            st.session_state.current_page = "home"

        for module_name, pages in MODULES.items():
            with st.expander(module_name, expanded=True):
                for page in pages:
                    if page["status"] == "active":
                        # Botones para páginas activas
                        is_active = (st.session_state.current_page == page["id"])
                        btn_type = "primary" if is_active else "secondary"
                        st.button(
                            page["name"],
                            key=f"nav_{page['id']}",
                            use_container_width=True,
                            type=btn_type,
                            on_click=change_page,
                            args=(page["id"],)
                        )
                    else:
                        # Label deshabilitado para las pendientes
                        st.markdown(f"<div style='padding: 0.4rem 1rem; color:#9ca3af; font-size:0.9rem;'>⏳ {page['name']} <i>(Próximamente)</i></div>", unsafe_allow_html=True)

    return st.session_state.current_page


def render_home():
    html_header = """<div class="home-container" style="padding-bottom: 0;">
<h1 class="home-title">Bienvenido a Sprinto AI Hub</h1>
<p class="home-subtitle" style="margin-bottom: 1.5rem;">Tu espacio de trabajo para la gestión ágil potenciada por Inteligencia Artificial.</p>
</div>"""
    st.markdown(html_header, unsafe_allow_html=True)
    
    # Renderizamos las secciones
    for module_name, pages in MODULES.items():
        st.markdown(f"### {module_name}")
        st.markdown("---")
        
        # Filtramos la página de inicio (home) del grid
        module_pages = [p for p in pages if p["id"] != "home"]
        
        cols = st.columns(3, gap="medium")
        for idx, page in enumerate(module_pages):
            col = cols[idx % 3]
            with col:
                is_pending = page["status"] == "pending"
                card_class = "tool-card card-pending" if is_pending else "tool-card"
                badge_html = '<div class="badge-pending">Próximamente</div>' if is_pending else ''
                
                st.markdown(f"""<div class="{card_class}">
<div class="card-content">
{badge_html}
<div class="card-icon">{page["icon"]}</div>
<h2 class="card-title">{page["name"].replace(page["icon"]+' ', '')}</h2>
<p class="card-desc">{page["desc"]}</p>
</div>
</div>""", unsafe_allow_html=True)

                if not is_pending:
                    st.button(
                        f"Abrir {page['name'].replace(page['icon']+' ', '')}", 
                        key=f"home_btn_{page['id']}",
                        use_container_width=True, 
                        type="primary", 
                        on_click=change_page, 
                        args=(page["id"],)
                    )
                else:
                    st.button("En desarrollo", key=f"home_btn_{page['id']}", disabled=True, use_container_width=True)
                    
        st.markdown("<br><br>", unsafe_allow_html=True)


def main() -> None:
    st.set_page_config(
        page_title="Sprinto AI Hub",
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
    elif page == "planning_poker":
        from src.ui.planning_poker_view import render_planning_poker
        render_planning_poker()
    elif page == "health_dash":
        from src.ui.health_dash_view import render_health_dash
        render_health_dash()
    elif page == "qa_gen":
        from src.ui.qa_generator_view import render_qa_generator
        render_qa_generator()
    else:
        st.warning(f"La herramienta '{page}' está en construcción.")

    # Footer fijo al fondo de la página
    st.markdown(
        '<div class="app-footer">⚡ Sprinto AI Hub · v0.6.0 · Modular UI · Powered by Llama 3 & Firestore</div>',
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
