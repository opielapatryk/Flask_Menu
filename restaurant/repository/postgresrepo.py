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
    
    def put(self, updated_dish):
        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()
        # query = session.query(Dish)
        dish_to_update = session.query(Dish).filter_by(id=updated_dish['id']).first()
        if dish_to_update:
            # Update the attributes of the existing dish
            dish_to_update.name = updated_dish['name']
            dish_to_update.description = updated_dish['description']
            dish_to_update.price = updated_dish['price']
            session.commit()
            # dishes = self._create_dish_object(query.all())
        query = session.query(Dish)
        return self._create_dish_object(query.all())

        for dish in dishes:
            if dish.id == updated_dish['id']:
                up_d = Dish(id=dish.id,name=updated_dish['name'], description=updated_dish['description'], price=updated_dish['price'])
                del_d = Dish(id=dish.id,name=dish.name, description=dish.description, price=dish.price)
                session.delete(del_d)
                session.add(up_d)
                session.commit()
                break
        
        
        query = session.query(Dish)
        return self._create_dish_object(query.all())
    
    # def delete(self, id):
    #     for dish in self.data:
    #         if dish['id'] == id:
    #             self.data.remove(dish)

    #     result = [Dish.from_dict(dish) for dish in self.data]
        
    #     return result

