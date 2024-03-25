from restaurant.domain.dish import Dish

def test_dish_model_init():
    dish = Dish(
        position=1,
        name='pierogi',
        description='My favorite Polish dish',
        price=20,
    )

    assert dish.position == 1
    assert dish.name == 'pierogi'
    assert dish.description == 'My favorite Polish dish'
    assert dish.price == 20

