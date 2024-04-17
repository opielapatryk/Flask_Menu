from flask import jsonify,Blueprint, request, Response
import json
from restaurant.serializers.dish import DishJsonEncoder
from restaurant.repository.mongorepo import MongoRepo
from restaurant.repository.memrepo import MemRepo
from restaurant.repository.postgresrepo import PostgresRepo
from restaurant.use_cases.dish_list import dish_list_use_case
from restaurant.use_cases.dish_get import dish_get_use_case
from restaurant.use_cases.dish_post import dish_post_use_case
from restaurant.use_cases.dish_put import dish_put_use_case
from restaurant.use_cases.dish_patch import dish_patch_use_case
from restaurant.use_cases.dish_delete import dish_delete_use_case
from restaurant.requests.dish_list import build_dish_list_request

blueprint = Blueprint("dish", __name__)

postgres_configuration = {
    "POSTGRES_USER": 'postgres',
    "POSTGRES_PASSWORD":'postgres',
    "POSTGRES_HOSTNAME": 'db',
    "POSTGRES_PORT": 5432,
    "APPLICATION_DB": 'postgres',
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

mongo_configuration = {
    "MONGODB_HOSTNAME": 'db',
    "MONGODB_PORT": 27017,
    "MONGODB_USER": 'root',
    "MONGODB_PASSWORD": 'mongodb',
    "APPLICATION_DB": 'restaurant',
}

repo = MemRepo(dishes)

@blueprint.route("/api/v1/dishes", methods=["GET","POST","PUT"])
def dish_view():
    if request.method == "GET":
        request_object = build_dish_list_request()
        result = dish_list_use_case(repo,request_object)

        # Filtering options
        description = request.args.get('description')
        min_price = float(request.args.get('min_price', 0))
        max_price = float(request.args.get('max_price', float('inf')))

        # Apply filters
        filtered_dishes = filter(lambda d: d['price'] >= min_price and d['price'] <= max_price, result.value)

        if description:
            filtered_dishes = filter(lambda d: d['description'] == description, filtered_dishes)


        # Sorting parameters
        sort_by = request.args.get('sort_by', 'id')
        sort_order = request.args.get('sort_order', 'asc')
        sorted_dishes = sorted(filtered_dishes, key=lambda p: p[sort_by], reverse=sort_order.lower() == 'desc')

        # Pagination parameters
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))

        # Paginate the results
        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        paginated_dishes = sorted_dishes[start_index:end_index]

        
        return Response(
            json.dumps(paginated_dishes, cls=DishJsonEncoder),
            mimetype="application/json",
            status=200,
        )
    
    if request.method == 'POST':
        dish = request.json

        id = dish.get('id')
        name = dish.get('name')
        description = dish.get('description')
        price = dish.get('price')

        if not name or not description or not price or not id:
            return Response(json.dumps({"message":"Missing required fields"}),mimetype="application/json",status=400)
        
        result = dish_post_use_case(repo, dish)

        return Response(
            json.dumps(result, cls=DishJsonEncoder),
            mimetype="application/json",
            status=201,
        )
    
    if request.method == 'PUT':
        updated_dish = request.json
        result = dish_put_use_case(repo, updated_dish)

        if result:
            return Response(
                json.dumps(result, cls=DishJsonEncoder),
                mimetype="application/json",
                status=201,
            )
        else:
            return Response(
                json.dumps({"message":"Dish not found"}),
                mimetype="application/json",
                status=404,
            )

        
@blueprint.route("/api/v1/dishes/<int:dish_id>", methods=["GET","PATCH","DELETE"])
def dish_specific_view(dish_id):
    if request.method == "GET":
        result = dish_get_use_case(repo, dish_id)

        if result:
            return Response(
                json.dumps(result, cls=DishJsonEncoder),
                mimetype="application/json",
                status=200,
            )
        else:
            return Response(
                json.dumps({"message":"Dish not found"}),
                mimetype="application/json",
                status=404,
            )
        
    if request.method == "PATCH":
        dish = request.json

        updated_dish_data = {}
        
        if dish.get('name') is not None: updated_dish_data['name'] = dish.get('name')
        if dish.get('description') is not None: updated_dish_data['description'] = dish.get('description')
        if dish.get('price') is not None: updated_dish_data['price'] = dish.get('price')

        result = dish_patch_use_case(repo, updated_dish_data, dish_id)

        if result:
            return Response(
                json.dumps(result, cls=DishJsonEncoder),
                mimetype="application/json",
                status=201,
            )
        else:
            return Response(
                json.dumps({"message":"Dish not found"}),
                mimetype="application/json",
                status=404,
            )
        
    if request.method == 'DELETE':
        result = dish_delete_use_case(repo, dish_id)

        if result:
            return Response(
                json.dumps(result, cls=DishJsonEncoder),
                mimetype="application/json",
                status=200,
            )
        else:
            return Response(
                json.dumps({"message":"Dish not found"}),
                mimetype="application/json",
                status=404,
            )