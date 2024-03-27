import pytest
from restaurant.repository.postgresrepo import PostgresRepo

pytestmark = pytest.mark.integration

def test_repository_list_without_parameters(app_configuration,pg_session,pg_test_data):
    repo = PostgresRepo(app_configuration)

    repo_dishes = repo.list()

    assert set([r.name for r in repo_dishes]) == set([r['name'] for r in pg_test_data])