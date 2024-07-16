import tkinter as tk

# Цвета для интерфейса
background_color = "gray90"
input_background = "white"
button_color = "SteelBlue1"
listbox_color = "LightCyan2"
text_color = "black"

def add_task():
    task = entry.get()
    if task:
        task_list_box.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task_index = task_list_box.curselection()
    if selected_task_index:
        task = task_list_box.get(selected_task_index)
        task_list_box.delete(selected_task_index)
        # Удаление задачи из всех списков
        for list_box in [completed_task_list_box, marked_task_list_box]:
            try:
                index = list_box.get(0, tk.END).index(task)
                list_box.delete(index)
            except ValueError:
                pass

def mark_task():
    selected_task_index = task_list_box.curselection()
    if selected_task_index:
        task = task_list_box.get(selected_task_index)
        marked_task_list_box.insert(tk.END, task)
        task_list_box.itemconfig(selected_task_index, bg="darkorchid3")

def complete_task():
    selected_task_index = task_list_box.curselection()
    if selected_task_index:
        task = task_list_box.get(selected_task_index)
        completed_task_list_box.insert(tk.END, task)
        task_list_box.delete(selected_task_index)

root = tk.Tk()
root.title("Список задач")
root.configure(bg=background_color)

text1 = tk.Label(root, text="Введите Вашу задачу", bg=button_color, fg=text_color)
text1.pack(pady=25)

# Увеличенная ширина Entry
entry = tk.Entry(root, width=88, bg=input_background, fg=text_color)
entry.pack(padx=100, pady=10)

buttons_frame = tk.Frame(root, bg=background_color)
buttons_frame.pack(pady=10)

add_task_button = tk.Button(buttons_frame, text="Добавить задачу", command=add_task, bg=button_color, fg=text_color)
add_task_button.pack(side=tk.LEFT, padx=5)

delete_task_button = tk.Button(buttons_frame, text="Удалить задачу", command=delete_task, bg=button_color, fg=text_color)
delete_task_button.pack(side=tk.LEFT, padx=5)

mark_task_button = tk.Button(buttons_frame, text="Отметить задачу", command=mark_task, bg=button_color, fg=text_color)
mark_task_button.pack(side=tk.LEFT, padx=5)

complete_task_button = tk.Button(buttons_frame, text="Выполненные задачи", command=complete_task, bg=button_color, fg=text_color)
complete_task_button.pack(side=tk.LEFT, padx=5)

frame = tk.Frame(root, bg=background_color)
frame.pack()

text2 = tk.Label(frame, text="Список задач", bg=button_color, fg=text_color)
text2.pack(side=tk.LEFT, padx=10)

# Увеличенные размеры Listbox'ов
task_list_box = tk.Listbox(frame, height=25, width=50, bg=listbox_color, fg=text_color)
task_list_box.pack(side=tk.LEFT, padx=10)

completed_tasks_label = tk.Label(frame, text="Выполненные задачи", bg=button_color, fg=text_color)
completed_tasks_label.pack(side=tk.LEFT, padx=10)

completed_task_list_box = tk.Listbox(frame, height=25, width=50, bg=listbox_color, fg=text_color)
completed_task_list_box.pack(side=tk.LEFT, padx=10)

marked_tasks_label = tk.Label(frame, text="Отмеченные задачи", bg=button_color, fg=text_color)
marked_tasks_label.pack(side=tk.LEFT, padx=10)

marked_task_list_box = tk.Listbox(frame, height=25, width=50, bg=listbox_color, fg=text_color)
marked_task_list_box.pack(side=tk.LEFT, padx=10)

root.mainloop()