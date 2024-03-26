# Computed fields
from pydantic import BaseModel, Field, computed_field, field_validator
from uuid import uuid4
from datetime import datetime


class Employee(BaseModel):
    id: str = Field(default_factory=lambda: uuid4().hex[:4])
    birth_year: int

    @computed_field
    @property
    def age(self) -> int:
        current_year = datetime.now().year
        age = current_year - self.birth_year
        return age


jane: Employee = Employee(birth_year='1980')

print(jane.model_dump())


class Employee(BaseModel):
    id: str = Field(default_factory=lambda: uuid4().hex[:4])
    birth_year: int

    # we can not perform the validation on a compute field
    @property
    def age(self) -> int:
        current_year = datetime.now().year
        age = current_year - self.birth_year
        return age

    @field_validator("birth_year")
    @classmethod
    def verify_age_limit(cls, v: int) -> int:
        current_year = datetime.now().year
        if current_year - v < 18:
            raise ValueError("An employee needs to be 18 or above")
        return v


jane: Employee = Employee(birth_year='2006')

print(jane.model_dump())
