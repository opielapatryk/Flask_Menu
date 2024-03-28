import pymongo
import pytest


@pytest.fixture(scope="session")
def mg_database_empty(app_configuration):
    client = pymongo.MongoClient(
        host=app_configuration["MONGODB_HOSTNAME"],
        port=int(app_configuration["MONGODB_PORT"]),
        username=app_configuration["MONGODB_USER"],
        password=app_configuration["MONGODB_PASSWORD"],
        authSource="admin",
    )
    db = client[app_configuration["APPLICATION_DB"]]

    yield db

    client.drop_database(app_configuration["APPLICATION_DB"])
    client.close()


@pytest.fixture(scope="function")
def mg_test_data():
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
    ]


@pytest.fixture(scope="function")
def mg_database(mg_database_empty, mg_test_data):
    collection = mg_database_empty.dishes

    collection.insert_many(mg_test_data)

    yield mg_database_empty

    collection.delete_many({})
