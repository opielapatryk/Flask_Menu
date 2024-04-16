def dish_patch_use_case(repo, updated_dish, id:int):
    return repo.patch(updated_dish, id)