from restaurant.requests.dish_list import DishListRequest

def test_build_dish_list_request_without_parameters():
    request = DishListRequest()

    assert bool(request) is True

def test_build_dish_list_request_from_empty_dict():
    request = DishListRequest.from_dict({})

    assert bool(request) is True
    