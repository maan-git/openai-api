from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI"
    admin_email: str = "manoel.alves.de.almeida.neto@gmail.com"
    OPENAI_API_KEY: str
    open_ai_image_generator_url: str = "https://api.openai.com/v1/images/generations"
    origins = [
        "http://localhost",
        "http://localhost:3000",
    ]

    class Config:
        env_file = ".env"
