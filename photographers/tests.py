my_list = [{'id': 11}, {'id': 12}, {'id': 13}, {'id': 14}, {'id': 15}]

print(my_list)

while my_list[0]["id"] != 13:
    test = my_list[0]
    my_list.append(test)
    del my_list[0]

print(my_list)