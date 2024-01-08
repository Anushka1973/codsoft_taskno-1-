import tkinter
from tkinter import *

root=Tk()
root.title("TO-DO-LIST")
root.geometry("400x650+400+100")
root.resizable(False,False)

task_list= []

def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        
        listbox.delete(ANCHOR)

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt",'r') as taskfile:
            tasks=taskfile.readlines()
        
        for task in tasks:
            if task!='\n':
                task_list.append(task)
                listbox.insert(END, task)
    
    except:
        file=open("tasklist.txt",'r')
        file.close

def updateTask():
    selected_index = listbox.curselection()
    if selected_index:
        updated_task = task_entry.get()
        if updated_task:
            task_list[selected_index[0]] = updated_task
            with open("tasklist.txt", 'w') as taskfile:
                for task in task_list:
                    taskfile.write(task + "\n")
            listbox.delete(selected_index)
            listbox.insert(selected_index, updated_task)
            task_entry.delete(0, END)
            

#icon
Image_icon=PhotoImage(file="task.png")
root.iconphoto(False,Image_icon)

#top bar
Top=PhotoImage(file="topbar.png")
Label(root,image=Top).pack()

dock=PhotoImage(file="dock.png")
Label(root,image=dock,bg="#32405b").place(x=30,y=25)

noteimage=PhotoImage(file="task.png")
Label(root,image=noteimage,bg="#32405b").place(x=30,y=25)


heading=Label(root,text="ALL TASK",font="arial 20 bold",fg="white",bg="#32405b").place(x=130,y=20)

#main
frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)

task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

#buttons(delete and update)
update_icon=PhotoImage(file="update.png")
Button(root,image=update_icon,bd=0,command=updateTask).pack(side=RIGHT,pady=13)

button=Button(frame,text="ADD",font=" Arial 20",width=4,bg="#5a95ff",fg="#fff",bd=2,command=addTask)
button.place(x=330,y=0)

# update_button = Button(frame, text="UPDATE", font="Arial 20", width=6, bg="#ffaa00", fg="#fff", bd=2, command=updateTask)
# update_button.place(x=230, y=0)


#listbox
frame1=Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160,0))

listbox=Listbox(frame1,font=("arial",12),width=40,height=16,bg="#32405b",fg="white",cursor="hand2",selectbackground="#5a95ff")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()
#delete
Delete_icon=PhotoImage(file="delete.png")
Button(root,image=Delete_icon,bd=0,command=deleteTask).pack(side=BOTTOM,pady=13)

root.mainloop()
