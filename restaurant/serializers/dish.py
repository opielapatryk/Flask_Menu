import json

class DishJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            to_serialize = {
                "position": obj.position,
                "name": obj.name,
                "description": obj.description,
                "price": obj.price,
            }
            return to_serialize
        except AttributeError:
            return super().default(obj)