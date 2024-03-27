import pytest
from unittest import mock

from restaurant.domain.dish import Dish
from restaurant.use_cases.dish_list import dish_list_use_case
from restaurant.requests.dish_list import DishListRequest


@pytest.fixture
def domain_dishes():
    dish_1 = Dish(
        id=1,
        name='pizza',
        description='italiano sepcailze',
        price=9.99
    )
    dish_2 = Dish(
        id=2,
        name='spagetti',
        description='italiano pasta',
        price=14.99
    )
    dish_3 = Dish(
        id=3,
        name='nalesniki',
        description='Something sweet',
        price=7.99,
    )
    dish_4 = Dish(
        id=4,
        name='chips',
        description='fried potatooo',
        price=3.29
    )

    return [dish_1, dish_2, dish_3, dish_4]


def test_dish_list_without_parameters(domain_dishes):
    repo = mock.Mock()
    repo.list.return_value = domain_dishes

    request = DishListRequest()

    response = dish_list_use_case(repo, request)

    assert bool(response) is True
    repo.list.assert_called_with()
    assert response.value == domain_dishes
