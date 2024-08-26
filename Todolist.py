class Task:
    def init(self, description):
        self.description = description
        self.completed = False

    def str(self):
        status = "Right" if self.completed else "False"
        return f"[{status}] {self.description}"

class ToDoList:
    def init(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Added task: {description}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return

        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def update_task(self, task_number, new_description=None, mark_complete=False):
        if 0 < task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            if new_description:
                task.description = new_description
                print(f"Updated task {task_number} description to: {new_description}")
            if mark_complete:
                task.completed = True
                print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Deleted task: {removed_task.description}")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            task_number = int(input("Enter task number to update: "))
            update_choice = input("Do you want to update the description (d) or mark as complete (c)? ").lower()
            if update_choice == 'd':
                new_description = input("Enter new description: ")
                todo_list.update_task(task_number, new_description=new_description)
            elif update_choice == 'c':
                todo_list.update_task(task_number, mark_complete=True)
        elif choice == '4':
            todo_list.view_tasks()
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
