
import openai
from models.nlp_model import PetModel

class NLPPetController:

    def __init__(self, specie: str):
        self.specie = specie

    def nlp_pet_response(self):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=self._generate_pet_name_prompt(self.specie),
            temperature=0.6,
        )
        names = response.choices[0].text.split(",")
        names = list(map(lambda x: x.strip(), names))
        return PetModel(specie=self.specie, names=names)


    def _generate_pet_name_prompt(self, animal):
        return """Suggest three names for an animal that is a superhero.
        Animal: Cat
        Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
        Animal: {}
        Names:""".format(
                animal.capitalize()
            )