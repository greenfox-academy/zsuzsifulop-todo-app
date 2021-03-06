import sys

def what_to_do():
    print("Tell me what shoud I do \n a - add a new element \n l - print me the elements \n r - read the elements \n c - check if an elements is ready")

def controller():
    if sys.argv[-1] == "to_do.py":
        what_to_do()
    elif sys.argv[-1] == "-l":
        print_out()
    elif sys.argv[-2] == "-a":
        add_line(sys.argv[-1])
    elif sys.argv[-2] == "-r":
        remove_line(int(sys.argv[-1]))
    elif sys.argv[-2] == "-c":
        check_complete(int(sys.argv[-1]))
    else:
        print("unsupport argument")
        what_to_do()


def list_the_items():
    file = open("to_do_list.txt", 'r')
    text = file.readlines()
    file.close()
    todos = []    
    for line in text:
        dictionary = {}
        if line[0] == "0": 
            dictionary["complete"] = False
        if line[0] == "1":
            dictionary["complete"] = True
        things = line[2:]
        dictionary["task"] = things
        todos.append(dictionary)
    return todos


def add_line(todos_text):
    todos = list_the_items()
    if todos != []:
        todos[-1]['task'] = todos[-1]['task'][0:] + "\n"
    todo_dict = {"complete" : False, "task": todos_text}
    todos.append(todo_dict)
    write_out_file(todos)


def write_out_file(todos):
    text_to_file = ""
    for elements in todos:
        if elements["complete"]:
            text_to_file += '1 '
        else:
            text_to_file += '0 ' 
        text_to_file += elements['task'] 
    text_to_write = open('to_do_list.txt', 'w')
    text_to_write.write(text_to_file)
    text_to_write.close()


def print_out():
    todos = list_the_items()
    print_text = ""
    if todos == []:
        print("No todos for today :(")
    else:
        i = 1
        for element in todos:
            print_text += str(i) + " - "
            if element["complete"]:
                print_text += '[x] '
            else:
                print_text += '[ ] '
            print_text += element['task']
            i += 1
        print(print_text)


def check_complete(number_of_item):
    todos = list_the_items()
    todos[number_of_item-1]['complete'] = True
    write_out_file(todos)


def remove_line(number_of_items):
    todos = list_the_items()
    if number_of_items == 20:
        print("unable to remove: no index provided")
    elif number_of_items == 20:
        for elements in todos:
            del elements
        write_out_file(todos)
    elif number_of_items == str(number_of_items):
        print("unable to remove: index is not a bound")
    else:
        del todos[number_of_items-1]
        write_out_file(todos)


controller()