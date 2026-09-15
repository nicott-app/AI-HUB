import streamlit as st

from src.repositories.firebase_repository import FirebaseRepository
from src.services.llm_service import LLMService
from src.ui.pipeline_banner import render_pipeline_banner

def render_health_dash():
    st.title("🩺 Dashboard de Salud")
    st.markdown("Diagnóstico en tiempo real del estado de tu backlog y posibles cuellos de botella.")
    render_pipeline_banner("health")

    repo = FirebaseRepository()
    projects = repo.get_projects()

    if not projects:
        st.info("No hay proyectos en Sprinto. Crea uno primero.")
        return

    # --- SELECTOR DE PROYECTO ---
    st.subheader("Selecciona un Proyecto")
    project_options = {p["id"]: p["name"] for p in projects}
    selected_project_id = st.selectbox(
        "Proyecto de Sprinto",
        options=list(project_options.keys()),
        format_func=lambda x: project_options[x],
        key="health_project"
    )

    if not selected_project_id:
        return

    # Extraer métricas reales
    with st.spinner("Analizando flujo de trabajo y métricas Kanban..."):
        all_stories = repo.get_stories(selected_project_id)
    
    if not all_stories:
        st.warning("El proyecto no tiene historias o están todas archivadas.")
        return

    # CÁLCULOS
    total_stories = len(all_stories)
    blocked_stories = sum(1 for s in all_stories if getattr(s, "isBlocked", False) or s.status == "bloqueado")
    
    # Story points
    sp_total = sum(s.story_points for s in all_stories if getattr(s, "story_points", None) is not None)
    sp_done = sum(s.story_points for s in all_stories if getattr(s, "story_points", None) is not None and s.status in ["done", "completado", "terminado"])
    
    # Estados
    status_counts = {}
    for s in all_stories:
        st_name = s.status if s.status else "backlog"
        status_counts[st_name] = status_counts.get(st_name, 0) + 1

    # MOSTRAR MÉTRICAS
    st.write("### Radiografía del Proyecto")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Historias Activas", total_stories)
    col2.metric("Puntos Completados", f"{sp_done} / {sp_total}" if sp_total else "0")
    col3.metric("Tickets Bloqueados", blocked_stories, delta_color="inverse", delta="Atención" if blocked_stories > 0 else "Normal")
    col4.metric("WIP (En curso)", status_counts.get("in_progress", 0) + status_counts.get("doing", 0))

    st.write("**Distribución del Tablero:**")
    st.bar_chart(status_counts)

    # --- DIAGNÓSTICO IA ---
    st.markdown("---")
    st.write("### 🤖 Diagnóstico Clínico (IA)")
    
    metrics_payload = {
        "Total de tickets activos": total_stories,
        "Total de tickets bloqueados": blocked_stories,
        "Puntos de Historia (Completados / Totales)": f"{sp_done} / {sp_total}",
        "Distribución por columnas (Kanban)": status_counts
    }

    if st.button("🔬 Generar Diagnóstico con IA", type="primary"):
        llm = LLMService()
        with st.spinner("Revisando métricas de flujo, identificando cuellos de botella y generando reporte..."):
            diagnosis = llm.diagnose_sprint(metrics_payload)
            
            # Rendering the diagnosis
            status_color = "🟢" if "Saludable" in diagnosis.overall_status else "🟡" if "Riesgo" in diagnosis.overall_status else "🔴"
            st.subheader(f"Estado General: {status_color} {diagnosis.overall_status}")
            st.write(f"_{diagnosis.summary}_")
            
            col_bot, col_rec = st.columns(2)
            with col_bot:
                st.write("**🚨 Cuellos de botella y Riesgos**")
                for bot in diagnosis.bottlenecks:
                    st.write(f"- {bot}")
            with col_rec:
                st.write("**💊 Acciones Recomendadas**")
                for rec in diagnosis.recommendations:
                    st.write(f"- {rec}")
