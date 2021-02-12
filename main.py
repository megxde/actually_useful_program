import os
import subprocess
import webbrowser
import tkinter as tk
import json
import time
from PIL import Image, ImageTk

os.chdir("C:\\Users\\batub\\OneDrive\\Masaüstü\\misc\\shortcuts")
webbrowser.register('chrome', None,	webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

changing_mode = False
button_to_change = None
command_to_execute = None
cause_of_error = None
button_to_check = None

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
    error_label.place(x=0, y=0, height=200, width=300)

    error_window.update()
    error_window.deiconify()


error_window = tk.Tk()
error_window.geometry("300x300")
error_window.configure(bg="purple")
error_window.propagate(False)


sorry_button = tk.Button(error_window, text="Alright, sorry that I broke your program.", bg="purple", fg="white", wraplengt=100, command=error_button_pressed)
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
    image_name_to_save = image_name_entry.get()
    url_entry.delete(0, 'end')
    path_entry.delete(0, 'end')
    shortcut_path_entry.delete(0, 'end')
    image_name_entry.delete(0, 'end')
    folder_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(folder_path, 'commands_info.json')
    image_json_path = os.path.join(folder_path, 'image_data.json')
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
    if image_name_to_save != "":
        with open(image_json_path, "r") as file:
            image_data = json.load(file)
        image_to_change = f"button{button_to_change[-3:]}_image"
        image_data[image_to_change] = image_name_to_save
        os.remove(image_json_path)
        with open(image_json_path, "w") as file:
            json.dump(image_data, file, indent=2)
    button_changing_window.withdraw()



button_changing_window = tk.Tk()
button_changing_window.wm_geometry("300x400")
button_changing_window.configure(bg="red")
main_window.propagate(False)  

url_label = tk.Label(button_changing_window, text="Url:", bg="green", fg="black")
url_label.place(x=0, y=0, width=20)

url_entry = tk.Entry(button_changing_window)
url_entry.place(x=20, y=1)

path_label = tk.Label(button_changing_window, text="Path:", bg="green", fg="black")
path_label.place(x=0, y=20, width=25)

path_entry = tk.Entry(button_changing_window)
path_entry.place(x=25, y=21)    

shortcut_path_label = tk.Label(button_changing_window, text="Shortcut Path:", bg="green", fg="black")
shortcut_path_label.place(x=0, y=40, width=73)

shortcut_path_entry = tk.Entry(button_changing_window)
shortcut_path_entry.place(x=73, y=41)   

image_warning_label = tk.Label(button_changing_window, text="The image has to be in the 'images' folder.", bg="green", fg="black")
image_warning_label.place(x=0, y=60)

image_name_label = tk.Label(button_changing_window, text="Image name:", bg="green", fg="black")
image_name_label.place(x=0, y=80, width=71)

image_name_entry = tk.Entry(button_changing_window)
image_name_entry.place(x=71, y=81)

save_button = tk.Button(button_changing_window, text="Save", bg="green", fg="black", command=save_command_url_path)
save_button.place(x=0, y=120)

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



with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image_data.json'), "r") as image_json:
    image_data = json.load(image_json)

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'placing_data.json'), "r") as placing_json:
    placing_data = json.load(placing_json)

image_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')

list_index = 0

from all_lists import buttons, image_list

for button in buttons:
    img_value = image_data[f"{button}_image"]
    if img_value != "":
        image_path = os.path.join(image_folder_path, img_value)
        button_image = ImageTk.PhotoImage(Image.open(image_path). resize((100, 100), Image.ANTIALIAS))
        buttons[list_index] = tk.Button(main_window, image=button_image, **bg_fg_var)
    else:
        buttons[list_index] = tk.Button(main_window, text=f"number{button[-3:]}", **bg_fg_var)
    raw_placement_data = placing_data[f"{button}"]
    x, y = raw_placement_data.split(" ")
    int_x = int(x)
    int_y = int(y)
    buttons[list_index].place(x=int_x, y=int_y, height=100, width=100)  # pylint: disable=maybe-no-member
    list_index+=1
    if list_index == 25:
        buttons[0].configure(command=command1x1)    # pylint: disable=maybe-no-member
        buttons[1].configure(command=command1x2)    # pylint: disable=maybe-no-member
        buttons[2].configure(command=command1x3)    # pylint: disable=maybe-no-member
        buttons[3].configure(command=command1x4)    # pylint: disable=maybe-no-member
        buttons[4].configure(command=command1x5)    # pylint: disable=maybe-no-member
        buttons[5].configure(command=command2x1)    # pylint: disable=maybe-no-member
        buttons[6].configure(command=command2x2)    # pylint: disable=maybe-no-member
        buttons[7].configure(command=command2x3)    # pylint: disable=maybe-no-member
        buttons[8].configure(command=command2x4)    # pylint: disable=maybe-no-member
        buttons[9].configure(command=command2x5)    # pylint: disable=maybe-no-member
        buttons[10].configure(command=command3x1)   # pylint: disable=maybe-no-member
        buttons[11].configure(command=command3x2)   # pylint: disable=maybe-no-member
        buttons[12].configure(command=command3x3)   # pylint: disable=maybe-no-member
        buttons[13].configure(command=command3x4)   # pylint: disable=maybe-no-member
        buttons[14].configure(command=command3x5)   # pylint: disable=maybe-no-member
        buttons[15].configure(command=command4x1)   # pylint: disable=maybe-no-member
        buttons[16].configure(command=command4x2)   # pylint: disable=maybe-no-member
        buttons[17].configure(command=command4x3)   # pylint: disable=maybe-no-member
        buttons[18].configure(command=command4x4)   # pylint: disable=maybe-no-member
        buttons[19].configure(command=command4x5)   # pylint: disable=maybe-no-member
        buttons[20].configure(command=command5x1)   # pylint: disable=maybe-no-member
        buttons[21].configure(command=command5x2)   # pylint: disable=maybe-no-member
        buttons[22].configure(command=command5x3)   # pylint: disable=maybe-no-member
        buttons[23].configure(command=command5x4)   # pylint: disable=maybe-no-member
        buttons[24].configure(command=command5x5)   # pylint: disable=maybe-no-member
        break



change_button = tk.Button(main_window, text="Changing mode", bg="purple", fg="white", command=change_command)
change_button.place(x=0, y=500, height=100, width=500)



main_window.mainloop()