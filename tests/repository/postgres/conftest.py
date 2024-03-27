import sqlalchemy
import pytest

from restaurant.repository.postgres_objects import Base, Dish


@pytest.fixture(scope="session")
def pg_session_empty(app_configuration):
    conn_str = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
        app_configuration["POSTGRES_USER"],
        app_configuration["POSTGRES_PASSWORD"],
        app_configuration["POSTGRES_HOSTNAME"],
        app_configuration["POSTGRES_PORT"],
        app_configuration["APPLICATION_DB"],
    )
    engine = sqlalchemy.create_engine(conn_str)
    connection = engine.connect()

    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    DBSession = sqlalchemy.orm.sessionmaker(bind=engine)
    session = DBSession()

    yield session

    session.close()
    connection.close()


@pytest.fixture(scope="session")
def pg_test_data():
    return [
        {
            "name":'pierogi',
            "description":'Ulubione Polskie danie ;)',
            "price":20,
        },
        {
            "name":'schabowy z ziemniaczkami',
            "description":'Krolewska uczta!',
            "price":30,
        },
        {
            "name":'nalesniki',
            "description":'Something sweet',
            "price":7.99,
        },
        {
            "name":'pizza',
            "description":'pizza pepperoni',
            "price":5,
        },
    ]

@pytest.fixture(scope="function")
def pg_session(pg_session_empty, pg_test_data):
    for d in pg_test_data:
        new_dish = Dish(
            name=d['name'],
            description=d['description'],
            price=d['price'],
        )
        pg_session_empty.add(new_dish)
        pg_session_empty.commit()

    yield pg_session_empty

    pg_session_empty.query(Dish).delete()
