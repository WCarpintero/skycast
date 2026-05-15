# SkyCast Dashboard API 🌤️

**SkyCast Dashboard API** es una solución moderna de backend construida con **FastAPI** que transforma datos meteorológicos crudos en información accionable y creativa.

---

## 🚀 ¿Para qué sirve?
Esta API actúa como un middleware inteligente entre el usuario y los servicios de OpenWeather. Su propósito no es solo informar la temperatura, sino mejorar la experiencia del usuario mediante:
* **Simplificación de Datos:** Filtra la respuesta masiva de OpenWeather para entregar solo lo que un dashboard necesita.
* **Contextualización de Estilo de Vida:** Ayuda al usuario a tomar decisiones rápidas sobre su vestimenta basándose en la temperatura real y sensación térmica.
* **Potenciador de Productividad:** Sugiere géneros musicales (enfocados en programación y enfoque) que armonicen con el ambiente exterior.

---

## 🛠️ Tecnologías y Dependencias
El proyecto utiliza las siguientes librerías core de Python:
* **Python 3.8+**
* **FastAPI**: Framework web moderno y rápido para construir APIs.
* **Uvicorn**: Servidor ASGI para la ejecución de la app.
* **Requests**: Cliente HTTP para consumir la API externa de OpenWeather.
* **Python-dotenv**: Gestión de variables de entorno para proteger datos sensibles.

---
## Endpoints Disponibles
* GET /api/v1/weather/current/{city}
  Descripción: Retorna telemetría detallada y limpia (temperatura, humedad, velocidad del viento y estado actual).
  Ejemplo: http://127.0.0.1:8000/api/v1/weather/current/Bogota
* GET /api/v1/weather/outfit/{city}
   Descripción: Analiza el clima y devuelve una recomendación textual e inteligente de vestimenta (capas, tipos de tela, accesorios para lluvia).
  Ejemplo: http://127.0.0.1:8000/api/v1/weather/outfit/Medellin
* GET /api/v1/weather/playlist/{city}
  Descripción: Cruza el estado del cielo (lluvia, nubes, sol) con perfiles musicales ideales para programar o concentrarse (Lo-Fi, Synthwave, Techno).
  Ejemplo: http://127.0.0.1:8000/api/v1/weather/playlist/Barranquilla


---

## 📁 Estructura del Proyecto
```text
skycast-api/
├── main.py           # Lógica principal de la API y endpoints
├── .env              # Variables de entorno (Claves de API - NO SUBIR A GIT)
├── requirements.txt  # Archivo de dependencias del proyecto
└── README.md         # Documentación de uso
