import json
import pytest
from unittest import mock

from restaurant.domain.dish import Dish

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

@mock.patch("application.rest.dish.dish_post_use_case")
def test_post(mock_use_case, client, domain_dishes):
    new_dish_data = {
        "id": 5,
        "name": "pomidorowa",
        "description": "Soup",
        "price": 3.99
    }
        
    mock_use_case.return_value = domain_dishes + [Dish(**new_dish_data)]

    http_response = client.post("/dishes", json=new_dish_data)
    expected_response = [dish.to_dict() for dish in domain_dishes + [Dish(**new_dish_data)]]

    assert json.loads(http_response.data.decode("UTF-8")) == expected_response

    mock_use_case.assert_called()

    assert http_response.status_code == 201
    assert http_response.mimetype == "application/json"

@mock.patch("application.rest.dish.dish_put_use_case")
def test_put(mock_use_case,client,domain_dishes):
    updated_dish_dict = {
        "id": 3,
        "name": "hot-dog",
        "description": "snack",
        "price": 2.99        
    }

    updated_dish = Dish(**updated_dish_dict)

    mock_use_case.return_value = [updated_dish if dish.id == updated_dish.id else dish for dish in domain_dishes]

    http_response = client.put("/dishes", json=updated_dish_dict)

    dishes = [updated_dish.to_dict() if dish.id == updated_dish.id else dish.to_dict() for dish in domain_dishes]

    assert json.loads(http_response.data.decode("UTF-8")) == dishes

    mock_use_case.assert_called()

    assert http_response.status_code == 201
    assert http_response.mimetype == "application/json"

@mock.patch("application.rest.dish.dish_delete_use_case")
def test_delete(mock_use_case,client,domain_dishes):
    mock_use_case.return_value = [dish for dish in domain_dishes if dish.id != 3]

    http_response = client.delete("/dishes/3")    

    mock_use_case.assert_called()
    assert http_response.status_code == 204
    assert http_response.mimetype == "application/json"