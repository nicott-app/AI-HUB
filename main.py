"""
Punto de entrada principal para la aplicación Streamlit 'Sprinto AI Hub'.
"""
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# ─── Módulos y Páginas disponibles ─────────────────────────────────────────────
MODULES = {
    "Sprinto Strategy": [
        {"name": "🧠 Generador de Casos de Uso IA", "id": "ai_usecase", "icon": "🧠", "desc": "Obtén una lista priorizada de oportunidades de IA", "status": "active"},
        {"name": "📋 Canvas de Proyecto IA", "id": "ai_canvas", "icon": "📋", "desc": "Define un proyecto de IA completo", "status": "active"},
        {"name": "🎯 Generador de OKRs", "id": "okr", "icon": "🎯", "desc": "Traduce tu visión en OKRs accionables", "status": "active"},
    ],
    "Sprinto Delivery": [
        {"name": "🪓 Troceador de Épicas", "id": "epic_breaker", "icon": "🪓", "desc": "Descompón épicas en historias de usuario", "status": "active"},
        {"name": "📊 Priorizador Multipropósito", "id": "prioritizer", "icon": "📊", "desc": "Evalúa tu backlog con frameworks (RICE, WSJF...)", "status": "active"},
        {"name": "🃏 AI Planning Poker", "id": "planning_poker", "icon": "🃏", "desc": "Estima el esfuerzo de las tareas con IA", "status": "active"},
    ],
    "Sprinto Ops & Quality": [
        {"name": "🩺 Dashboard de Salud", "id": "health_dash", "icon": "🩺", "desc": "Diagnóstico del Sprint en tiempo real", "status": "active"},
        {"name": "🧪 Generador de Pruebas", "id": "qa_gen", "icon": "🧪", "desc": "Gherkin a partir de historias", "status": "active"},
        {"name": "📚 Documentación Automática", "id": "docs_gen", "icon": "📚", "desc": "Redacta Release Notes y manuales", "status": "active"},
    ]
}

def inject_nav_css():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500;700&display=swap');
        @import url('https://cdn.jsdelivr.net/npm/geist@1.0.0/dist/fonts/geist-sans/style.css');

        /* Aplicar fuentes globales */
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif !important;
        }
        h1, h2, h3, .nav-logo, .home-title, .card-title {
            font-family: 'Geist', 'Inter', sans-serif !important;
        }
        .nav-subtitle, .badge-pending, code {
            font-family: 'JetBrains Mono', monospace !important;
        }

        /* Ocultar elementos nativos innecesarios */
        #MainMenu, footer, header { visibility: hidden; }

        /* Sidebar — fondo claro con borde derecho sutil */
        section[data-testid="stSidebar"] > div:first-child {
            background: #f8f9fc;
            border-right: 1px solid #e2e8f0;
            padding: 0;
        }

        /* Cabecera del sidebar */
        .nav-header {
            padding: 2rem 1.5rem 1.5rem;
            border-bottom: 1px solid #e2e8f0;
            margin-bottom: 0.5rem;
        }
        .nav-logo {
            font-size: 1.4rem;
            font-weight: 800;
            background: linear-gradient(135deg, #006d3e 0%, #16a34a 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            letter-spacing: -0.5px;
            line-height: 1.1;
        }
        .nav-subtitle {
            font-size: 0.65rem;
            color: #94a3b8;
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
            color: #94a3b8;
            text-align: center;
            background: rgba(255,255,255,0.85);
            backdrop-filter: blur(4px);
            border-top: 1px solid #e2e8f0;
            z-index: 999;
            font-family: 'JetBrains Mono', monospace !important;
        }

        /* Área principal */
        .block-container {
            padding-top: 2rem !important;
            max-width: 1200px;
            padding-bottom: 2rem !important;
            background: #f4f5f8;
        }
        
        /* ─── ESTILO BOTONES PRINCIPALES Y NAVEGACIÓN ─── */
        button[kind="primary"] {
            background: #006d3e !important;
            border: 1px solid #00522d !important;
            border-radius: 6px !important;
            color: white !important;
            font-weight: 500 !important;
            transition: background 0.2s !important;
            font-family: 'Inter', sans-serif !important;
        }
        button[kind="primary"]:hover {
            background: #16a34a !important;
            border-color: #16a34a !important;
        }
        
        /* Botón de navegación ACTIVO (Primary) en el sidebar */
        section[data-testid="stSidebar"] button[kind="primary"] {
            background: #86efac !important; /* Primary Container */
            color: #00210f !important;      /* On Primary Fixed */
            border: 1px solid #73db9a !important;
            box-shadow: none !important;
            font-weight: 600 !important;
            min-height: 2.2rem !important;
            padding-top: 0.1rem !important;
            padding-bottom: 0.1rem !important;
        }

        /* Botones de navegación INACTIVOS (Secondary) en el sidebar */
        section[data-testid="stSidebar"] button[kind="secondary"] {
            border: none !important;
            background: transparent !important;
            box-shadow: none !important;
            color: #4b5563 !important;
            font-weight: 500 !important;
            min-height: 2.2rem !important;
            padding-top: 0.1rem !important;
            padding-bottom: 0.1rem !important;
        }
        
        section[data-testid="stSidebar"] button {
            justify-content: center !important;
            padding-left: 0 !important;
        }
        section[data-testid="stSidebar"] button p, 
        section[data-testid="stSidebar"] button div {
            text-align: center !important;
            justify-content: center !important;
        }

        section[data-testid="stSidebar"] [data-testid="stExpander"] button {
            justify-content: flex-start !important;
            padding-left: 1rem !important;
        }
        section[data-testid="stSidebar"] [data-testid="stExpander"] button p, 
        section[data-testid="stSidebar"] [data-testid="stExpander"] button div {
            text-align: left !important;
            justify-content: flex-start !important;
        }

        section[data-testid="stSidebar"] div.stButton {
            margin-bottom: -0.5rem !important;
        }
        section[data-testid="stSidebar"] button[kind="secondary"]:hover {
            background: #e2e8f0 !important;
            color: #111827 !important;
        }
        
        /* Eliminar bordes de los expanders */
        section[data-testid="stSidebar"] [data-testid="stExpander"] {
            border: none !important;
            box-shadow: none !important;
            background: transparent !important;
        }
        section[data-testid="stSidebar"] [data-testid="stExpander"] > details {
            border: none !important;
        }
        /* Añadir borde verde corporativo al título de las secciones */
        section[data-testid="stSidebar"] [data-testid="stExpander"] details summary {
            border-left: 3px solid #006d3e !important;
            padding-left: 0.75rem !important;
            margin-bottom: 0.2rem !important;
            border-radius: 0 !important;
            color: #111827 !important;
            font-family: 'Geist', sans-serif !important;
        }
        
        section[data-testid="stSidebar"] [data-testid="stExpanderDetails"] {
            padding-left: 1rem !important;
            padding-right: 0 !important;
            padding-bottom: 0 !important;
        }
        
        /* HOME PAGE STYLES */
        .home-container {
            text-align: center;
            padding: 2rem 0 2rem;
        }
        .home-title {
            font-size: 3.5rem;
            font-weight: 700;
            color: #111827;
            margin-bottom: 0.5rem;
            line-height: 1.1;
            letter-spacing: -0.03em;
        }
        .home-subtitle {
            font-size: 1.1rem;
            color: #4b5563;
            margin-bottom: 2rem;
            font-weight: 400;
            font-family: 'Inter', sans-serif;
        }
        .tool-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
            width: 100%;
            height: 260px !important;
            display: flex;
            flex-direction: column;
            overflow: hidden;
            transition: border-color 0.2s, box-shadow 0.2s;
            margin-bottom: 1rem;
        }
        .tool-card:hover {
            border-color: #cbd5e1;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        }
        .card-content {
            padding: 1.5rem 1rem 2rem;
            flex-grow: 1;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            height: 100%;
            gap: 0.3rem;
        }
        .card-icon {
            font-size: 2.2rem;
            margin-bottom: 0.1rem;
        }
        .card-title {
            font-size: 0.95rem;
            font-weight: 600;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #111827;
            line-height: 1.3;
        }
        .card-desc {
            color: #4b5563;
            font-size: 0.85rem;
            line-height: 1.4;
            text-align: center;
            margin: 0;
        }
        .card-pending {
            opacity: 0.6;
            background: #f8f9fc;
        }
        .badge-pending {
            background: #e2e8f0;
            color: #4b5563;
            font-size: 0.65rem;
            padding: 2px 8px;
            border-radius: 4px;
            font-weight: 600;
            text-transform: uppercase;
            margin-bottom: 5px;
            font-family: 'JetBrains Mono', monospace;
            border: 1px solid #cbd5e1;
        }
        </style>
    """, unsafe_allow_html=True)


def change_page(new_page: str):
    st.session_state.current_page = new_page

def render_sidebar() -> str:
    """Renderiza la navegación lateral dividida en módulos."""
    with st.sidebar:
        # Cabecera con logo de Sprinto
        st.markdown("""
            <div class="nav-header">
                <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 2px;">
                    <img src="https://sprinto-board.web.app/sprinto-logo.svg" alt="Sprinto Logo" style="width: 34px; height: 34px; object-fit: contain;" />
                    <div>
                        <div class="nav-logo">Sprinto AI Hub</div>
                        <div class="nav-subtitle">Intelligent Agile Tooling</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        if "current_page" not in st.session_state:
            st.session_state.current_page = "home"

        # Botón de Inicio independiente
        is_home_active = (st.session_state.current_page == "home")
        st.button(
            "🏠 Inicio",
            key="nav_home",
            use_container_width=True,
            type="primary" if is_home_active else "secondary",
            on_click=change_page,
            args=("home",)
        )
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

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

        st.markdown("<br><br>", unsafe_allow_html=True)
        # Logout button removed as per user request

    return st.session_state.current_page


def render_home():
    html_header = """<div class="home-container" style="padding-bottom: 0;">
<h1 class="home-title">Bienvenido a Sprinto AI Hub</h1>
<p class="home-subtitle" style="margin-bottom: 1.5rem;">Tu espacio de trabajo para la gestión ágil potenciada por Inteligencia Artificial.</p>
</div>"""
    st.markdown(html_header, unsafe_allow_html=True)
    
    # Renderizamos las secciones
    for module_name, pages in MODULES.items():
        with st.container(border=True):
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
                    
                    st.markdown(f"""
<div class="{card_class}">
<div class="card-content">
{badge_html}
<div class="card-icon">{page["icon"]}</div>
<h2 class="card-title">{page["name"].replace(page["icon"]+' ', '')}</h2>
<p class="card-desc">{page["desc"]}</p>
</div>
</div>
""", unsafe_allow_html=True)

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
            
            st.markdown("<br>", unsafe_allow_html=True)
            
        st.markdown("<br><br>", unsafe_allow_html=True)


def main() -> None:
    st.set_page_config(
        page_title="Sprinto AI Hub",
        page_icon="https://sprinto-board.web.app/sprinto-logo.svg",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Eliminar la página de auth y mostrar el hub directamente
    
    # Mockear un usuario si la app sigue dependiendo de él temporalmente
    if "user" not in st.session_state:
        st.session_state.user = {
            "uid": "OdFBPw4aGLMAK5MVAXX3jyKPJYx1", # El ID de Nicolás que vimos en la DB
            "email": "nicolas@example.com",
            "displayName": "Nicolás Tercero"
        }

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
    elif page == "docs_gen":
        from src.ui.docs_generator_view import render_docs_generator
        render_docs_generator()
    else:
        st.warning(f"La herramienta '{page}' está en construcción.")

    # Footer fijo al fondo de la página
    st.markdown(
        '<div class="app-footer">⚡ Sprinto AI Hub · v0.6.0 · Modular UI · Powered by Llama 3 & Firestore</div>',
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
