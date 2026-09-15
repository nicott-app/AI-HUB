import streamlit as st

from src.repositories.firebase_repository import FirebaseRepository
from src.services.llm_service import LLMService
from src.ui.pipeline_banner import render_pipeline_banner

def render_qa_generator():
    st.title("🧪 Generador de Pruebas (Gherkin)")
    st.markdown("Selecciona una Historia de Usuario para generar automáticamente sus Casos de Prueba (Happy Path, Edge Cases, Negative Flows).")
    render_pipeline_banner("qa")

    repo = FirebaseRepository()
    projects = repo.get_projects()

    if not projects:
        st.info("No hay proyectos en Sprinto.")
        return

    st.subheader("1. Selecciona un Proyecto")
    project_options = {p["id"]: p["name"] for p in projects}
    selected_project_id = st.selectbox(
        "Proyecto de Sprinto",
        options=list(project_options.keys()),
        format_func=lambda x: project_options[x],
        key="qa_project"
    )

    if not selected_project_id:
        return

    all_stories = repo.get_stories(selected_project_id)
    if not all_stories:
        st.warning("El proyecto no tiene historias.")
        return

    st.subheader("2. Selecciona una Historia de Usuario")
    story_options = {s.id: f"{s.code} - {s.title}" for s in all_stories}
    selected_story_id = st.selectbox(
        "Historia de Usuario",
        options=list(story_options.keys()),
        format_func=lambda x: story_options[x],
        key="qa_story"
    )

    selected_story = next((s for s in all_stories if s.id == selected_story_id), None)
    
    if selected_story:
        with st.expander("Ver detalles de la Historia de Usuario", expanded=False):
            st.write(selected_story.description)
            if selected_story.acceptanceCriteria:
                st.write("**Criterios de Aceptación:**")
                for ac in selected_story.acceptanceCriteria:
                    st.write(f"- {ac}")

        if st.button("🧪 Generar Casos de Prueba (IA)", type="primary"):
            llm = LLMService()
            with st.spinner("Analizando requerimientos y redactando Gherkin..."):
                test_cases = llm.generate_test_cases(selected_story)
                
            if test_cases:
                st.success(f"Se han generado {len(test_cases)} casos de prueba.")
                st.markdown("---")
                
                # Renderizar los resultados
                for case in test_cases:
                    # Emoji según tipo
                    icon = "✅" if "Happy" in case.test_type else "⚠️" if "Edge" in case.test_type else "🚫"
                    
                    st.write(f"### {icon} {case.title}")
                    st.caption(f"**Tipo:** {case.test_type}")
                    st.code(case.gherkin_syntax, language="gherkin")
                    st.markdown("<br>", unsafe_allow_html=True)
