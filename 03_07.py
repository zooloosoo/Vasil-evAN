import random


def max_item(sorted_list):
    final_list = [max(sorted_list), sorted_list.index(max(sorted_list))]
    return final_list


test_list = [random.randint(0, 100) for f in range(10)]
print(test_list)
print(max_item(test_list))
