import json

from restaurant.serializers.dish import DishJsonEncoder
from restaurant.domain.dish import Dish


def test_serialize_domain_dish():

    dish = Dish(
        position=1,
        name="pizza",
        description="italian speciality",
        price=9.99
    )

    expected_json = """
            {
                "position": 1,
                "name": "pizza",
                "description": "italian speciality",
                "price": 9.99
            }
        """

    json_dish = json.dumps(dish, cls=DishJsonEncoder)

    assert json.loads(json_dish) == json.loads(expected_json)
