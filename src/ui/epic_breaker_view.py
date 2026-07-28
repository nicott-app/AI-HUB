import streamlit as st
from src.models.agile import Epic
from src.data.cache import get_repository, get_llm_service, cached_projects, cached_epics, cached_stories


def inject_custom_css():
    st.markdown("""
        <style>
        .block-container { padding-top: 2rem !important; padding-bottom: 2rem !important; }
        div[data-testid="stVerticalBlockBorderWrapper"] {
            border-radius: 12px !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            background-color: rgba(30, 30, 30, 0.4) !important;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }
        div[data-testid="stVerticalBlockBorderWrapper"]:hover {
            border-color: rgba(255, 255, 255, 0.3) !important;
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
        }
        div[data-testid="stExpander"] {
            border-radius: 12px !important;
            border: 1px solid rgba(0, 174, 255, 0.3) !important;
            background-color: rgba(0, 174, 255, 0.12) !important;
            transition: all 0.3s ease;
        }
        div[data-testid="stExpander"]:hover {
            border-color: rgba(0, 174, 255, 0.6) !important;
            background-color: rgba(0, 174, 255, 0.18) !important;
        }
        .badge-low { background-color: rgba(46,204,113,0.2); color:#2ecc71; padding:4px 12px; border-radius:16px; font-weight:600; font-size:0.85rem; display:inline-block; }
        .badge-medium { background-color: rgba(241,196,15,0.2); color:#f1c40f; padding:4px 12px; border-radius:16px; font-weight:600; font-size:0.85rem; display:inline-block; }
        .badge-high { background-color: rgba(231,76,60,0.2); color:#e74c3c; padding:4px 12px; border-radius:16px; font-weight:600; font-size:0.85rem; display:inline-block; }
        .bi-chip {
            display: inline-block;
            background: rgba(99,102,241,0.15);
            border: 1px solid rgba(99,102,241,0.35);
            color: #a5b4fc;
            border-radius: 20px;
            padding: 2px 10px;
            font-size: 0.78rem;
            margin: 2px 2px 2px 0;
        }
        .bi-chip-orange {
            background: rgba(251,146,60,0.15);
            border: 1px solid rgba(251,146,60,0.35);
            color: #fdba74;
        }
        .bi-chip-green {
            background: rgba(52,211,153,0.15);
            border: 1px solid rgba(52,211,153,0.35);
            color: #6ee7b7;
        }
        button[kind="primary"] { font-weight:bold !important; border-radius:8px !important; }
        </style>
    """, unsafe_allow_html=True)


# ─── Helpers de renderizado de tarjetas ───────────────────────────────────────

def _complexity_badge(sp: int) -> str:
    if sp <= 3:
        return '<div class="badge-low">Baja Complejidad</div>'
    elif sp <= 5:
        return '<div class="badge-medium">Media Complejidad</div>'
    return '<div class="badge-high">Alta Complejidad</div>'


def _render_generic_card(story):
    """Tarjeta estándar para historias de usuario genéricas."""
    sp = story.story_points or 3
    badge = _complexity_badge(sp)
    with st.container(border=True):
        c1, c2 = st.columns([0.75, 0.25])
        with c1:
            st.markdown(f"**{story.title}**")
        with c2:
            st.markdown(f"<div style='text-align:right;'>{badge}</div>", unsafe_allow_html=True)
        st.markdown(
            f"<span style='color:#b0bec5;font-size:0.95rem;'>{story.description}</span>",
            unsafe_allow_html=True
        )
        with st.expander("✅ Criterios de Aceptación"):
            for c in story.acceptanceCriteria:
                st.markdown(f"- {c}")


def _render_bi_card(story):
    """Tarjeta enriquecida para historias de desarrollo PowerBI."""
    sp = story.story_points or 3
    badge = _complexity_badge(sp)

    with st.container(border=True):
        # Cabecera: título + complejidad
        c1, c2 = st.columns([0.75, 0.25])
        with c1:
            st.markdown(f"**{story.title}**")
        with c2:
            st.markdown(f"<div style='text-align:right;'>{badge}</div>", unsafe_allow_html=True)

        st.markdown(
            f"<span style='color:#b0bec5;font-size:0.95rem;'>{story.description}</span>",
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # Metadatos BI en columnas
        m1, m2 = st.columns(2)
        with m1:
            st.markdown("**🗄️ Orígenes de datos**")
            if story.data_sources:
                chips = "".join(f'<span class="bi-chip">{s}</span>' for s in story.data_sources)
                st.markdown(chips, unsafe_allow_html=True)
            else:
                st.caption("No especificados")

            st.markdown("<br>**🔄 Frecuencia de refresco**", unsafe_allow_html=True)
            refresh_colors = {
                "Tiempo real": "bi-chip-orange",
                "Diaria": "bi-chip-green",
                "Semanal": "bi-chip-green",
                "Bajo demanda": "bi-chip",
            }
            color_class = refresh_colors.get(story.refresh_frequency, "bi-chip")
            st.markdown(
                f'<span class="bi-chip {color_class}">⏱ {story.refresh_frequency}</span>',
                unsafe_allow_html=True
            )

        with m2:
            st.markdown("**📐 Tipo de visual**")
            if story.visual_type:
                st.markdown(
                    f'<span class="bi-chip">📊 {story.visual_type}</span>',
                    unsafe_allow_html=True
                )

            st.markdown("<br>**⚡ Medidas DAX**", unsafe_allow_html=True)
            if story.dax_measures:
                for measure in story.dax_measures:
                    st.code(measure, language="")
            else:
                st.caption("No especificadas")

        with st.expander("✅ Criterios de Aceptación"):
            for c in story.acceptanceCriteria:
                st.markdown(f"- {c}")


# ─── Vista principal ───────────────────────────────────────────────────────────

def render_epic_breaker():
    inject_custom_css()

    repo = get_repository()
    llm = get_llm_service()

    # ── PANTALLA 1: FORMULARIO DE ENTRADA ──────────────────────────────────────
    if "generated_stories" not in st.session_state:
        st.markdown("## 🪓 Configuración de la Épica")
        st.caption("Define el contexto inicial y deja que la IA construya el desglose de tareas.")

        # ── SELECTOR DE MODO ──────────────────────────────────────────────────
        st.markdown("<br>", unsafe_allow_html=True)
        mode = st.radio(
            "**Modo de generación:**",
            options=["🌐 Genérico (Agile)", "📊 PowerBI / Business Intelligence"],
            horizontal=True,
            label_visibility="visible",
        )
        bi_mode = mode.startswith("📊")
        st.session_state["bi_mode"] = bi_mode

        if bi_mode:
            st.info(
                "**Modo PowerBI activo.** Las historias generadas incluirán: "
                "orígenes de datos, medidas DAX, tipo de visual y frecuencia de refresco.",
                icon="📊"
            )

        st.markdown("<br>", unsafe_allow_html=True)

        with st.container(border=True):
            projects = cached_projects()
            project_options = {p["id"]: p["name"] for p in projects}

            selected_project_id = None
            if project_options:
                selected_project_id = st.selectbox(
                    "📁 Entorno (Proyecto)",
                    options=list(project_options.keys()),
                    format_func=lambda x: project_options[x]
                )

            epic_title, epic_description, epic_priority, selected_epic_id = "", "", "medium", None

            if selected_project_id:
                epics = cached_epics(selected_project_id)
                epic_options = {e.id: f"[{e.type.upper()}] {e.title}" for e in epics} if epics else {}

                if epic_options:
                    selected_epic_id = st.selectbox(
                        "🔗 Importar Épica (Base de Datos)",
                        options=[""] + list(epic_options.keys()),
                        format_func=lambda x: epic_options[x] if x else "--- Redactar Manualmente ---"
                    )

                if selected_epic_id:
                    epic = next((e for e in epics if e.id == selected_epic_id), None)
                    if epic:
                        epic_title = epic.title
                        epic_description = epic.description
                        epic_priority = epic.priority

            st.markdown("<hr style='margin:1rem 0; opacity:0.2;'>", unsafe_allow_html=True)
            epic_title = st.text_input("📝 Título de la Épica", value=epic_title)
            epic_description = st.text_area("🧠 Contexto / Notas para la IA", value=epic_description, height=200)

            button_label = "✨ Trocear con IA (modo PowerBI)" if bi_mode else "✨ Trocear con IA"
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button(button_label, type="primary", use_container_width=True):
                if not epic_title or not epic_description:
                    st.warning("Por favor, completa el título y contexto.")
                else:
                    spinner_msg = (
                        "Analizando épica PowerBI con Llama 3..." if bi_mode
                        else "Analizando y diseñando historias con Llama 3..."
                    )
                    with st.spinner(spinner_msg):
                        try:
                            temp_epic = Epic(
                                title=epic_title, description=epic_description,
                                type="analisis", priority=epic_priority
                            )
                            # ── Delegación por modo: no toca el flujo genérico ──
                            if bi_mode:
                                stories = llm.break_epic_into_bi_stories(temp_epic)
                            else:
                                stories = llm.break_epic_into_stories(temp_epic)

                            st.session_state.update({
                                "generated_stories": stories,
                                "current_epic": temp_epic,
                                "selected_epic_id": selected_epic_id,
                                "target_project_id": selected_project_id,
                            })
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error en la IA: {e}")

    # ── PANTALLA 2: DASHBOARD DE VALIDACIÓN ───────────────────────────────────
    else:
        bi_mode = st.session_state.get("bi_mode", False)
        mode_label = "📊 PowerBI" if bi_mode else "🌐 Genérico"

        st.markdown(f"## 📊 Dashboard de Desglose Ágil  `{mode_label}`")

        if st.button("← Volver a Configuración"):
            del st.session_state["generated_stories"]
            st.rerun()

        stories = st.session_state["generated_stories"]
        col_main, col_metrics = st.columns([0.7, 0.3], gap="large")

        with col_main:
            st.markdown("#### 📑 Tarjetas Generadas")
            for story in stories:
                if bi_mode:
                    _render_bi_card(story)
                else:
                    _render_generic_card(story)

        with col_metrics:
            st.markdown("#### 📈 Métricas del Lote")
            with st.container(border=True):
                total = len(stories)
                total_sp = sum(s.story_points or 3 for s in stories)
                avg_sp = round(total_sp / total, 1) if total else 0
                st.metric("Total de Historias", total)
                st.metric("Puntos de Historia", total_sp, delta=f"{avg_sp} Promedio", delta_color="off")

                if bi_mode:
                    st.markdown("---")
                    # Estadísticas específicas BI
                    total_dax = sum(len(s.dax_measures) for s in stories if hasattr(s, "dax_measures"))
                    total_sources = len(set(
                        src for s in stories if hasattr(s, "data_sources")
                        for src in s.data_sources
                    ))
                    st.metric("Medidas DAX", total_dax)
                    st.metric("Orígenes de datos", total_sources)

            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown("#### 🚀 Despliegue")

            if st.button("Enviar a Pragma", type="primary", use_container_width=True):
                project_id = st.session_state.get("target_project_id")
                epic = st.session_state.get("current_epic")
                parent_id = st.session_state.get("selected_epic_id")

                if not project_id:
                    st.error("❌ No hay proyecto destino configurado. Vuelve atrás y selecciona un proyecto.")
                else:
                    progress = st.progress(0, text="Preparando envío...")
                    try:
                        # Paso 1: Guardar épica si es nueva
                        if not parent_id:
                            progress.progress(10, text="Guardando épica en Firebase...")
                            repo.save_ticket(project_id, epic)

                        # Paso 2: Enriquecer historias con la tag de la épica
                        progress.progress(30, text="Enriqueciendo historias...")
                        for story in stories:
                            if epic.title:
                                story.tags = story.tags or []
                                if f"epic:{epic.title}" not in story.tags:
                                    story.tags.append(f"epic:{epic.title}")

                        # Paso 3: Enviar historias una por una (sin threads, para evitar problemas en Streamlit Cloud)
                        total = len(stories)
                        saved_ids = []
                        for i, story in enumerate(stories):
                            progress.progress(
                                30 + int(60 * (i + 1) / total),
                                text=f"Enviando historia {i+1}/{total}: {story.title[:40]}..."
                            )
                            sid = repo.save_ticket(project_id, story)
                            saved_ids.append(sid)

                        # Paso 4: Limpiar caché
                        progress.progress(95, text="Limpiando caché...")
                        cached_epics.clear()
                        cached_stories.clear()

                        progress.progress(100, text="¡Listo!")

                        # Mostrar resultado y limpiar sin st.rerun() inmediato
                        st.success(
                            f"✅ **¡{total} historia{'s' if total > 1 else ''} enviada{'s' if total > 1 else ''} a Pragma!** "
                            f"Ya puedes verlas en tu tablero en el proyecto seleccionado."
                        )
                        st.balloons()
                        st.session_state["send_success"] = True
                        del st.session_state["generated_stories"]

                    except Exception as e:
                        progress.empty()
                        st.error(f"❌ **Fallo en el envío:** {str(e)}")
                        st.info("Revisa los logs en 'Manage app' de Streamlit Cloud para más detalles.")

        # Botón de regreso tras éxito
        if st.session_state.get("send_success"):
            if st.button("← Volver al inicio", type="secondary"):
                del st.session_state["send_success"]
                st.rerun()
