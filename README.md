# 🚀 Sprinto AI Hub

**Sprinto AI Hub** es una plataforma avanzada impulsada por Inteligencia Artificial diseñada para acelerar y optimizar el ciclo de vida de la gestión de productos y proyectos tecnológicos. Actúa como el cerebro analítico y generativo detrás de **Sprinto**, integrándose perfectamente con su ecosistema de tableros Kanban.

A través de asistentes de IA especializados, Sprinto AI Hub permite a Product Managers, Agile Coaches y equipos técnicos pasar de la concepción de una idea a un *backlog* completamente refinado y priorizado en cuestión de minutos.

---

## ✨ Características Principales

### 1. 💡 Generador de Casos de Uso IA
Diseñado para la fase de ideación. A partir del sector de la empresa, su tamaño y sus puntos de dolor, la IA genera propuestas de Casos de Uso de Inteligencia Artificial altamente viables.
* **Pipeline Integrado:** Puedes lanzar directamente un caso de uso generado hacia un proyecto nuevo y empezar a desglosar sus épicas.

### 2. 🗺️ AI Project Canvas
Crea un lienzo estratégico completo (basado en el modelo Canvas) para definir proyectos de IA. Documenta la propuesta de valor, los modelos de ML sugeridos, requisitos de datos, restricciones éticas y KPIs críticos de éxito.

### 3. 🎯 Generador de OKRs
Convierte el contexto de un proyecto en **Objetivos y Resultados Clave (OKRs)** perfectamente estructurados. Diferencia entre objetivos cualitativos inspiradores y métricas cuantitativas precisas para medir el éxito del equipo.

### 4. 🪓 Troceador de Épicas (Epic Breaker)
La joya de la corona del refinamiento ágil. Toma una Épica general y la desglosa automáticamente en Historias de Usuario accionables. 
* **Modo Ágil Genérico:** Crea historias de usuario estándar con Criterios de Aceptación.
* **Modo BI / PowerBI:** Crea historias técnicas especializadas que incluyen Orígenes de Datos, Frecuencia de Refresco, Medidas DAX y Tipos de Visuales.

### 5. 📊 Priorizador Multipropósito
Evalúa un *backlog* de historias de usuario frente a marcos de trabajo estándar de la industria, usando el razonamiento del LLM para asignar puntuaciones justificadas de forma objetiva. Soporta:
* **RICE** (Reach, Impact, Confidence, Effort)
* **WSJF** (Weighted Shortest Job First - SAFe)
* **MoSCoW** (Must, Should, Could, Won't)
* **Kano Model** (Basic, Performance, Excitement)
* **Valor vs Complejidad**

### 6. 🔄 Pipeline Ágil End-to-End
Permite encadenar herramientas sin perder el contexto. El usuario puede:
1. Generar casos de uso.
2. Seleccionar uno y crear un proyecto nuevo en Sprinto.
3. Desglosar sus Épicas en Historias.
4. Priorizar todas las historias automáticamente.
5. Inyectarlas en el tablero Kanban de Firebase con un solo clic.

---

## 🛠️ Arquitectura y Tecnologías

* **Frontend:** [Streamlit](https://streamlit.io/) — Interfaces de usuario reactivas, limpias y basadas en Python.
* **Base de Datos:** Firebase Firestore — Sincronización en tiempo real con el frontend React de Sprinto.
* **Motor LLM:** Groq API (Llama 3 / Mixtral) — Inferencias de IA ultrarrápidas. Integración flexible mediante la capa `LLMService`.
* **Modelado de Datos:** Pydantic — Validación estricta de esquemas estructurados para garantizar que la IA devuelva formatos predecibles.

## 🚀 Instalación y Despliegue Local

### Requisitos previos
- Python 3.10 o superior.
- Una cuenta en [Groq](https://console.groq.com/) para la API Key.
- Credenciales de servicio de Firebase (`firebase_credentials.json`).

### Pasos
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/nicott-app/AI-HUB.git
   cd AI-HUB
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar secretos:**
   Crea una carpeta `.streamlit` en la raíz y dentro un archivo `secrets.toml`:
   ```toml
   GROQ_API_KEY = "tu_api_key_aqui"

   # Credenciales de Firebase (Copia el contenido de tu JSON de servicio)
   [firebase]
   type = "service_account"
   project_id = "tu-proyecto"
   private_key_id = "..."
   private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
   client_email = "..."
   client_id = "..."
   auth_uri = "https://accounts.google.com/o/oauth2/auth"
   token_uri = "https://oauth2.googleapis.com/token"
   auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
   client_x509_cert_url = "..."
   ```

4. **Ejecutar la aplicación:**
   ```bash
   streamlit run main.py
   ```

---

## 🧠 Protección Inteligente de Rate Limits
El `LLMService` de Sprinto AI Hub implementa un mecanismo inteligente para respetar las cuotas de las APIs gratuitas (como Groq):
- **Cooldown entre peticiones:** Pausas automáticas inyectadas para no superar los límites de RPM.
- **Retry con Back-off amigable:** Intercepción de errores `429 Too Many Requests`, lectura del header de la API y reintento automático transparente para el usuario mediante temporizadores en la interfaz.

---

*Desarrollado para potenciar el ecosistema de gestión ágil Sprinto.*
