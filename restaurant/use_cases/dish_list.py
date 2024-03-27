from restaurant.responses import ResponseSuccess

def dish_list_use_case(repo, request):
    dishes = repo.list()
    return ResponseSuccess(dishes)
