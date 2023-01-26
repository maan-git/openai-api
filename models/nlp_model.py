from typing import List, Union
from pydantic import BaseModel

class PetModel(BaseModel):
    names: Union[List[str], None] = None
    specie: str