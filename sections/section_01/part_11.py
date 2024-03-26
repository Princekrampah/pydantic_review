# strick mode
from pydantic import BaseModel, Field
from uuid import uuid4


class Employee(BaseModel):
    id: str = Field(..., alias="user_id",
                    default_factory=lambda: uuid4().hex[:6])
    name: str = Field(max_length=10, min_length=2)
    age: int = Field(gt=18, lt=100)


# This will still word despite the age being string
# value cause Pydantic supports type coercion
Employee.model_validate({"name": "Helen", "age": "19"})


# This will fail due to strict mode
Employee.model_validate({"name": "Helen", "age": "19"}, strict=True)

# This will work
Employee.model_validate({"name": "Helen", "age": 19}, strict=True)
