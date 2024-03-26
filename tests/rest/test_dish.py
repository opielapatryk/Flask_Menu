import json
import pytest
from unittest import mock

from restaurant.domain.dish import Dish

@pytest.fixture
def domain_dishes():
    dish_1 = Dish(
        position=1,
        name='pizza',
        description='italiano sepcailze',
        price=9.99
    )
    dish_2 = Dish(
        position=2,
        name='spagetti',
        description='italiano pasta',
        price=14.99
    )
    dish_3 = Dish(
        position=3,
        name='nalesniki',
        description='Something sweet',
        price=7.99,
    )
    dish_4 = Dish(
        position=4,
        name='chips',
        description='fried potatooo',
        price=3.29
    )

    return [dish_1, dish_2, dish_3, dish_4]


@mock.patch("application.rest.dish.dish_list_use_case")
def test_list(mock_use_case, client, domain_dishes):
    mock_use_case.return_value = domain_dishes

    http_response = client.get("/dishes")

    dishes = [dish.to_dict() for dish in domain_dishes]

    assert json.loads(http_response.data.decode("UTF-8")) == dishes

    mock_use_case.assert_called()

    assert http_response.status_code == 200
    assert http_response.mimetype == "application/json"

@mock.patch("application.rest.dish.dish_get_use_case")
def test_get(mock_use_case, client, domain_dishes):
    mock_use_case.return_value = domain_dishes[2]

    http_response = client.get("/dishes/3")

    dish = domain_dishes[2].to_dict()

    assert json.loads(http_response.data.decode("UTF-8")) == dish

    mock_use_case.assert_called()

    assert http_response.status_code == 200
    assert http_response.mimetype == "application/json"