
import tkinter
import tkinter.messagebox
from tkinter import*
import pickle
import os

window = tkinter.Tk()

window.title("To do list")
home_dir= os.path.expanduser("~")
file_path = os.path.join(home_dir,"tasks.dat")
# Change this to the desired file path
try:
        with open(file_path,"wb") as file:
            file.write(b"Test data")
            print(f"Succesfully wrote to {file_path}")
except Exception as e:
      print(f"Error:{e}") 

def ensure_file_exists():
    if not os.path.exists("C:\\Users\\pirut\\OneDrive\\OfficeMobile\\Documents\\tasks.dat - Shortcut.lnk"):
        with open(file_path, "wb") as file:
            pickle.dump([], file)  # Initialize with an empty list

def task_adding():
    todo = task_add.get()
    if todo != "":
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)

    else:
        tkinter.messagebox.showwarning(title="Attention !!",message="To do a task,please enter task!")

def task_removing():
    try:
        index_todo = todo_box.curselection()[0]
        todo_box.delete(index_todo)
    except IndexError:
        tkinter.messagebox.showwarning(title = "Attention !!",message="To delete a task,you must select a task !!")

def task_load():
    ensure_file_exists()
    try:
        print(f"Loading from{file_path}")
        with open("file_path","rb") as file:
                  
         todo_list = pickle.load(file)
        todo_box.delete(0,tkinter.END)
        for task in todo_list:
            todo_box.insert(tkinter.END,task)
    except FileNotFoundError: 
        tkinter.messagebox.showwarning(title="Attention !!",message="Cannot find tasks.dat")
    except EOFError:
        tkinter.messagebox.showwarning(title="Attention !!",message="The file tasks.dat is empty")
    except Exception as e:
        tkinter.messagebox.showwarning(title="Attention !!",message=f"An error occured while loading: {str(e)}")    


def task_save():
    ensure_file_exists()
    try:   
        todo_list=todo_box.get(0,todo_box.size())
        with open("file_path","wb") as file:
         pickle.dump(todo_list,file)
         tkinter.messagebox.showinfo(title="Success",message="Task saved successfully")
    except PermissionError:
      tkinter.messagebox.showwarning(title="Permission Denied",message=f"Permission denied: Unable to save{file_path}")  
    except Exception as e:
        tkinter.messagebox.showwarning(title="Attention !!",message=f"An error occured while saving:{str(e)}")

list_frame = tkinter.Frame(window)
list_frame.pack()
todo_box = tkinter.Listbox(list_frame,height= 25,width = 55)
todo_box.pack(side=tkinter.LEFT)

scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT,fill = tkinter.Y)

todo_box.config(yscrollcommand=scroller.set)
scroller.config(command=todo_box.yview)

task_add = tkinter.Entry(window,width=60)
task_add.pack()

add_task_button = tkinter.Button(window, text="CLICK TO ADD TASK",font=("arial",15,"bold"),background="green",width=35,command = task_adding)

add_task_button.pack()

remove_task_button = tkinter.Button(window, text="CLICK TO DELETE TASK",font=("arial",15,"bold"),background="blue",width=35,command=task_removing)
remove_task_button.pack()

load_task_button = tkinter.Button(window,text ="CLICK TO LOAD TASK",font=("arial",15,"bold"),background="green",width=35,command=task_load)
load_task_button.pack()

save_task_button = tkinter.Button(window,text="CLICK TO SAVE TASK",font=("arial",15,"bold"),background="blue",width=35,command=task_save)
save_task_button.pack()

window.mainloop()



