from restaurant.domain.dish import Dish


class MemRepo:
   def __init__(self, data):
      self.data = data
   
   def list(self):
      return self.data
    
   def get(self, id):
      dish = [Dish.from_dict(dish) for dish in self.data if dish['id'] == id]
      return dish

   def post(self, dish):
      if dish['id'] > len(self.data):
         self.data.append(dish)
         result = [Dish.from_dict(i) for i in self.data]
         return result

   def put(self, updated_dish):
      for dish in self.data:
         if dish['id'] == updated_dish['id']:
            dish['name'] = updated_dish['name']
            dish['description'] = updated_dish['description']
            dish['price'] = updated_dish['price']

            result = [Dish.from_dict(i) for i in self.data]
            return result

   def patch(self, updated_dish,dish_id):
      for dish in self.data:
         if dish['id'] == dish_id:
               for key in updated_dish.keys():
                  dish[key] = updated_dish[key]

               result = [Dish.from_dict(i) for i in self.data]
               return result
   
   def delete(self, id):
      for dish in self.data:
         if dish['id'] == id:
               self.data.remove(dish)
               result = [Dish.from_dict(dish) for dish in self.data]
               return result