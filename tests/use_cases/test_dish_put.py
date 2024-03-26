from unittest import mock
import pytest
from restaurant.domain.dish import Dish
from restaurant.use_cases.dish_put import dish_put_use_case

@pytest.fixture
def domain_dishes_put():
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

def test_dish_put(domain_dishes_put):
    repo = mock.Mock()
    repo.put.return_value = domain_dishes_put

    updated_dish = Dish(
        id=3,
        name='hot-dog',
        description='snack',
        price=2.99
    )

    result = dish_put_use_case(repo, updated_dish)
    
    repo.put.assert_called_with(updated_dish)
    assert result == domain_dishes_put