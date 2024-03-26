import dataclasses
@dataclasses.dataclass
class Dish:
    id: int
    name: str
    description: str
    price: float
    
    @classmethod
    def from_dict(self,item):
        return self(**item)
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
        }