import streamlit as st

from src.repositories.firebase_repository import FirebaseRepository
from src.services.llm_service import LLMService
from src.ui.pipeline_banner import render_pipeline_banner

def render_docs_generator():
    st.title("📚 Documentación Automática (Release Notes)")
    st.markdown("Genera las Notas de la Versión automáticamente basándote en las historias completadas de un proyecto.")
    render_pipeline_banner("docs")

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
        key="docs_project"
    )

    if not selected_project_id:
        return

    # Buscar historias completadas
    all_stories = repo.get_stories(selected_project_id)
    done_statuses = ["done", "completado", "terminado"]
    completed_stories = [s for s in all_stories if s.status and s.status.lower() in done_statuses]

    st.write(f"Historias totales: **{len(all_stories)}** | Historias completadas: **{len(completed_stories)}**")

    if not completed_stories:
        st.warning("No hay historias en estado 'Completado' para generar documentación.")
        return

    with st.expander("Ver historias que se incluirán en el documento", expanded=False):
        for s in completed_stories:
            st.write(f"- **{s.code}**: {s.title}")

    st.subheader("2. Configura el Documento")
    
    col1, col2 = st.columns(2)
    with col1:
        version_input = st.text_input("Versión del Lanzamiento", value="v1.0.0", placeholder="Ej. v1.2.3")
    with col2:
        tone_input = st.radio(
            "Tono de la Documentación",
            options=["business", "technical"],
            format_func=lambda x: "👔 Para Clientes / Negocio (Marketing)" if x == "business" else "💻 Para el Equipo Técnico (Detallado)",
            horizontal=True
        )

    if st.button("📚 Generar Release Notes", type="primary"):
        llm = LLMService()
        with st.spinner(f"Redactando Release Notes ({tone_input}) para {len(completed_stories)} historias..."):
            notes = llm.generate_release_notes(completed_stories, version_input, tone_input)
            
        if notes and notes.markdown_content:
            st.success("¡Documentación generada con éxito!")
            st.markdown("---")
            
            # Vista previa renderizada
            st.subheader("Vista Previa")
            with st.container(border=True):
                st.markdown(notes.markdown_content)
                
            st.markdown("---")
            st.subheader("Código Markdown (Copiar y Pegar)")
            st.code(notes.markdown_content, language="markdown")
        else:
            st.error("Hubo un error generando las notas de la versión.")
