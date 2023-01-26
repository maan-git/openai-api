import json
import requests

from models.cv_model import ImageGeneratorModel
from config import Settings

class ImageGeneratorController:

    def __init__(self, descriptions: str):
        self.descriptions = descriptions
        self.setting = Settings()
    
    def image_generator_response(self):
    
        response = self._get_image_url(self.descriptions)
        return ImageGeneratorModel(descriptions=self.descriptions, 
                                    url=response['data'][0]['url'])

        
    def _get_image_url(self, image_descriptions):

        payload = json.dumps(
            {
                "prompt": image_descriptions,
                "n": 1,
                "size": "1024x1024"
            }
        )
        headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {self.setting.OPENAI_API_KEY}'
        }
        result = requests.request("POST", 
                                    self.setting.open_ai_image_generator_url, 
                                    headers=headers, 
                                    data=payload)
        return result.json()