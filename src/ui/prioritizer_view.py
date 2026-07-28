import streamlit as st
import pandas as pd
from src.data.cache import get_repository, get_llm_service, cached_projects, cached_stories


def render_prioritizer():
    st.header("Priorizador Ágil Multipropósito 📊")
    st.write("Evalúa tus historias usando frameworks de la industria apoyado por Inteligencia Artificial.")

    repo = get_repository()
    llm = get_llm_service()

    projects = cached_projects()
    project_options = {p["id"]: p["name"] for p in projects}

    if not project_options:
        st.warning("No hay proyectos disponibles.")
        return

    col1, col2 = st.columns([1, 1])
    with col1:
        selected_project_id = st.selectbox(
            "1. Entorno (Proyecto)",
            options=list(project_options.keys()),
            format_func=lambda x: project_options[x]
        )
    with col2:
        frameworks = ["RICE", "WSJF", "MoSCoW", "Kano", "Valor vs Complejidad"]
        selected_framework = st.selectbox("2. Framework de Priorización", options=frameworks)

    stories = cached_stories(selected_project_id)

    if not stories:
        st.info("No se encontraron tickets compatibles sin finalizar en este proyecto.")
        return

    st.markdown("**3. Tickets a evaluar:**")
    st.caption(f"{len(stories)} tickets disponibles. Marca los que quieras incluir en el análisis.")
    
    search_query = st.text_input("🔍 Buscar tickets por título o ID:", "").strip().lower()

    def sort_key(s):
        parts = (s.id or "").split("-")
        return (0, parts[0], int(parts[-1])) if len(parts) == 2 and parts[-1].isdigit() else (1, s.id or "", 0)

    sorted_stories = sorted(stories, key=sort_key)
    
    if search_query:
        sorted_stories = [
            s for s in sorted_stories 
            if search_query in s.title.lower() or search_query in (s.code or s.id or "").lower()
        ]

    if not sorted_stories:
        st.info("No hay tickets que coincidan con la búsqueda.")
        
    cols = st.columns(3)
    selected_ids = []

    for idx, story in enumerate(sorted_stories):
        display_id = story.code or story.id or "?"
        label = f"`{display_id}` — {story.title}"
        if cols[idx % 3].checkbox(label, value=True, key=f"chk_{story.id}"):
            selected_ids.append(story.id)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button(f"🚀 Evaluar con {selected_framework} (IA)", type="primary"):
        if not selected_ids:
            st.warning("Selecciona al menos un ticket.")
            return

        selected = [s for s in stories if s.id in selected_ids]
        with st.spinner(f"Calculando {selected_framework} con Llama 3..."):
            try:
                results = llm.prioritize_stories(selected, selected_framework)
                st.session_state["prioritization_results"] = results
                st.session_state["active_framework"] = selected_framework
                st.success("¡Análisis completado!")
            except Exception as e:
                st.error(f"Error al evaluar: {e}")

    if "prioritization_results" not in st.session_state:
        return

    st.markdown("---")
    st.subheader("Resultados de Priorización")
    results = st.session_state["prioritization_results"]
    active_fw = st.session_state["active_framework"]

    df_data = []
    for p in results:
        row = {"ID": p.code or p.id, "Título": p.title}
        if active_fw == "RICE" and p.rice_score:
            row.update({"Reach": p.rice_score.reach, "Impact": p.rice_score.impact,
                        "Confidence": p.rice_score.confidence, "Effort": p.rice_score.effort,
                        "Score": round(p.rice_score.total_score, 2), "Justificación": p.rice_score.rationale})
        elif active_fw == "WSJF" and p.wsjf_score:
            row.update({"Bus. Value": p.wsjf_score.user_business_value,
                        "Time Crit.": p.wsjf_score.time_criticality,
                        "Risk Red.": p.wsjf_score.risk_reduction_opportunity,
                        "Job Size": p.wsjf_score.job_size,
                        "Score WSJF": round(p.wsjf_score.total_score, 2),
                        "Justificación": p.wsjf_score.rationale})
        elif active_fw == "MoSCoW" and p.moscow_score:
            row.update({"Categoría": p.moscow_score.category, "Justificación": p.moscow_score.rationale})
        elif active_fw == "Kano" and p.kano_score:
            row.update({"Clasificación": p.kano_score.category, "Justificación": p.kano_score.rationale})
        elif active_fw == "Valor vs Complejidad" and p.value_complexity_score:
            row.update({"Valor": p.value_complexity_score.value,
                        "Complejidad": p.value_complexity_score.complexity,
                        "Cuadrante": p.value_complexity_score.quadrant,
                        "Justificación": p.value_complexity_score.rationale})
        df_data.append(row)

    st.dataframe(pd.DataFrame(df_data), use_container_width=True, hide_index=True)

    if st.button("💾 Guardar Scores en Pragma (Firebase)", type="primary"):
        field_map = {
            "RICE": "rice_score", "WSJF": "wsjf_score", "MoSCoW": "moscow_score",
            "Kano": "kano_score", "Valor vs Complejidad": "value_complexity_score"
        }
        with st.spinner("Actualizando base de datos..."):
            try:
                db_field = field_map[active_fw]
                for p in results:
                    score_obj = getattr(p, db_field)
                    if score_obj:
                        repo.update_ticket_score(selected_project_id, p.id, db_field, score_obj.model_dump())

                cached_stories.clear()  # Invalidar caché para reflejar los scores guardados
                st.success("¡Scores guardados correctamente!")
                del st.session_state["prioritization_results"]
            except Exception as e:
                st.error(f"Error actualizando Firebase: {e}")
