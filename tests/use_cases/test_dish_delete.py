from unittest import mock
import pytest
from restaurant.domain.dish import Dish
from restaurant.use_cases.dish_delete import dish_delete_use_case

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

@pytest.fixture
def domain_dishes_deleted():
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


def test_dish_delete_use_case(domain_dishes):
    repo = mock.Mock()
    repo.delete.return_value = [dish for dish in domain_dishes if dish.id != 3] 
    
    result = dish_delete_use_case(repo, 3)

    repo.delete.assert_called_with(3)
    assert result == [dish for dish in domain_dishes if dish.id != 3]