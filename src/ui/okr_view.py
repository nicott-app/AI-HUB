"""
Vista del Generador de OKRs.
"""
import streamlit as st
from src.data.cache import get_llm_service

def _render_okr_card(obj_index: int, obj):
    """Renderiza la tarjeta de un Objective y sus Key Results."""
    with st.container(border=True):
        st.markdown(
            f'<div style="background:linear-gradient(90deg,#f3f4f6,#ffffff);padding:1rem;'
            f'border-left:4px solid #7c3aed;border-radius:6px;margin-bottom:1rem;">'
            f'<div style="font-size:0.75rem;color:#7c3aed;font-weight:700;letter-spacing:1px;text-transform:uppercase;">'
            f'Objetivo {obj_index}</div>'
            f'<div style="font-size:1.2rem;font-weight:800;color:#1f2937;margin-top:4px;">{obj.title}</div>'
            f'<div style="font-size:0.9rem;color:#6b7280;margin-top:4px;"><i>{obj.description}</i></div>'
            f'</div>',
            unsafe_allow_html=True
        )

        for kr_idx, kr in enumerate(obj.key_results, 1):
            with st.expander(f"📈 KR {obj_index}.{kr_idx}: {kr.title}"):
                c1, c2, c3 = st.columns([0.2, 0.2, 0.6])
                c1.metric("Baseline", f"{kr.baseline} {kr.unit}")
                c2.metric("Target", f"{kr.target} {kr.unit}")
                
                with c3:
                    st.markdown("**Iniciativas / Épicas clave:**")
                    for init in kr.initiatives:
                        st.markdown(f"- {init}")
                
                # Barra de progreso visual (decorativa, asumiendo 0% de avance inicial)
                st.markdown(
                    f'<div style="width:100%;background:#e5e7eb;height:8px;border-radius:4px;margin-top:1rem;overflow:hidden;">'
                    f'<div style="width:5%;background:#10b981;height:100%;"></div>'
                    f'</div>'
                    f'<div style="display:flex;justify-content:space-between;font-size:0.7rem;color:#9ca3af;margin-top:4px;">'
                    f'<span>{kr.baseline}</span><span>{kr.target}</span></div>',
                    unsafe_allow_html=True
                )


def _okr_to_markdown(okrset) -> str:
    """Genera la versión exportable a Markdown."""
    lines = [
        f"# OKRs: {okrset.timeframe}",
        f"**Alineación Estratégica:** {okrset.strategic_alignment}",
        ""
    ]
    
    for i, obj in enumerate(okrset.objectives, 1):
        lines.append(f"## Objetivo {i}: {obj.title}")
        lines.append(f"*{obj.description}*\n")
        
        for j, kr in enumerate(obj.key_results, 1):
            lines.append(f"### KR {i}.{j}: {kr.title}")
            lines.append(f"- **Métrica:** {kr.metric_name}")
            lines.append(f"- **De:** {kr.baseline} {kr.unit} **A:** {kr.target} {kr.unit}")
            lines.append(f"- **Iniciativas propuestas:**")
            for init in kr.initiatives:
                lines.append(f"  - {init}")
            lines.append("")
        lines.append("---\n")
        
    return "\n".join(lines)


def render_okr_generator():
    llm = get_llm_service()

    st.markdown("""<h2 style='margin-bottom:0.2rem;'>🎯 Generador de OKRs</h2>
<p style='color:#6b7280;margin-top:0;'>Traduce tu visión en Objetivos inspiracionales y Key Results medibles, listos para ejecutar.</p>""",
        unsafe_allow_html=True
    )

    # ── PANTALLA 1: FORMULARIO ─────────────────────────────────────────────────
    if "okr_set" not in st.session_state:
        with st.form("okr_form"):
            st.markdown("#### Define el foco del ciclo")

            col_time, col_focus = st.columns([0.3, 0.7])
            with col_time:
                timeframe = st.text_input(
                    "⏱️ Ciclo temporal",
                    placeholder="ej: Q3 2026, H2, Anual..."
                )
            with col_focus:
                strategic_focus = st.text_input(
                    "🚀 Reto o Foco Estratégico",
                    placeholder="ej: Escalar ventas B2B, Reducir el churn, Lanzar v2..."
                )

            project_context = st.text_area(
                "📝 Contexto del Proyecto/Producto",
                placeholder="Describe brevemente el estado actual de tu producto, mercado o equipo para dar contexto a la IA.",
                height=120
            )

            submitted = st.form_submit_button(
                "🎯 Generar OKRs",
                type="primary",
                use_container_width=True
            )

        if submitted:
            if not strategic_focus or not timeframe:
                st.warning("Por favor, rellena el ciclo temporal y el foco estratégico.")
            else:
                with st.spinner("🧠 Diseñando estructura de OKRs... (puede tardar 10-15 segundos)"):
                    try:
                        okrset = llm.generate_okrs(
                            project_context=project_context or "Sin contexto adicional.",
                            timeframe=timeframe,
                            strategic_focus=strategic_focus,
                        )
                        if okrset:
                            st.session_state["okr_set"] = okrset
                            st.rerun()
                        else:
                            st.error("❌ El modelo no devolvió una estructura JSON válida. Inténtalo de nuevo.")
                    except Exception as e:
                        st.error(f"❌ Error al generar los OKRs: {e}")

    # ── PANTALLA 2: RESULTADOS ─────────────────────────────────────────────────
    else:
        okrset = st.session_state["okr_set"]

        col_back, col_title, col_export = st.columns([0.2, 0.6, 0.2])
        with col_back:
            if st.button("← Nuevo ciclo", type="secondary"):
                del st.session_state["okr_set"]
                st.rerun()
        with col_title:
            st.markdown(
                f'<div style="text-align:center;">'
                f'<h3 style="margin:0;color:#1f2937;">OKRs para {okrset.timeframe}</h3>'
                f'<p style="font-size:0.85rem;color:#6b7280;margin:0;">{okrset.strategic_alignment}</p>'
                f'</div>',
                unsafe_allow_html=True
            )
        with col_export:
            # Botón de exportar a Markdown
            okr_md = _okr_to_markdown(okrset)
            st.download_button(
                "⬇️ Exportar .md",
                data=okr_md,
                file_name=f"okrs_{okrset.timeframe.replace(' ','_')}.md",
                mime="text/markdown",
                use_container_width=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

        for i, obj in enumerate(okrset.objectives, 1):
            _render_okr_card(i, obj)

