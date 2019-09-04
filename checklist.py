import sys
checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    return checklist[int(index)]

def update(item, index):
    checklist[int(index)] = item

def is_valid_index(index):
    if index.isdigit():
        if 0 <= int(index) < len(checklist):
            return True
        else:
            return False
    else:
        return False

def remove(index):
    checklist.pop(int(index))

def list_all_items():
    for item in checklist:
        print("  "+item)

def mark_completed(index):
    if checklist[index].startswith("√"):
        update(checklist[index][2:], index)
    else:
        update("√ " + checklist[index], index)

def find_index(item):
    try:
        checklist.index(item)
    except:
        print("There is no \"" + item + "\" in the checklist.")

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def help():
    print(" ~~ Checklist Menu ~~ ")
    print("C to add to list; P to display list; M to mark/unmark item;")
    print("R to Read from list; U to update item;")
    print("D to delete item; F to find the index of an item;")
    print("Help or H to see this menu again; X to exit")
    print()

def select(fxn_code):
    if fxn_code == "C":
        input_item = user_input("Add new list item: ")
        create(input_item)
    elif fxn_code == "R":
        input_index = user_input("Read item at this index: ")
        while not is_valid_index(input_index):
            input_index = user_input("Invalid index, try again: ")
        print("  "+read(input_index))
    elif fxn_code == "P":
        list_all_items()
    elif fxn_code == "M":
        input_index = user_input("Mark/Unmark this index as completed: ")
        while not is_valid_index(input_index):
            input_index = user_input("Invalid index, try again: ")
        mark_completed(int(input_index))
    elif fxn_code == "U":
        input_index = user_input("Update item at this index: ")
        while not is_valid_index(input_index):
            input_index = user_input("Invalid index, try again: ")
        input_item = user_input("Updated item for index " + input_index + ": ")
        update(input_item, input_index)
    elif fxn_code == "D":
            input_index = user_input("Remove item at this index: ")
            while not is_valid_index(input_index):
                input_index = user_input("Invalid index, try again: ")
            remove(input_index)
    elif fxn_code == "F":
        help()
    elif fxn_code == "HELP" or fxn_code == "H":
        help()
    elif fxn_code == "X":
        sys.exit()
    else:
        print("Unknown Option")

def test():
    help()
    select("C")
    select("C")
    select("P")
    select("R")
    select("U")
    select("P")
    select("D")
    select("P")
    select("M")
    select("P")
    select("M")
    select("P")
    print("test finished")
    print()

test()
running = True
help()
while running:
    selection = user_input("--> ")
    select(selection.upper())
    print("Choose another option:")
