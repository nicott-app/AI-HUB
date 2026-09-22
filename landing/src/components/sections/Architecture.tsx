export default function Architecture() {
  return (
    <section className="w-full py-20 bg-surface-card border-t border-border-subtle">
      <div className="max-w-[1200px] mx-auto px-margin-mobile md:px-margin">
        <div className="max-w-2xl mb-14 text-center mx-auto">
          <span className="font-label-meta text-label-meta uppercase tracking-wider text-text-muted block mb-2">Arquitectura del Ecosistema</span>
          <h2 className="font-headline-lg text-headline-lg font-semibold text-text-primary tracking-tight mb-3">
            Del qué y por qué al cómo y cuándo.
          </h2>
          <p className="font-body-md text-text-secondary">
            La suite Sprinto une la toma de decisiones estratégicas con la ejecución de alta velocidad en ingeniería. Dos herramientas especializadas, una sola fuente de verdad.
          </p>
        </div>
        
        {/* Architectural Workflow Diagram */}
        <div className="bg-surface-canvas border border-border-subtle rounded-lg p-6 md:p-8">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 relative">
            {/* Box 1: Sprinto AI HUB */}
            <div className="p-6 bg-surface-card border border-border-strong rounded-lg flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between pb-3 border-b border-border-subtle mb-4">
                  <div className="flex items-center gap-2">
                    <span className="w-2.5 h-2.5 rounded-full bg-accent-mint-deep"></span>
                    <span className="font-label-code text-sm font-bold text-text-primary">SPRINTO AI HUB</span>
                  </div>
                  <span className="font-label-code text-[11px] text-text-muted">Capa Estratégica</span>
                </div>
                <p className="font-body-sm text-text-secondary mb-6">
                  Espacio para Product Managers, Tech Leads y Stakeholders. Foco permanente en el valor de negocio y el impacto validable.
                </p>
                {/* Inner Steps */}
                <div className="space-y-3 font-label-code text-xs">
                  <div className="p-2.5 bg-surface-canvas rounded border border-border-subtle flex items-center justify-between">
                    <span>1. Captura de problemas & feedback</span>
                    <span className="text-text-muted">&rarr;</span>
                  </div>
                  <div className="p-2.5 bg-surface-canvas rounded border border-border-subtle flex items-center justify-between">
                    <span>2. Casos de uso estructurados con IA</span>
                    <span className="text-text-muted">&rarr;</span>
                  </div>
                  <div className="p-2.5 bg-surface-canvas rounded border border-border-subtle flex items-center justify-between">
                    <span>3. Matriz de Priorización (RICE/MoSCoW)</span>
                    <span className="text-text-muted">&rarr;</span>
                  </div>
                  <div className="p-2.5 bg-surface-canvas rounded border border-border-strong bg-primary-container/20 flex items-center justify-between font-semibold text-text-primary">
                    <span>4. Épica Técnica con criterios Gherkin</span>
                    <span className="text-accent-mint-deep font-bold">&#10003;</span>
                  </div>
                </div>
              </div>
              <div className="mt-6 pt-4 border-t border-border-subtle font-label-code text-[11px] text-text-muted">
                Métricas clave: ROI de Feature, Cobertura de Hipótesis, Alignment Score.
              </div>
            </div>
            
            {/* Box 2: Sprinto Ticketing / Board */}
            <div className="p-6 bg-surface-card border border-border-subtle rounded-lg flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between pb-3 border-b border-border-subtle mb-4">
                  <div className="flex items-center gap-2">
                    <span className="w-2.5 h-2.5 rounded-full bg-text-primary"></span>
                    <span className="font-label-code text-sm font-bold text-text-primary">SPRINTO TICKETING / BOARD</span>
                  </div>
                  <span className="font-label-code text-[11px] text-text-muted">Capa de Ejecución</span>
                </div>
                <p className="font-body-sm text-text-secondary mb-6">
                  Espacio para Ingenieros de Software, QA y DevOps. Foco ininterrumpido en la velocidad de delivery y la calidad del código.
                </p>
                {/* Inner Steps */}
                <div className="space-y-3 font-label-code text-xs">
                  <div className="p-2.5 bg-surface-canvas rounded border border-border-subtle flex items-center justify-between">
                    <span>1. Descomposición automática en tickets</span>
                    <span className="text-text-muted">&rarr;</span>
                  </div>
                  <div className="p-2.5 bg-surface-canvas rounded border border-border-subtle flex items-center justify-between">
                    <span>2. Asignación por capacidad y estimación</span>
                    <span className="text-text-muted">&rarr;</span>
                  </div>
                  <div className="p-2.5 bg-surface-canvas rounded border border-border-subtle flex items-center justify-between">
                    <span>3. Sprints ágiles vinculados a ramas Git</span>
                    <span className="text-text-muted">&rarr;</span>
                  </div>
                  <div className="p-2.5 bg-surface-canvas rounded border border-border-subtle flex items-center justify-between">
                    <span>4. Release a producción & CI/CD feedback</span>
                    <span className="text-text-primary font-bold">&#10003;</span>
                  </div>
                </div>
              </div>
              <div className="mt-6 pt-4 border-t border-border-subtle font-label-code text-[11px] text-text-muted">
                Métricas clave: Cycle Time, Lead Time, DORA metrics, Burndown.
              </div>
            </div>
          </div>
          
          {/* Sync Bridge Callout */}
          <div className="mt-6 p-4 rounded bg-surface-card border border-border-strong flex flex-col sm:flex-row items-center justify-between gap-4 text-center sm:text-left">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 rounded bg-primary-container/30 border border-accent-mint-deep/30 flex items-center justify-center shrink-0">
                <span className="material-symbols-outlined text-text-primary text-[18px]">sync_alt</span>
              </div>
              <div>
                <span className="font-headline-sm text-sm font-semibold text-text-primary block">Sincronización Bidireccional Continua (&lt;1s)</span>
                <span className="font-body-sm text-xs text-text-secondary">Cuando una épica avanza en el tablero técnico, el Product Health del Hub se recalcula automáticamente.</span>
              </div>
            </div>
            <span className="font-label-code text-xs text-text-primary font-medium shrink-0 px-3 py-1 bg-surface-canvas rounded border border-border-subtle">
              Sync State: HEALTHY
            </span>
          </div>
        </div>
      </div>
    </section>
  );
}
