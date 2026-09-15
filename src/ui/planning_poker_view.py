import streamlit as st
import time

from src.repositories.firebase_repository import FirebaseRepository
from src.services.llm_service import LLMService
from src.ui.pipeline_banner import render_pipeline_banner

def render_planning_poker():
    st.title("🃏 AI Planning Poker")
    st.markdown("Estima el esfuerzo de tus historias de usuario utilizando la IA y la serie de Fibonacci.")
    render_pipeline_banner("planning")

    repo = FirebaseRepository()
    projects = repo.get_projects()

    if not projects:
        st.info("No hay proyectos en Sprinto. Crea uno primero.")
        return

    # --- SELECTOR DE PROYECTO ---
    st.subheader("1. Selecciona un Proyecto")
    project_options = {p["id"]: p["name"] for p in projects}
    selected_project_id = st.selectbox(
        "Proyecto de Sprinto",
        options=list(project_options.keys()),
        format_func=lambda x: project_options[x],
        key="poker_project"
    )

    if not selected_project_id:
        return

    # Obtener todas las historias
    all_stories = repo.get_stories(selected_project_id)
    # Filtrar las no estimadas
    unestimated = [s for s in all_stories if not s.story_points and not s.estimatedHours]

    st.write(f"Historias totales: **{len(all_stories)}** | Pendientes de estimar: **{len(unestimated)}**")

    if not unestimated:
        st.success("¡Todo el backlog está estimado! 🎉")
        return

    # --- SELECTOR DE MODO ---
    mode = st.radio("Modo de Estimación:", ["Modo Individual (Historia por historia)", "Modo Batch (Estimación masiva)"], horizontal=True)

    if mode.startswith("Modo Batch"):
        _render_batch_mode(selected_project_id, unestimated)
    else:
        _render_individual_mode(selected_project_id, unestimated)

def _render_batch_mode(project_id: str, stories: list):
    st.subheader("Estimación Masiva")
    st.info("Selecciona las historias que deseas estimar. La IA procesará todas juntas.")
    
    selected_indices = []
    for i, s in enumerate(stories):
        if st.checkbox(f"**{s.title}** ({s.code})", key=f"chk_{s.id}_{i}", value=True):
            selected_indices.append(i)
            
    if st.button("🎲 Estimar Seleccionadas", type="primary", disabled=len(selected_indices)==0):
        selected_stories = [stories[i] for i in selected_indices]
        llm = LLMService()
        
        with st.spinner("Analizando complejidad técnica y estimando..."):
            estimations = llm.estimate_stories(selected_stories)
            
        if estimations:
            st.session_state["poker_batch_results"] = list(zip(selected_stories, estimations))
            st.success("¡Estimación completada!")

    if "poker_batch_results" in st.session_state:
        results = st.session_state["poker_batch_results"]
        st.markdown("---")
        st.subheader("Resultados")
        
        for story, est in results:
            with st.expander(f"{story.code} - {story.title} | {est.story_points} SP", expanded=True):
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.metric("Puntos de Historia", est.story_points)
                    st.metric("Horas Aproximadas", est.estimated_hours)
                with col2:
                    st.write("**Justificación:**")
                    st.write(est.rationale)
                    if est.risks:
                        st.write("**Riesgos:**")
                        for r in est.risks:
                            st.write(f"- ⚠️ {r}")
                    if est.complexity_drivers:
                        st.write("**Complejidad:**")
                        for c in est.complexity_drivers:
                            st.write(f"- 🔧 {c}")
                            
        if st.button("💾 Guardar Todas las Estimaciones", type="primary"):
            repo = FirebaseRepository()
            with st.spinner("Guardando en Sprinto..."):
                for story, est in results:
                    repo.update_ticket_estimation(project_id, story.id, est.story_points, est.estimated_hours)
                # clear project cache here
                from src.data.cache import clear_project_cache
                clear_project_cache(project_id)
                del st.session_state["poker_batch_results"]
            st.success("Estimaciones guardadas correctamente. Refresca la página para continuar.")
            time.sleep(2)
            st.rerun()

def _render_individual_mode(project_id: str, stories: list):
    st.subheader("Poker Individual")
    
    if "poker_current_index" not in st.session_state:
        st.session_state.poker_current_index = 0
        
    idx = st.session_state.poker_current_index
    if idx >= len(stories):
        st.success("Has terminado con la cola de estimaciones.")
        if st.button("Reiniciar"):
            st.session_state.poker_current_index = 0
            st.rerun()
        return
        
    story = stories[idx]
    
    st.progress((idx) / len(stories), text=f"Estimando {idx+1} de {len(stories)}")
    
    with st.container(border=True):
        st.write(f"### {story.code} - {story.title}")
        st.write(story.description)
        if story.acceptanceCriteria:
            st.write("**Criterios de Aceptación:**")
            for ac in story.acceptanceCriteria:
                st.write(f"- {ac}")
                
        if st.button("🎲 Estimar Historia", type="primary", key=f"est_btn_{story.id}"):
            llm = LLMService()
            with st.spinner("Pensando..."):
                estimations = llm.estimate_stories([story])
                if estimations:
                    st.session_state[f"poker_res_{story.id}"] = estimations[0]
                    
        if f"poker_res_{story.id}" in st.session_state:
            est = st.session_state[f"poker_res_{story.id}"]
            st.markdown("---")
            col1, col2 = st.columns([1, 2])
            with col1:
                st.metric("Puntos de Historia", est.story_points)
                st.metric("Horas Aproximadas", est.estimated_hours)
            with col2:
                st.write("**Justificación:**", est.rationale)
                if est.risks:
                    st.write("**Riesgos:**", ", ".join(est.risks))
                    
            col_save, col_skip = st.columns(2)
            with col_save:
                if st.button("💾 Guardar y Siguiente", type="primary", key=f"save_{story.id}"):
                    repo = FirebaseRepository()
                    repo.update_ticket_estimation(project_id, story.id, est.story_points, est.estimated_hours)
                    from src.data.cache import clear_project_cache
                    clear_project_cache(project_id)
                    st.session_state.poker_current_index += 1
                    st.rerun()
            with col_skip:
                if st.button("⏭️ Saltar", key=f"skip_{story.id}"):
                    st.session_state.poker_current_index += 1
                    st.rerun()
