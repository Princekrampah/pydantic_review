# Field Validators
from pydantic import (
    BaseModel,
    EmailStr,
    constr,
    field_validator
)

from datetime import datetime
import secrets


class Employee(BaseModel):
    id: str
    name: constr(min_length=2, max_length=10)  # type: ignore
    DOF: datetime
    email: EmailStr

    # we need the classmethod because this method is
    # called before the actual instantiation occurs

    @field_validator("name")
    @classmethod
    def full_employee_name(cls, v: str) -> str:
        """Checks if the caller provided name separated with ' '"""
        if not " " in v:
            raise ValueError(
                "You must provide two of your names separated with ' '")
        return v.title()


jane: Employee = Employee(
    id=secrets.token_hex(2),
    name="jane doe",
    DOF=datetime.now(),
    email="jane.doe@gmail.com"
)


print(jane.name)
