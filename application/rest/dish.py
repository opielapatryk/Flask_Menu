import json

from flask import Blueprint, Response

from restaurant.repository.memrepo import MemRepo
from restaurant.use_cases.dish_list import dish_list_use_case
from restaurant.serializers.dish import DishJsonEncoder

blueprint = Blueprint("dish", __name__)

dishes = [
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
]

@blueprint.route("/dishes", methods=["GET"])
def dish_list():
    repo = MemRepo(dishes)
    result = dish_list_use_case(repo)

    return Response(
        json.dumps(result, cls=DishJsonEncoder),
        mimetype="application/json",
        status=200,
    )