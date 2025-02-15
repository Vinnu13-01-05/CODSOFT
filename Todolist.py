class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added!")

    def view_tasks(self):
        print("\nYour Tasks:")
        print("-" * 20)
        if not self.tasks:
            print("No tasks yet. Add one!")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
        print("-" * 20)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Task '{removed_task}' deleted!")
        else:
            print("Invalid task number.")

def main():
    todo = ToDoList()
    options = ["1", "2", "3", "4"]
    predefined_inputs = ["1", "Buy groceries", "2", "1", "3", "1", "2", "4"]
    input_index = 0
    
    while input_index < len(predefined_inputs):
        choice = predefined_inputs[input_index]
        print(f"\nSimple To-Do List\nChoice: {choice}")
        input_index += 1
        
        if choice == "1":
            task = predefined_inputs[input_index]
            print(f"Enter a task: {task}")
            todo.add_task(task)
            input_index += 1
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.view_tasks()
            try:
                index = int(predefined_inputs[input_index]) - 1
                print(f"Enter task number to delete: {index + 1}")
                todo.delete_task(index)
                input_index += 1
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye! Keep up with your tasks!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
