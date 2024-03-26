from dataclasses import dataclass, field
from pydantic import TypeAdapter, Field


@dataclass
class Employee:
    name: str
    age: int = field(
        metadata=dict(name="age", ge=18, le=100)
    )
    # you can use pydantic Fields in data classes
    location: str = Field(..., alias="residence")


jane: Employee = Employee(
    name="John Doe",
    age=11
)


print(jane)

# convert to pydantic
print(TypeAdapter(Employee).json_schema())


# NOTE: IF you want to use dataclasses stick to dataclasses if you want to
# use pydantic stick to pydantic. Avoid combining the two.
