import pytest
from unittest import mock

from restaurant.domain.dish import Dish
from restaurant.use_cases.dish_post import dish_post_use_case


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
def domain_dishes_post():
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
    dish_5 = Dish(
        id=5,
        name='pomidorowa',
        description='Soup',
        price=3.99
    )

    return [dish_1, dish_2, dish_3, dish_4, dish_5]


def test_dish_post(domain_dishes_post):
    repo = mock.Mock()
    repo.post.return_value = domain_dishes_post

    dish = Dish(
        id=5,
        name='pomidorowa',
        description='Soup',
        price=3.99
    )

    result = dish_post_use_case(repo, dish)
    
    repo.post.assert_called_with(dish)
    assert result == domain_dishes_post