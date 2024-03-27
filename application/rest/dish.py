import os
import json
from flask import jsonify

from flask import Blueprint, Response, request

from restaurant.repository.postgresrepo import PostgresRepo
from restaurant.repository.memrepo import MemRepo
from restaurant.use_cases.dish_list import dish_list_use_case
from restaurant.use_cases.dish_get import dish_get_use_case
from restaurant.use_cases.dish_post import dish_post_use_case
from restaurant.use_cases.dish_put import dish_put_use_case
from restaurant.use_cases.dish_delete import dish_delete_use_case
from restaurant.serializers.dish import DishJsonEncoder
from restaurant.requests.dish_list import build_dish_list_request

blueprint = Blueprint("dish", __name__)

postgres_configuration = {
    "POSTGRES_USER": os.environ["POSTGRES_USER"],
    "POSTGRES_PASSWORD": os.environ["POSTGRES_PASSWORD"],
    "POSTGRES_HOSTNAME": os.environ["POSTGRES_HOSTNAME"],
    "POSTGRES_PORT": os.environ["POSTGRES_PORT"],
    "APPLICATION_DB": os.environ["APPLICATION_DB"],
}

dishes = [
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
    repo = PostgresRepo(postgres_configuration)
    request_object = build_dish_list_request()
    result = dish_list_use_case(repo,request_object)

    return Response(
        json.dumps(result.value, cls=DishJsonEncoder),
        mimetype="application/json",
        status=200,
    )

@blueprint.route("/dishes/<int:dish_id>", methods=["GET"])
def dish_get(dish_id):
    repo = PostgresRepo(postgres_configuration)
    result = dish_get_use_case(repo, dish_id)

    return Response(
        json.dumps(result, cls=DishJsonEncoder),
        mimetype="application/json",
        status=200,
    )

@blueprint.route("/dishes", methods=["POST"])
def dish_post():
    dish_data = request.json
    repo = PostgresRepo(postgres_configuration)
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

@blueprint.route("/dishes/<int:dish_id>", methods=["DELETE"])
def dish_delete(dish_id):
    repo = MemRepo(dishes)
    result = dish_delete_use_case(repo, dish_id)

    return Response(
        json.dumps(result, cls=DishJsonEncoder),
        mimetype="application/json",
        status=204,
    )