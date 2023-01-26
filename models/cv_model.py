from pydantic import BaseModel

class ImageGeneratorModel(BaseModel):
    descriptions: str
    url: str