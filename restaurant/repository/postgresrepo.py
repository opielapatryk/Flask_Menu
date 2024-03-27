from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from restaurant.domain import dish
from restaurant.repository.postgres_objects import Base, Dish

class PostgresRepo:
    def __init__(self, configuration):
        connection_string = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
            configuration["POSTGRES_USER"],
            configuration["POSTGRES_PASSWORD"],
            configuration["POSTGRES_HOSTNAME"],
            configuration["POSTGRES_PORT"],
            configuration["APPLICATION_DB"],
        )

        self.engine = create_engine(connection_string)
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine
    
    def _create_dish_object(self, results):
        return [
            dish.Dish(
                id = q.id,
                name = q.name,
                description=q.description,
                price=q.price,
            )
            for q in results
        ]
    
    def list(self):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(Dish)

        return self._create_dish_object(query.all())