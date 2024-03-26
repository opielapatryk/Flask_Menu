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
    
    def to_dict(self):
        return {
            "position": self.position,
            "name": self.name,
            "description": self.description,
            "price": self.price,
        }