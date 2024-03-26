import pytest

from restaurant.repository.memrepo import MemRepo
from restaurant.domain.dish import Dish

@pytest.fixture
def dish_dicts():
    return [
        {
            "position":1,
            "name":'pierogi',
            "description":'Ulubione Polskie danie ;)',
            "price":20,
        },
        {
            "position":2,
            "name":'schabowy z ziemniaczkami',
            "description":'Krolewska uczta!',
            "price":30,
        },
        {
            "position":3,
            "name":'nalesniki',
            "description":'Something sweet',
            "price":7.99,
        },
        {
            "position":4,
            "name":'pizza',
            "description":'pizza pepperoni',
            "price":5,
        }
    ]

@pytest.fixture
def dish_dicts_post():
    return [
        {
            "position":1,
            "name":'pierogi',
            "description":'Ulubione Polskie danie ;)',
            "price":20,
        },
        {
            "position":2,
            "name":'schabowy z ziemniaczkami',
            "description":'Krolewska uczta!',
            "price":30,
        },
        {
            "position":3,
            "name":'nalesniki',
            "description":'Something sweet',
            "price":7.99,
        },
        {
            "position":4,
            "name":'pizza',
            "description":'pizza pepperoni',
            "price":5,
        },
        {
        "position":5,
        "name":'pomidorowa',
        "description":'Soup',
        "price":4.99,
        }
    ]

def test_repository_list_without_parameters(dish_dicts):
    repo = MemRepo(dish_dicts)

    dishes = [Dish.from_dict(i) for i in dish_dicts]

    assert repo.list() == dishes

def test_repository_get(dish_dicts):
    repo = MemRepo(dish_dicts)

    dish = {
            "position":3,
            "name":'nalesniki',
            "description":'Something sweet',
            "price":7.99,
        }

    assert repo.get(3) == dish

def test_repository_post(dish_dicts, dish_dicts_post):
    repo = MemRepo(dish_dicts)

    dish = {
        "position":5,
        "name":'pomidorowa',
        "description":'Soup',
        "price":4.99,
    }

    assert repo.post(dish) == dish_dicts_post