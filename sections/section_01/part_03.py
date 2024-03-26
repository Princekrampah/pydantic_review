from pydantic import BaseModel


class Car(BaseModel):
    name: str
    top_speed: int


# Here we are not using strict mode hence, we can pass in
# string to the top_speed parameter despite of it being int type,
# this will work as long as the string can be converted into int. If not
# you then get an error being raised.

# this will work
toyoto_supra: Car = Car(name="Supra", top_speed="223")

# this will not work
# toyoto_supra: Car = Car(name="Supra", top_speed="2u23")


###### Default Values ######
class Car(BaseModel):
    name: str
    top_speed: int = 120


toyoto_supra: Car = Car(name="Supra")
print(toyoto_supra.top_speed)


# model json schema to view the schema details
print(toyoto_supra.model_json_schema())

# model field sets
print(toyoto_supra.model_fields_set)

toyoto_supra: Car = Car(name="Supra", top_speed=130)
print(toyoto_supra.model_fields_set)


# model dumps
print("====================== Model Dump ========================")
print(f"Convert to a dict: {toyoto_supra.model_dump()}")
print(f"Convert to a JSON: {toyoto_supra.model_dump_json()}")
