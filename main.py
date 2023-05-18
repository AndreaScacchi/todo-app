while True:
    user_action = input("Type add, show(or display), edit, complete(or delete), or exit: ")
    user_action = user_action.strip()

    match user_action: # check user action

        case 'add':
            todo = input("Enter a todo: ") + "\n"

            # open the file
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            # open the file
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
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
                print(row) # --> second method

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number -= 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case 'complete' | 'delete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)

        case 'exit':
            break

        case _:
            print("Hey, you enter an unknown command. Please select one action!")

print("See you!🖐️")