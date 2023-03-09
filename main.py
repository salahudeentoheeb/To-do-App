import functions as f
import time

today = time.strftime("%b %d, %Y %H:%M:%S")
print("Today is: ",today)
while True:
    user_text = input("Type add, show, edit, complete or exit: ")
    user_text = user_text.strip()

    if user_text.startswith("add"):
        todo = user_text[4:]

        todos = f.read_todos()

        todos.append(todo.title() + '\n')

        f.write_todos(todos)

    elif user_text.startswith("show"):
        todos = f.read_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")
    elif user_text.startswith("edit"):
        try:
            number = int(user_text[5:])
            number = number - 1
            todos = f.read_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo.title() + '\n'

            f.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_text.startswith("complete"):
        try:
            number = int(user_text[9:])

            todos = f.read_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            f.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
        except ValueError:
            print("Please enter a number")
            continue

    elif user_text.startswith("exit"):
        break
    else:
        print("Command is not valid")

print("Bye")
print('This is very nice')
