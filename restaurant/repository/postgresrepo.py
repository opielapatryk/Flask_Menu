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
            {
                'id':result.id,
                'name':result.name,
                'description':result.description,
                'price':result.price,
            }
            for result in results
        ]
    
    def list(self):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        query = session.query(Dish)
        result = self._create_dish_object(query.all())
        return result
    

    def get(self, id):
        dishes = self.list()
        for dish in dishes:
            if dish['id'] == id:
                return dish
    
    def post(self, dish):
        dish_instance = Dish(name=dish['name'], description=dish['description'], price=dish['price'])

        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        session.add(dish_instance)
        session.commit()
        query = session.query(Dish)

        return self._create_dish_object(query.all())
    
    def put(self, updated_dish):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        dish_to_update = session.query(Dish).filter_by(id=updated_dish['id']).first()
        if dish_to_update:
            dish_to_update.name = updated_dish['name']
            dish_to_update.description = updated_dish['description']
            dish_to_update.price = updated_dish['price']
            session.commit()

        query = session.query(Dish)
        return self._create_dish_object(query.all())
    
    def patch(self, updated_dish, dish_id):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        dish_to_update = session.query(Dish).filter_by(id=dish_id).first()
        if dish_to_update:
            for key in updated_dish.keys():
                if key == 'name':
                    dish_to_update.name = updated_dish['name']
                if key == 'description':
                    dish_to_update.description = updated_dish['description']
                if key == 'price':
                    dish_to_update.price = updated_dish['price']
            session.commit()

        query = session.query(Dish)
        return self._create_dish_object(query.all())

    
    def delete(self, id):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        dish_to_delete = session.query(Dish).filter_by(id=id).first()
        if dish_to_delete:
            session.delete(dish_to_delete)
            session.commit()

        query = session.query(Dish)
        return self._create_dish_object(query.all())
    