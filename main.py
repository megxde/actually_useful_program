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



def launch_error_window(arg):
    global command_to_execute
    global cause_of_error
    error_window.title(f"Error: command{arg}")
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



# def execute_command():
#     global command_to_execute
#     global cause_of_error
#     folder_path = os.path.dirname(os.path.abspath(__file__))
#     json_path = os.path.join(folder_path, 'commands_info.json')
#     with open(json_path, "r") as info:
#         info_data = json.load(info)
#         url = info_data[command_to_execute]["url"]
#         path = info_data[command_to_execute]["path"]
#         shortcut_path = info_data[command_to_execute]["shortcut_path"]

#     if url != "" and path != "" and shortcut_path != "":
#         cause_of_error = "The program broke. How did you manage to get everything filled up? Fix it yourself or reinstall."
#         launch_error_window()
#         return

#     elif url == "" and path == "" and shortcut_path == "":
#         cause_of_error = "You have everything empty for this. Go fill em up."
#         launch_error_window()
#         return
    
#     elif url != "" and path != "":
#         cause_of_error = "Two things are filled up at the same time. Go fix it or reinstall."
#         launch_error_window()
#         return

#     elif url != "" and shortcut_path != "":
#         cause_of_error = "Two things are filled up at the same time. Go fix it or reinstall."
#         launch_error_window()
#         return

#     elif path != "" and shortcut_path != "":
#         cause_of_error = "Two things are filled up at the same time. Go fix it or reinstall."
#         launch_error_window()
#         return

#     if url != "":
#         webbrowser.get('chrome').open_new_tab(url)
#         return
#     elif path != "":
#         subprocess.Popen(path)
#         return
#     elif shortcut_path != "":
#         os.startfile(shortcut_path)
#         return



def change_command():
    global changing_mode
    if changing_mode == False:
        changing_mode = True
        change_button.configure(bg="green", fg="black")
    elif changing_mode == True:
        changing_mode = False
        change_button.configure(bg="purple", fg="white")    



# def save_command_url_path():
#     global button_to_change
#     command_to_change = f"command{button_to_change[-3:]}"
#     url_to_save = url_entry.get()
#     path_to_save = path_entry.get()
#     shortcut_path_to_save = shortcut_path_entry.get()
#     image_name_to_save = image_name_entry.get()
#     url_entry.delete(0, 'end')
#     path_entry.delete(0, 'end')
#     shortcut_path_entry.delete(0, 'end')
#     image_name_entry.delete(0, 'end')
#     folder_path = os.path.dirname(os.path.abspath(__file__))
#     json_path = os.path.join(folder_path, 'commands_info.json')
#     image_json_path = os.path.join(folder_path, 'image_data.json')
#     with open(json_path, "r") as file:
#         data = json.load(file)
#     if url_to_save != "":
#         data[command_to_change]["url"] = url_to_save
#     if path_to_save != "":
#         data[command_to_change]["path"] = path_to_save
#     if shortcut_path_to_save != "":
#         data[command_to_change]["shortcut_path"] = shortcut_path_to_save
#     os.remove(json_path)
#     with open(json_path, "w") as file:
#         json.dump(data, file, indent=2)
#     if image_name_to_save != "":
#         with open(image_json_path, "r") as file:
#             image_data = json.load(file)
#         image_to_change = f"button{button_to_cha:]}"
#         image_data[image_to_change] = image_name_to_save
#         os.remove(image_json_path)
#         with open(image_json_path, "w") as file:
#             json.dump(image_data, file, indent=2)
#     button_changing_window.withdraw()



def save_url_command():
    global button_to_change
    folder_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(folder_path, 'commands_info.json')
    with open(json_path, "r") as file:
        data = json.load(file)
    url_to_write = url_entry.get()
    data[button_to_change]["url"] = url_to_write
    os.remove(json_path)
    with open(json_path, "w") as file:
        json.dump(data, file, indent=2)
    save_image_withdraw()

def save_path_command():
    global button_to_change
    folder_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(folder_path, 'commands_info.json')
    with open(json_path, "r") as file:
        data = json.load(file)
    path_to_write = path_entry.get()
    data[button_to_change]["path"] = path_to_write
    os.remove(json_path)
    with open(json_path, "w") as file:
        json.dump(data, file, indent=2)
    save_image_withdraw()

def save_shortcut_path_command():
    global button_to_change
    folder_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(folder_path, 'commands_info.json')
    with open(json_path, "r") as file:
        data = json.load(file)
    shortcut_path_to_write = shortcut_path_entry.get()
    data[button_to_change]["shortcut_path"] = shortcut_path_to_write
    os.remove(json_path)
    with open(json_path, "w") as file:
        json.dump(data, file, indent=2)
    save_image_withdraw()

def save_image_withdraw():
    global button_to_change
    folder_path = os.path.dirname(os.path.abspath(__file__))
    image_json_path = os.path.join(folder_path, 'image_data.json')
    with open(image_json_path, "r") as file:
        image_data = json.load(file)
    image_to_write = image_name_entry.get()
    image_data[button_to_change] = image_to_write
    os.remove(image_json_path)
    with open(image_json_path, "w") as file:
        json.dump(image_data, file, indent=2)
    url_entry.delete(0, 'end')
    path_entry.delete(0, 'end')
    shortcut_path_entry.delete(0, 'end')
    image_name_entry.delete(0, 'end')
    button_changing_window.withdraw()

def clear_button_command():
    global button_to_change
    folder_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(folder_path, 'commands_info.json')
    image_json_path = os.path.join(folder_path, 'image_data.json')
    with open(json_path, "r") as file:
        command_data = json.load(file)
    with open(image_json_path, "r") as file:
        image_data = json.load(file)
    command_data[button_to_change]["url"] = ""
    command_data[button_to_change]["path"] = ""
    command_data[button_to_change]["shortcut_path"] = ""
    image_data[button_to_change] = ""
    os.remove(json_path)
    with open(json_path, "w") as file:
        json.dump(command_data, file, indent=2)
    os.remove(image_json_path)
    with open(image_json_path, "w") as file:
        json.dump(image_data, file, indent=2)
    url_entry.delete(0, 'end')
    path_entry.delete(0, 'end')
    shortcut_path_entry.delete(0, 'end')
    image_name_entry.delete(0, 'end')
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

save_url_button = tk.Button(button_changing_window, text="Save Url", bg="green", fg="black", command=save_url_command)
save_url_button.place(x=0, y=120)

save_path_button = tk.Button(button_changing_window, text="Save Path", bg="green", fg="black", command=save_path_command)
save_path_button.place(x=0, y=140)

save_shortcut_path_button = tk.Button(button_changing_window, text="Save Shortcut Path", bg="green", fg="black", command=save_shortcut_path_command)
save_shortcut_path_button.place(x=0, y=160)

clear_button = tk.Button(button_changing_window, text="Clear", bg="green", fg="black", command=clear_button_command)
clear_button.place(x=0, y=180)

button_changing_window.withdraw()



def launch_button_change_window(arg):
    global button_to_change
    button_to_change = arg
  
    button_changing_window.title(f"Changing {button_to_change}")

    button_changing_window.update()
    button_changing_window.deiconify()

    button_changing_window.mainloop()



# def command1x1():
#     global changing_mode
#     global button_to_change
#     global command_to_execute
#     if changing_mode == True:
#         button_to_change = "button1x1"
#         launch_button_change_window()
#     elif changing_mode == False:
#         command_to_execute = "command1x1"
#         execute_command()   



with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'image_data.json'), "r") as image_json:
    image_data = json.load(image_json)

image_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')



def callback(arg):
    global changing_mode
    global cause_of_error
    if changing_mode == True:
        launch_button_change_window(arg)
    elif changing_mode == False:
        folder_path = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(folder_path, 'commands_info.json')
        with open(json_path, "r") as file:
            command_data = json.load(file)
        url = command_data[arg]["url"]
        path = command_data[arg]["path"]
        shortcut_path = command_data[arg]["shortcut_path"]
        if url != "" and path != "" and shortcut_path != "":
            cause_of_error = "The program broke. How did you manage to get everything filled up? Fix it yourself or reinstall."
            launch_error_window(arg)
            return

        elif url == "" and path == "" and shortcut_path == "":
            cause_of_error = "You have everything empty for this. Go fill em up."
            launch_error_window(arg)
            return
        
        elif url != "" and path != "":
            cause_of_error = "Two things are filled up at the same time. Go fix it or reinstall."
            launch_error_window(arg)
            return

        elif url != "" and shortcut_path != "":
            cause_of_error = "Two things are filled up at the same time. Go fix it or reinstall."
            launch_error_window(arg)
            return

        elif path != "" and shortcut_path != "":
            cause_of_error = "Two things are filled up at the same time. Go fix it or reinstall."
            launch_error_window(arg)
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
        




image_1x1_name = image_data["1x1"]
image_1x2_name = image_data["1x2"]
image_1x3_name = image_data["1x3"]
image_1x4_name = image_data["1x4"]
image_1x5_name = image_data["1x5"]
image_2x1_name = image_data["2x1"]
image_2x2_name = image_data["2x2"]
image_2x3_name = image_data["2x3"]
image_2x4_name = image_data["2x4"]
image_2x5_name = image_data["2x5"]
image_3x1_name = image_data["3x1"]
image_3x2_name = image_data["3x2"]
image_3x3_name = image_data["3x3"]
image_3x4_name = image_data["3x4"]
image_3x5_name = image_data["3x5"]
image_4x1_name = image_data["4x1"]
image_4x2_name = image_data["4x2"]
image_4x3_name = image_data["4x3"]
image_4x4_name = image_data["4x4"]
image_4x5_name = image_data["4x5"]
image_5x1_name = image_data["5x1"]
image_5x2_name = image_data["5x2"]
image_5x3_name = image_data["5x3"]
image_5x4_name = image_data["5x4"]
image_5x5_name = image_data["5x5"]



if image_1x1_name != "":
    image_1x1_path = os.path.join(image_folder_path, image_1x1_name)
    image_1x1 = ImageTk.PhotoImage(Image.open(image_1x1_path).resize((100, 100), Image.ANTIALIAS))
    button1x1 = tk.Button(main_window, image=image_1x1, **bg_fg_var, command=lambda: callback("1x1"))
elif image_1x1_name == "":
    button1x1 = tk.Button(main_window, text="button1x1", **bg_fg_var, command=lambda: callback("1x1"))

button1x1.place(x=0, y=0, height=100, width=100)



if image_1x2_name != "":
    image_1x2_path = os.path.join(image_folder_path, image_1x2_name)
    image_1x2 = ImageTk.PhotoImage(Image.open(image_1x2_path).resize((100, 100), Image.ANTIALIAS))
    button1x2 = tk.Button(main_window, image=image_1x2, **bg_fg_var, command=lambda: callback("1x2"))
elif image_1x2_name == "":
    button1x2 = tk.Button(main_window, text="button1x2", **bg_fg_var, command=lambda: callback("1x2"))

button1x2.place(x=100, y=0, height=100, width=100)



if image_1x3_name != "":
    image_1x3_path = os.path.join(image_folder_path, image_1x3_name)
    image_1x3 = ImageTk.PhotoImage(Image.open(image_1x3_path).resize((100, 100), Image.ANTIALIAS))
    button1x3 = tk.Button(main_window, image=image_1x3, **bg_fg_var, command=lambda: callback("1x3"))
elif image_1x3_name == "":
    button1x3 = tk.Button(main_window, text="button1x3", **bg_fg_var, command=lambda: callback("1x3"))

button1x3.place(x=200, y=0, height=100, width=100)



if image_1x4_name != "":
    image_1x4_path = os.path.join(image_folder_path, image_1x4_name)
    image_1x4 = ImageTk.PhotoImage(Image.open(image_1x4_path).resize((100, 100), Image.ANTIALIAS))
    button1x4 = tk.Button(main_window, image=image_1x4, **bg_fg_var, command=lambda: callback("1x4"))
elif image_1x4_name == "":
    button1x4 = tk.Button(main_window, text="button1x4", **bg_fg_var, command=lambda: callback("1x4"))

button1x4.place(x=300, y=0, height=100, width=100)



if image_1x5_name != "":
    image_1x5_path = os.path.join(image_folder_path, image_1x5_name)
    image_1x5 = ImageTk.PhotoImage(Image.open(image_1x5_path).resize((100, 100), Image.ANTIALIAS))
    button1x5 = tk.Button(main_window, image=image_1x5, **bg_fg_var, command=lambda: callback("1x5"))
elif image_1x5_name == "":
    button1x5 = tk.Button(main_window, text="button1x5", **bg_fg_var, command=lambda: callback("1x5"))

button1x5.place(x=400, y=0, height=100, width=100)



if image_2x1_name != "":
    image_2x1_path = os.path.join(image_folder_path, image_2x1_name)
    image_2x1 = ImageTk.PhotoImage(Image.open(image_2x1_path).resize((100, 100), Image.ANTIALIAS))
    button2x1 = tk.Button(main_window, image=image_2x1, **bg_fg_var, command=lambda: callback("2x1"))
elif image_2x1_name == "":
    button2x1 = tk.Button(main_window, text="button2x1", **bg_fg_var, command=lambda: callback("2x1"))

button2x1.place(x=0, y=100, height=100, width=100)



if image_2x2_name != "":
    image_2x2_path = os.path.join(image_folder_path, image_2x2_name)
    image_2x2 = ImageTk.PhotoImage(Image.open(image_2x2_path).resize((100, 100), Image.ANTIALIAS))
    button2x2 = tk.Button(main_window, image=image_2x2, **bg_fg_var, command=lambda: callback("2x2"))
elif image_2x2_name == "":
    button2x2 = tk.Button(main_window, text="button2x2", **bg_fg_var, command=lambda: callback("2x2"))

button2x2.place(x=100, y=100, height=100, width=100)



if image_2x3_name != "":
    image_2x3_path = os.path.join(image_folder_path, image_2x3_name)
    image_2x3 = ImageTk.PhotoImage(Image.open(image_2x3_path).resize((100, 100), Image.ANTIALIAS))
    button2x3 = tk.Button(main_window, image=image_2x3, **bg_fg_var, command=lambda: callback("2x3"))
elif image_2x3_name == "":
    button2x3 = tk.Button(main_window, text="button2x3", **bg_fg_var, command=lambda: callback("2x3"))

button2x3.place(x=200, y=100, height=100, width=100)



if image_2x4_name != "":
    image_2x4_path = os.path.join(image_folder_path, image_2x4_name)
    image_2x4 = ImageTk.PhotoImage(Image.open(image_2x4_path).resize((100, 100), Image.ANTIALIAS))
    button2x4 = tk.Button(main_window, image=image_2x4, **bg_fg_var, command=lambda: callback("2x4"))
elif image_2x4_name == "":
    button2x4 = tk.Button(main_window, text="button2x4", **bg_fg_var, command=lambda: callback("2x4"))

button2x4.place(x=300, y=100, height=100, width=100)



if image_2x5_name != "":
    image_2x5_path = os.path.join(image_folder_path, image_2x5_name)
    image_2x5 = ImageTk.PhotoImage(Image.open(image_2x5_path).resize((100, 100), Image.ANTIALIAS))
    button2x5 = tk.Button(main_window, image=image_2x5, **bg_fg_var, command=lambda: callback("2x5"))
elif image_2x5_name == "":
    button2x5 = tk.Button(main_window, text="button2x5", **bg_fg_var, command=lambda: callback("2x5"))

button2x5.place(x=400, y=100, height=100, width=100)



if image_3x1_name != "":
    image_3x1_path = os.path.join(image_folder_path, image_3x1_name)
    image_3x1 = ImageTk.PhotoImage(Image.open(image_3x1_path).resize((100, 100), Image.ANTIALIAS))
    button3x1 = tk.Button(main_window, image=image_3x1, **bg_fg_var, command=lambda: callback("3x1"))
elif image_3x1_name == "":
    button3x1 = tk.Button(main_window, text="button3x1", **bg_fg_var, command=lambda: callback("3x1"))

button3x1.place(x=0, y=200, height=100, width=100)



if image_3x2_name != "":
    image_3x2_path = os.path.join(image_folder_path, image_3x2_name)
    image_3x2 = ImageTk.PhotoImage(Image.open(image_3x2_path).resize((100, 100), Image.ANTIALIAS))
    button3x2 = tk.Button(main_window, image=image_3x2, **bg_fg_var, command=lambda: callback("3x2"))
elif image_3x2_name == "":
    button3x2 = tk.Button(main_window, text="button3x2", **bg_fg_var, command=lambda: callback("3x2"))

button3x2.place(x=100, y=200, height=100, width=100)



if image_3x3_name != "":
    image_3x3_path = os.path.join(image_folder_path, image_3x3_name)
    image_3x3 = ImageTk.PhotoImage(Image.open(image_3x3_path).resize((100, 100), Image.ANTIALIAS))
    button3x3 = tk.Button(main_window, image=image_3x3, **bg_fg_var, command=lambda: callback("3x3"))
elif image_3x3_name == "":
    button3x3 = tk.Button(main_window, text="button3x3", **bg_fg_var, command=lambda: callback("3x3"))

button3x3.place(x=200, y=200, height=100, width=100)



if image_3x4_name != "":
    image_3x4_path = os.path.join(image_folder_path, image_3x4_name)
    image_3x4 = ImageTk.PhotoImage(Image.open(image_3x4_path).resize((100, 100), Image.ANTIALIAS))
    button3x4 = tk.Button(main_window, image=image_3x4, **bg_fg_var, command=lambda: callback("3x4"))
elif image_3x4_name == "":
    button3x4 = tk.Button(main_window, text="button3x4", **bg_fg_var, command=lambda: callback("3x4"))

button3x4.place(x=300, y=200, height=100, width=100)



if image_3x5_name != "":
    image_3x5_path = os.path.join(image_folder_path, image_3x5_name)
    image_3x5 = ImageTk.PhotoImage(Image.open(image_3x5_path).resize((100, 100), Image.ANTIALIAS))
    button3x5 = tk.Button(main_window, image=image_3x5, **bg_fg_var, command=lambda: callback("3x5"))
elif image_3x5_name == "":
    button3x5 = tk.Button(main_window, text="button3x5", **bg_fg_var, command=lambda: callback("3x5"))

button3x5.place(x=400, y=200, height=100, width=100)



if image_4x1_name != "":
    image_4x1_path = os.path.join(image_folder_path, image_4x1_name)
    image_4x1 = ImageTk.PhotoImage(Image.open(image_4x1_path).resize((100, 100), Image.ANTIALIAS))
    button4x1 = tk.Button(main_window, image=image_4x1, **bg_fg_var, command=lambda: callback("4x1"))
elif image_4x1_name == "":
    button4x1 = tk.Button(main_window, text="button4x1", **bg_fg_var, command=lambda: callback("4x1"))

button4x1.place(x=0, y=300, height=100, width=100)



if image_4x2_name != "":
    image_4x2_path = os.path.join(image_folder_path, image_4x2_name)
    image_4x2 = ImageTk.PhotoImage(Image.open(image_4x2_path).resize((100, 100), Image.ANTIALIAS))
    button4x2 = tk.Button(main_window, image=image_4x2, **bg_fg_var, command=lambda: callback("4x2"))
elif image_4x2_name == "":
    button4x2 = tk.Button(main_window, text="button4x2", **bg_fg_var, command=lambda: callback("4x2"))

button4x2.place(x=100, y=300, height=100, width=100)



if image_4x3_name != "":
    image_4x3_path = os.path.join(image_folder_path, image_4x3_name)
    image_4x3 = ImageTk.PhotoImage(Image.open(image_4x3_path).resize((100, 100), Image.ANTIALIAS))
    button4x3 = tk.Button(main_window, image=image_4x3, **bg_fg_var, command=lambda: callback("4x3"))
elif image_4x3_name == "":
    button4x3 = tk.Button(main_window, text="button4x3", **bg_fg_var, command=lambda: callback("4x3"))

button4x3.place(x=200, y=300, height=100, width=100)



if image_4x4_name != "":
    image_4x4_path = os.path.join(image_folder_path, image_4x4_name)
    image_4x4 = ImageTk.PhotoImage(Image.open(image_4x4_path).resize((100, 100), Image.ANTIALIAS))
    button4x4 = tk.Button(main_window, image=image_4x4, **bg_fg_var, command=lambda: callback("4x4"))
elif image_4x4_name == "":
    button4x4 = tk.Button(main_window, text="button4x4", **bg_fg_var, command=lambda: callback("4x4"))

button4x4.place(x=300, y=300, height=100, width=100)



if image_4x5_name != "":
    image_4x5_path = os.path.join(image_folder_path, image_4x5_name)
    image_4x5 = ImageTk.PhotoImage(Image.open(image_4x5_path).resize((100, 100), Image.ANTIALIAS))
    button4x5 = tk.Button(main_window, image=image_4x5, **bg_fg_var, command=lambda: callback("4x5"))
elif image_4x5_name == "":
    button4x5 = tk.Button(main_window, text="button4x5", **bg_fg_var, command=lambda: callback("4x5"))

button4x5.place(x=400, y=300, height=100, width=100)



if image_5x1_name != "":
    image_5x1_path = os.path.join(image_folder_path, image_5x1_name)
    image_5x1 = ImageTk.PhotoImage(Image.open(image_5x1_path).resize((100, 100), Image.ANTIALIAS))
    button5x1 = tk.Button(main_window, image=image_5x1, **bg_fg_var, command=lambda: callback("5x1"))
elif image_5x1_name == "":
    button5x1 = tk.Button(main_window, text="button5x1", **bg_fg_var, command=lambda: callback("5x1"))

button5x1.place(x=0, y=400, height=100, width=100)



if image_5x2_name != "":
    image_5x2_path = os.path.join(image_folder_path, image_5x2_name)
    image_5x2 = ImageTk.PhotoImage(Image.open(image_5x2_path).resize((100, 100), Image.ANTIALIAS))
    button5x2 = tk.Button(main_window, image=image_5x2, **bg_fg_var, command=lambda: callback("5x2"))
elif image_5x2_name == "":
    button5x2 = tk.Button(main_window, text="button5x2", **bg_fg_var, command=lambda: callback("5x2"))

button5x2.place(x=100, y=400, height=100, width=100)



if image_5x3_name != "":
    image_5x3_path = os.path.join(image_folder_path, image_5x3_name)
    image_5x3 = ImageTk.PhotoImage(Image.open(image_5x3_path).resize((100, 100), Image.ANTIALIAS))
    button5x3 = tk.Button(main_window, image=image_5x3, **bg_fg_var, command=lambda: callback("5x3"))
elif image_5x3_name == "":
    button5x3 = tk.Button(main_window, text="button5x3", **bg_fg_var, command=lambda: callback("5x3"))

button5x3.place(x=200, y=400, height=100, width=100)



if image_5x4_name != "":
    image_5x4_path = os.path.join(image_folder_path, image_5x4_name)
    image_5x4 = ImageTk.PhotoImage(Image.open(image_5x4_path).resize((100, 100), Image.ANTIALIAS))
    button5x4 = tk.Button(main_window, image=image_5x4, **bg_fg_var, command=lambda: callback("5x4"))
elif image_5x4_name == "":
    button5x4 = tk.Button(main_window, text="button5x4", **bg_fg_var, command=lambda: callback("5x4"))

button5x4.place(x=300, y=400, height=100, width=100)



if image_5x5_name != "":
    image_5x5_path = os.path.join(image_folder_path, image_5x5_name)
    image_5x5 = ImageTk.PhotoImage(Image.open(image_5x5_path).resize((100, 100), Image.ANTIALIAS))
    button5x5 = tk.Button(main_window, image=image_5x5, **bg_fg_var, command=lambda: callback("5x5"))
elif image_5x5_name == "":
    button5x5 = tk.Button(main_window, text="button5x5", **bg_fg_var, command=lambda: callback("5x5"))

button5x5.place(x=400, y=400, height=100, width=100)







change_button = tk.Button(main_window, text="Changing mode", bg="purple", fg="white", command=change_command)
change_button.place(x=0, y=500, height=100, width=500)



main_window.mainloop()