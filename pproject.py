import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Function to delete a selected task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)

# Create a frame to hold the list and entry box
frame = tk.Frame(root)
frame.pack(pady=20)

# Listbox to display tasks
task_listbox = tk.Listbox(frame, width=30, height=10)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Entry box to enter a task
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Add and delete buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Run the application
root.mainloop()
