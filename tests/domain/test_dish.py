from restaurant.domain.dish import Dish

def test_dish_model_init():
    dish = Dish(
        id=1,
        name='pierogi',
        description='My favorite Polish dish',
        price=20,
    )

    assert dish.id == 1
    assert dish.name == 'pierogi'
    assert dish.description == 'My favorite Polish dish'
    assert dish.price == 20

