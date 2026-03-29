import tkinter as Ui
from tkinter import messagebox, filedialog
parent = Ui.Tk()
parent.title("Mini Project: GUI Manager")
parent.geometry("600x400")
operation = Ui.Label(parent, text="Welcome! Select an option from the Menu.", font=("Arial",
12))
operation.pack(pady=50)
def info():
    messagebox.showinfo("Information", "This is a standard Information Box.")
def error():
    messagebox.showerror("Error", "An unexpected error occurred!")
def warning():
    messagebox.showwarning("Warning", "This is a warning message.")
def feedback():
    response = messagebox.askyesno("Feedback", "Do you like this program?")
    if response: # True
        operation.config(text="Status: User loves the program!", fg="green")
    else: # False
        operation.config(text="Status: User gave negative feedback.", fg="red")
def open_file_dialog():
    file_path = filedialog.askopenfilename()
    if file_path:
        operation.config(text=f"Selected: {file_path.split('/')[-1]}")
    else:
        operation.config(text="No file selected.")
def open_list_window():
    top = Ui.Toplevel(parent)
    top.title("Language Selector")
    top.geometry("200x150")
    Ui.Label(top, text="Select a Programming Language:", pady=10).pack()
    scrollbar = Ui.Scrollbar(top)
    scrollbar.pack(side=Ui.RIGHT, fill=Ui.Y)
    listbox = Ui.Listbox(top, yscrollcommand=scrollbar.set, selectmode=Ui.SINGLE)
    languages = ["Python", "JavaScript", "C++", "Java", "Ruby", "Go", "Swift", "Kotlin", "Rust","PHP"]
    for lang in languages:
        listbox.insert(Ui.END, lang)
    listbox.pack(side=Ui.LEFT, fill=Ui.BOTH, expand=True)
    scrollbar.config(command=listbox.yview)
mainMenu = Ui.Menu(parent)
fileMenu = Ui.Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open File", command=open_file_dialog)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=parent.destroy)
showMenu = Ui.Menu(mainMenu)
mainMenu.add_cascade(label="Show", menu=showMenu)
showMenu.add_command(label="Info Box", command=info)
showMenu.add_command(label="Error Box", command=error)
showMenu.add_command(label="Warning Box", command=warning)
showMenu.add_separator()
showMenu.add_command(label="Feedback Survey", command=feedback)
extraMenu = Ui.Menu(mainMenu)
mainMenu.add_cascade(label="Extra", menu=extraMenu)
extraMenu.add_command(label="Open Language List", command=open_list_window)
extraMenu.add_command(label="Do Nothing", command=lambda: print("Doing nothing..."))
parent.config(menu=mainMenu)
parent.mainloop()

