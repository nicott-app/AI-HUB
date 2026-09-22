export default function SocialProof() {
  return (
    <section className="w-full py-10 bg-surface-card border-y border-border-subtle">
      <div className="max-w-[1200px] mx-auto px-margin-mobile md:px-margin text-center">
        <p className="font-label-meta text-label-meta uppercase tracking-wider text-text-muted mb-6">
          Equipos de producto y VP of Engineering deciden su roadmap en Sprinto AI HUB
        </p>
        
        {/* Minimalist typographic tech team marks */}
        <div className="flex flex-wrap items-center justify-center gap-8 md:gap-16 opacity-75">
          <span className="font-label-code text-sm md:text-base font-bold tracking-widest text-text-secondary hover:text-text-primary transition-colors">MONOLITH//</span>
          <span className="font-label-code text-sm md:text-base font-bold tracking-widest text-text-secondary hover:text-text-primary transition-colors">VERTEX.SYS</span>
          <span className="font-label-code text-sm md:text-base font-bold tracking-widest text-text-secondary hover:text-text-primary transition-colors">LAYERFLOW_</span>
          <span className="font-label-code text-sm md:text-base font-bold tracking-widest text-text-secondary hover:text-text-primary transition-colors">[HYPERION]</span>
          <span className="font-label-code text-sm md:text-base font-bold tracking-widest text-text-secondary hover:text-text-primary transition-colors">KUBESTACK.IO</span>
        </div>
        
        {/* Quick Metrics Ribbon */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-6 mt-10 pt-8 border-t border-border-subtle text-left">
          <div>
            <div className="font-label-code text-2xl font-bold text-text-primary">82%</div>
            <div className="font-body-sm text-body-sm text-text-secondary">Reducción en tiempo de especificación técnica</div>
          </div>
          <div>
            <div className="font-label-code text-2xl font-bold text-text-primary">0</div>
            <div className="font-body-sm text-body-sm text-text-secondary">Épicas huérfanas sin hipótesis de negocio</div>
          </div>
          <div>
            <div className="font-label-code text-2xl font-bold text-text-primary">&lt; 1s</div>
            <div className="font-body-sm text-body-sm text-text-secondary">Sincronización con el backlog de ingeniería</div>
          </div>
          <div>
            <div className="font-label-code text-2xl font-bold text-text-primary">94.8%</div>
            <div className="font-body-sm text-body-sm text-text-secondary">Alineación estratégica de commits en dev</div>
          </div>
        </div>
      </div>
    </section>
  );
}
