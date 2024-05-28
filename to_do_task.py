# import datetime

# class TaskManager:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, description, priority, due_date):
#         if not description:
#             raise ValueError("Task description cannot be empty")
#         if priority not in ['low', 'medium', 'high']:
#             raise ValueError("Priority must be 'low', 'medium', or 'high'")
#         try:
#             due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
#         except ValueError:
#             raise ValueError("Due date must be in YYYY-MM-DD format")
#         task = {"description": description, "completed": False, "priority": priority, "due_date": due_date}
#         self.tasks.append(task)

#     def remove_task(self, index):
#         if index < 0 or index >= len(self.tasks):
#             raise IndexError("Invalid task index")
#         self.tasks.pop(index)

#     def mark_task_completed(self, index):
#         if index < 0 or index >= len(self.tasks):
#             raise IndexError("Invalid task index")
#         if self.tasks[index]["completed"]:
#             raise ValueError("Task is already completed")
#         self.tasks[index]["completed"] = True

#     def list_tasks(self, filter_by=None):
#         if not self.tasks:
#             return "No tasks available."
#         result = []
#         for i, task in enumerate(self.tasks):
#             if filter_by == "completed" and not task["completed"]:
#                 continue
#             if filter_by == "not_completed" and task["completed"]:
#                 continue
#             if filter_by == "high_priority" and task["priority"] != "high":
#                 continue
#             status = "completed" if task["completed"] else "not completed"
#             result.append(f"{i}: {task['description']} [{status}] Priority: {task['priority']} Due: {task['due_date'].strftime('%Y-%m-%d')}")
#         return "\n".join(result)

#     def update_task(self, index, description=None, priority=None, due_date=None):
#         if index < 0 or index >= len(self.tasks):
#             raise IndexError("Invalid task index")
#         if description is not None:
#             self.tasks[index]['description'] = description
#         if priority is not None:
#             if priority not in ['low', 'medium', 'high']:
#                 raise ValueError("Priority must be 'low', 'medium', or 'high'")
#             self.tasks[index]['priority'] = priority
#         if due_date is not None:
#             try:
#                 due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
#             except ValueError:
#                 raise ValueError("Due date must be in YYYY-MM-DD format")
#             self.tasks[index]['due_date'] = due_date

# if __name__ == "__main__":
#     task_manager = TaskManager()
#     while True:
#         print("\nTask Manager")
#         print("1. Add Task")
#         print("2. Remove Task")
#         print("3. Mark Task as Completed")
#         print("4. List Tasks")
#         print("5. Update Task")
#         print("6. Exit")
#         choice = input("Choose an option: ")
        
#         if choice == "1":
#             description = input("Enter task description: ")
#             priority = input("Enter task priority (low, medium, high): ")
#             due_date = input("Enter due date (YYYY-MM-DD): ")
#             try:
#                 task_manager.add_task(description, priority, due_date)
#                 print("Task added successfully.")
#             except ValueError as e:
#                 print(e)

#         elif choice == "2":
#             index = int(input("Enter task index to remove: "))
#             try:
#                 task_manager.remove_task(index)
#                 print("Task removed successfully.")
#             except (IndexError, ValueError) as e:
#                 print(e)

#         elif choice == "3":
#             index = int(input("Enter task index to mark as completed: "))
#             try:
#                 task_manager.mark_task_completed(index)
#                 print("Task marked as completed.")
#             except (IndexError, ValueError) as e:
#                 print(e)

#         elif choice == "4":
#             filter_by = input("Filter tasks by (none, completed, not_completed, high_priority): ")
#             if filter_by not in ['none', 'completed', 'not_completed', 'high_priority']:
#                 print("Invalid filter option.")
#             else:
#                 tasks = task_manager.list_tasks(filter_by if filter_by != 'none' else None)
#                 print(tasks)

#         elif choice == "5":
#             index = int(input("Enter task index to update: "))
#             description = input("Enter new description (leave blank to keep current): ")
#             priority = input("Enter new priority (low, medium, high) (leave blank to keep current): ")
#             due_date = input("Enter new due date (YYYY-MM-DD) (leave blank to keep current): ")
#             try:
#                 task_manager.update_task(index, description if description else None, priority if priority else None, due_date if due_date else None)
#                 print("Task updated successfully.")
#             except (IndexError, ValueError) as e:
#                 print(e)

#         elif choice == "6":
#             break

#         else:
#             print("Invalid choice. Please try again.")

import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []

    # Method to add a new task
    def add_task(self, description, priority, due_date):
        # Check if the task description is empty
        if not description:
            raise ValueError("Task description cannot be empty")
        
        # Check if the priority is valid
        if priority not in ['low', 'medium', 'high']:
            raise ValueError("Priority must be 'low', 'medium', or 'high'")
        
        # Validate the due date format
        try:
            due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Due date must be in YYYY-MM-DD format")
        
        # Create a task dictionary and append to the tasks list
        task = {"description": description, "completed": False, "priority": priority, "due_date": due_date}
        self.tasks.append(task)

    # Method to remove a task by its index
    def remove_task(self, index):
        # Check if the index is valid
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index")
        
        # Remove the task from the list
        self.tasks.pop(index)

    # Method to mark a task as completed
    def mark_task_completed(self, index):
        # Check if the index is valid
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index")
        
        # Check if the task is already completed
        if self.tasks[index]["completed"]:
            raise ValueError("Task is already completed")
        
        # Mark the task as completed
        self.tasks[index]["completed"] = True

    # Method to list tasks with optional filtering
    def list_tasks(self, filter_by=None):
        # Check if there are no tasks
        if not self.tasks:
            return "No tasks available."
        
        result = []
        for i, task in enumerate(self.tasks):
            # Apply filters
            if filter_by == "completed" and not task["completed"]:
                continue
            if filter_by == "not_completed" and task["completed"]:
                continue
            if filter_by == "high_priority" and task["priority"] != "high":
                continue
            
            # Determine the status of the task
            status = "completed" if task["completed"] else "not completed"
            # Add task details to the result list
            result.append(f"{i}: {task['description']} [{status}] Priority: {task ['priority']} Due: {task['due_date'].strftime('%Y-%m-%d')}")
        
        return "\n".join(result)

    # Method to update task details
    def update_task(self, index, description=None, priority=None, due_date=None):
        # Check if the index is valid
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index")
        
        # Update the task description if provided
        if description is not None:
            self.tasks[index]['description'] = description
        
        # Update the task priority if provided and valid
        if priority is not None:
            if priority not in ['low', 'medium', 'high']:
                raise ValueError("Priority must be 'low', 'medium', or 'high'")
            self.tasks[index]['priority'] = priority
        
        # Update the task due date if provided and valid
        if due_date is not None:
            try:
                due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Due date must be in YYYY-MM-DD format")
            self.tasks[index]['due_date'] = due_date

if __name__ == "__main__":
    task_manager = TaskManager()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Update Task")
        print("6. Exit")
        
        # Get user choice
        choice = input("Choose an option: ")
        
        if choice == "1":
            # Add a new task
            description = input("Enter task description: ")
            priority = input("Enter task priority (low, medium, high): ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            try:
                task_manager.add_task(description, priority, due_date)
                print("Task added successfully.")
            except ValueError as e:
                print(e)

        elif choice == "2":
            # Remove a task by index
            index = int(input("Enter task index to remove: "))
            try:
                task_manager.remove_task(index)
                print("Task removed successfully.")
            except (IndexError, ValueError) as e:
                print(e)

        elif choice == "3":
            # Mark a task as completed
            index = int(input("Enter task index to mark as completed: "))
            try:
                task_manager.mark_task_completed(index)
                print("Task marked as completed.")
            except (IndexError, ValueError) as e:
                print(e)

        elif choice == "4":
            # List tasks with optional filtering
            filter_by = input("Filter tasks by (none, completed, not_completed, high_priority): ")
            if filter_by not in ['none', 'completed', 'not_completed', 'high_priority']:
                print("Invalid filter option.")
            else:
                tasks = task_manager.list_tasks(filter_by if filter_by != 'none' else None)
                print(tasks)

        elif choice == "5":
            # Update task details
            index = int(input("Enter task index to update: "))
            description = input("Enter new description (leave blank to keep current): ")
            priority = input("Enter new priority (low, medium, high) (leave blank to keep current): ")
            due_date = input("Enter new due date (YYYY-MM-DD) (leave blank to keep current): ")
            try:
                task_manager.update_task(index, description if description else None, priority if priority else None, due_date if due_date else None)
                print("Task updated successfully.")
            except (IndexError, ValueError) as e:
                print(e)

        elif choice == "6":
            # Exit the program
            break

        else:
            # Handle invalid choice
            print("Invalid choice. Please try again.")
