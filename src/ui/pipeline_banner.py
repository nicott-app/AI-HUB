"""
Componente reutilizable: Banner de progreso del Pipeline Integrado.

Se muestra en cada herramienta cuando hay un pipeline activo,
indicando el paso actual, el progreso de épicas y opción de cancelar.
"""
import streamlit as st


def render_pipeline_banner(current_step: str):
    """
    Renderiza el banner de pipeline en la vista actual.
    current_step: 'epic_breaker' | 'prioritizer'
    """
    pipeline = st.session_state.get("pipeline", {})
    if not pipeline.get("active"):
        return

    epics = pipeline.get("epics", [])
    idx = pipeline.get("pending_epic_index", 0)
    total = len(epics)
    current_epic_title = epics[idx].title if idx < total else "✅ Todas procesadas"

    STEPS = [
        ("🧠", "Casos de Uso", "done"),
        ("🪓", "Troceador", "epic_breaker"),
        ("📊", "Priorizador", "prioritizer"),
        ("🚀", "Pragma", "done"),
    ]

    steps_html = ""
    for icon, label, step_id in STEPS:
        if step_id == "done" and current_step == "done":
            color, weight = "#16a34a", "800"
        elif step_id == current_step:
            color, weight = "#7c3aed", "800"
        elif STEPS.index((icon, label, step_id)) < [s[2] for s in STEPS].index(current_step):
            color, weight = "#16a34a", "600"
        else:
            color, weight = "#9ca3af", "400"

        steps_html += (
            f'<span style="color:{color};font-weight:{weight};font-size:0.85rem;">'
            f'{icon} {label}</span>'
            f'<span style="color:#d1d5db;margin:0 6px;">→</span>'
        )
    steps_html = steps_html.rstrip('<span style="color:#d1d5db;margin:0 6px;">→</span>')

    col_banner, col_cancel = st.columns([0.88, 0.12])
    with col_banner:
        st.markdown(
            f"""<div style="background:linear-gradient(90deg,#7c3aed12,#2563eb12);
            border:1px solid #7c3aed50;border-radius:8px;padding:0.65rem 1rem;">
            <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:6px;">
                <div>{steps_html}</div>
                <div style="font-size:0.75rem;color:#6b7280;font-weight:500;">
                    Épica {min(idx + 1, total)} de {total}
                </div>
            </div>
            <div style="margin-top:4px;font-size:0.85rem;color:#374151;">
                📌 <strong>Procesando:</strong> {current_epic_title}
            </div>
            </div>""",
            unsafe_allow_html=True
        )
    with col_cancel:
        if st.button("✕ Cancelar", key="cancel_pipeline_btn", use_container_width=True):
            cancel_pipeline()
            st.rerun()


def cancel_pipeline():
    """Cancela y limpia el estado del pipeline."""
    for key in ["pipeline"]:
        if key in st.session_state:
            del st.session_state[key]
