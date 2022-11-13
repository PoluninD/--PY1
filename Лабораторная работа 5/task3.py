from random import randint

def get_unique_list_numbers() -> list[int]:
    val_list = []
    for i in range(15):
        rand_value = randint(-10,10)
        if rand_value not in val_list:
            val_list.append((rand_value))
    return val_list


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
