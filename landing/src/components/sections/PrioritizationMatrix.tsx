export default function PrioritizationMatrix() {
  return (
    <section className="w-full py-20 bg-surface-card border-t border-border-subtle">
      <div className="max-w-[1200px] mx-auto px-margin-mobile md:px-margin">
        <div className="flex flex-col md:flex-row md:items-end justify-between mb-12 gap-4">
          <div className="max-w-xl">
            <span className="font-label-meta text-label-meta uppercase tracking-wider text-text-muted block mb-2">Frameworks de Decisión</span>
            <h2 className="font-headline-lg text-headline-lg font-semibold text-text-primary tracking-tight">
              Pasa de opiniones subjetivas a decisiones estructuradas.
            </h2>
          </div>
          <p className="font-body-md text-text-secondary max-w-md">
            Sprinto AI HUB no pretende eliminar el juicio humano, sino proporcionarle un marco analítico objetivo que alinee a producto, diseño y negocio en cada sprint.
          </p>
        </div>
        
        {/* Framework Multi-View Container */}
        <div className="bg-surface-canvas border border-border-subtle rounded-lg p-5">
          {/* View Tabs Bar */}
          <div className="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-border-subtle mb-6">
            <div className="flex items-center gap-2">
              <button className="px-3 py-1.5 rounded bg-surface-card text-text-primary font-label-code text-xs font-semibold border border-border-strong shadow-sm flex items-center gap-1.5">
                <span className="w-2 h-2 rounded-full bg-accent-mint-deep"></span>
                RICE Matrix
              </button>
              <button className="px-3 py-1.5 rounded hover:bg-surface-card/70 text-text-secondary font-label-code text-xs transition-colors">
                MoSCoW Board
              </button>
              <button className="px-3 py-1.5 rounded hover:bg-surface-card/70 text-text-secondary font-label-code text-xs transition-colors">
                Kano Model Map
              </button>
            </div>
            <span className="font-label-code text-[11px] text-text-muted">Filtro: Todos los proyectos &bull; Vista Activa</span>
          </div>
          
          {/* 1. Technical Data Table: RICE Matrix View */}
          <div className="bg-surface-card border border-border-subtle rounded overflow-x-auto">
            <table className="w-full text-left text-xs border-collapse">
              <thead>
                <tr className="bg-surface-canvas/60 border-b border-border-subtle font-label-meta text-text-muted uppercase text-[10px] tracking-wider">
                  <th className="p-3 font-semibold">Iniciativa / Hipótesis</th>
                  <th className="p-3 font-semibold">Reach (Usuarios/mes)</th>
                  <th className="p-3 font-semibold">Impacto (1-5)</th>
                  <th className="p-3 font-semibold">Confianza</th>
                  <th className="p-3 font-semibold">Esfuerzo (Sprints)</th>
                  <th className="p-3 font-semibold text-right">RICE Score</th>
                  <th className="p-3 font-semibold text-center">Clasificación</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-border-subtle font-body-sm">
                <tr className="hover:bg-surface-canvas/40 transition-colors">
                  <td className="p-3">
                    <div className="font-medium text-text-primary">Optimización de onboarding B2B con auto-configuración</div>
                    <div className="font-label-code text-[11px] text-text-muted">UC-209 &bull; Growth Squad</div>
                  </td>
                  <td className="p-3 font-label-code text-text-secondary">4,200</td>
                  <td className="p-3 font-label-code text-text-secondary">4 (Muy alto)</td>
                  <td className="p-3">
                    <div className="flex items-center gap-1.5">
                      <div className="w-16 h-1.5 bg-surface-container rounded-full overflow-hidden">
                        <div className="h-full bg-accent-mint-deep w-[92%]"></div>
                      </div>
                      <span className="font-label-code text-[11px] text-text-primary">92%</span>
                    </div>
                  </td>
                  <td className="p-3 font-label-code text-text-secondary">2.0 sp</td>
                  <td className="p-3 font-label-code text-right font-bold text-text-primary">77.2</td>
                  <td className="p-3 text-center">
                    <span className="px-2 py-0.5 rounded bg-primary-container text-on-primary-fixed font-label-code text-[10px] font-semibold">MUST HAVE</span>
                  </td>
                </tr>
                <tr className="hover:bg-surface-canvas/40 transition-colors">
                  <td className="p-3">
                    <div className="font-medium text-text-primary">Conector nativo con Snowflake y BigQuery</div>
                    <div className="font-label-code text-text-muted">UC-184 &bull; Data Core</div>
                  </td>
                  <td className="p-3 font-label-code text-text-secondary">1,100</td>
                  <td className="p-3 font-label-code text-text-secondary">5 (Crítico)</td>
                  <td className="p-3">
                    <div className="flex items-center gap-1.5">
                      <div className="w-16 h-1.5 bg-surface-container rounded-full overflow-hidden">
                        <div className="h-full bg-accent-mint-deep w-[85%]"></div>
                      </div>
                      <span className="font-label-code text-[11px] text-text-primary">85%</span>
                    </div>
                  </td>
                  <td className="p-3 font-label-code text-text-secondary">4.5 sp</td>
                  <td className="p-3 font-label-code text-right font-bold text-text-primary">69.4</td>
                  <td className="p-3 text-center">
                    <span className="px-2 py-0.5 rounded bg-surface-container text-text-primary font-label-code text-[10px] font-semibold">SHOULD HAVE</span>
                  </td>
                </tr>
                <tr className="hover:bg-surface-canvas/40 transition-colors">
                  <td className="p-3">
                    <div className="font-medium text-text-primary">Exportación de reportes a PDF personalizado</div>
                    <div className="font-label-code text-text-muted">UC-177 &bull; Platform Ops</div>
                  </td>
                  <td className="p-3 font-label-code text-text-secondary">850</td>
                  <td className="p-3 font-label-code text-text-secondary">2 (Bajo)</td>
                  <td className="p-3">
                    <div className="flex items-center gap-1.5">
                      <div className="w-16 h-1.5 bg-surface-container rounded-full overflow-hidden">
                        <div className="h-full bg-border-strong w-[60%]"></div>
                      </div>
                      <span className="font-label-code text-[11px] text-text-secondary">60%</span>
                    </div>
                  </td>
                  <td className="p-3 font-label-code text-text-secondary">1.0 sp</td>
                  <td className="p-3 font-label-code text-right font-bold text-text-primary">42.5</td>
                  <td className="p-3 text-center">
                    <span className="px-2 py-0.5 rounded bg-surface-card text-text-secondary border border-border-subtle font-label-code text-[10px]">COULD HAVE</span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          
          {/* Framework Visual Summary */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-4">
            <div className="p-3 bg-surface-card rounded border border-border-subtle">
              <span className="font-label-meta text-[10px] uppercase tracking-wider text-text-muted block mb-1">RICE Formula Aplicada</span>
              <div className="font-label-code text-xs text-text-secondary">(Reach &times; Impact &times; Confidence) &divide; Effort</div>
            </div>
            <div className="p-3 bg-surface-card rounded border border-border-subtle">
              <span className="font-label-meta text-[10px] uppercase tracking-wider text-text-muted block mb-1">Capacidad de Sprint Asignada</span>
              <div className="font-label-code text-xs text-text-primary font-semibold">68% Must Have &bull; 24% Should &bull; 8% Could</div>
            </div>
            <div className="p-3 bg-surface-card rounded border border-border-subtle">
              <span className="font-label-meta text-[10px] uppercase tracking-wider text-text-muted block mb-1">Desviación de Confianza</span>
              <div className="font-label-code text-xs text-accent-mint-deep font-semibold">&plusmn;4.1% respecto al resultado real en Q3</div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
