while True:
    # ask the user to type a command
    user_action = input("Type add, show(or display), edit, complete(or delete), or exit: ")
    user_action = user_action.strip()

    match user_action: # check user action

        case 'add':
            todo = input("Enter a todo: ") + "\n"

            # open the file
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # append the todos to the file todos.txt
            todos.append(todo)

            # open the file
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            # open the file
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # clean up the list, remove the space between todos
            # new_todos = []
            # for item in todos:
            #    new_item = item.strip('\n')
            #    new_todos.append(new_item)

            # to clean up the list you can also use list comprehensions
            # new_todos = [item.strip('\n') for item in todos]

            # loop through the todos list and take the index and the todo(item)
            for index, item in enumerate(todos):
                item = item.title()

                # to clean up the list you can also use the follow method inside the loop
                item = item.strip('\n')

                # print(index, '-', item) --> first method

                # second method
                row = f"{index + 1}-{item}"
                print(row) # --> second method

        case 'edit':
            # ask the user to enter the number of the todo you want to edit
            number = int(input("Number of the todo to edit: "))
            number -= 1

            # open the file
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            # ask the user to enter a new todo
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            # open the file
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete' | 'delete':
            # ask the user to enter the number of the todo you want to delete/complete
            number = int(input("Number of the todo to complete: "))
            
            # open the file
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # todo index you want to remove store inside the following variable
            todo_index = number - 1
            todo_to_remove = todos[todo_index].strip('\n')
            todos.pop(number - 1)

            # open the file
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            # alert the user that the todo is removed 
            message = f"Todo '{todo_to_remove}' was removed from the list!"
            print(message)

        case 'exit':
            break # break the loop

        case _:
            print("Hey, you enter an unknown command. Please select one action!")

print("See you!🖐️")