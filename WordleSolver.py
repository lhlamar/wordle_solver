



import os
import string
import tkinter as tk
from tkinter import CENTER, END, INSERT, LEFT, RIGHT, Frame, Toplevel, filedialog, Text, Entry
import pathlib
from tkinter import ttk
from turtle import bgcolor, color, left, pos, xcor

used_filter = ""
green_filter = ["\n", "\n", "\n", "\n", "\n"]
yellow_filter = ["\n", "\n", "\n", "\n", "\n"]
entrylist = ["", "", "", "", ""]
green_mode = False
yellow_mode = False
used_mode = False
global entry0
global entry1
global entry2
global entry3
global entry4





def add_print_window(word_list:list):


    for i in root.winfo_children():
        if i.widgetName == "toplevel":
            i.destroy()
    

    print_window = tk.Toplevel(root)
    print_window.geometry("100x600")
    print_window.configure(bg = "black")
    print_window.resizable(width=False, height=False)

    list_text = tk.Text(print_window, height = 600, width=100)
    scroll_bar = tk.Scrollbar(print_window)
    scroll_bar.pack(side=RIGHT)
    list_text.pack(side=LEFT)

    for i in word_list:
        list_text.insert(END, i + "\n")

    

    

root = tk.Tk()
root.geometry("600x600")
root.configure(background="black")
root.resizable(width=False, height=False)


info = tk.Label(root, bg = "black", fg = "white",
font = "Arial 12 bold", text = "HOW TO USE: Select green or yellow mode, then enter \nthe characters corresponding to your each \nturn of your game in the boxes, then select search.")
info.pack(side="top")


instructions2 = tk.Label(root, bg = "black", fg = "gray", 
font = "ComicSans 15 bold", text = "Have fun winning :)")
instructions2.pack(side="bottom")

instructions1 = tk.Label(root, bg = "black", fg = "yellow", 
font = "ComicSans 15 bold", text = "Click here to enter yellow filter mode")
instructions1.pack(side="bottom")


instructions = tk.Label(root, bg = "black", fg = "green", 
font = "ComicSans 15 bold", text = "Click here to enter green filter mode")
instructions.pack(side="bottom")

instructions_frame = tk.Frame(root, bg = "black", width=525, height=250)
instructions_frame.place(anchor=CENTER, relx="0.5", rely="0.4")

testbutton = tk.Button(root, bg = "gray", width=20, height = 1, text="test")
testbutton.pack(side="bottom")

search_button = tk.Button(root, bg = "gray", width = 20, height = 1, text = "search")
search_button.place(anchor="center", relx=0.5, rely=0.75)

used_character_entry = tk.Entry(root, background="gray", fg="black", width=50)
used_character_entry.place(anchor=CENTER, relx=0.5, rely=0.25)

used_character_instructions = tk.Label(root, background="black", foreground="white",
font="ComicSane 12", text="Enter your used characters here")
used_character_instructions.place(anchor=CENTER, relx="0.5", rely="0.2")


error_message = tk.Label(root, background="black", foreground="black",
font="Arial 14", text="Error: Please only enter letters in the English alphabet")
error_message.place(anchor=CENTER, relx="0.5", rely="0.6")

path1 = pathlib.Path(__file__)
path2 = path1.parent
os.chdir(path2)
print(os.getcwd())
#opens word_list.txt and stores it in a list
try:
    my_file = open("word_list.txt" , "r")
except FileNotFoundError: 
    if not os.path.exists("word_list.txt"):
        print("word_list.txt was not found, please make sure it is in the same folder as the app")
        input("Please press enter to close program: ")
        exit()
        
word_list = my_file.read().splitlines()
my_file.close()
#checks to see if the list was properly created
if bool(word_list): 
    print("List of 5 letter English words has been successfully imported")


def get_color(entrynum, index):
    for tag in entrynum.tag_names(index)[::-1]:
        fg = entrynum.tag_cget(tag, "foreground")
        if fg != "":
            return fg
    return entrynum.cget("foreground")

def trim_entry():
    entry0.delete("1.1", END)
    entry1.delete("1.1", END)
    entry2.delete("1.1", END)
    entry3.delete("1.1", END)
    entry4.delete("1.1", END)
    root.after(100, trim_entry)
    
    
def check_alpha():

    

    if ((entry0.get("1.0").isalpha() or entry0.get("1.0") == "\n")
    and (entry1.get("1.0").isalpha() or entry1.get("1.0") == "\n")
    and (entry2.get("1.0").isalpha() or entry2.get("1.0") == "\n")
    and (entry3.get("1.0").isalpha() or entry3.get("1.0") == "\n")
    and (entry4.get("1.0").isalpha() or entry4.get("1.0") == "\n")
    and (used_character_entry.get().isalpha() or used_character_entry.get() == "")):
        return True
    else:
        return False


        






def updatefilters(*args):
    global entry0
    global entry1
    global entry2
    global entry3
    global entry4
    global green_mode
    global yellow_mode
    global entrylist
    global yellow_filter
    global green_filter
    global used_filter


    


    if check_alpha():
        entrylist[0] = entry0.get("1.0").lower()
        entrylist[1] = entry1.get("1.0").lower()
        entrylist[2] = entry2.get("1.0").lower()
        entrylist[3] = entry3.get("1.0").lower()
        entrylist[4] = entry4.get("1.0").lower()
        
        if get_color(entry0, "1.0") == "green":
            green_filter[0] = entry0.get("1.0").lower()
        if get_color(entry1, "1.0") == "green":
            green_filter[1] = entry1.get("1.0").lower()
        if get_color(entry2, "1.0") == "green":
            green_filter[2] = entry2.get("1.0").lower()
        if get_color(entry3, "1.0") == "green":
            green_filter[3] = entry3.get("1.0").lower()
        if get_color(entry4, "1.0") == "green":
            green_filter[4] = entry4.get("1.0").lower()

        if get_color(entry0, "1.0") == "yellow":
            yellow_filter[0] = entry0.get("1.0").lower()
        if get_color(entry1, "1.0") == "yellow":
            yellow_filter[1] = entry1.get("1.0").lower()
        if get_color(entry2, "1.0") == "yellow":
            yellow_filter[2] = entry2.get("1.0").lower()
        if get_color(entry3, "1.0") == "yellow":
            yellow_filter[3] = entry3.get("1.0").lower()
        if get_color(entry4, "1.0") == "yellow":
            yellow_filter[4] = entry4.get("1.0").lower()



        used_filter = used_character_entry.get().lower()


        error_message.configure(fg="black")

    else: error_message.configure(fg="red")
    

    # if yellow_mode:
        
    #     yellow_filter[0] = entry0.get("1.0")
    #     yellow_filter[1] = entry1.get("1.0")
    #     yellow_filter[2] = entry2.get("1.0")
    #     yellow_filter[3] = entry3.get("1.0")
    #     yellow_filter[4] = entry4.get("1.0")

    # if green_mode:
    #     green_filter[0] = entry0.get("1.0")
    #     green_filter[1] = entry1.get("1.0")
    #     green_filter[2] = entry2.get("1.0")
    #     green_filter[3] = entry3.get("1.0")
    #     green_filter[4] = entry4.get("1.0")





entry_frame = tk.Frame(root, bg = "black", width=400, height = 75 )
entry_frame.place(relx=0.5, rely=0.5, anchor=CENTER)


def entry_builder(color: string):

    global entry0
    global entry1
    global entry2
    global entry3
    global entry4
    global entry_frame
    global green_mode
    global yellow_mode
    global used_mode
    
    

    
    if entrylist[0] == "":
        entry0 = tk.Text(entry_frame, font="Arial 38", bg="gray",fg=color, width=1, height=1)
        entry0.place(relx=0.1, rely=0.5, anchor=CENTER)
    
    if entrylist[1] == "":
        entry1 = tk.Text(entry_frame, font="Arial 38", bg="gray",fg=color, width=1, height=1)
        entry1.place(relx=0.3, rely=0.5, anchor=CENTER)
    
    if entrylist[2] == "":
        entry2 = tk.Text(entry_frame, font="Arial 38", bg="gray",fg=color, width=1, height=1)
        entry2.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    if entrylist[3] == "":
        entry3 = tk.Text(entry_frame, font="Arial 38", bg="gray",fg=color, width=1, height=1)
        entry3.place(relx=0.7, rely=0.5, anchor=CENTER)
    
    if entrylist[4] == "":
        entry4 = tk.Text(entry_frame, font="Arial 38", bg="gray",fg=color, width=1, height=1)
        entry4.place(relx=0.9, rely=0.5, anchor=CENTER)

#entry_builder("green")
#green_instructions = tk.Label(instructions_frame, bg="black", fg="green", text="enter your green characters in the correct position",
#font="Arial 13 bold",)
#green_instructions.pack()


# entry_builder("green")
# green_mode = True
# green_instructions = tk.Label(instructions_frame, bg="black", fg="green", text="enter your green characters in the correct position",
#     font="Arial 13 bold",)
# green_instructions.pack()


def clear_instructions_frame():
    for x in instructions_frame.winfo_children():
        x.destroy()




def press_g(*args):

    global green_mode
    global yellow_mode
    global used_mode
    
    if not green_mode:
        entry_builder("green")
        for x in entry_frame.winfo_children():
            if not x.get("1.0").isalpha():
                x.config(fg="green")  
    trim_entry()
         
    used_mode = False
    yellow_mode = False
    green_mode = True
    updatefilters()
    clear_instructions_frame()
    green_instructions = tk.Label(instructions_frame, bg="black", fg="green", text="enter your green characters in the correct position",
    font="Arial 13 bold",)
    green_instructions.pack()

def press_y(*args):
    global green_mode
    global yellow_mode
    global used_mode
    
    if not yellow_mode:
        entry_builder("yellow")
        for x in entry_frame.winfo_children():
            if not x.get("1.0").isalpha():
                x.config(fg="yellow")
    trim_entry()
    used_mode = False
    yellow_mode = True
    green_mode = False
    updatefilters()
    clear_instructions_frame()
    yellow_instructions = tk.Label(instructions_frame, bg="black", fg="yellow", text="enter your yellow letters in the correct position",
    font="Arial 13 bold")
    yellow_instructions.pack()

def press_u(*args):
    global green_mode
    global yellow_mode
    global used_mode
    used_mode = True
    yellow_mode = False
    green_mode = False
    clear_instructions_frame()
    used_instructions = tk.Label(instructions_frame, bg="black", fg="gray", text="used instructions",
    font="Arial 13 bold")
    used_instructions.pack()





def press_t(*args):

    #print(entry0.get("1.0"))
    # print(str(entrylist) + "entry list")
    # print(str(green_filter) + "green filter list")
    # print(str(yellow_filter) + "yellow filter list")
    # print(str(green_mode) + " green mode")
    # print(str(yellow_mode) + " yellow mode")
    # print(str(used_mode) + " used mode")
    # print(get_color(entry0, "1.0"))
    # print(used_filter)

     for i in used_filter:
         print(i)

     
     print(used_character_entry.get().isalpha())

     print(used_character_entry.get() == "")

    


    
    
    


def delete(*args):
    for widget in root.winfo_children():
        widget.destroy()
def quit(*args):
    root.quit()

temp_list = word_list
def reset(*args):
    temp_list = word_list

def search(*args):
    global temp_list
    
    updatefilters()
    trim_entry()
    
    temp_list = active_green_filter(temp_list)
    temp_list = active_yellow_filter(temp_list)
    temp_list = active_used_filter(temp_list)
    
    if check_alpha():
        add_print_window(temp_list)
    
    



    
instructions1.bind("<Button-1>", press_y)

instructions.bind("<Button-1>", press_g)
instructions2.bind("<Button-1>", press_u)
testbutton.bind("<Button-1>", press_t)
search_button.bind("<Button-1>", search)





    


   



# about = Text(frame, bg="black", fg="white", font="Arial")
# about.insert(INSERT, "Welcome to Wordle Solver toolkit! Follow onscreen instructions to   continue.")    
# about.pack()
# about.pack(side="top")



#sets working directory to the parent of the .py file so that the program can open the .txt file



def active_green_filter(word_list:list):
    
    temp = []
    for i in word_list:
        if ((i[0] == green_filter[0] or green_filter[0] == "\n")
        and (i[1] == green_filter[1] or green_filter[1] == "\n")
        and (i[2] == green_filter[2] or green_filter[2] == "\n")
        and (i[3] == green_filter[3] or green_filter[3] == "\n")
        and (i[4] == green_filter[4] or green_filter[4] == "\n")):
            temp.append(i)
            
    return temp


def active_yellow_filter(word_list:list):
    temp = []
    for i in word_list:
        if (((yellow_filter[0] in i or yellow_filter[0] == "\n") and yellow_filter[0] != i[0])
        and ((yellow_filter[1] in i or yellow_filter[1] == "\n") and yellow_filter[1] != i[1])
        and ((yellow_filter[2] in i or yellow_filter[2] == "\n") and yellow_filter[2] != i[2])
        and ((yellow_filter[3] in i or yellow_filter[3] == "\n") and yellow_filter[3] != i[3])
        and ((yellow_filter[4] in i or yellow_filter[4] == "\n") and yellow_filter[4] != i[4])):
            temp.append(i)
    return temp

def print_word_list(word_list:list):
    for i in word_list:
        print(i)


def active_used_filter(word_list:list):
    temp_list = word_list.copy()
    temp_list1 = word_list.copy()
    hashset = []
    for char in used_filter:
        hashset.append(char)
    print(hashset)

    for word in temp_list:
        for char in word:
            if char in hashset:
                temp_list1.remove(word)
                break
                

    return temp_list1
        

    

    









root.mainloop()


#pulls in user input to see what input they want to use
# opt = {'g', 'y', 'u', 'z'}
# switch = 'b'
# while switch not in opt:
#     switch = str(input("Enter 'g' to filter by green spaces, Enter 'y' to filter by yellow spaces, Enter 'u' to filter out unused chars,\nor enter"
#     " 'z' to exit the program: "))
#     if switch not in opt:
#         print("Please enter a valid character")


#     if switch == 'g':
#         switch = 'b'
        

#         g_filter = input("Please enter known green chars, with _ for unknown chars as a placeholder: ")

#     if switch == 'y':
#         switch = 'b'
#         y_filter = input("Please enter known yellow chars, with _ for uknown chars as a placeholder: ")

#     if switch == 'u': 
#         switch = 'b'
#         u_filter = input("Please enter your list of used chars in the form \"abc...\" replacing a, b, and c\nwith as many chars as you need: ")

#     if switch == 'z':
#         switch = 'b'
#         exit()


