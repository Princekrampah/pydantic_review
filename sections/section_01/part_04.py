from pydantic import BaseModel
from typing import List, Optional


class Car(BaseModel):
    name: str
    top_speed: Optional[int] = 120


class Manufacturer(BaseModel):
    name: str
    location: str
    vehicles: List[Car]


toyota: Manufacturer = Manufacturer(
    name="Toyota",
    location="Japan",
    vehicles=[
        {"name": "Supra", "top_speed": 140},
        {"name": "RAV4"}
    ]
)


print(toyota.model_dump())
