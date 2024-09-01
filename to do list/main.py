from tkinter import *
import sqlite3

def connect():
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            task TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert(task):
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()
    view()

def view():
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    conn.close()
    listbox.delete(0, END)
    for row in rows:
        listbox.insert(END, row)

def delete():
    selected_task = listbox.get(ACTIVE)
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id=?", (selected_task[0],))
    conn.commit()
    conn.close()
    view()

def update():
    selected_task = listbox.get(ACTIVE)
    conn = sqlite3.connect("todo.db")
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET task=? WHERE id=?", (task_entry.get(), selected_task[0]))
    conn.commit()
    conn.close()
    view()

# GUI Setup
connect()
app = Tk()
app.title("Simple To-Do List")

frame = Frame(app)
frame.pack(pady=10)

task_entry = Entry(frame, width=30)
task_entry.grid(row=0, column=0, padx=10)

add_button = Button(frame, text="Add Task", command=lambda: insert(task_entry.get()))
add_button.grid(row=0, column=1)

listbox = Listbox(app, height=10, width=50)
listbox.pack(pady=10)

delete_button = Button(app, text="Delete Task", command=delete)
delete_button.pack(pady=5)

update_button = Button(app, text="Update Task", command=update)
update_button.pack(pady=5)

view()

app.mainloop()