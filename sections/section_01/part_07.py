# Model validators
from pydantic import (
    BaseModel,
    EmailStr,
    constr,
    field_validator,
    model_validator
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

    # The mode="before" will make sure this is checked before types are validated
    @model_validator(mode="before")
    @classmethod
    def check_for_sensitive_info(cls, employee_details: dict) -> dict:
        if isinstance(employee_details, dict):
            if "national_security_code" in employee_details:
                raise ValueError(
                    "National Security Code Should Not Be provided")
            return employee_details

    # This will be called after the types have been validated
    # for this reason we do not have the classmethod decorator in place

    @model_validator(mode="after")
    def modal_full_employee_name(self) -> "Employee":
        """Checks if the caller provided name separated with ' '"""
        if not " " in self.name:
            raise ValueError(
                "You must provide two of your names separated with ' '")
        return self


jane: Employee = Employee(
    id=secrets.token_hex(2),
    name="jane doe",
    DOF=datetime.now(),
    email="jane.doe@gmail.com",
    # national_security_code="3diii33220jw"
)

print(jane.name)
