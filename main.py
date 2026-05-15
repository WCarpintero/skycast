import os
import requests
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "[https://api.openweathermap.org/data/2.5/weather](https://api.openweathermap.org/data/2.5/weather)"

if not API_KEY:
    raise RuntimeError("CRÍTICO: La variable de entorno OPENWEATHER_API_KEY no está configurada.")

# Inicializar FastAPI con documentación personalizada
app = FastAPI(
    title="SkyCast Dashboard API",
    description="API creativa que consume OpenWeather para dar recomendaciones de outfit y música según el clima.",
    version="1.0.0"
)

# Configurar CORS por si deseas consumirla desde un frontend (Vue, Angular, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Función auxiliar para consumir la API externa de OpenWeather
def fetch_weather_data(city: str) -> dict:
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric", # Para obtener grados Celsius
        "lang": "es"       # Respuestas en español
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        
        if response.status_code == 404:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"La ciudad '{city}' no fue encontrada en los registros de OpenWeather."
            )
        elif response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail="Error al comunicarse con el servicio externo de clima."
            )
            
        return response.json()
    except requests.exceptions.RequestException:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="El servicio de clima externo no está disponible en este momento."
        )

# --- ENDPOINTS ---

@app.get("/", tags=["General"])
def root():
    """Endpoint de bienvenida y estado de la API."""
    return {
        "status": "online",
        "message": "Bienvenido a SkyCast Dashboard API. Visita /docs para ver la documentación interactiva."
    }


@app.get("/api/v1/weather/current/{city}", tags=["Weather Core"])
def get_current_weather(city: str):
    """Obtiene el estado del clima actual filtrado y formateado de una ciudad específica."""
    data = fetch_weather_data(city)
    
    return {
        "city": data.get("name"),
        "country": data.get("sys", {}).get("country"),
        "telemetries": {
            "temperature": data.get("main", {}).get("temp"),
            "feels_like": data.get("main", {}).get("feels_like"),
            "humidity": f"{data.get('main', {}).get('humidity')}%",
            "wind_speed": f"{data.get('wind', {}).get('speed')} m/s"
        },
        "status": data.get("weather", [{}])[0].get("description", "N/A").capitalize(),
        "icon_code": data.get("weather", [{}])[0].get("icon", "")
    }


@app.get("/api/v1/weather/outfit/{city}", tags=["Smart Recommendations"])
def get_outfit_recommendation(city: str):
    """Recomienda el outfit ideal para el día basado en la temperatura actual de la ciudad."""
    data = fetch_weather_data(city)
    temp = data.get("main", {}).get("temp", 20)
    condition = data.get("weather", [{}])[0].get("main", "").lower()
    
    # Lógica de recomendación de outfit
    if temp < 15:
        recommendation = "Hace frío. Te sugerimos usar una chaqueta abrigada o un saco cómodo, jeans gruesos y calzado cerrado."
    elif 15 <= temp <= 24:
        recommendation = "Clima templado ideal. Una sudadera ligera, una camiseta fresca y pantalones cómodos o jeans serán perfectos."
    else:
        recommendation = "Hace calor. Opta por ropa muy fresca: bermudas, camisetas ligeras de algodón y calzado transpirable."
        
    if "rain" in condition or "drizzle" in condition:
        recommendation += " ¡Ojo! Está lloviendo o hay llovizna, no olvides llevar un paraguas o una chaqueta impermeable."

    return {
        "city": data.get("name"),
        "current_temperature": f"{temp}°C",
        "condition_group": condition,
        "recommended_outfit": recommendation
    }


@app.get("/api/v1/weather/playlist/{city}", tags=["Smart Recommendations"])
def get_weather_playlist(city: str):
    """Sugiere un estilo o mood musical perfecto para acompañar el clima actual de la ciudad."""
    data = fetch_weather_data(city)
    condition = data.get("weather", [{}])[0].get("main", "").lower()
    temp = data.get("main", {}).get("temp", 20)

    # Lógica creativa para emparejar el clima con géneros musicales
    if "thunderstorm" in condition:
        mood = "Cyberpunk / Dark Synthwave"
        suggestion = "El cielo ruge. Es la atmósfera perfecta para programar con ritmos pesados de sintetizadores, beats industriales y techno oscuro."
    elif "rain" in condition or "drizzle" in condition:
        mood = "Lo-Fi Beats / Acoustic Mood"
        suggestion = "Día lluvioso y nostálgico. Ideal para relajarse con música melódica, jazz suave o instrumentales Lo-Fi mientras ves las gotas caer."
    elif "cloud" in condition:
        mood = "Deep House / Indie Lounge"
        suggestion = "Cielo nublado y calmado. Un ritmo constante de Deep House o un ambiente Indie te mantendrán enfocado y con buena energía."
    elif temp > 26:
        mood = "Vibrant Synthwave / High Energy"
        suggestion = "¡Día soleado y radiante! Sube el volumen con Synthwave retro de los 80s lleno de energía, ritmos veraniegos o pop electrónico para programar al máximo."
    else:
        mood = "Chillwave / Ambient Tech"
        suggestion = "Clima balanceado y despejado. Una playlist de Chillwave o música ambiental tecnológica mantendrá tu mente en un estado de flujo perfecto."

    return {
        "city": data.get("name"),
        "weather_condition": data.get("weather", [{}])[0].get("description").capitalize(),
        "recommended_mood": mood,
        "playlist_description": suggestion
    }