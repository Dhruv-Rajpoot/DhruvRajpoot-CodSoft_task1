import tkinter as tk
from tkinter import messagebox

class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.status = 'incomplete'

    def update_description(self, new_description):
        self.description = new_description

    def mark_as_complete(self):
        self.status = 'completed'

    def __str__(self):
        return f"{self.task_id}. {self.description} - {self.status}"

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, description):
        task = Task(self.next_id, description)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def view_tasks(self):
        return self.tasks

    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.mark_as_complete()
                return task
        return None

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return task
        return None

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.todo_list = ToDoList()

        self.create_widgets()

    def create_widgets(self):
        # Create and place widgets
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.complete_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
        self.complete_button.grid(row=2, column=1, padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, padx=10, pady=10)

    def add_task(self):
        description = self.task_entry.get()
        if description:
            task = self.todo_list.add_task(description)
            messagebox.showinfo("Task Added", f"Task added: {task}")
            self.refresh_list()
        else:
            messagebox.showwarning("Input Error", "Please enter a task description.")

    def update_task(self):
        selected_task = self.get_selected_task()
        if selected_task:
            new_description = self.task_entry.get()
            if new_description:
                task = self.todo_list.update_task(selected_task.task_id, new_description)
                messagebox.showinfo("Task Updated", f"Task updated: {task}")
                self.refresh_list()
            else:
                messagebox.showwarning("Input Error", "Please enter a new task description.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to update.")

    def complete_task(self):
        selected_task = self.get_selected_task()
        if selected_task:
            task = self.todo_list.complete_task(selected_task.task_id)
            messagebox.showinfo("Task Completed", f"Task completed: {task}")
            self.refresh_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to complete.")

    def delete_task(self):
        selected_task = self.get_selected_task()
        if selected_task:
            task = self.todo_list.delete_task(selected_task.task_id)
            messagebox.showinfo("Task Deleted", f"Task deleted: {task}")
            self.refresh_list()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def refresh_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.view_tasks():
            self.task_listbox.insert(tk.END, task)

    def get_selected_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            selected_task = self.todo_list.view_tasks()[selected_index]
            return selected_task
        except IndexError:
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
