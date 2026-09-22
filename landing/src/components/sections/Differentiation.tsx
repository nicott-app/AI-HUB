export default function Differentiation() {
  return (
    <section className="w-full py-20 bg-surface-canvas">
      <div className="max-w-[1200px] mx-auto px-margin-mobile md:px-margin">
        <div className="max-w-xl mb-12">
          <span className="font-label-meta text-label-meta uppercase tracking-wider text-text-muted block mb-2">Diferenciación Técnica</span>
          <h2 className="font-headline-lg text-headline-lg font-semibold text-text-primary tracking-tight mb-3">
            Por qué Sprinto AI HUB no es otra herramienta más.
          </h2>
          <p className="font-body-md text-text-secondary">
            Diseñado para equipos que desprecian el software inflado y necesitan herramientas que respeten su tiempo cognitivo.
          </p>
        </div>
        
        {/* Comparative Table */}
        <div className="bg-surface-card border border-border-subtle rounded-lg overflow-x-auto shadow-sm">
          <table className="w-full text-left text-xs border-collapse">
            <thead>
              <tr className="bg-surface-canvas border-b border-border-subtle font-label-meta text-text-muted uppercase text-[10px] tracking-wider">
                <th className="p-4 font-semibold w-1/4">Aspecto</th>
                <th className="p-4 font-semibold w-1/3">Otras herramientas (Chatbots / Gestores genéricos)</th>
                <th className="p-4 font-semibold w-5/12 text-text-primary bg-primary-container/10">Sprinto AI HUB</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-border-subtle font-body-sm">
              <tr>
                <td className="p-4 font-semibold text-text-primary">Arquitectura de la IA</td>
                <td className="p-4 text-text-secondary">Chatbots de lenguaje abierto que producen prosa genérica sin esquema relacional.</td>
                <td className="p-4 text-text-primary bg-primary-container/10 font-medium">Motor heurístico determinista que transforma inputs en objetos de datos estructurados con IDs únicos.</td>
              </tr>
              <tr>
                <td className="p-4 font-semibold text-text-primary">Foco Operativo</td>
                <td className="p-4 text-text-secondary">Crear listas infinitas de tareas y micro-tickets sin evaluar la justificación de negocio.</td>
                <td className="p-4 text-text-primary bg-primary-container/10 font-medium">Evalúa viabilidad, impacto y alineación estratégica antes de autorizar la creación de épicas.</td>
              </tr>
              <tr>
                <td className="p-4 font-semibold text-text-primary">Ciclo de vida del PRD</td>
                <td className="p-4 text-text-secondary">Páginas estáticas de texto que quedan desactualizadas apenas inicia el primer sprint.</td>
                <td className="p-4 text-text-primary bg-primary-container/10 font-medium">Toda especificación vive conectada en tiempo real a las ramas de código y al avance del delivery.</td>
              </tr>
              <tr>
                <td className="p-4 font-semibold text-text-primary">Conexión con Dev</td>
                <td className="p-4 text-text-secondary">Copiar y pegar manualmente requisitos entre cinco aplicaciones distintas.</td>
                <td className="p-4 text-text-primary bg-primary-container/10 font-medium">Integración nativa zero-latency con Sprinto Ticketing o exportación directa a Linear y Jira.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
  );
}
