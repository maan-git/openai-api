
import openai

from fastapi import FastAPI
from config import Settings
from controllers.nlp_controller import NLPPetController
from controllers.cv_controller import ImageGeneratorController

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
setting = Settings()
openai.api_key = setting.OPENAI_API_KEY

app.add_middleware(
    CORSMiddleware,
    allow_origins=setting.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health-check/")
async def read_root():
    return {"response": "ok"}

@app.post("/nlp-pet-name/specie/{specie}")
async def nlp_pet_name(specie: str):
    nlp_pet_controller = NLPPetController(specie)
    response = nlp_pet_controller.nlp_pet_response()
    return response

@app.post("/nlp-pet-name-fake/specie/{specie}")
async def nlp_pet_name(specie: str):
    return{
        "names": [
            "Super Woofer",
            "The Amazing Canine",
            "Captain Fido"
        ],
        "specie": specie
    }
    
@app.post("/cv-image-generator/description/{descriptions}")
async def cv_image_generator(descriptions: str):
    cv_image_generator_controller = ImageGeneratorController(descriptions)
    response = cv_image_generator_controller.image_generator_response()
    return response