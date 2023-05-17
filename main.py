while True:
    user_action = input("Type add, show(or display), edit, complete(or delete), or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w') # to write the file todos.txt
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                item = item.title()
                # print(index, '-', item) --> first method

                # second method
                row = f"{index + 1}-{item}"
                print(row) # --> second method