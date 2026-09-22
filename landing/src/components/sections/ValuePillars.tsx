export default function ValuePillars() {
  return (
    <section className="w-full py-20 bg-surface-card border-t border-border-subtle">
      <div className="max-w-[1200px] mx-auto px-margin-mobile md:px-margin">
        <div className="max-w-xl mb-14">
          <span className="font-label-meta text-label-meta uppercase tracking-wider text-text-muted block mb-2">El Sistema de Decisión</span>
          <h2 className="font-headline-lg text-headline-lg font-semibold text-text-primary tracking-tight">
            Cuatro pilares para diseñar productos con rigor técnico.
          </h2>
        </div>
        
        {/* Bento Grid 4 Columns */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {/* Pillar 01 */}
          <div className="p-6 bg-surface-canvas border border-border-subtle rounded-lg flex flex-col justify-between hover:border-border-strong transition-colors">
            <div>
              <div className="flex items-center justify-between mb-4">
                <span className="font-label-code text-sm font-bold text-text-primary">01 //</span>
                <span className="font-label-code text-[11px] uppercase tracking-wider text-text-muted">FASE DISCOVERY</span>
              </div>
              <h3 className="font-headline-sm text-headline-sm font-semibold text-text-primary mb-2">DESCUBRIR</h3>
              <p className="font-body-sm text-body-sm text-text-secondary leading-relaxed mb-4">
                Convierte problemas e ideas en casos de uso estructurados. Extrae insights de feedback disperso y categoriza hipótesis con impacto validable sin perderse en transcripciones infinitas.
              </p>
            </div>
            <div className="pt-4 border-t border-border-subtle/80 flex items-center justify-between text-xs">
              <span className="font-label-code text-text-muted">UC-Generator v2</span>
              <span className="material-symbols-outlined text-text-secondary text-[16px]">travel_explore</span>
            </div>
          </div>
          
          {/* Pillar 02 */}
          <div className="p-6 bg-surface-canvas border border-border-subtle rounded-lg flex flex-col justify-between hover:border-border-strong transition-colors">
            <div>
              <div className="flex items-center justify-between mb-4">
                <span className="font-label-code text-sm font-bold text-text-primary">02 //</span>
                <span className="font-label-code text-[11px] uppercase tracking-wider text-text-muted">FASE PRIORIZACIÓN</span>
              </div>
              <h3 className="font-headline-sm text-headline-sm font-semibold text-text-primary mb-2">PRIORIZAR</h3>
              <p className="font-body-sm text-body-sm text-text-secondary leading-relaxed mb-4">
                Frameworks cuantitativos integrados (RICE, MoSCoW, Kano). Compara iniciativas con ponderaciones reales de esfuerzo técnico, impacto y alcance para mitigar sesgos de equipo.
              </p>
            </div>
            <div className="pt-4 border-t border-border-subtle/80 flex items-center justify-between text-xs">
              <span className="font-label-code text-text-muted">Algoritmos RICE/Kano</span>
              <span className="material-symbols-outlined text-text-secondary text-[16px]">balance</span>
            </div>
          </div>
          
          {/* Pillar 03 */}
          <div className="p-6 bg-surface-canvas border border-border-subtle rounded-lg flex flex-col justify-between hover:border-border-strong transition-colors">
            <div>
              <div className="flex items-center justify-between mb-4">
                <span className="font-label-code text-sm font-bold text-text-primary">03 //</span>
                <span className="font-label-code text-[11px] uppercase tracking-wider text-text-muted">FASE ROADMAP</span>
              </div>
              <h3 className="font-headline-sm text-headline-sm font-semibold text-text-primary mb-2">PLANIFICAR</h3>
              <p className="font-body-sm text-body-sm text-text-secondary leading-relaxed mb-4">
                De la oportunidad a la épica de ingeniería. Descompone necesidades de negocio en requerimientos técnicos, criterios de aceptación y dependencias antes de tocar una sola línea de código.
              </p>
            </div>
            <div className="pt-4 border-t border-border-subtle/80 flex items-center justify-between text-xs">
              <span className="font-label-code text-text-muted">Gherkin Specs & Epics</span>
              <span className="material-symbols-outlined text-text-secondary text-[16px]">account_tree</span>
            </div>
          </div>
          
          {/* Pillar 04 */}
          <div className="p-6 bg-surface-canvas border border-border-subtle rounded-lg flex flex-col justify-between hover:border-border-strong transition-colors">
            <div>
              <div className="flex items-center justify-between mb-4">
                <span className="font-label-code text-sm font-bold text-text-primary">04 //</span>
                <span className="font-label-code text-[11px] uppercase tracking-wider text-text-muted">FASE TELEMETRÍA</span>
              </div>
              <h3 className="font-headline-sm text-headline-sm font-semibold text-text-primary mb-2">MEDIR</h3>
              <p className="font-body-sm text-body-sm text-text-secondary leading-relaxed mb-4">
                Dashboard de Product Health en tiempo real. Visualiza cuellos de botella en delivery, desalineación de prioridades y riesgos de deuda de producto antes de que sea tarde.
              </p>
            </div>
            <div className="pt-4 border-t border-border-subtle/80 flex items-center justify-between text-xs">
              <span className="font-label-code text-text-muted">Health Index 0-100</span>
              <span className="material-symbols-outlined text-text-secondary text-[16px]">vital_signs</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
