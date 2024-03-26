# Writing custom type checkers

class Car:
    def __init__(self, name: str, top_speed: int) -> None:
        if not isinstance(name, str):
            raise TypeError(f"Expected str, got {type(name)}")
        
        if not isinstance(top_speed, int):
            raise TypeError(f"Expected int, got {type(top_speed)}")
        
        

toyota_supra: Car = Car(name="Supra", top_speed="2323")

print(toyota_supra.name)