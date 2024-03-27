import pytest
from restaurant.repository import postgresrepo

pytestmark = pytest.mark.integration

def test_repository_list_without_parameters(app_configuration,pg_session,pg_test_data):
    repo = postgresrepo.PostgresRepo(app_configuration)

    repo_dishes = repo.list()

    assert set([d.name for d in repo_dishes]) == set([d['name'] for d in pg_test_data])

def test_repository_get(app_configuration,pg_session,pg_test_data):
    repo = postgresrepo.PostgresRepo(app_configuration)

    dish = repo.get(5) # it's seems like data from pg_test_data are in id's range 5-8

    assert dish.name == pg_test_data[0]['name']

def test_repository_post(app_configuration,pg_session,pg_test_data):
    repo = postgresrepo.PostgresRepo(app_configuration)

    dish = {
        "name":'lazania',
        "description":'italiano',
        "price":12.99
    }

    repo_dishes = repo.post(dish) 

    assert len(repo_dishes) == 5
