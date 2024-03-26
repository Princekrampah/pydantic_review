# Field values
from pydantic import BaseModel, Field, EmailStr
import secrets
from decimal import Decimal


class Employee(BaseModel):
    id: str = Field(default="123")


jane: Employee = Employee()

print(jane.id)


# Default factory to create dynamic values. These default values can also be
# overriden
class Employee(BaseModel):
    id: str = Field(default_factory=lambda: secrets.token_hex(2))


jane: Employee = Employee()

print(jane.id)


# Aliases
class Employee(BaseModel):
    id: str = Field(..., alias="user_id",
                    default_factory=lambda: secrets.token_hex(2))


jane: Employee = Employee(user_id="23k")

print(jane.model_dump(by_alias=True))


class Account(BaseModel):
    id: str = Field(..., alias="accnt_id",
                    default_factory=lambda: secrets.token_hex(3))
    name: str = Field(..., max_length=10, min_length=2)
    email: EmailStr = Field(...)
    balance: Decimal = Field(max_digits=10, decimal_places=3)
    withdraw_range: Decimal = Field(gt=100.000, lt=100_000.000)


my_accnt: Account = Account(
    name="Helen",
    email="helen.doe@example.com",
    balance=20_000.08,
    withdraw_range=700
)

print(my_accnt.model_dump())
print(my_accnt.model_dump_json())
