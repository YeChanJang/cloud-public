from pydantic import BaseModel
from ollama import chat


class Pet(BaseModel):
    name: str
    animal: str
    age: int


class PetList(BaseModel):
    pets: list[Pet]


response = chat(
    model="gemma3",
    messages=[
        {
            "role": "user",
            "content": "I have a 3-year-old dog named Bori and a 2-year-old cat named Nabi.",
        }
    ],
    format=PetList.model_json_schema(),
    options={"temperature": 0},
)

pets = PetList.model_validate_json(response.message.content)
print(pets)
