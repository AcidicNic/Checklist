checklist = list()

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

def update(item, index):
    checklist[index] = item

def is_valid_index(index):
    if index.isdigit():
        if 0 <= int(index) < len(checklist):
            return True
        else:
            return False
    else:
        return False

def remove(index):
    checklist.pop(index)

def list_all_items():
    for item in checklist:
        print("  "+item)

def mark_completed(index):
    update("√ " + checklist[index], index)

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def help():
    print(" ~~ Checklist Menu ~~ ")
    print("C to add to list; R to Read from list; P to display list;")
    print("M to mark completed; U to update item; D to delete item;")
    print("Help or H to see this menu again")

def select(fxn_code):
    if fxn_code == "C":
        input_item = user_input("New Item: ")
        create(input_item)
    elif fxn_code == "R":
        input_index = user_input("Index Number: ")
        while not is_valid_index(input_index):
            input_index = user_input("Index Number: ")
        read(input_index)
    elif fxn_code == "P":
        list_all_items()
    elif fxn_code == "M":
        input_index = user_input("Index Number: ")
        while not is_valid_index(input_index):
            input_index = user_input("Index Number: ")
        mark_completed(int(input_index))
    elif fxn_code == "U":
        input_index = user_input("Index Number: ")
        while not is_valid_index(input_index):
            input_index = user_input("Index Number: ")
        input_item = user_input("New Item: ")
        update(input_item, input_index)

    elif fxn_code == "D":
            input_index = user_input("Index Number: ")
            while not is_valid_index(input_index):
                input_index = user_input("Index Number: ")
            remove(input_index)
    elif fxn_code == "HELP" or fxn_code == "H":
        help()
    else:
        print("Unknown Option")

def test():
    select("C")
    list_all_items()
    select("R")
    list_all_items()

running = True
help()
while running:
    selection = user_input("--> ")
    select(selection.upper())
    print("Choose another option:")
