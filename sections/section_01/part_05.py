from pydantic import (
    BaseModel,
    HttpUrl,
    PositiveInt,
    EmailStr,
    conlist,
    constr,
    Field
)
from typing import List, Optional
from datetime import datetime
import secrets


class Car(BaseModel):
    name: str
    top_speed: Optional[int] = 120


class Manufacturer(BaseModel):
    name: str
    location: str
    vehicles: List[Car]


class Employee(BaseModel):
    id: str
    name: constr(min_length=2, max_length=10)  # type: ignore
    DOF: datetime
    # poetry add pydantic[email]
    email: EmailStr


class Branch(BaseModel):
    id: str
    name: str = Field(..., pattern=r"^[a-zA-Z0-9-' ]+$")  # type: ignore
    location: str
    website: HttpUrl
    employee_count: PositiveInt
    # constrainted types
    employees: conlist(item_type=Employee, min_length=2,
                       max_length=25)  # type: ignore


toyota: Manufacturer = Manufacturer(
    name="Toyota",
    location="Japan",
    vehicles=[
        {"name": "Supra", "top_speed": 140},
        {"name": "RAV4"}
    ]
)

jane: Employee = Employee(
    id=secrets.token_hex(2),
    name="Jane Doe",
    DOF=datetime.now(),
    email="jane.doe@example.com"
)


john: Employee = Employee(
    id=secrets.token_hex(2),
    name="John Doe",
    DOF=datetime.now(),
    email="john.doe@example.com"
)


nairobi_branch: Branch = Branch(
    id=secrets.token_hex(2),
    name="Nairobi Branch",
    location="Nairobi",
    website="https://www.toyota.nairobi.co.ke",
    employee_count=10,
    employees=[
        john.model_dump(),
        jane.model_dump()
    ]
)


print(nairobi_branch.employees)
print(nairobi_branch.employees[0].DOF)
