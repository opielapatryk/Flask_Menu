from restaurant.domain.dish import Dish


class MemRepo:
    def __init__(self, data):
        self.data = data

    def list(self):
        result = [Dish.from_dict(i) for i in self.data]

        return result

    def get(self, id):
        result = self.data[id-1]

        return result
    
    def post(self, dish):
        self.data.append(dish)
        result = [Dish.from_dict(i) for i in self.data]

        return result
    
    def put(self, updated_dish):
        updated_data = []

        for dish in self.data:
            if dish['id'] == updated_dish['id']:
                updated_data.append(updated_dish)
            else:
                updated_data.append(dish)

        result = [Dish.from_dict(dish) for dish in updated_data]
        
        return result
    
    def delete(self, id):
        for dish in self.data:
            if dish['id'] == id:
                self.data.remove(dish)

        result = [Dish.from_dict(dish) for dish in self.data]
        
        return result

