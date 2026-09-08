"""
Vista del Canvas de Proyecto IA.

Genera un canvas estructurado de 8 bloques para definir un proyecto de IA,
presentado en un formato visual tipo documento ejecutivo.
"""
import streamlit as st
from src.data.cache import get_llm_service

# Colores por bloque del canvas
_BLOCK_COLORS = {
    "problema":  ("#fef3c7", "#92400e", "⚠️"),
    "solucion":  ("#ede9fe", "#5b21b6", "🧠"),
    "datos":     ("#dbeafe", "#1e40af", "🗄️"),
    "metricas":  ("#dcfce7", "#166534", "📊"),
    "equipo":    ("#fce7f3", "#9d174d", "👥"),
    "riesgos":   ("#fee2e2", "#991b1b", "⚠️"),
    "roadmap":   ("#f0f9ff", "#0369a1", "🗺️"),
    "valor":     ("#f0fdf4", "#14532d", "💰"),
}

_PROB_COLOR = {"Alta": "#dc2626", "Media": "#d97706", "Baja": "#16a34a"}
_PHASE_COLORS = ["#7c3aed", "#2563eb", "#0891b2", "#059669", "#d97706"]


def _section_header(title: str, icon: str, bg: str, color: str):
    st.markdown(
        f'<div style="background:{bg};border-left:4px solid {color};padding:0.6rem 1rem;'
        f'border-radius:6px;margin-bottom:0.8rem;">'
        f'<span style="font-weight:700;color:{color};font-size:1rem;">{icon} {title}</span>'
        f'</div>',
        unsafe_allow_html=True
    )


def _pill(text: str, bg: str = "#f3f4f6", color: str = "#374151") -> str:
    return (
        f'<span style="background:{bg};color:{color};padding:3px 10px;'
        f'border-radius:12px;font-size:0.8rem;font-weight:500;margin:2px;display:inline-block;">'
        f'{text}</span>'
    )


def render_canvas(canvas):
    """Renderiza el canvas completo en bloques visuales."""

    # ── Cabecera del Canvas ────────────────────────────────────────────────────
    st.markdown(
        f'<div style="background:linear-gradient(135deg,#7c3aed,#2563eb);'
        f'padding:1.5rem 2rem;border-radius:10px;color:white;margin-bottom:1.5rem;">'
        f'<div style="font-size:0.75rem;text-transform:uppercase;letter-spacing:2px;opacity:0.8;">Canvas de Proyecto IA</div>'
        f'<div style="font-size:1.6rem;font-weight:800;margin-top:4px;">{canvas.business_value[:80]}</div>'
        f'<div style="margin-top:0.5rem;opacity:0.9;font-size:0.9rem;">⏱ Duración total: {canvas.total_duration} &nbsp;·&nbsp; 💰 {canvas.estimated_budget}</div>'
        f'</div>',
        unsafe_allow_html=True
    )

    # ── Fila 1: Problema + Solución ───────────────────────────────────────────
    col1, col2 = st.columns(2, gap="medium")

    with col1:
        bg, color, icon = _BLOCK_COLORS["problema"]
        _section_header("Problema", icon, bg, color)
        st.markdown(f"**{canvas.problem_statement}**")
        st.caption(f"👤 Afectados: {canvas.affected_users}")
        st.markdown(f'<div style="background:#fef9c3;padding:0.5rem 0.8rem;border-radius:6px;font-size:0.875rem;margin-top:0.5rem;">💥 {canvas.current_pain}</div>', unsafe_allow_html=True)

    with col2:
        bg, color, icon = _BLOCK_COLORS["solucion"]
        _section_header("Solución IA", icon, bg, color)
        st.markdown(f"**{canvas.proposed_solution}**")
        st.markdown(f'<div style="background:{bg};padding:0.4rem 0.8rem;border-radius:6px;font-size:0.85rem;margin-top:0.5rem;color:{color};font-weight:600;">🔬 {canvas.ai_approach}</div>', unsafe_allow_html=True)
        if canvas.alternatives_considered:
            with st.expander("Alternativas descartadas"):
                for alt in canvas.alternatives_considered:
                    st.markdown(f"- {alt}")

    st.markdown("---")

    # ── Fila 2: Datos + Métricas ──────────────────────────────────────────────
    col3, col4 = st.columns(2, gap="medium")

    with col3:
        bg, color, icon = _BLOCK_COLORS["datos"]
        _section_header("Datos", icon, bg, color)
        st.markdown(f"📦 **Volumen:** {canvas.data_volume}")
        st.markdown("**Fuentes:**")
        for ds in canvas.data_sources:
            st.markdown(f"- {ds}")
        if canvas.data_quality_risks:
            st.markdown("**⚠️ Riesgos de datos:**")
            for r in canvas.data_quality_risks:
                st.markdown(f'<div style="color:#991b1b;font-size:0.85rem;">• {r}</div>', unsafe_allow_html=True)

    with col4:
        bg, color, icon = _BLOCK_COLORS["metricas"]
        _section_header("Métricas de Éxito", icon, bg, color)
        st.markdown(
            f'<div style="background:{bg};border:1px solid {color};padding:0.8rem;border-radius:8px;">'
            f'<div style="font-size:0.7rem;color:{color};text-transform:uppercase;font-weight:700;">KPI Principal</div>'
            f'<div style="font-size:1rem;font-weight:700;margin-top:2px;">{canvas.primary_kpi}</div>'
            f'</div>',
            unsafe_allow_html=True
        )
        m1, m2 = st.columns(2)
        m1.metric("Baseline", canvas.baseline)
        m2.metric("Objetivo", canvas.target)
        if canvas.secondary_kpis:
            st.markdown("**KPIs secundarios:**")
            pills_html = " ".join([_pill(k, "#dcfce7", "#166534") for k in canvas.secondary_kpis])
            st.markdown(pills_html, unsafe_allow_html=True)

    st.markdown("---")

    # ── Fila 3: Equipo + Riesgos ──────────────────────────────────────────────
    col5, col6 = st.columns(2, gap="medium")

    with col5:
        bg, color, icon = _BLOCK_COLORS["equipo"]
        _section_header("Equipo y Recursos", icon, bg, color)
        for role in canvas.team_needed:
            st.markdown(f"👤 {role}")
        st.markdown(f"🖥️ **Infraestructura:** {canvas.infrastructure}")

    with col6:
        bg, color, icon = _BLOCK_COLORS["riesgos"]
        _section_header("Riesgos", icon, bg, color)
        for risk in canvas.risks:
            prob = risk.get("probability", "Media")
            prob_color = _PROB_COLOR.get(prob, "#d97706")
            with st.container(border=True):
                st.markdown(
                    f'<span style="font-weight:600;">{risk.get("risk","")}</span> &nbsp;'
                    f'<span style="background:{prob_color};color:white;padding:1px 8px;border-radius:10px;font-size:0.75rem;">'
                    f'P:{prob}</span> &nbsp;'
                    f'<span style="background:#374151;color:white;padding:1px 8px;border-radius:10px;font-size:0.75rem;">'
                    f'I:{risk.get("impact","?")}</span>',
                    unsafe_allow_html=True
                )
                st.caption(f"🛡️ {risk.get('mitigation','')}")

    st.markdown("---")

    # ── Roadmap ───────────────────────────────────────────────────────────────
    bg, color, icon = _BLOCK_COLORS["roadmap"]
    _section_header("Roadmap del Proyecto", icon, bg, color)

    phase_cols = st.columns(len(canvas.phases))
    for i, (phase, col) in enumerate(zip(canvas.phases, phase_cols)):
        ph_color = _PHASE_COLORS[i % len(_PHASE_COLORS)]
        with col:
            st.markdown(
                f'<div style="background:{ph_color};color:white;padding:0.8rem;border-radius:8px;text-align:center;min-height:80px;">'
                f'<div style="font-size:0.7rem;opacity:0.8;text-transform:uppercase;">Fase {i+1}</div>'
                f'<div style="font-weight:700;margin:4px 0;">{phase.get("name","")}</div>'
                f'<div style="font-size:0.8rem;opacity:0.9;">⏱ {phase.get("duration","")}</div>'
                f'</div>',
                unsafe_allow_html=True
            )
            st.markdown("")
            for d in phase.get("deliverables", []):
                st.markdown(f"✅ {d}")

    st.markdown("---")

    # ── Valor de Negocio + ROI ────────────────────────────────────────────────
    bg, color, icon = _BLOCK_COLORS["valor"]
    _section_header("Valor de Negocio", icon, bg, color)
    vcol1, vcol2 = st.columns([2, 1])
    with vcol1:
        st.markdown(canvas.business_value)
    with vcol2:
        st.markdown(
            f'<div style="background:{bg};border:2px solid {color};padding:1rem;border-radius:10px;text-align:center;">'
            f'<div style="font-size:0.7rem;text-transform:uppercase;color:{color};font-weight:700;">ROI Estimado</div>'
            f'<div style="font-size:1rem;font-weight:700;margin-top:6px;">{canvas.roi_estimate}</div>'
            f'</div>',
            unsafe_allow_html=True
        )


def render_ai_canvas():
    llm = get_llm_service()

    st.markdown("""<h2 style='margin-bottom:0.2rem;'>📋 Canvas de Proyecto IA</h2>
<p style='color:#6b7280;margin-top:0;'>Define tu proyecto de IA con rigor. La herramienta genera un documento ejecutivo listo para presentar a stakeholders.</p>""",
        unsafe_allow_html=True
    )

    # ── PANTALLA 1: FORMULARIO ─────────────────────────────────────────────────
    if "ai_canvas" not in st.session_state:
        with st.form("canvas_form"):
            st.markdown("#### Describe tu proyecto")

            project_name = st.text_input(
                "🏷️ Nombre del proyecto",
                placeholder="ej: Predictor de churn de clientes, Asistente IA para soporte técnico..."
            )

            objective = st.text_area(
                "🎯 Objetivo principal",
                placeholder="¿Qué quieres conseguir con este proyecto de IA? ¿Qué problema concreto resuelve?",
                height=100
            )

            col1, col2 = st.columns(2)
            with col1:
                sector = st.text_input(
                    "🏭 Sector / industria",
                    placeholder="ej: Banca retail, Manufactura, eCommerce..."
                )
            with col2:
                constraints = st.text_input(
                    "🚧 Restricciones conocidas",
                    placeholder="ej: Presupuesto <50k€, sin GPU, plazo 6 meses, datos en silos..."
                )

            context = st.text_area(
                "📝 Contexto adicional (opcional)",
                placeholder="Infraestructura actual, intentos previos, regulaciones, datos disponibles...",
                height=90
            )

            submitted = st.form_submit_button(
                "📋 Generar Canvas con IA",
                type="primary",
                use_container_width=True
            )

        if submitted:
            if not project_name or not objective:
                st.warning("Rellena al menos el nombre del proyecto y el objetivo.")
            else:
                with st.spinner("🧠 Generando el Canvas de Proyecto IA... (puede tardar 15-20 segundos)"):
                    try:
                        canvas = llm.generate_ai_canvas(
                            project_name=project_name,
                            objective=objective,
                            sector=sector or "No especificado",
                            context=context or "Sin información adicional",
                            constraints=constraints or "Sin restricciones conocidas",
                        )
                        st.session_state["ai_canvas"] = canvas
                        st.session_state["ai_canvas_name"] = project_name
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ Error al generar el canvas: {e}")

    # ── PANTALLA 2: CANVAS ─────────────────────────────────────────────────────
    else:
        canvas = st.session_state["ai_canvas"]
        project_name = st.session_state.get("ai_canvas_name", "Proyecto IA")

        col_back, col_title, col_export = st.columns([0.2, 0.6, 0.2])
        with col_back:
            if st.button("← Nuevo canvas", type="secondary"):
                del st.session_state["ai_canvas"]
                del st.session_state["ai_canvas_name"]
                st.rerun()
        with col_title:
            st.markdown(
                f'<p style="text-align:center;font-weight:700;font-size:1.1rem;padding-top:0.3rem;">📋 {project_name}</p>',
                unsafe_allow_html=True
            )
        with col_export:
            # Botón de exportar como texto plano (Markdown)
            canvas_md = _canvas_to_markdown(canvas, project_name)
            st.download_button(
                "⬇️ Exportar .md",
                data=canvas_md,
                file_name=f"canvas_{project_name.lower().replace(' ','_')}.md",
                mime="text/markdown",
                use_container_width=True,
            )

        st.markdown("---")
        render_canvas(canvas)


def _canvas_to_markdown(canvas, project_name: str) -> str:
    """Genera una versión Markdown exportable del canvas."""
    lines = [
        f"# Canvas de Proyecto IA: {project_name}",
        "",
        "## ⚠️ Problema",
        canvas.problem_statement,
        f"- **Afectados:** {canvas.affected_users}",
        f"- **Impacto actual:** {canvas.current_pain}",
        "",
        "## 🧠 Solución IA",
        canvas.proposed_solution,
        f"- **Enfoque:** {canvas.ai_approach}",
        "",
        "## 🗄️ Datos",
        f"- **Volumen:** {canvas.data_volume}",
        "**Fuentes:**",
    ] + [f"  - {ds}" for ds in canvas.data_sources] + [
        "",
        "## 📊 Métricas de Éxito",
        f"- **KPI Principal:** {canvas.primary_kpi}",
        f"- **Baseline:** {canvas.baseline}",
        f"- **Objetivo:** {canvas.target}",
    ] + [f"- {k}" for k in canvas.secondary_kpis] + [
        "",
        "## 👥 Equipo y Recursos",
    ] + [f"- {r}" for r in canvas.team_needed] + [
        f"- **Infraestructura:** {canvas.infrastructure}",
        f"- **Presupuesto estimado:** {canvas.estimated_budget}",
        "",
        "## ⚠️ Riesgos",
    ] + [f"- **{r['risk']}** (P:{r.get('probability','?')} / I:{r.get('impact','?')}): {r.get('mitigation','')}" for r in canvas.risks] + [
        "",
        "## 🗺️ Roadmap",
        f"**Duración total:** {canvas.total_duration}",
    ] + [f"\n### Fase {i+1}: {p['name']} ({p['duration']})\n" + "\n".join([f"- {d}" for d in p.get('deliverables', [])]) for i, p in enumerate(canvas.phases)] + [
        "",
        "## 💰 Valor de Negocio",
        canvas.business_value,
        f"- **ROI estimado:** {canvas.roi_estimate}",
    ]
    return "\n".join(lines)
