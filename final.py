import tkinter
from tkinter import *
from tkinter import PhotoImage, filedialog, messagebox
from PIL import Image, ImageTk
import os
import keyboard

root = Tk()
root.title("To-Do List")
root.geometry("400x650+400+100")
root.resizable(False, False)
bglightmode = "white"
fglightmode = "white"
root["bg"] = format(bglightmode)

task_list = []

#functions

#delete function
def deletetask():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        listbox.delete(ANCHOR)
        messagebox.showinfo("Task Deleted!",f"{task} deleted successfully!")

#add task function
def addtask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        task_list.append(task)
        listbox.insert(END, task)

#complete task
def complete_task():
    global task_list
    task = str(listbox.get(ANCHOR))
    if task in task_list:
       index= task_list.index(task)
       task_list[index]=f"{task} 👍"
       listbox.insert(END, task_list[index])
       listbox.delete(ANCHOR)
       messagebox.showinfo("congratulations!",f"{task} completed successfully!")

#file path
def openTaskFile():
    global task_list
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        task_list.clear()
        listbox.delete(0, END)
        with open(file_path, 'r') as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task.strip() != "":
                task_list.append(task.strip())
                listbox.insert(END, task.strip())

        file_name = os.path.splitext(os.path.basename(file_path))[0] #file name beside heading
        root.title(f"To-Do List - {file_name}")

#saves txt file of the list
def saveTaskFile():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, 'w') as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        messagebox.showinfo("Save", "Task list saved successfully!")

#png image in header
Image_icon = PhotoImage(file="images/icon.png")
root.iconphoto(False, Image_icon)

#pink header
image = Image.open("images/topbar2.png")
photo = ImageTk.PhotoImage(image)
resized_image = image.resize((435, 200), Image.Resampling.LANCZOS)
new_image = ImageTk.PhotoImage(resized_image)
Label(root, image=new_image, bg='white').place(x=-20.5, y=-75)

heading = Label(root, text="ALL TASKS", font="arial 27 bold", bg="#FF9999", fg="white")
heading.place(x=96, y=25)

frame = Frame(root, width=400, height=290, bg="white")
frame.place(x=0, y=150)
frame.config(bd=0)

#png of text box
dashed = Image.open("images/dashed.png")
dashedphoto = ImageTk.PhotoImage(dashed)
resdashed = dashed.resize((270, 20), Image.Resampling.LANCZOS)
newdashed = ImageTk.PhotoImage(resdashed)
Label(frame, image=newdashed, bg="white").place(x=40, y=35)

#png of tick box
searchimage = Image.open("images/tickl.png")
searchphoto = ImageTk.PhotoImage(searchimage)
ressearch = searchimage.resize((30, 30), Image.Resampling.LANCZOS)
new_search = ImageTk.PhotoImage(ressearch)
Button(frame, image=new_search, command=addtask).place(x=280, y=7.5)

#text box over the line
task = StringVar()
task_entry = Entry(frame, width=16, font="arial 18", bd=0, bg="white", fg="black")
task_entry.place(x=50, y=8)
task_entry.focus()

#button = Button(frame, text="ADD", font="arial 15 bold", width=6, bg="#5a95ff", fg="white", bd=0, command=addtask)
#button.place(x=310, y=7.5)

keyboard.add_hotkey("enter",addtask)

#frame behind list box
frame1 = Frame(root, bd=3, width=700, height=360, bg="#32405b")
frame1.pack(pady=(200, 0))

#list box
listbox = Listbox(frame1, font=("arial", 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2", selectbackground="#FF9999")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

#scroll bar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#Delete box png
delete = Image.open("images/cross.png")
delphoto = ImageTk.PhotoImage(delete)
resdelete = delete.resize((30, 30), Image.Resampling.LANCZOS)
newdelete = ImageTk.PhotoImage(resdelete)
Button(frame, image=newdelete, command=deletetask).place(x=330, y=7.5)

keyboard.add_hotkey("delete",deletetask)

#save button
save_button = Button(root, text="Save list", font="arial 15 bold", width=7, bg="#FF9999", fg='white', command=saveTaskFile)
save_button.place(x=92,y=515)

keyboard.add_hotkey("ctrl+s",saveTaskFile)

#done button
done_button = Button(root, text="Done Task", font="arial 15 bold", width=9, bg="black", fg='pink', command=complete_task)
done_button.place(x=142,y=565)

#open button
open_button = Button(root, text="Open list", font="arial 15 bold", width=7, bg="#FF9999", fg='white', command=openTaskFile)
open_button.place(x=212,y=515)


root.mainloop()
