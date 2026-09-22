export default function ProblemStatement() {
  return (
    <section className="w-full py-20 bg-surface-canvas">
      <div className="max-w-[1200px] mx-auto px-margin-mobile md:px-margin">
        <div className="max-w-2xl mb-12">
          <span className="font-label-meta text-label-meta uppercase tracking-wider text-text-muted block mb-2">Fricción Estratégica</span>
          <h2 className="font-headline-lg text-headline-lg font-semibold text-text-primary tracking-tight mb-4">
            ¿Por qué las decisiones de producto se sienten desconectadas de la ejecución?
          </h2>
          <p className="font-body-lg text-body-lg text-text-secondary">
            Las ideas están dispersas en notas. Los requisitos en documentos obsoletos. Las prioridades cambian por opiniones sin datos. Y la ejecución técnica avanza a ciegas sin contexto de negocio.
          </p>
        </div>
        
        {/* Comparison Split Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* El caos habitual */}
          <div className="p-6 md:p-8 bg-surface-card border border-border-subtle rounded-lg flex flex-col justify-between">
            <div>
              <div className="flex items-center justify-between pb-4 border-b border-border-subtle mb-6">
                <span className="font-label-code text-label-code font-bold uppercase text-text-muted">El flujo fragmentado tradicional</span>
                <span className="material-symbols-outlined text-text-muted text-[20px]">close</span>
              </div>
              <ul className="space-y-4">
                <li className="flex items-start gap-3">
                  <span className="material-symbols-outlined text-text-muted text-[18px] mt-0.5">description</span>
                  <div>
                    <h4 className="font-body-md font-semibold text-text-primary">PRDs estáticos desactualizados</h4>
                    <p className="font-body-sm text-text-secondary mt-0.5">Documentos kilométricos en Notion o Docs que nadie lee y quedan obsoletos a los tres días del kickoff.</p>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <span className="material-symbols-outlined text-text-muted text-[18px] mt-0.5">record_voice_over</span>
                  <div>
                    <h4 className="font-body-md font-semibold text-text-primary">Priorización por jerarquía (HiPPO)</h4>
                    <p className="font-body-sm text-text-secondary mt-0.5">La persona con el sueldo más alto decide el roadmap basándose en intuiciones sin cálculo de esfuerzo ni impacto medible.</p>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <span className="material-symbols-outlined text-text-muted text-[18px] mt-0.5">link_off</span>
                  <div>
                    <h4 className="font-body-md font-semibold text-text-primary">Ruptura entre negocio e ingeniería</h4>
                    <p className="font-body-sm text-text-secondary mt-0.5">Los desarrolladores ejecutan tickets sin saber qué KPI resuelven ni cuál es la hipótesis que están validando en producción.</p>
                  </div>
                </li>
              </ul>
            </div>
            <div className="mt-8 pt-4 border-t border-border-subtle font-label-code text-[11px] text-text-muted">
              Resultado: Deuda de producto masiva y entregas que nadie adopta.
            </div>
          </div>
          
          {/* Con Sprinto AI HUB */}
          <div className="p-6 md:p-8 bg-surface-card border border-border-strong rounded-lg flex flex-col justify-between shadow-sm relative">
            <div className="absolute -top-3 right-6 px-2.5 py-0.5 rounded bg-text-primary text-surface-card font-label-code text-[10px] tracking-wider uppercase">
              ESTÁNDAR SPRINTO
            </div>
            <div>
              <div className="flex items-center justify-between pb-4 border-b border-border-subtle mb-6">
                <span className="font-label-code text-label-code font-bold uppercase text-accent-mint-deep">Con Sprinto AI HUB</span>
                <span className="material-symbols-outlined text-accent-mint-deep text-[20px]">check_circle</span>
              </div>
              <ul className="space-y-4">
                <li className="flex items-start gap-3">
                  <span className="material-symbols-outlined text-accent-mint-deep text-[18px] mt-0.5">schema</span>
                  <div>
                    <h4 className="font-body-md font-semibold text-text-primary">Capa unificada de decisión técnica</h4>
                    <p className="font-body-sm text-text-secondary mt-0.5">Casos de uso estructurados con datos empíricos de analítica, feedback clasificado y métricas base en un solo modelo vivo.</p>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <span className="material-symbols-outlined text-accent-mint-deep text-[18px] mt-0.5">tune</span>
                  <div>
                    <h4 className="font-body-md font-semibold text-text-primary">Scoring cuantitativo auditable</h4>
                    <p className="font-body-sm text-text-secondary mt-0.5">Frameworks RICE, MoSCoW y Kano calculados con rigor de ingeniería, intervalos de confianza y estimaciones de esfuerzo reales.</p>
                  </div>
                </li>
                <li className="flex items-start gap-3">
                  <span className="material-symbols-outlined text-accent-mint-deep text-[18px] mt-0.5">sync_alt</span>
                  <div>
                    <h4 className="font-body-md font-semibold text-text-primary">Trazabilidad determinista hasta el commit</h4>
                    <p className="font-body-sm text-text-secondary mt-0.5">Descomposición instantánea en épicas con criterios Gherkin enviadas directamente al tablero de desarrollo de tu equipo.</p>
                  </div>
                </li>
              </ul>
            </div>
            <div className="mt-8 pt-4 border-t border-border-subtle font-label-code text-[11px] text-text-primary font-medium flex items-center gap-1.5">
              <span className="w-1.5 h-1.5 rounded-full bg-accent-mint-deep"></span>
              Resultado: 100% de los sprints respaldados por una hipótesis validada.
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
