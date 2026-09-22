import Link from 'next/link';

export default function Navbar() {
  return (
    <header className="fixed top-0 w-full z-50 bg-surface-card/90 backdrop-blur-md border-b border-border-subtle">
      <div className="h-16 max-w-[1200px] mx-auto px-margin-mobile md:px-margin flex items-center justify-between gap-space-md">
        <div className="flex items-center gap-space-md">
          <Link href="/" className="flex items-center gap-space-xs" data-path="overview">
            <img 
              alt="Sprinto logo" 
              className="h-8 w-auto object-contain" 
              src="https://lh3.googleusercontent.com/aida/AEtjO1XXOH2hGlUoSCNWpAMyUdHI2gR-qwoFwjE8-MweI1y6OhnuJcQol32L_9rpYjr141hZ47Ckyf1T623I944jQEMNkujZZo1Z3j5VnCLXlGJN1LzqNqrT63mbYyosZa26f50j8buytaf3lcXVjkpJMZP00bIo2Qc-DYYVH-l3vz5K-FYTy_W_dmED9xaSIPCF02_S0-rzKrUY2NZMWW5BqiSd-nMzze1fHhgWnjXZX1TinTnCyZ5L6_qBBtQ" 
            />
            <span className="font-headline-sm text-headline-sm tracking-tight text-text-primary">Sprinto</span>
            <span className="font-label-code text-label-code bg-surface-container px-space-xs py-0.5 rounded text-text-secondary border border-border-subtle">AI HUB</span>
          </Link>
          <nav className="hidden lg:flex items-center gap-space-lg ml-space-md">
            <Link href="#producto" className="transition-colors text-text-primary font-medium" data-path="overview">Producto</Link>
            <Link href="#casos" className="text-text-secondary hover:text-text-primary transition-colors font-body-sm text-body-sm" data-path="use-cases">Casos de uso</Link>
            <Link href="#priorizacion" className="text-text-secondary hover:text-text-primary transition-colors font-body-sm text-body-sm" data-path="prioritization">Priorización</Link>
            <Link href="#ia" className="text-text-secondary hover:text-text-primary transition-colors font-body-sm text-body-sm" data-path="ai-engine">IA</Link>
            <Link href="#ecosistema" className="text-text-secondary hover:text-text-primary transition-colors font-body-sm text-body-sm" data-path="ecosystem">Ecosistema</Link>
            <Link href="#recursos" className="text-text-secondary hover:text-text-primary transition-colors font-body-sm text-body-sm" data-path="resources">Recursos</Link>
          </nav>
        </div>
        <div className="flex items-center gap-space-sm">
          <Link href="https://sprinto-agile.streamlit.app" className="hidden sm:inline-flex items-center px-space-sm py-1.5 font-body-sm text-body-sm text-text-secondary hover:text-text-primary transition-colors" data-path="login">
            Iniciar sesión
          </Link>
          <Link href="https://sprinto-agile.streamlit.app" className="inline-flex items-center justify-center px-space-md h-9 bg-primary-container hover:bg-primary-fixed text-on-primary-fixed font-headline-sm text-body-sm rounded-lg border border-border-subtle transition-all" data-path="signup">
            Empezar gratis
          </Link>
          <div className="w-8 h-8 rounded-full bg-primary flex items-center justify-center ml-space-xs">
            <span className="material-symbols-outlined text-on-primary text-[18px]">person</span>
          </div>
        </div>
      </div>
    </header>
  );
}
