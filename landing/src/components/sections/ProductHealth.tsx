export default function ProductHealth() {
  return (
    <section className="w-full py-20 bg-surface-canvas">
      <div className="max-w-[1200px] mx-auto px-margin-mobile md:px-margin">
        <div className="max-w-xl mb-12">
          <span className="font-label-meta text-label-meta uppercase tracking-wider text-text-muted block mb-2">Observabilidad de Producto</span>
          <h2 className="font-headline-lg text-headline-lg font-semibold text-text-primary tracking-tight mb-3">
            Monitorea la salud de tus decisiones y el pulso del delivery.
          </h2>
          <p className="font-body-md text-text-secondary">
            No midas únicamente velocidad de tickets completados. Mide si lo que estás construyendo responde a hipótesis estratégicas validadas.
          </p>
        </div>
        
        {/* Health Dashboard Interface Component */}
        <div className="bg-surface-card border border-border-subtle rounded-lg shadow-sm p-6">
          {/* Top Metrics Row */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4 pb-6 border-b border-border-subtle">
            <div className="p-4 bg-surface-canvas rounded border border-border-subtle">
              <div className="flex items-center justify-between text-xs mb-1">
                <span className="font-label-meta text-[10px] uppercase text-text-muted">Health Score Global</span>
                <span className="font-label-code text-accent-mint-deep font-semibold">+4% vs Q3</span>
              </div>
              <div className="flex items-baseline gap-2">
                <span className="font-label-code text-3xl font-bold text-text-primary">91</span>
                <span className="font-label-code text-xs text-text-muted">/ 100</span>
              </div>
              <span className="font-body-sm text-[11px] text-text-secondary block mt-1">Calidad de alineación óptima</span>
            </div>
            
            <div className="p-4 bg-surface-canvas rounded border border-border-subtle">
              <div className="flex items-center justify-between text-xs mb-1">
                <span className="font-label-meta text-[10px] uppercase text-text-muted">Delivery Alignment</span>
                <span className="font-label-code text-text-secondary">Meta: &gt;80%</span>
              </div>
              <div className="flex items-baseline gap-2">
                <span className="font-label-code text-3xl font-bold text-text-primary">89%</span>
              </div>
              <span className="font-body-sm text-[11px] text-text-secondary block mt-1">Tiempo en iniciativas Must-Have</span>
            </div>
            
            <div className="p-4 bg-surface-canvas rounded border border-border-subtle">
              <div className="flex items-center justify-between text-xs mb-1">
                <span className="font-label-meta text-[10px] uppercase text-text-muted">Time-To-Spec</span>
                <span className="font-label-code text-accent-mint-deep font-semibold">-83% tiempo</span>
              </div>
              <div className="flex items-baseline gap-2">
                <span className="font-label-code text-3xl font-bold text-text-primary">2.4</span>
                <span className="font-label-code text-xs text-text-muted">días</span>
              </div>
              <span className="font-body-sm text-[11px] text-text-secondary block mt-1">Vs. 14 días media del sector</span>
            </div>
            
            <div className="p-4 bg-surface-canvas rounded border border-border-subtle">
              <div className="flex items-center justify-between text-xs mb-1">
                <span className="font-label-meta text-[10px] uppercase text-text-muted">Scope Drift Index</span>
                <span className="font-label-code text-text-primary font-semibold">Bajo riesgo</span>
              </div>
              <div className="flex items-baseline gap-2">
                <span className="font-label-code text-3xl font-bold text-text-primary">4.8%</span>
              </div>
              <span className="font-body-sm text-[11px] text-text-secondary block mt-1">Desviación media de requerimientos</span>
            </div>
          </div>
          
          {/* Initiatives Status Breakdown & Pipeline Progress */}
          <div className="pt-6">
            <div className="flex items-center justify-between mb-4">
              <h4 className="font-headline-sm text-sm font-semibold text-text-primary">Estado de Iniciativas en Curso</h4>
              <span className="font-label-code text-xs text-text-muted">Total: 34 casos de uso rastreados</span>
            </div>
            
            {/* Progress Segmented Bar */}
            <div className="w-full h-3 rounded-full bg-surface-container overflow-hidden flex mb-4">
              <div className="h-full bg-text-muted" style={{ width: '15%' }} title="En Descubrimiento (15%)"></div>
              <div className="h-full bg-border-strong" style={{ width: '20%' }} title="En Validación (20%)"></div>
              <div className="h-full bg-primary-container" style={{ width: '30%' }} title="En Especificación (30%)"></div>
              <div className="h-full bg-accent-mint-deep" style={{ width: '35%' }} title="En Desarrollo Activo (35%)"></div>
            </div>
            
            {/* Legend Grid */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-xs font-body-sm">
              <div className="flex items-center gap-2">
                <span className="w-2.5 h-2.5 rounded-full bg-text-muted"></span>
                <div>
                  <span className="font-semibold text-text-primary">5</span>
                  <span className="text-text-secondary ml-1">En Descubrimiento</span>
                </div>
              </div>
              <div className="flex items-center gap-2">
                <span className="w-2.5 h-2.5 rounded-full bg-border-strong"></span>
                <div>
                  <span className="font-semibold text-text-primary">7</span>
                  <span className="text-text-secondary ml-1">En Validación</span>
                </div>
              </div>
              <div className="flex items-center gap-2">
                <span className="w-2.5 h-2.5 rounded-full bg-primary-container"></span>
                <div>
                  <span className="font-semibold text-text-primary">10</span>
                  <span className="text-text-secondary ml-1">En Especificación</span>
                </div>
              </div>
              <div className="flex items-center gap-2">
                <span className="w-2.5 h-2.5 rounded-full bg-accent-mint-deep"></span>
                <div>
                  <span className="font-semibold text-text-primary">12</span>
                  <span className="text-text-secondary ml-1">En Desarrollo Activo</span>
                </div>
              </div>
            </div>
            
            {/* Warning callout for backlog risk */}
            <div className="mt-6 p-3 bg-surface-canvas rounded border border-border-subtle flex items-center justify-between">
              <div className="flex items-center gap-2">
                <span className="material-symbols-outlined text-text-secondary text-[18px]">verified</span>
                <span className="font-body-sm text-xs text-text-primary">Backlog Risk: Solo 2 épicas huérfanas sin sponsor de negocio detectadas en el sprint actual.</span>
              </div>
              <a className="font-label-code text-xs text-text-primary font-semibold hover:underline" href="#">Auditar &rarr;</a>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
