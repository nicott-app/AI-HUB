"""
Vista del Generador de Casos de Uso de IA.

Guía al usuario a través de un formulario de contexto y le devuelve
una lista priorizada de casos de uso con su análisis de impacto/esfuerzo.
"""
import streamlit as st
from src.data.cache import get_llm_service


# ── Mapas de color para badges ─────────────────────────────────────────────────
_IMPACT_STYLE = {
    "Alto":  ("🟢", "#dcfce7", "#166534"),
    "Medio": ("🟡", "#fef9c3", "#854d0e"),
    "Bajo":  ("🔴", "#fee2e2", "#991b1b"),
}
_EFFORT_STYLE = {
    "Alto":  ("🔴", "#fee2e2", "#991b1b"),
    "Medio": ("🟡", "#fef9c3", "#854d0e"),
    "Bajo":  ("🟢", "#dcfce7", "#166534"),
}
_AI_TYPE_ICONS = {
    "NLP": "💬", "Chatbot": "💬", "NLP / Chatbot": "💬",
    "Computer Vision": "👁️",
    "Forecasting": "📈", "Series Temporales": "📈", "Forecasting / Series Temporales": "📈",
    "Clasificación ML": "🏷️",
    "Automatización RPA": "🤖", "Automatización RPA + IA": "🤖",
    "Generative AI": "✨",
    "Detección de Anomalías": "🔍",
    "Sistemas de Recomendación": "⭐",
}


def _badge(label: str, bg: str, color: str) -> str:
    return (
        f'<span style="background:{bg};color:{color};padding:3px 10px;'
        f'border-radius:12px;font-size:0.78rem;font-weight:600;">{label}</span>'
    )


def _render_use_case_card(uc, rank: int, selectable: bool = False) -> bool:
    """Renderiza una tarjeta enriquecida para un caso de uso.
    Si selectable=True, incluye checkbox y devuelve si está seleccionada.
    """
    impact_icon, impact_bg, impact_color = _IMPACT_STYLE.get(uc.estimated_impact, ("⚪", "#f3f4f6", "#374151"))
    effort_icon, effort_bg, effort_color = _EFFORT_STYLE.get(uc.estimated_effort, ("⚪", "#f3f4f6", "#374151"))
    ai_icon = next((v for k, v in _AI_TYPE_ICONS.items() if k.lower() in uc.ai_type.lower()), "🧠")

    with st.container(border=True):
        # Cabecera: ranking + título + score
        col_rank, col_title, col_score = st.columns([0.08, 0.72, 0.20])
        with col_rank:
            st.markdown(
                f'<div style="font-size:1.8rem;font-weight:800;color:#d1d5db;line-height:1;">'
                f'#{rank}</div>',
                unsafe_allow_html=True
            )
        with col_title:
            st.markdown(f"**{ai_icon} {uc.title}**")
            st.caption(f"📁 {uc.business_area}  ·  🧪 {uc.ai_type}")
        with col_score:
            score_color = "#16a34a" if (uc.priority_score or 0) >= 70 else "#d97706" if (uc.priority_score or 0) >= 40 else "#dc2626"
            st.markdown(
                f'<div style="text-align:right;">'
                f'<div style="font-size:1.5rem;font-weight:800;color:{score_color};">'
                f'{uc.priority_score:.0f}</div>'
                f'<div style="font-size:0.65rem;color:#9ca3af;text-transform:uppercase;">Score</div>'
                f'</div>',
                unsafe_allow_html=True
            )

        # Descripción
        st.markdown(
            f'<p style="color:#374151;font-size:0.95rem;margin:0.5rem 0 1rem;">{uc.description}</p>',
            unsafe_allow_html=True
        )

        # Badges de impacto, esfuerzo y tiempo
        impact_badge = _badge(f"{impact_icon} Impacto {uc.estimated_impact}", impact_bg, impact_color)
        effort_badge = _badge(f"{effort_icon} Esfuerzo {uc.estimated_effort}", effort_bg, effort_color)
        time_badge   = _badge(f"⏱ {uc.time_to_value}", "#eff6ff", "#1e40af")
        st.markdown(
            f'{impact_badge} &nbsp; {effort_badge} &nbsp; {time_badge}',
            unsafe_allow_html=True
        )
        st.markdown("<br>", unsafe_allow_html=True)

        # KPIs y Prerequisites en dos columnas
        col_kpi, col_pre = st.columns(2)
        with col_kpi:
            st.markdown("**📊 KPIs que mejoraría**")
            for kpi in uc.kpis:
                st.markdown(f"- {kpi}")
        with col_pre:
            st.markdown("**⚙️ Prerrequisitos**")
            for pre in uc.prerequisites:
                st.markdown(f"- {pre}")

        # Checkbox de selección para pipeline (solo si selectable=True)
        if selectable:
            st.markdown("<hr style='margin:0.8rem 0 0.4rem;opacity:0.15;'>", unsafe_allow_html=True)
            selected = st.checkbox(
                "✅ Añadir al pipeline",
                key=f"uc_select_{rank}",
                help="Selecciona este caso de uso para trocearlo como épica"
            )
            return selected
    return False


def _launch_pipeline(selected_ucs, project_id: str):
    """Inicializa el pipeline con los casos de uso seleccionados."""
    from src.models.agile import Epic

    epics = [
        Epic(
            title=uc.title,
            description=(
                f"{uc.description}\n\n"
                f"Área de negocio: {uc.business_area}\n"
                f"Tecnología IA: {uc.ai_type}\n"
                f"KPIs objetivo: {', '.join(uc.kpis[:3])}\n"
                f"Prerrequisitos: {', '.join(uc.prerequisites[:2])}"
            ),
            type="desarrollo",
            priority="high",
        )
        for uc in selected_ucs
    ]

    st.session_state["pipeline"] = {
        "active": True,
        "epics": epics,
        "pending_epic_index": 0,
        "all_stories": [],
        "project_id": project_id,
    }


def render_ai_usecase_generator():
    llm = get_llm_service()

    st.markdown("""
<h2 style='margin-bottom:0.2rem;'>🧠 Generador de Casos de Uso de IA</h2>
<p style='color:#6b7280;margin-top:0;'>Describe tu organización y obtén una lista priorizada de oportunidades de IA adaptadas a tu contexto.</p>
""", unsafe_allow_html=True)

    # ── PANTALLA 1: FORMULARIO ─────────────────────────────────────────────────
    if "ai_use_cases" not in st.session_state:
        with st.form("usecase_form"):
            st.markdown("#### 1. Cuéntanos sobre tu organización")

            col1, col2 = st.columns(2)
            with col1:
                sector = st.text_input(
                    "🏭 Sector o industria",
                    placeholder="ej: Retail, Banca, Manufactura, Salud, Consultoría..."
                )
            with col2:
                company_size = st.selectbox(
                    "👥 Tamaño de la empresa",
                    ["Startup (1-50 personas)", "PYME (50-250 personas)",
                     "Empresa mediana (250-1000)", "Gran empresa (>1000 personas)"]
                )

            pain_points = st.text_area(
                "😤 ¿Cuáles son vuestros principales retos o puntos de dolor?",
                placeholder="ej: Perdemos mucho tiempo en tareas manuales de reporting, tenemos alta tasa de abandono de clientes, no sabemos predecir la demanda...",
                height=120
            )
            current_tech = st.text_input(
                "💻 Infraestructura / tecnología actual",
                placeholder="ej: ERP SAP, datos en Excel, CRM Salesforce, sin cloud, Azure..."
            )
            goals = st.text_area(
                "🎯 Objetivos estratégicos del próximo año",
                placeholder="ej: Reducir costes operativos un 20%, mejorar NPS, lanzar nuevo canal digital, escalar internacionalmente...",
                height=100
            )

            submitted = st.form_submit_button(
                "✨ Generar casos de uso con IA",
                type="primary",
                use_container_width=True
            )

        if submitted:
            if not sector or not pain_points or not goals:
                st.warning("Por favor, rellena al menos el sector, los retos y los objetivos.")
            else:
                with st.spinner("🧠 Analizando tu organización con Llama 3... (puede tardar 10-15 segundos)"):
                    try:
                        use_cases = llm.generate_ai_use_cases(
                            sector=sector,
                            company_size=company_size,
                            pain_points=pain_points,
                            current_tech=current_tech,
                            goals=goals,
                        )
                        st.session_state["ai_use_cases"] = use_cases
                        st.session_state["ai_usecase_context"] = {
                            "sector": sector,
                            "company_size": company_size,
                        }
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ Error al generar casos de uso: {e}")

    # ── PANTALLA 2: RESULTADOS ─────────────────────────────────────────────────
    else:
        use_cases = st.session_state["ai_use_cases"]
        context = st.session_state.get("ai_usecase_context", {})

        # Barra superior con resumen y botón de reset
        col_back, col_info = st.columns([0.25, 0.75])
        with col_back:
            if st.button("← Nueva consulta", type="secondary"):
                del st.session_state["ai_use_cases"]
                del st.session_state["ai_usecase_context"]
                st.rerun()
        with col_info:
            st.markdown(
                f'<p style="color:#6b7280;padding-top:0.4rem;">📌 <b>{len(use_cases)} casos de uso</b> '
                f'generados para el sector <b>{context.get("sector","")}</b> · '
                f'{context.get("company_size","")}</p>',
                unsafe_allow_html=True
            )

        # Métricas resumen
        high_impact = sum(1 for uc in use_cases if uc.estimated_impact == "Alto")
        quick_wins  = sum(1 for uc in use_cases if uc.estimated_impact == "Alto" and uc.estimated_effort == "Bajo")
        avg_score   = round(sum(uc.priority_score or 0 for uc in use_cases) / len(use_cases), 1) if use_cases else 0

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total de casos", len(use_cases))
        m2.metric("Alto impacto", high_impact)
        m3.metric("Quick Wins 🏆", quick_wins)
        m4.metric("Score medio", avg_score)

        st.markdown("---")

        # Filtros rápidos
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            filter_impact = st.multiselect(
                "Filtrar por impacto:", ["Alto", "Medio", "Bajo"],
                default=["Alto", "Medio", "Bajo"]
            )
        with col_f2:
            filter_effort = st.multiselect(
                "Filtrar por esfuerzo:", ["Alto", "Medio", "Bajo"],
                default=["Alto", "Medio", "Bajo"]
            )

        filtered = [
            uc for uc in use_cases
            if uc.estimated_impact in filter_impact and uc.estimated_effort in filter_effort
        ]

        # ── PANEL SUPERIOR: LANZAR PIPELINE ─────────────────────────────────────────
        # Leer estado actual de selecciones antes de renderizar
        selected_usecases = [
            uc for i, uc in enumerate(filtered, 1)
            if st.session_state.get(f"uc_select_{i}", False)
        ]

        if selected_usecases:
            st.markdown(
                f"<div style='background:#f3e8ff; border:2px solid #a855f7; border-radius:8px; padding:1.2rem; margin-bottom:1.5rem;'>"
                f"<h3 style='margin-top:0; color:#7e22ce;'>🚀 Lanzar Pipeline Ágil</h3>"
                f"<p style='color:#6b21a8; margin-bottom:1rem;'>Has seleccionado <b>{len(selected_usecases)}</b> caso(s) de uso para convertir en épicas.</p>",
                unsafe_allow_html=True
            )
            
            from src.data.cache import cached_projects, get_repository
            repo = get_repository()
            projects = cached_projects()
            
            # Opción especial para crear nuevo proyecto
            NEW_PROJ_KEY = "___NEW___"
            project_options = {p["id"]: p["name"] for p in projects}
            project_options[NEW_PROJ_KEY] = "✨ + Crear Nuevo Proyecto"

            col_proj, col_new, col_btn = st.columns([0.4, 0.3, 0.3])
            with col_proj:
                selected_project_id = st.selectbox(
                    "📁 Proyecto destino",
                    options=list(project_options.keys()),
                    format_func=lambda x: project_options[x]
                )
            
            new_project_name = ""
            with col_new:
                if selected_project_id == NEW_PROJ_KEY:
                    new_project_name = st.text_input("Nombre del nuevo proyecto")
            
            with col_btn:
                st.markdown("<div style='margin-top:28px;'></div>", unsafe_allow_html=True)
                btn_disabled = (selected_project_id == NEW_PROJ_KEY and not new_project_name.strip())
                if st.button("🪓 Trocear como Épicas →", type="primary", use_container_width=True, disabled=btn_disabled):
                    final_project_id = selected_project_id
                    
                    if selected_project_id == NEW_PROJ_KEY:
                        # Crear el proyecto al vuelo
                        with st.spinner("Creando proyecto en Sprinto..."):
                            final_project_id = repo.create_project(new_project_name.strip())
                            # Forzar recarga de caché de proyectos
                            st.cache_data.clear()
                    
                    _launch_pipeline(selected_usecases, final_project_id)
                    st.session_state.current_page = "🪓 Troceador de Épicas"
                    st.rerun()
            
            st.markdown("</div>", unsafe_allow_html=True)

        if not filtered:
            st.info("No hay casos de uso con los filtros seleccionados.")
        else:
            for i, uc in enumerate(filtered, 1):
                # El checkbox actualizará la página y el panel de arriba reaccionará
                _render_use_case_card(uc, i, selectable=True)
