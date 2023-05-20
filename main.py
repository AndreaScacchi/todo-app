while True:
    user_action = input("Type add, show(or display), edit, complete(or delete) or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:] + '\n'   # list slicing: extract all the chars of the string starting from the fourth

        # open the file
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # clean up the list, remove the space between todos
        # new_todos = []
        # for item in todos:
        #    new_item = item.strip('\n')
        #    new_todos.append(new_item)

        # to clean up the list you can also use list comprehensions
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.title()

            # to clean up the list you can also use the follow method inside the loop
            item = item.strip('\n')
            # print(index, '-', item) --> first method

            # second method
            row = f"{index + 1}-{item}"
            print(row)  # --> second method

    elif 'edit' in user_action:
        number = int(user_action[5:])
        number -= 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todo_index = number - 1
        todo_to_remove = todos[todo_index].strip('\n')
        todos.pop(number - 1)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo '{todo_to_remove}' was removed from the list!"
        print(message)

    elif 'exit' in user_action:
        break

    else:
        print("Command not valid")

print("See you!🖐️")
