import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3

# project module
import show_attendance
import takeImage
import trainImage
import automaticAttedance

# engine = pyttsx3.init()
# engine.say("Welcome!")
# engine.say("Please browse through your options..")
# engine.runAndWait()


# def text_to_speech(user_text):
#     engine = pyttsx3.init()
#     engine.say(user_text)
#     engine.runAndWait()


haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = (
    "TrainingImageLabel/Trainner.yml"
)
trainimage_path = "TrainingImage/"
studentdetail_path = (
    "StudentDetails/studentdetails.csv"
)
attendance_path = "Attendence/"


window = Tk()
window.title("Face recognizer")
window.geometry("1280x720")
dialog_title = "QUIT"
dialog_text = "Are you sure want to close?"
window.configure(background="black")


# to destroy screen
def del_sc1():
    sc1.destroy()


# error message for name and no
def err_screen(): # Creating a new window 'sc1' using the 'tk.Tk()' command from the tkinter library
    global sc1
    sc1 = tk.Tk() # creates a new Tk root window
    sc1.geometry("400x110") # sets the geometry of the window to 400x110 pixels
    sc1.iconbitmap("AMS.ico") # sets the icon of the window to the file "AMS.ico"
    sc1.title("Warning!!") # sets the title of the window to "Warning!!"
    sc1.configure(background="black") # sets the background color of the window to black
    sc1.resizable(0, 0) # sets the window to be not resizable
   # Adding a label with specific text, color, background color, and font to the window
    tk.Label(  # creates a new label
        sc1, # specifies the parent window of the label
        text="Enrollment & Name required!!!",  # sets the text of the label
        fg="yellow",  # sets the foreground color of the label to yellow
        bg="black", # sets the background color of the label to black
        font=("times", 20, " bold "),  # sets the font of the label to Times New Roman, 20 point, bold
    ).pack() # packs the label into the parent window
   # Adding a button with specific text, color, background color, and font to the window
    tk.Button( # creates a new button
        sc1,  # specifies the parent window of the button
        text="OK", # sets the text of the button to "OK"
        command=del_sc1, # sets the command that will be executed when the button is clicked
        fg="yellow",  # sets the foreground color of the button to yellow
        bg="black", # sets the background color of the button to black
        width=9, # sets the width of the button to 9 characters
        height=1, # sets the height of the button to 1 character
        activebackground="Red", # sets the background color of the button when it is active (clicked) to red
        font=("times", 20, " bold "),  # sets the font of the button to Times New Roman, 20 point, bold
    ).place(x=110, y=50) # places the button at the position x=110, y=50 in the parent window


def testVal(inStr, acttyp):
    if acttyp == "1":  # insert
        if not inStr.isdigit():
            return False
    return True


logo = Image.open("UI_Image/0001.png") #Opening the logo image
logo = logo.resize((50, 47), Image.LANCZOS) #Resizing the logo image to (50, 47) pixels using the Lanczos resampling filter
logo1 = ImageTk.PhotoImage(logo) #Converting the resized logo image to a PhotoImage object and saving it in the logo1 variable
titl = tk.Label(window, bg="black", relief=RIDGE, bd=10, font=("arial", 35)) #Creating a label with a black background, a raised border, and a thickness of 10 pixels, and setting its text, font, and foreground color to "Smart College!!"
titl.pack(fill=X) #Packing the label to fill the X axis
l1 = tk.Label(window, image=logo1, bg="black",) #Creating a label with the logo image and setting its background color to black
l1.place(x=470, y=10) # Placing the logo image at the position (470, 10) in the window

titl = tk.Label( #
    window, text="Smart College!!", bg="black", fg="green", font=("arial", 27), 
) #Creating a label with the text "Smart College!!" and setting its background color, foreground color, font, and position
titl.place(x=525, y=12) #Placing the label at the position (525, 12) in the window

a = tk.Label( 
    window, 
    text="Welcome to the Face Recognition Based\nAttendance Management System", #
    bg="black", 
    fg="yellow", 
    bd=10, 
    font=("arial", 35), 
) #Creating a label with a black background and a raised border, and setting its text, font, foreground color, and position
a.pack() #Packing the label to fill the window

ri = Image.open("UI_Image/register.png") #Opening the register image
r = ImageTk.PhotoImage(ri) #Converting the register image to a PhotoImage object
label1 = Label(window, image=r) # Creating a label with the register image
label1.image = r #Saving the register image in the label1 variable
label1.place(x=100, y=270) #Placing the register image at the position (100, 270) in the window

ai = Image.open("UI_Image/attendance.png") #Opening the attendance image
a = ImageTk.PhotoImage(ai) # Converting the attendance image to a PhotoImage object
label2 = Label(window, image=a) #Creating a label with the attendance image
label2.image = a #Saving the attendance image in the label2 variable
label2.place(x=980, y=270) #Placing the attendance image at the position (980, 270) in the window

vi = Image.open("UI_Image/verifyy.png") #Opening the verify image
v = ImageTk.PhotoImage(vi) #Converting the verify image to a PhotoImage object
label3 = Label(window, image=v) # Creating a label with the verify image
label3.image = v # Saving the verify image in the label3 variable
label3.place(x=600, y=270) #Placing the verify image at the position (600, 270) in the window


def TakeImageUI():
    ImageUI = Tk() # Create a new Tkinter window
    ImageUI.title("Take Student Image..") # Create a new Tkinter window
    ImageUI.geometry("780x480") # Set the window geometry
    ImageUI.configure(background="black") # Configure the background color
    ImageUI.resizable(0, 0) # Prevent the window from being resized
    titl = tk.Label(ImageUI, bg="black", relief=RIDGE, bd=10, font=("arial", 35)) # Create a title label
    titl.pack(fill=X)
    # image and title
    titl = tk.Label(
        ImageUI, text="Register Your Face", bg="black", fg="green", font=("arial", 30),
    )  # Add an image and title to the window
    titl.place(x=270, y=12)
 # Create a heading label
    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="black",
        fg="yellow",
        bd=10,
        font=("arial", 24),
    )
    a.place(x=280, y=75)

     # Create a label and entry for the Enrollment Number
    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        validate="key",
        bg="black",
        fg="yellow",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

     # Create a label and entry for the Name
    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=17,
        bd=5,
        bg="black",
        fg="yellow",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt2.place(x=250, y=200)
    # Create a label for the notification
    lbl3 = tk.Label(
        ImageUI,
        text="Notification",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12),
    )
    lbl3.place(x=120, y=270)
    # Create a notification message
    message = tk.Label(
        ImageUI,
        text="",
        width=32,
        height=2,
        bd=5,
        bg="black",
        fg="yellow",
        relief=RIDGE,
        font=("times", 12, "bold"),
    )
    message.place(x=250, y=270)

    def take_image():    # Define a function to view attendance
        l1 = txt1.get()    # Get values from text input fields
        l2 = txt2.get()
        takeImage.TakeImage(    # Call the TakeImage function with the specified parameters
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            err_screen,
            #text_to_speech,
        )
        txt1.delete(0, "end")    # Clear text input fields after taking the image
        txt2.delete(0, "end")

    # take Image button
    # image
    takeImg = tk.Button(
        ImageUI,
        text="Take Image",
        command=take_image,
        bd=10,
        font=("times new roman", 18),
        bg="black",
        fg="yellow",
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=350)

    def train_image():    # Define a function to train the image
        trainImage.TrainImage(    # Call the TrainImage function with the specified parameters
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            #text_to_speech,
        )

    # train Image function call
    # Button for training the image
    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("times new roman", 18),
        bg="black",
        fg="yellow",
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=360, y=350)


r = tk.Button(    # Create a button to register a new student
    window,   # Specify the parent window for the button
    text="Register a new student",   # Set the text for the button
    command=TakeImageUI,   # Assign the TakeImageUI function to be called when the button is clicked
    bd=10,   # Set the border width for the button
    font=("times new roman", 16),   # Set the font for the button text
    bg="black",   # Set the background color for the button
    fg="yellow",   # Set the foreground color for the button text
    height=2,   # Set the height of the button in text lines
    width=17,   # Set the width of the button in text characters
)
r.place(x=100, y=520)    # Use the place method to position the button at a specific location in the window


def automatic_attedance():    # Define the function for taking attendance
    automaticAttedance.subjectChoose()    #removed text_to_speech argument


r = tk.Button(    # Create a button to take attendance
    window,   # Specify the parent window for the button
    text="Take Attendance",   # Set the text for the button
    command=automatic_attedance,   # Assign the automaticAttedance function to be called when the button is clicked
    bd=10,   # Set the border width for the button
    font=("times new roman", 16),   # Set the font for the button text
    bg="black",   # Set the background color for the button
    fg="yellow",   # Set the foreground color for the button text
    height=2,   # Set the height of the button in text lines
    width=17,   # Set the width of the button in text characters
)
r.place(x=600, y=520)


def view_attendance():
    show_attendance.subjectchoose() #removed text_to_speech argument

# Create a button to view attendance
r = tk.Button(
    window,    # Specify the parent window for the button
    text="View Attendance",    # This is the text that will be displayed on the button
    command=view_attendance,    # Assign the view_attendance function to be called when the button is clicked
    bd=10,    # Set the border width for the button
    font=("times new roman", 16),    # Set the font for the button text
    bg="black",    # Set the background color for the button
    fg="yellow",    # Set the foreground color for the button text
    height=2,    # Set the height of the button in text lines
    width=17,    # Set the width of the button in text characters
)
r.place(x=1000, y=520)    # Use the place method to position the button at a specific location in the window
r = tk.Button(    # Create an EXIT button
    window,    # Specify the parent window for the button
    text="EXIT",    # Set the text for the button
    bd=10,    # Set the border width for the button
    command=quit,    # Set the command to quit the application when the button is clicked
    font=("times new roman", 16),    # Set the font for the button text
    bg="black",    # Set the background color for the button
    fg="yellow",    # Set the foreground color for the button text
    height=2,    # Set the height of the button in text lines
    width=17,    # Set the width of the button in text characters
)
r.place(x=600, y=660)

window.mainloop()
