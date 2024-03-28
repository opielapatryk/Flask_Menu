import pytest
from restaurant.repository import mongorepo

pytestmark = pytest.mark.integration


def test_repository_list_without_parameters(
    app_configuration, mg_database, mg_test_data
):
    repo = mongorepo.MongoRepo(app_configuration)

    repo_dishes = repo.list()

    assert set([d.name for d in repo_dishes]) == set(
        [d["name"] for d in mg_test_data]
    )