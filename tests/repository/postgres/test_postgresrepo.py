import pytest
from restaurant.repository.postgres_objects import Dish

pytestmark = pytest.mark.integration

def test_dummy(pg_session):
    assert len(pg_session.query(Dish).all()) == 4