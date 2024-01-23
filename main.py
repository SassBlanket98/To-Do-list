from tkinter import *

# Initialize GUI
root = Tk()
root.title("Todays To-Do List")
root.geometry("300x400")
root.resizable(0, 0)
root.config(bg = "PaleVioletRed")

# Heading
Label(root, text = "To-Do List", bg = "PaleVioletRed", font = ("Helvetica"), wraplength = 300).place(x = 35, y = 0)

# Listbox and a scrollbar
tasks = Listbox(root, selectbackground = "gold", bg = "Silver", font = ("Helvetica", 12), height = 12, width = 25)

scroller = Scrollbar(root, orient = VERTICAL, command = tasks.yview)
scroller.place(x = 260, y = 50, height = 232)

tasks.config(yscrollcommand = scroller.set)

tasks.place(x = 35, y = 50)

# add item to boxlist
with open("tasks.txt", "r+") as tasks_list:
    for task in tasks_list:
        tasks.insert(END, task)
    tasks_list.close()

# Entry widget
entry = Entry(root)
entry.place(x = 45, y = 310)

# add and delete func
def add_item(entry: Entry, listbox: Listbox):
    new_task = entry.get()

    listbox.insert(END, new_task)

    with open("tasks.txt", "a") as tasks_list_file:
        tasks_list_file.write(f"\n{new_task}")

def delete_item(listbox: Listbox):
    listbox.delete(ACTIVE)

    with open("tasks.txt", "r+") as tasks_list_file:
        lines = tasks_list_file.readlines()

        tasks_list_file.truncate()

        for line in lines:
            if listbox.get(ACTIVE) == line[:-2]:
                lines.remove(line)
            tasks_list_file.write(line)
            tasks_list_file.close()

#add
add_btn = Button(root, text = "Add Item", bg = "Azure", width = 10, font = ("Helvetica", 12), command = lambda: add_item(entry, tasks))
add_btn.place(x = 45, y = 350)
# delete
delete_btn = Button(root, text = "Delete Item", bg = "Azure", width = 10, font = ("Helvetica", 12), command = lambda: delete_item(tasks))
delete_btn.place(x = 150, y = 350)

#Finalize window
root.update()
root.mainloop()
        
        


