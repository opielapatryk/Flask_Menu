class DishListRequest:
    @classmethod
    def from_dict(cls, adict):
        return cls()

    def __bool__(self):
        return True

def build_dish_list_request():
    return DishListRequest()