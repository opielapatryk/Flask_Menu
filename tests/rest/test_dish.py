import json
from unittest import mock

from restaurant.domain.dish import Dish

dish_dict = {
    "position": 1,
    "name": "oreoooooooooooooooo",
    "description": 'awesome snack',
    "price": 9.99,
}

dishes = [Dish.from_dict(dish_dict)]


@mock.patch("application.rest.dish.dish_list_use_case")
def test_get(mock_use_case, client):
    mock_use_case.return_value = dishes

    http_response = client.get("/dishes")

    assert json.loads(http_response.data.decode("UTF-8")) == [dish_dict]

    mock_use_case.assert_called()

    assert http_response.status_code == 200
    assert http_response.mimetype == "application/json"