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

## 📁 Estructura del Proyecto
```text
skycast-api/
├── main.py           # Lógica principal de la API y endpoints
├── .env              # Variables de entorno (Claves de API - NO SUBIR A GIT)
├── requirements.txt  # Archivo de dependencias del proyecto
└── README.md         # Documentación de uso
