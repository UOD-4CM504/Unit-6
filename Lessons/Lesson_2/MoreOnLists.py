def change_list(my_list):
    my_list = my_list.copy()
    my_list.pop(1)
    my_list.append("Banana")
    my_list.sort()
    return my_list


if __name__ == "__main__":
    fruit_list = ["Pear", "Orange", "Peach", "Apple"]
    print(fruit_list)  # prints ["Pear", "Orange", "Peach", "Apple"]
    new_fruit_list = change_list(fruit_list)
    print(fruit_list)  # prints ["Pear", "Orange", "Peach", "Apple"]
    print(new_fruit_list)  # prints ["Apple", "Banana", "Peach", "Pear"]
