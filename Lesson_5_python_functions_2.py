# 2. The Shopping List Maker

# Objective: The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list, make sure you ask the user what they would like to add (reminder: ensure the function has a parameter to receive the list). 


def main ():
    my_list = []
    print("Let's add items to your list.")
    updated_list = add_to_list(my_list)
    print("Final list: ", updated_list)


def add_to_list (existing_list):
    while True:
        item = input("Enter the item you'd like to add to the list. Enter 'done' when finished. Item: ")
        if item == 'done':
            break
        existing_list.append(item)
        print(f"{item} has been added to the list.")
    return existing_list


if __name__ == "__main__":
    main()





# Task 2: Include a feature to remove items from the list. 

def remove_from_list(existing_list):
    while True:
        item = input("Enter the item you'd like to remove from the list. Enter 'done' when finished. Item: ")
        if item == 'done':
            break
        if item in existing_list:
            existing_list.remove(item)
            print(f"{item} has been removed from the list.")
        else:
            print(f"{item} is not in the list.")
    return existing_list

# Task 3: Add a function that prints out the entire list.

def print_list(existing_list):
    print("Current list:")
    for item in existing_list:
        print(f"- {item}")



