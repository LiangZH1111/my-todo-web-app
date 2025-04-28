def get_todo(filepath="todo.txt"):
    """ Read a text file and
    return a list of to-do list
    """
    with open(filepath, "r") as file:
        todo_list = file.readlines()
    return todo_list

def set_todo(todo_list, filepath="todo.txt"):
    """ Write a list of to-do items into a text file"""
    with open(filepath, "w") as file:
        file.writelines(todo_list)

def append_todo(new_todo, filepath="todo.txt"):
    with open(filepath, 'a') as file:
        file.write(new_todo.strip()+"\n")

if __name__ == "__main__":
    append_todo("test append1")