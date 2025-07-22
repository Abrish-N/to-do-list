import tkinter 
from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
# import keyboard

root = Tk()
root.title("To-Do List")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list = []

def deletetask():
    global task_list
    task =str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("savefile.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)


def addtask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("savefile.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)




def openTaskFile():

    try:
        global task_list
        with open("savefile.txt",'r') as taskfile:
            tasks  =  taskfile.readlines()

        for task in tasks:
            if task != "\n":
                task_list.append(task)
                listbox.insert(END, task)
    
    except:
        file = open('savefile.txt', "w")
        file.close()
#Image_icon = PhotoImage(file="icon.png")
#root.iconphoto(False, Image_icon)


image = Image.open("topbar.png")
photo = ImageTk.PhotoImage(image)
resized_image= image.resize((435,175), Image.Resampling.LANCZOS)
new_image= ImageTk.PhotoImage(resized_image)
#Topimage = PhotoImage(file="topbar.png")
Label(root,image=new_image).place(x=-17.5,y=-70)


heading = Label(root,text="ALL TASKS",font="arial 20 bold",bg="#FFB2B2", fg="white")
heading.place(x=123,y=20)


frame = Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=130)

dashed = Image.open("dashed.png")
dashedphoto = ImageTk.PhotoImage(dashed)
resdashed= dashed.resize((305,20), Image.Resampling.LANCZOS)
newdashed= ImageTk.PhotoImage(resdashed)
Label(frame,image=newdashed,bg="white").place(x=40,y=35)

searchimage = Image.open("search.png")
searchphoto = ImageTk.PhotoImage(searchimage)
ressearch= searchimage.resize((30,30), Image.Resampling.LANCZOS)
new_search= ImageTk.PhotoImage(ressearch)
Label(frame,image=new_search,bg="white").place(x=10,y=7)

task = StringVar()
task_entry = Entry(frame, width=16, font = "arial 18",bd=0,bg="white",fg="black")
task_entry.place(x=50,y=12)
task_entry.focus()

button = Button(frame, text="ADD", font="arial 15 bold",width=6, bg="#5a95ff",fg="white",bd=0, command=addtask)
button.place(x=310,y=7.5)
# key.bind('<Return>', lambda event: addtask())
# keyboard.add_hotkey('Space', addtask())


frame1 = Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(200,0))

listbox = Listbox(frame1,font=("arial",12),width=40, height=16, bg="#32405b",fg="white",cursor="hand2",selectbackground="#FF9999")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()

delete = Image.open("delete.png")
delphoto = ImageTk.PhotoImage(delete)
resdelete= delete.resize((60,60), Image.Resampling.LANCZOS)
newdelete= ImageTk.PhotoImage(resdelete)
Button(root, image=newdelete,bd=0, command=deletetask).pack(side=BOTTOM,pady=13)

root.mainloop()