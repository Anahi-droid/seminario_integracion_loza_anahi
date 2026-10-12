Seminario de Integración
Autor: Anahi Loza

Bienvenido al repositorio oficial de la materia Seminario de Integración. Este espacio está diseñado para integrar el desarrollo backend de alto rendimiento con arquitecturas frontend modernas, utilizando herramientas de última generación para la gestión de dependencias y entornos virtuales.

🛠️ Tecnologías y Mini Conceptos

1. Python

¿Qué es? Un lenguaje de programación de alto nivel, interpretado y de propósito general, conocido por su sintaxis limpia, legibilidad y versatilidad en áreas como el desarrollo web, la ciencia de datos y la automatización.

2. UV (por Astral)

¿Qué es? Un administrador de paquetes y entornos virtuales para Python extremadamente rápido, escrito en Rust. Reemplaza a herramientas tradicionales como pip, virtualenv y poetry, ofreciendo una resolución de dependencias ultra veloz y gestión centralizada de versiones.

3. FastAPI

¿Qué es? Un framework web moderno y de alto rendimiento para construir APIs con Python, basado en los tipos estándar de Python (type hints). Destaca por su velocidad similar a NodeJS y Go, su documentación automática interactiva (Swagger UI / ReDoc) y su facilidad de uso.

4. Angular

¿Qué es? Una plataforma y framework de desarrollo frontend basada en TypeScript, mantenida por Google. Permite construir aplicaciones web de una sola página (SPA) robustas y escalables mediante una arquitectura basada en componentes, inyección de dependencias y herramientas potentes de CLI.

📂 Estructura del Repositorio

El proyecto está organizado como un monorepo que contiene tanto los servicios de backend (FastAPI con uv) como las aplicaciones frontend (Angular), asegurando que los entornos virtuales, módulos compilados y dependencias locales sean ignorados correctamente por Git.

├── backend/          # Servicios FastAPI y gestión de entorno con UV
├── frontend/         # Aplicación Angular
└── README.md         # Documentación general del seminario


🚀 Guía Rápida de Configuración

Backend (Python + FastAPI + UV)

Navega a la carpeta del backend:

cd backend


Crea el entorno virtual con uv:

uv venv


Activa el entorno virtual:

En Windows: .venv\Scripts\activate

En macOS/Linux: source .venv/bin/activate

Instala las dependencias y ejecuta el servidor de desarrollo con FastAPI.

Frontend (Angular)

Navega a la carpeta del frontend:

cd frontend


Instala las dependencias de Node.js:

npm install


Inicia el servidor de desarrollo:

ng serve
