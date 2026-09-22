export default function FinalCta() {
  return (
    <section className="w-full py-20 bg-surface-canvas" id="empezar">
      <div className="max-w-[1200px] mx-auto px-margin-mobile md:px-margin">
        <div className="p-8 md:p-14 bg-text-primary text-surface-card rounded-xl flex flex-col items-center text-center relative overflow-hidden">
          {/* Architectural grid lines in dark card */}
          <div className="absolute inset-0 pointer-events-none opacity-10 bg-[linear-gradient(to_right,#ffffff_1px,transparent_1px),linear-gradient(to_bottom,#ffffff_1px,transparent_1px)] bg-[size:32px_32px]"></div>
          
          <div className="relative z-10 max-w-2xl">
            <span className="font-label-code text-[11px] text-accent-mint-deep uppercase tracking-widest font-semibold block mb-3">
              EMPIEZA HOY MISMO
            </span>
            <h2 className="font-headline-lg text-headline-lg font-semibold text-surface-card tracking-tight mb-4">
              Deja de gestionar ideas dispersas. Empieza a tomar decisiones de producto con contexto.
            </h2>
            <p className="font-body-md text-text-muted mb-8 max-w-xl mx-auto">
              Configura tu espacio de producto en menos de 2 minutos. Conecta tus fuentes de feedback y genera tu primer caso de uso priorizado hoy mismo.
            </p>
            
            {/* Direct Email Capture Form */}
            <div className="flex flex-col sm:flex-row items-center gap-2 w-full max-w-md mx-auto mb-4">
              <input 
                className="w-full h-11 px-3.5 rounded bg-[#1f2937] text-surface-card placeholder-text-muted text-sm border border-secondary focus:outline-none focus:border-accent-mint-deep transition-colors" 
                placeholder="tu.nombre@empresa.com" 
                type="email" 
              />
              <a href="https://sprinto-agile.streamlit.app" className="w-full sm:w-auto shrink-0 h-11 px-6 flex items-center justify-center rounded bg-primary-container text-on-primary-fixed font-headline-sm text-sm font-semibold hover:bg-primary-fixed transition-colors">
                Empezar gratis
              </a>
            </div>
            
            {/* Trust Markers */}
            <div className="flex flex-wrap items-center justify-center gap-4 text-xs font-label-code text-text-muted pt-2">
              <span>&#10003; Configuración en 2 minutos</span>
              <span>&bull;</span>
              <span>&#10003; Sin tarjeta de crédito</span>
              <span>&bull;</span>
              <span>&#10003; Exportación directa a tu stack actual</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
