import Link from 'next/link';

export default function Hero() {
  return (
    <section className="relative w-full pt-12 pb-20 overflow-hidden">
      {/* Subtle architectural grid backplate */}
      <div className="absolute inset-0 pointer-events-none opacity-40 bg-[linear-gradient(to_right,#E2E8F0_1px,transparent_1px),linear-gradient(to_bottom,#E2E8F0_1px,transparent_1px)] bg-[size:48px_48px]"></div>
      
      <div className="relative max-w-[1200px] mx-auto px-margin-mobile md:px-margin flex flex-col items-center text-center">
        {/* Top Badge */}
        <div className="inline-flex items-center gap-space-xs px-space-sm py-1 rounded-full bg-surface-card border border-border-subtle shadow-sm mb-space-lg">
          <span className="w-2 h-2 rounded-full bg-accent-mint-deep animate-pulse"></span>
          <span className="font-label-code text-label-code text-text-primary uppercase tracking-wider">Sprinto AI HUB · Sistema operativo de Product Management</span>
        </div>
        
        {/* Main Headline */}
        <h1 className="font-display text-display md:text-[64px] md:leading-[72px] tracking-tight text-text-primary max-w-4xl font-semibold mb-space-md">
          Convierte ideas en decisiones de producto.
        </h1>
        
        {/* Subheadline */}
        <p className="font-body-lg text-body-lg text-text-secondary max-w-3xl mb-space-lg">
          Una plataforma asistida por IA para descubrir oportunidades reales, estructurar casos de uso con contexto, priorizar iniciativas con rigor técnico y supervisar la salud de tu producto.
        </p>
        
        {/* Action CTAs */}
        <div className="flex flex-col sm:flex-row items-center gap-space-sm w-full sm:w-auto mb-space-md">
          <Link href="https://sprinto-agile.streamlit.app" className="w-full sm:w-auto inline-flex items-center justify-center px-space-lg h-11 bg-text-primary hover:bg-[#1f2937] text-surface-card font-body-md text-body-md rounded transition-colors shadow-sm">
            Empezar gratis
            <span className="material-symbols-outlined ml-2 text-[18px]">arrow_forward</span>
          </Link>
          <Link href="#pipeline-ia" className="w-full sm:w-auto inline-flex items-center justify-center px-space-lg h-11 bg-surface-card hover:bg-surface-canvas text-text-primary font-body-md text-body-md rounded border border-border-subtle transition-colors">
            <span className="material-symbols-outlined mr-2 text-[20px] text-text-secondary">play_circle</span>
            Ver cómo funciona
          </Link>
        </div>
        
        {/* Trust Microcopy */}
        <p className="font-label-code text-label-code text-text-muted flex items-center gap-2">
          <span className="inline-block w-1.5 h-1.5 rounded-full bg-border-strong"></span>
          Prueba de 14 días sin tarjeta · Compatible con Sprinto Ticketing y exportación a Jira/Linear
        </p>
        
        {/* HERO PRODUCT MOCKUP: Precision High-Density Dashboard */}
        <div className="w-full mt-12 bg-surface-card border border-border-subtle rounded-lg shadow-sm overflow-hidden text-left">
          {/* Dashboard Top Control Header */}
          <div className="bg-surface-canvas px-4 py-2.5 border-b border-border-subtle flex flex-wrap items-center justify-between gap-3 text-xs">
            <div className="flex items-center gap-2">
              <span className="inline-flex gap-1.5 mr-2">
                <span className="w-2.5 h-2.5 rounded-full bg-[#E2E8F0]"></span>
                <span className="w-2.5 h-2.5 rounded-full bg-[#E2E8F0]"></span>
                <span className="w-2.5 h-2.5 rounded-full bg-[#E2E8F0]"></span>
              </span>
              <span className="font-label-code text-label-code text-text-muted font-normal">espacio://</span>
              <span className="font-label-code text-label-code text-text-primary font-medium">Checkout & Growth / Hub</span>
            </div>
            <div className="flex items-center gap-2 overflow-x-auto">
              <span className="inline-flex items-center px-2 py-0.5 rounded bg-surface-card border border-border-subtle font-label-code text-label-code text-text-secondary">
                Trimestre: <strong className="text-text-primary ml-1">Q4 2024</strong>
              </span>
              <span className="inline-flex items-center px-2 py-0.5 rounded bg-surface-card border border-border-subtle font-label-code text-label-code text-text-secondary">
                Framework: <strong className="text-text-primary ml-1">RICE Score (Ponderado)</strong>
              </span>
              <span className="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded bg-primary-container/30 border border-accent-mint-deep/30 font-label-code text-label-code text-text-primary">
                <span className="w-1.5 h-1.5 rounded-full bg-accent-mint-deep"></span>
                Health Score: <strong className="text-text-primary">94/100 (Óptimo)</strong>
              </span>
            </div>
          </div>
          
          {/* Main Dashboard Split Pane */}
          <div className="grid grid-cols-1 lg:grid-cols-12 divide-y lg:divide-y-0 lg:divide-x divide-border-subtle">
            {/* Left Column: Initiatives & Strategic Bets */}
            <div className="lg:col-span-5 p-4 bg-surface-card flex flex-col justify-between">
              <div>
                <div className="flex items-center justify-between pb-3 border-b border-border-subtle mb-3">
                  <span className="font-label-meta text-label-meta uppercase tracking-wider text-text-muted">Apuestas Estratégicas Activas (12)</span>
                  <span className="font-label-code text-label-code text-text-secondary">Orden: RICE DESC</span>
                </div>
                
                {/* Item 1 (Selected) */}
                <div className="p-3 mb-2 rounded bg-surface-canvas border-l-2 border-text-primary flex flex-col gap-1.5">
                  <div className="flex items-center justify-between">
                    <span className="font-label-code text-label-code font-semibold text-text-primary">UC-104</span>
                    <div className="flex items-center gap-1.5">
                      <span className="px-1.5 py-0.5 text-[10px] font-label-code font-semibold rounded bg-primary-container text-on-primary-fixed border border-accent-mint-deep/30">RICE 86.4</span>
                      <span className="px-1.5 py-0.5 text-[10px] font-label-code rounded bg-surface-card text-text-secondary border border-border-subtle">MUST</span>
                    </div>
                  </div>
                  <p className="font-headline-sm text-sm font-medium text-text-primary leading-snug">
                    Recuperación preventiva de carritos mediante análisis heurístico
                  </p>
                  <div className="flex items-center justify-between text-xs text-text-muted pt-1">
                    <span className="font-body-sm text-[12px]">Impacto: +$142K ARR</span>
                    <span className="font-label-code text-[11px] text-text-secondary">Confianza: 92%</span>
                  </div>
                </div>
                
                {/* Item 2 */}
                <div className="p-3 mb-2 rounded hover:bg-surface-canvas/60 transition-colors border-l-2 border-transparent flex flex-col gap-1.5">
                  <div className="flex items-center justify-between">
                    <span className="font-label-code text-label-code text-text-muted">UC-102</span>
                    <div className="flex items-center gap-1.5">
                      <span className="px-1.5 py-0.5 text-[10px] font-label-code rounded bg-surface-container text-text-primary">RICE 78.1</span>
                      <span className="px-1.5 py-0.5 text-[10px] font-label-code rounded bg-surface-card text-text-secondary border border-border-subtle">SHOULD</span>
                    </div>
                  </div>
                  <p className="font-body-md text-sm text-text-secondary leading-snug">
                    Facturación multidivisa B2B con deducción fiscal automática
                  </p>
                  <div className="flex items-center justify-between text-xs text-text-muted pt-1">
                    <span className="font-body-sm text-[12px]">Impacto: Expansión EMEA</span>
                    <span className="font-label-code text-[11px]">Confianza: 85%</span>
                  </div>
                </div>
                
                {/* Item 3 */}
                <div className="p-3 rounded hover:bg-surface-canvas/60 transition-colors border-l-2 border-transparent flex flex-col gap-1.5">
                  <div className="flex items-center justify-between">
                    <span className="font-label-code text-label-code text-text-muted">UC-098</span>
                    <div className="flex items-center gap-1.5">
                      <span className="px-1.5 py-0.5 text-[10px] font-label-code rounded bg-surface-container text-text-primary">RICE 62.0</span>
                      <span className="px-1.5 py-0.5 text-[10px] font-label-code rounded bg-surface-card text-text-secondary border border-border-subtle">COULD</span>
                    </div>
                  </div>
                  <p className="font-body-md text-sm text-text-secondary leading-snug">
                    Autenticación biométrica WebAuthn sin contraseñas para checkout
                  </p>
                  <div className="flex items-center justify-between text-xs text-text-muted pt-1">
                    <span className="font-body-sm text-[12px]">Impacto: -4s en checkout</span>
                    <span className="font-label-code text-[11px]">Confianza: 70%</span>
                  </div>
                </div>
              </div>
              
              <div className="pt-3 mt-3 border-t border-border-subtle flex items-center justify-between text-xs text-text-muted">
                <span>9 iniciativas más evaluadas</span>
                <span className="font-label-code text-text-primary hover:underline cursor-pointer">Ver matriz completa &rarr;</span>
              </div>
            </div>
            
            {/* Right Column: Inspector Panel of UC-104 */}
            <div className="lg:col-span-7 p-5 bg-surface-card flex flex-col gap-4">
              <div className="flex items-start justify-between">
                <div>
                  <div className="flex items-center gap-2 mb-1">
                    <span className="font-label-code text-label-code text-text-muted">USE CASE CONTEXT</span>
                    <span className="w-1 h-1 rounded-full bg-border-strong"></span>
                    <span className="font-label-code text-[11px] text-accent-mint-deep font-semibold">VALIDADO POR IA</span>
                  </div>
                  <h3 className="font-headline-sm text-lg font-semibold text-text-primary">
                    UC-104: Recuperación preventiva de carritos mediante análisis heurístico
                  </h3>
                </div>
                <div className="text-right">
                  <span className="font-label-code text-[11px] text-text-muted block">Score Estratégico</span>
                  <span className="font-label-code text-base font-bold text-text-primary">86.4 / 100</span>
                </div>
              </div>
              
              {/* Problem & Metrics Box */}
              <div className="bg-surface-canvas p-3 rounded border border-border-subtle">
                <span className="font-label-meta text-[10px] uppercase tracking-wider text-text-muted block mb-1">Problema de Negocio Cuantificado</span>
                <p className="font-body-sm text-body-sm text-text-secondary">
                  Abandono anómalo del <strong className="text-text-primary">24.3%</strong> en el paso de confirmación de pasarela 3DS. El 68% de las sesiones fallidas corresponden a micro-latencias en la precarga de proveedores bancarios secundarios.
                </p>
              </div>
              
              {/* AI Hypothesis Box */}
              <div className="bg-surface-card p-3 rounded border border-border-strong/70 relative">
                <div className="flex items-center gap-2 mb-1.5">
                  <span className="w-2 h-2 rounded-full bg-accent-mint-deep"></span>
                  <span className="font-label-code text-[11px] font-semibold text-text-primary">Hipótesis Estructurada (Motor Síntesis)</span>
                </div>
                <p className="font-body-sm text-body-sm text-text-primary italic">
                  &quot;Si implementamos la pre-carga heurística de métodos locales en &lt;150ms basada en IP y fingerprint de dispositivo, la tasa de conversión global aumentará en un +6.2% neto sin incrementar los riesgos de contracargos.&quot;
                </p>
              </div>
              
              {/* Structured Epics Decomposition */}
              <div>
                <div className="flex items-center justify-between mb-2">
                  <span className="font-label-meta text-[11px] uppercase tracking-wider text-text-muted">Descomposición en Épicas de Ingeniería (3)</span>
                  <span className="font-label-code text-[11px] text-text-secondary">Listo para Sprinto Board</span>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-2">
                  <div className="p-2.5 rounded bg-surface-canvas border border-border-subtle flex flex-col justify-between">
                    <div className="font-label-code text-[10px] text-text-muted mb-1">EPIC-241</div>
                    <div className="font-body-sm text-[12px] font-medium text-text-primary leading-tight mb-2">Edge Routing para Pasarelas de Pago</div>
                    <div className="font-label-code text-[10px] text-text-secondary">Backend · 5d</div>
                  </div>
                  <div className="p-2.5 rounded bg-surface-canvas border border-border-subtle flex flex-col justify-between">
                    <div className="font-label-code text-[10px] text-text-muted mb-1">EPIC-242</div>
                    <div className="font-body-sm text-[12px] font-medium text-text-primary leading-tight mb-2">Fallback inteligente de autenticación 3DS</div>
                    <div className="font-label-code text-[10px] text-text-secondary">SecOps · 4d</div>
                  </div>
                  <div className="p-2.5 rounded bg-surface-canvas border border-border-subtle flex flex-col justify-between">
                    <div className="font-label-code text-[10px] text-text-muted mb-1">EPIC-243</div>
                    <div className="font-body-sm text-[12px] font-medium text-text-primary leading-tight mb-2">Telemetría de latencia en Checkout UI</div>
                    <div className="font-label-code text-[10px] text-text-secondary">Frontend · 3d</div>
                  </div>
                </div>
              </div>
              
              {/* Health Footer Pill */}
              <div className="pt-2 flex flex-wrap items-center justify-between gap-2 border-t border-border-subtle text-xs">
                <div className="flex items-center gap-2">
                  <span className="font-label-code text-[11px] text-text-secondary">Impacto: <strong>Alto (4/5)</strong></span>
                  <span className="text-border-strong">&bull;</span>
                  <span className="font-label-code text-[11px] text-text-secondary">Esfuerzo: <strong>3 semanas</strong></span>
                  <span className="text-border-strong">&bull;</span>
                  <span className="font-label-code text-[11px] text-accent-mint-deep font-semibold">Confianza: 92%</span>
                </div>
                <button className="px-2.5 py-1 rounded bg-text-primary text-surface-card font-label-code text-[11px] hover:bg-[#1f2937] transition-colors">
                  Exportar a Sprint &rarr;
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
