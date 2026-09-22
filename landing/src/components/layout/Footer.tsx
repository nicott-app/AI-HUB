import Link from 'next/link';

export default function Footer() {
  return (
    <footer className="w-full bg-surface-card border-t border-border-subtle mt-space-xl">
      <div className="max-w-[1200px] mx-auto px-margin-mobile md:px-margin py-space-xl">
        <div className="grid grid-cols-2 md:grid-cols-5 gap-space-lg mb-space-xl">
          <div className="col-span-2 md:col-span-1 flex flex-col gap-space-sm">
            <div className="flex items-center gap-space-xs">
              <img 
                alt="Sprinto logo" 
                className="h-6 w-auto object-contain" 
                src="https://sprinto-board.web.app/sprinto-logo.svg" 
              />
              <span className="font-headline-sm text-headline-sm tracking-tight text-text-primary">Sprinto</span>
              <span className="font-label-code text-label-code bg-surface-container px-space-xs py-0.5 rounded text-text-secondary border border-border-subtle">AI</span>
            </div>
            <p className="font-body-sm text-body-sm text-text-muted">
              Plataforma de Product Management con inteligencia continua para equipos técnicos B2B.
            </p>
          </div>
          
          <div className="flex flex-col gap-space-xs">
            <span className="font-label-meta text-label-meta uppercase tracking-wider text-text-muted mb-space-xs">Producto</span>
            <Link href="#overview" className="font-body-sm text-body-sm text-text-secondary hover:text-text-primary transition-colors">Visión general</Link>
            <Link href="#prioritization" className="font-body-sm text-body-sm text-text-secondary hover:text-text-primary transition-colors">Priorización RICE</Link>
            <Link href="#ai-engine" className="font-body-sm text-body-sm text-text-secondary hover:text-text-primary transition-colors">Motor de IA</Link>
            <Link href="#roadmaps" className="font-body-sm text-body-sm text-text-secondary hover:text-text-primary transition-colors">Roadmaps</Link>
          </div>
          
          <div className="flex flex-col gap-space-xs">
            <span className="font-label-meta text-label-meta uppercase tracking-wider text-text-muted mb-space-xs">Ecosistema</span>
            <Link href="#ecosystem" className="font-body-sm text-body-sm text-text-secondary hover:text-text-primary transition-colors">Sprinto Ticketing</Link>
            <Link href="#integrations" className="font-body-sm text-body-sm text-text-secondary hover:text-text-primary transition-colors">Integraciones GitHub</Link>
            <Link href="#api-docs" className="font-body-sm text-body-sm text-text-secondary hover:text-text-primary transition-colors">API REST & Webhooks</Link>
            <Link href="#sync-engine" className="font-body-sm text-body-sm text-text-secondary hover:text-text-primary transition-colors">Sincronización bidireccional</Link>
          </div>
          
          <div className="flex flex-col gap-space-xs">
            <span className="font-label-meta text-label-meta uppercase tracking-wider text-text-muted mb-space-xs">Recursos</span>
            <Link href="#docs" className="font-body-sm text-body-sm text-text-secondary hover:text-text-primary transition-colors">Documentación</Link>
            <Link href="#guides" className="font-body-sm text-body-sm text-text-secondary hover:text-text-primary transition-colors">Guías de PM</Link>
            <Link href="#changelog" className="font-body-sm text-body-sm text-text-secondary hover:text-text-primary transition-colors">Changelog</Link>
            <Link href="#community" className="font-body-sm text-body-sm text-text-secondary hover:text-text-primary transition-colors">Comunidad</Link>
          </div>
          
          <div className="flex flex-col gap-space-xs">
            <span className="font-label-meta text-label-meta uppercase tracking-wider text-text-muted mb-space-xs">Empresa & Legal</span>
            <Link href="#about" className="font-body-sm text-body-sm text-text-secondary hover:text-text-primary transition-colors">Acerca de Sprinto</Link>
            <Link href="#security" className="font-body-sm text-body-sm text-text-secondary hover:text-text-primary transition-colors">Seguridad SOC2</Link>
            <Link href="#privacy" className="font-body-sm text-body-sm text-text-secondary hover:text-text-primary transition-colors">Privacidad</Link>
            <Link href="#terms" className="font-body-sm text-body-sm text-text-secondary hover:text-text-primary transition-colors">Términos del servicio</Link>
          </div>
        </div>
        
        <div className="pt-space-md border-t border-border-subtle flex flex-col sm:flex-row items-center justify-between gap-space-sm">
          <p className="font-label-code text-label-code text-text-muted">© 2026 Sprinto Software Inc. Todos los derechos reservados.</p>
          <div className="flex items-center gap-space-md">
            <span className="inline-flex items-center gap-1.5 font-label-code text-label-code text-text-secondary">
              <span className="w-2 h-2 rounded-full bg-accent-mint-deep"></span>
              Sistemas Operativos 99.99%
            </span>
          </div>
        </div>
      </div>
    </footer>
  );
}
