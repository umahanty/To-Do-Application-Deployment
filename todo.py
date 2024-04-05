# todo.py


class TodoList:
    def __init__(self):
        self.tasks = []

    def create_task(self, task):
        self.tasks.append(task)

    def read_tasks(self):
        return self.tasks

    def update_task(self, task_index, new_task):
        self.tasks[task_index] = new_task

    def delete_task(self, task_index):
        del self.tasks[task_index]


def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. Update Task")
        print("3. Remove Task")
        print("4. Display Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.create_task(task)
            print("Task added successfully.")

        elif choice == "2":
            tasks = todo_list.read_tasks()
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            task_index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_index, new_task)
            print("Task updated successfully.")

        elif choice == "3":
            tasks = todo_list.read_tasks()
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task}")
            task_index = int(input("Enter the task number to remove: ")) - 1
            todo_list.delete_task(task_index)
            print("Task removed successfully.")

        elif choice == "4":
            tasks = todo_list.read_tasks()
            if tasks:
                print("Tasks:")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task}")
            else:
                print("No tasks in the list.")

        elif choice == "5":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()

