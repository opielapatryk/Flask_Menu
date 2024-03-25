import dataclasses
@dataclasses.dataclass
class Dish:
    position: int
    name: str
    description: str
    price: float
    
    @classmethod
    def from_dict(self,item):
        return self(**item)