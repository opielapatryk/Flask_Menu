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
                id=result.id,
                name=result.name,
                description=result.description,
                price=result.price,
            )
            for result in results
        ]
    
    def list(self):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(Dish)

        return self._create_dish_object(query.all())
    

    def get(self, id):
        dishes = self.list()
        for dish in dishes:
            if dish.id == id:
                return dish
        return '404 Not Found'
    
    def post(self, dish):
        dish_instance = Dish(name=dish['name'], description=dish['description'], price=dish['price'])

        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        session.add(dish_instance)
        session.commit()
        query = session.query(Dish)

        return self._create_dish_object(query.all())
    
    # def put(self, updated_dish):
    #     updated_data = []

    #     for dish in self.data:
    #         if dish['id'] == updated_dish['id']:
    #             updated_data.append(updated_dish)
    #         else:
    #             updated_data.append(dish)

    #     result = [Dish.from_dict(dish) for dish in updated_data]
        
    #     return result
    
    # def delete(self, id):
    #     for dish in self.data:
    #         if dish['id'] == id:
    #             self.data.remove(dish)

    #     result = [Dish.from_dict(dish) for dish in self.data]
        
    #     return result

