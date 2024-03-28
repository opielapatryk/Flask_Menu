import pymongo

from restaurant.domain import dish


class MongoRepo:
    def __init__(self, configuration):
        client = pymongo.MongoClient(
            host=configuration["MONGODB_HOSTNAME"],
            port=int(configuration["MONGODB_PORT"]),
            username=configuration["MONGODB_USER"],
            password=configuration["MONGODB_PASSWORD"],
            authSource="admin",
        )

        self.db = client[configuration["APPLICATION_DB"]]

    def _create_dish_objects(self, results):
        return [
            dish.Dish(
                id=q["id"],
                name=q["name"],
                description=q["description"],
                price=q["price"],
            )
            for q in results
        ]

    def list(self):
        collection = self.db.dishes

        result = collection.find()

        return self._create_dish_objects(result)
