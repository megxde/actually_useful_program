import os
import subprocess
import webbrowser
import tkinter as tk
import json
import time

os.chdir("C:\\Users\\batub\\OneDrive\\Masaüstü\\misc\\shortcuts")
webbrowser.register('chrome', None,	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

changing_mode = False
button_to_change = None
command_to_execute = None
cause_of_error = None

main_window = tk.Tk()

main_window.wm_geometry("500x600")
main_window.title("Shortcuts App")
main_window.configure(bg="purple")
main_window.propagate(False)



bg_fg_var = {"bg": 'purple', "fg": 'white'}

first_number = 1
second_number = 1



def error_button_pressed():
    error_window.withdraw()



def launch_error_window():
    global command_to_execute
    global cause_of_error
    error_window.title(f"Error: {command_to_execute}")
    error_label = tk.Label(error_window, text=cause_of_error, bg="purple", fg="white", wraplengt=200, borderwidth=2, relief="raised")
    error_label.pack()
    error_label.place(x=0, y=0, height=200, width=300)

    error_window.update()
    error_window.deiconify()


error_window = tk.Tk()
error_window.geometry("300x300")
error_window.configure(bg="purple")
error_window.propagate(False)


sorry_button = tk.Button(error_window, text="Alright, sorry that I broke your program.", bg="purple", fg="white", wraplengt=100, command=error_button_pressed)
sorry_button.pack()
sorry_button.place(x=100, y=200, height=100, width=100)



error_window.withdraw()



def execute_command():
    global command_to_execute
    global cause_of_error
    folder_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(folder_path, 'commands_info.json')
    with open(json_path, "r") as info:
        info_data = json.load(info)
        url = info_data[command_to_execute]["url"]
        path = info_data[command_to_execute]["path"]
        shortcut_path = info_data[command_to_execute]["shortcut_path"]

    if url != "" and path != "" and shortcut_path != "":
        cause_of_error = "The program broke. How did you manage to get everything filled up? Fix it yourself or reinstall."
        launch_error_window()
        return

    elif url == "" and path == "" and shortcut_path == "":
        cause_of_error = "You have everything empty for this. Go fill em up."
        launch_error_window()
        return
    
    elif url != "" and path != "":
        cause_of_error = "Two things are filled up at the same time. Go fix it or reinstall."
        launch_error_window()
        return

    elif url != "" and shortcut_path != "":
        cause_of_error = "Two things are filled up at the same time. Go fix it or reinstall."
        launch_error_window()
        return

    elif path != "" and shortcut_path != "":
        cause_of_error = "Two things are filled up at the same time. Go fix it or reinstall."
        launch_error_window()
        return

    if url != "":
        webbrowser.get('chrome').open_new_tab(url)
        return
    elif path != "":
        subprocess.Popen(path)
        return
    elif shortcut_path != "":
        os.startfile(shortcut_path)
        return



def change_command():
    global changing_mode
    if changing_mode == False:
        changing_mode = True
        change_button.configure(bg="green", fg="black")
    elif changing_mode == True:
        changing_mode = False
        change_button.configure(bg="purple", fg="white")    



def save_command_url_path():
    global button_to_change
    command_to_change = f"command{button_to_change[-3:]}"
    url_to_save = url_entry.get()
    path_to_save = path_entry.get()
    shortcut_path_to_save = shortcut_path_entry.get()
    url_entry.delete(0, 'end')
    path_entry.delete(0, 'end')
    shortcut_path_entry.delete(0, 'end')
    folder_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(folder_path, 'commands_info.json')
    with open(json_path, "r") as file:
        data = json.load(file)
    if url_to_save != "":
        data[command_to_change]["url"] = url_to_save
    if path_to_save != "":
        data[command_to_change]["path"] = path_to_save
    if shortcut_path_to_save != "":
        data[command_to_change]["shortcut_path"] = shortcut_path_to_save
    os.remove(json_path)
    with open(json_path, "w") as file:
        json.dump(data, file, indent=2)
    button_changing_window.withdraw()



button_changing_window = tk.Tk()
button_changing_window.wm_geometry("300x400")
button_changing_window.configure(bg="red")
main_window.propagate(False)  

url_label = tk.Label(button_changing_window, text="Url:", bg="green", fg="black")
url_label.pack()
url_label.place(x=0, y=0, width=20)

url_entry = tk.Entry(button_changing_window)
url_entry.pack()
url_entry.place(x=20, y=1)

path_label = tk.Label(button_changing_window, text="Path:", bg="green", fg="black")
path_label.pack()
path_label.place(x=0, y=20, width=25)

path_entry = tk.Entry(button_changing_window)
path_entry.pack()
path_entry.place(x=25, y=21)    

shortcut_path_label = tk.Label(button_changing_window, text="Shortcut Path:", bg="green", fg="black")
shortcut_path_label.pack()
shortcut_path_label.place(x=0, y=40, width=73)

shortcut_path_entry = tk.Entry(button_changing_window)
shortcut_path_entry.pack()
shortcut_path_entry.place(x=73, y=41)   

save_button = tk.Button(button_changing_window, text="Save", bg="green", fg="black", command=save_command_url_path)
save_button.pack()
save_button.place(x=0, y=75)

button_changing_window.withdraw()



def launch_button_change_window():
    global button_to_change
  
    button_changing_window.title(f"Changing {button_to_change}")

    button_changing_window.update()
    button_changing_window.deiconify()

    button_changing_window.mainloop()



def command1x1():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button1x1"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command1x1"
        execute_command()

def command1x2():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button1x2"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command1x2"
        execute_command()

def command1x3():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button1x3"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command1x3"
        execute_command()

def command1x4():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button1x4"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command1x4"
        execute_command()

def command1x5():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button1x5"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command1x5"
        execute_command()

def command2x1():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button2x1"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command2x1"
        execute_command()

def command2x2():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button2x2"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command2x2"
        execute_command()

def command2x3():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button2x3"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command2x3"
        execute_command()    

def command2x4():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button2x4"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command2x4"
        execute_command()    

def command2x5():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button2x5"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command2x5"
        execute_command()

def command3x1():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button3x1"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command3x1"
        execute_command()    

def command3x2():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button3x2"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command3x2"
        execute_command()    

def command3x3():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button3x3"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command3x3"
        execute_command()    

def command3x4():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button3x4"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command3x4"
        execute_command()    

def command3x5():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button3x5"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command3x5"
        execute_command()    

def command4x1():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button4x1"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command4x1"
        execute_command()    

def command4x2():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button4x2"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command4x2"
        execute_command()    

def command4x3():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button4x3"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command4x3"
        execute_command()    

def command4x4():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button4x4"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command4x4"
        execute_command()    

def command4x5():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button4x5"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command4x5"
        execute_command()    

def command5x1():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button5x1"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command5x1"
        execute_command()    

def command5x2():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button5x2"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command5x2"
        execute_command()    

def command5x3():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button5x3"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command5x3"
        execute_command()    

def command5x4():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button5x4"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command5x4"
        execute_command()    
    
def command5x5():
    global changing_mode
    global button_to_change
    global command_to_execute
    if changing_mode == True:
        button_to_change = "button5x5"
        launch_button_change_window()
    elif changing_mode == False:
        command_to_execute = "command5x5"
        execute_command()    






button1x1 = tk.Button(main_window, text="number1x1", bg="purple", fg="white", command=command1x1)
button1x1.pack()
button1x1.place(x=0, y=0, height=100, width=100)



button1x2 = tk.Button(main_window, text="number1x2", bg="purple", fg="white", command=command1x2)
button1x2.pack()
button1x2.place(x=100, y=0, height=100, width=100)



button1x3 = tk.Button(main_window, text="number1x3", bg="purple", fg="white", command=command1x3)
button1x3.pack()
button1x3.place(x=200, y=0, height=100, width=100)



button1x4 = tk.Button(main_window, text="number1x4", bg="purple", fg="white", command=command1x4)
button1x4.pack()
button1x4.place(x=300, y=0, height=100, width=100)



button1x5 = tk.Button(main_window, text="number1x5", bg="purple", fg="white", command=command1x5)
button1x5.pack()
button1x5.place(x=400, y=0, height=100, width=100)



button2x1 = tk.Button(main_window, text="number2x1", bg="purple", fg="white", command=command2x1)
button2x1.pack()
button2x1.place(x=0, y=100, height=100, width=100)



button2x2 = tk.Button(main_window, text="number2x2", bg="purple", fg="white", command=command2x2)
button2x2.pack()
button2x2.place(x=100, y=100, height=100, width=100)



button2x3 = tk.Button(main_window, text="number2x3", bg="purple", fg="white", command=command2x3)
button2x3.pack()
button2x3.place(x=200, y=100, height=100, width=100)



button2x4 = tk.Button(main_window, text="number2x4", bg="purple", fg="white", command=command2x4)
button2x4.pack()
button2x4.place(x=300, y=100, height=100, width=100)



button2x5 = tk.Button(main_window, text="number2x5", bg="purple", fg="white", command=command2x5)
button2x5.pack()
button2x5.place(x=400, y=100, height=100, width=100)



button3x1 = tk.Button(main_window, text="number3x1", bg="purple", fg="white", command=command3x1)
button3x1.pack()
button3x1.place(x=0, y=200, height=100, width=100)



button3x2 = tk.Button(main_window, text="number3x2", bg="purple", fg="white", command=command3x2)
button3x2.pack()
button3x2.place(x=100, y=200, height=100, width=100)



button3x3 = tk.Button(main_window, text="number3x3", bg="purple", fg="white", command=command3x3)
button3x3.pack()
button3x3.place(x=200, y=200, height=100, width=100)



button3x4 = tk.Button(main_window, text="number3x4", bg="purple", fg="white", command=command3x4)
button3x4.pack()
button3x4.place(x=300, y=200, height=100, width=100)



button3x5 = tk.Button(main_window, text="number3x5", bg="purple", fg="white", command=command3x5)
button3x5.pack()
button3x5.place(x=400, y=200, height=100, width=100)



button4x1 = tk.Button(main_window, text="number4x1", bg="purple", fg="white", command=command4x1)
button4x1.pack()
button4x1.place(x=0, y=300, height=100, width=100)



button4x2 = tk.Button(main_window, text="number4x2", bg="purple", fg="white", command=command4x2)
button4x2.pack()
button4x2.place(x=100, y=300, height=100, width=100)



button4x3 = tk.Button(main_window, text="number4x3", bg="purple", fg="white", command=command4x3)
button4x3.pack()
button4x3.place(x=200, y=300, height=100, width=100)



button4x4 = tk.Button(main_window, text="number4x4", bg="purple", fg="white", command=command4x4)
button4x4.pack()
button4x4.place(x=300, y=300, height=100, width=100)



button4x5 = tk.Button(main_window, text="number4x5", bg="purple", fg="white", command=command4x5)
button4x5.pack()
button4x5.place(x=400, y=300, height=100, width=100)



button5x1 = tk.Button(main_window, text="number5x1", bg="purple", fg="white", command=command5x1)
button5x1.pack()
button5x1.place(x=0, y=400, height=100, width=100)



button5x2 = tk.Button(main_window, text="number5x2", bg="purple", fg="white", command=command5x2)
button5x2.pack()
button5x2.place(x=100, y=400, height=100, width=100)



button5x3 = tk.Button(main_window, text="number5x3", bg="purple", fg="white", command=command5x3)
button5x3.pack()
button5x3.place(x=200, y=400, height=100, width=100)



button5x4 = tk.Button(main_window, text="number5x4", bg="purple", fg="white", command=command5x4)
button5x4.pack()
button5x4.place(x=300, y=400, height=100, width=100)



button5x5 = tk.Button(main_window, text="number5x5", bg="purple", fg="white", command=command5x5)
button5x5.pack()
button5x5.place(x=400, y=400, height=100, width=100)



change_button = tk.Button(main_window, text="Changing mode", bg="purple", fg="white", command=change_command)
change_button.pack()
change_button.place(x=0, y=500, height=100, width=500)



main_window.mainloop()