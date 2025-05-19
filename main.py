from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from pathlib import Path
import os
from fastapi import FastAPI, Request
from utils.github import obtener_proyectos


app = FastAPI(title="BitAnkor Portfolio", version="1.0.0")

# Configuración de archivos estáticos y plantillas
BASE_DIR = Path(__file__).parent
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")
        
# Datos de ejemplo para proyectos
PROJECTS_DATA = [
    {
        "id": 1,
        "title": "AI Dev Bro",
        "description": "Asistente de IA personalizado para desarrolladores con integración de OpenAI",
        "technologies": ["FastAPI", "Tailwind", "OpenAI"],
        "image": "ai-dev-bro.jpg"
    },
    {
        "id": 2,
        "title": "E-commerce API",
        "description": "Plataforma de comercio electrónico escalable con sistema de pagos integrado",
        "technologies": ["Node.js", "MongoDB", "Stripe"],
        "image": "ecommerce-api.jpg"
    }
]

# Rutas de la API
@app.get("/")
async def index(request: Request):
    proyectos = await obtener_proyectos()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "proyectos": proyectos
    })

@app.post("/contact", response_class=HTMLResponse)
async def handle_contact(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...)
):
    # Aquí podrías agregar lógica para enviar el correo
    print(f"Nuevo mensaje de contacto: {name} <{email}> - {subject}: {message}")
    return RedirectResponse(url="/?message=success", status_code=303)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))