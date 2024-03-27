import pytest

from restaurant.repository.memrepo import MemRepo
from restaurant.domain.dish import Dish

@pytest.fixture
def dish_dicts():
    return [
        {
            "id":1,
            "name":'pierogi',
            "description":'Ulubione Polskie danie ;)',
            "price":20,
        },
        {
            "id":2,
            "name":'schabowy z ziemniaczkami',
            "description":'Krolewska uczta!',
            "price":30,
        },
        {
            "id":3,
            "name":'nalesniki',
            "description":'Something sweet',
            "price":7.99,
        },
        {
            "id":4,
            "name":'pizza',
            "description":'pizza pepperoni',
            "price":5,
        }
    ]

@pytest.fixture
def dish_dicts_delete():
    return [
        {
            "id":1,
            "name":'pierogi',
            "description":'Ulubione Polskie danie ;)',
            "price":20,
        },
        {
            "id":2,
            "name":'schabowy z ziemniaczkami',
            "description":'Krolewska uczta!',
            "price":30,
        },
        {
            "id":4,
            "name":'pizza',
            "description":'pizza pepperoni',
            "price":5,
        }
    ]

@pytest.fixture
def dish_dicts_post():
    return [
        {
            "id":1,
            "name":'pierogi',
            "description":'Ulubione Polskie danie ;)',
            "price":20,
        },
        {
            "id":2,
            "name":'schabowy z ziemniaczkami',
            "description":'Krolewska uczta!',
            "price":30,
        },
        {
            "id":3,
            "name":'nalesniki',
            "description":'Something sweet',
            "price":7.99,
        },
        {
            "id":4,
            "name":'pizza',
            "description":'pizza pepperoni',
            "price":5,
        },
        {
        "id":5,
        "name":'pomidorowa',
        "description":'Soup',
        "price":4.99,
        }
    ]

@pytest.fixture
def dish_dicts_put():
    return [
        {
            "id":1,
            "name":'pierogi',
            "description":'Ulubione Polskie danie ;)',
            "price":20,
        },
        {
            "id":2,
            "name":'schabowy z ziemniaczkami',
            "description":'Krolewska uczta!',
            "price":30,
        },
        {
            "id":3,
            "name":'hot-dog',
            "description":'snack',
            "price":2.99,
        },
        {
            "id":4,
            "name":'pizza',
            "description":'pizza pepperoni',
            "price":5,
        }
    ]



def test_repository_list_without_parameters(dish_dicts):
    repo = MemRepo(dish_dicts)

    dishes = [Dish.from_dict(i) for i in dish_dicts]

    assert repo.list() == dishes

def test_repository_get(dish_dicts):
    repo = MemRepo(dish_dicts)

    dish = {
            "id":3,
            "name":'nalesniki',
            "description":'Something sweet',
            "price":7.99,
        }

    assert repo.get(3) == dish

def test_repository_post(dish_dicts, dish_dicts_post):
    repo = MemRepo(dish_dicts)

    dish = {
        "id":5,
        "name":'pomidorowa',
        "description":'Soup',
        "price":4.99,
    }

    result = [Dish.from_dict(dish) for dish in dish_dicts_post]
    assert repo.post(dish) == result

def test_repository_put(dish_dicts,dish_dicts_put):
    repo = MemRepo(dish_dicts)

    updated_dish = {
        "id":3,
        "name":'hot-dog',
        "description":'snack',
        "price":2.99
    }

    result = [Dish.from_dict(dish) for dish in dish_dicts_put]

    assert repo.put(updated_dish) == result

def test_repository_delete(dish_dicts,dish_dicts_delete):
    repo = MemRepo(dish_dicts)

    result = [Dish.from_dict(dish) for dish in dish_dicts_delete if dish['id'] != id]

    assert repo.delete(3) == result
    assert repo.list() == result