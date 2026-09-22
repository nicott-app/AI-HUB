export default function AiPipeline() {
  return (
    <section className="w-full py-20 bg-surface-canvas" id="pipeline-ia">
      <div className="max-w-[1200px] mx-auto px-margin-mobile md:px-margin">
        <div className="max-w-2xl mb-12">
          <div className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-surface-card border border-border-subtle mb-3">
            <span className="w-1.5 h-1.5 rounded-full bg-text-primary"></span>
            <span className="font-label-code text-label-code text-text-primary uppercase tracking-wider">IA Determinista & Contextual</span>
          </div>
          <h2 className="font-headline-lg text-headline-lg font-semibold text-text-primary tracking-tight mb-3">
            La IA no inventa tu producto. Estructura tu criterio.
          </h2>
          <p className="font-body-lg text-body-lg text-text-secondary">
            Sin interfaces de chat genéricas ni respuestas vagas. La IA actúa como un motor de síntesis que procesa inputs desestructurados de negocio y los transforma en especificaciones accionables de ingeniería.
          </p>
        </div>
        
        {/* Walkthrough Card: The Transformation Pipeline */}
        <div className="bg-surface-card border border-border-subtle rounded-lg shadow-sm overflow-hidden">
          {/* Input Banner */}
          <div className="bg-surface-canvas/80 p-5 border-b border-border-subtle flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div className="flex items-start gap-3">
              <span className="material-symbols-outlined text-text-secondary text-[20px] mt-0.5">forum</span>
              <div>
                <span className="font-label-meta text-[11px] uppercase tracking-wider text-text-muted block">Input de Negocio / Feedback Crudo</span>
                <p className="font-headline-sm text-sm font-medium text-text-primary">
                  “Feedback recurrente en soporte y llamadas de ventas: Los clientes corporativos abandonan el proceso de contratación cuando se requieren datos de facturación avanzados y validación fiscal asíncrona.”
                </p>
              </div>
            </div>
            <span className="font-label-code text-[11px] text-text-muted shrink-0 self-start md:self-center px-2 py-1 bg-surface-card rounded border border-border-subtle">
              ORIGEN: Intercom + HubSpot
            </span>
          </div>
          
          {/* 5-Step Pipeline Grid */}
          <div className="p-6 grid grid-cols-1 md:grid-cols-5 gap-4 relative">
            {/* Step 1 */}
            <div className="p-4 bg-surface-canvas rounded border border-border-subtle flex flex-col justify-between">
              <div>
                <div className="font-label-code text-[11px] text-text-muted mb-1">PASO 01</div>
                <h4 className="font-body-md font-semibold text-text-primary text-sm mb-2">Problema Detectado</h4>
                <p className="font-body-sm text-xs text-text-secondary leading-snug">
                  Fricción por bloqueo sincrónico en pasarela tributaria gubernamental en 3 mercados clave.
                </p>
              </div>
              <div className="mt-4 pt-2 border-t border-border-subtle/60 font-label-code text-[10px] text-text-muted">
                Latencia: &gt; 4.2s
              </div>
            </div>
            
            {/* Step 2 */}
            <div className="p-4 bg-surface-canvas rounded border border-border-subtle flex flex-col justify-between">
              <div>
                <div className="font-label-code text-[11px] text-text-muted mb-1">PASO 02</div>
                <h4 className="font-body-md font-semibold text-text-primary text-sm mb-2">Caso de Uso Formulado</h4>
                <p className="font-body-sm text-xs text-text-secondary leading-snug">
                  Flujo tolerante a fallos con validación asíncrona en segundo plano y token temporal de cuenta.
                </p>
              </div>
              <div className="mt-4 pt-2 border-t border-border-subtle/60 font-label-code text-[10px] text-text-muted">
                ID: UC-B2B-TAX
              </div>
            </div>
            
            {/* Step 3 */}
            <div className="p-4 bg-surface-canvas rounded border border-border-subtle flex flex-col justify-between">
              <div>
                <div className="font-label-code text-[11px] text-text-muted mb-1">PASO 03</div>
                <h4 className="font-body-md font-semibold text-text-primary text-sm mb-2">Hipótesis Medible</h4>
                <p className="font-body-sm text-xs text-text-secondary leading-snug">
                  Reducción del drop-off del 18% en cuentas Enterprise y aceleración del ciclo de cierre en 3 días.
                </p>
              </div>
              <div className="mt-4 pt-2 border-t border-border-subtle/60 font-label-code text-[10px] text-accent-mint-deep font-semibold">
                Confianza: 88%
              </div>
            </div>
            
            {/* Step 4 */}
            <div className="p-4 bg-surface-canvas rounded border border-border-subtle flex flex-col justify-between">
              <div>
                <div className="font-label-code text-[11px] text-text-muted mb-1">PASO 04</div>
                <h4 className="font-body-md font-semibold text-text-primary text-sm mb-2">Scoring & Prioridad</h4>
                <p className="font-body-sm text-xs text-text-secondary leading-snug">
                  Clasificado como 'Must Have' con RICE score de 88.5 ponderado por valor de contrato.
                </p>
              </div>
              <div className="mt-4 pt-2 border-t border-border-subtle/60 font-label-code text-[10px] text-text-primary font-semibold">
                RICE: 88.5 / MUST
              </div>
            </div>
            
            {/* Step 5 */}
            <div className="p-4 bg-surface-canvas rounded border border-border-strong bg-primary-container/10 flex flex-col justify-between">
              <div>
                <div className="font-label-code text-[11px] text-accent-mint-deep font-semibold mb-1">PASO 05 · DEV READY</div>
                <h4 className="font-body-md font-semibold text-text-primary text-sm mb-2">Épica Técnica Gherkin</h4>
                <p className="font-body-sm text-xs text-text-secondary leading-snug">
                  Given / When / Then redactados, endpoints definidos y asignación directa a sprint.
                </p>
              </div>
              <div className="mt-4 pt-2 border-t border-border-strong/50 font-label-code text-[10px] text-text-primary font-semibold flex items-center justify-between">
                <span>Sincronizado</span>
                <span className="material-symbols-outlined text-[14px]">check</span>
              </div>
            </div>
          </div>
          
          <div className="p-4 bg-surface-canvas border-t border-border-subtle flex flex-wrap items-center justify-between gap-3 text-xs">
            <div className="flex items-center gap-2">
              <span className="material-symbols-outlined text-text-secondary text-[16px]">terminal</span>
              <span className="font-label-code text-[11px] text-text-secondary">Pipeline ejecutado en 1.8 segundos · Cero intervención manual de formateo</span>
            </div>
            <span className="font-label-code text-[11px] text-text-muted">Motor: Sprinto Heuristic Engine 4.2</span>
          </div>
        </div>
      </div>
    </section>
  );
}
