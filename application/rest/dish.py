import json
from flask import jsonify

from flask import Blueprint, Response, request

from restaurant.repository.memrepo import MemRepo
from restaurant.use_cases.dish_list import dish_list_use_case
from restaurant.use_cases.dish_get import dish_get_use_case
from restaurant.use_cases.dish_post import dish_post_use_case
from restaurant.use_cases.dish_put import dish_put_use_case
from restaurant.serializers.dish import DishJsonEncoder
from restaurant.domain.dish import Dish

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

@blueprint.route("/", methods=["GET"])
def welcome():
    return jsonify({
        "message": "Welcome to the Restaurant API!",
        "endpoints": {
            "dishes": "/dishes"
        }
    })


@blueprint.route("/dishes", methods=["GET"])
def dish_list():
    repo = MemRepo(dishes)
    result = dish_list_use_case(repo)

    return Response(
        json.dumps(result, cls=DishJsonEncoder),
        mimetype="application/json",
        status=200,
    )

@blueprint.route("/dishes/<int:dish_id>", methods=["GET"])
def dish_get(dish_id):
    repo = MemRepo(dishes)
    result = dish_get_use_case(repo, dish_id)

    return Response(
        json.dumps(result, cls=DishJsonEncoder),
        mimetype="application/json",
        status=200,
    )

@blueprint.route("/dishes", methods=["POST"])
def dish_post():
    dish_data = request.json
    # dish = Dish(**dish_data)
    repo = MemRepo(dishes)
    result = dish_post_use_case(repo, dish_data)

    return Response(
        json.dumps(result, cls=DishJsonEncoder),
        mimetype="application/json",
        status=201,
    )

@blueprint.route("/dishes", methods=["PUT"])
def dish_put():
    repo = MemRepo(dishes)
    updated_dish = request.json
    result = dish_put_use_case(repo, updated_dish)

    return Response(
        json.dumps(result, cls=DishJsonEncoder),
        mimetype="application/json",
        status=201,
    )
