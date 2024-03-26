from restaurant.domain.dish import Dish


class MemRepo:
    def __init__(self, data):
        self.data = data

    def list(self):

        result = [Dish.from_dict(i) for i in self.data]

        return result

    def get(self, position):
        result = self.data[position-1]

        return result
    
    def post(self, dish):
        self.data.append(dish)
        result = self.data

        return result