import pandas as pd    # Importing the pandas library for data manipulation
from glob import glob    # Importing the glob module for file path matching
import os    # Importing the os module for interacting with the operating system
import tkinter    # Importing the tkinter library for creating GUIs
import csv    # Importing the csv module for reading and writing CSV files
import tkinter as tk    # Importing the tkinter module with an alias
from tkinter import *    # Importing all classes and functions from tkinter

def subjectchoose():    #removed text_to_speech 
    def calculate_attendance():    # Define a function to calculate and display attendance
        Subject = tx.get()    # Get the subject name from the user input
        if Subject=="":    # Check if the subject name is empty
            t='Please enter the subject name.'
            #text_to_speech(t)    # Call text-to-speech function (commented out)
            print(t)
        # os.chdir(
        #     f"Attendance/{Subject}"
        # )
        filenames = glob(
            f"Attendance/{Subject}/{Subject}*.csv"    # Get a list of CSV files for the subject
        )
        
        df = [pd.read_csv(f) for f in filenames]    # Read each CSV file into a pandas DataFrame
        newdf = df[0]    # Initialize a new DataFrame with the first CSV file
        for i in range(1, len(df)):
            newdf = newdf.merge(df[i], how="outer")    # Merge all CSV files into one DataFrame
        newdf.fillna(0, inplace=True)    # Fill NaN values with 0
        newdf["Attendance"] = 0    # Add a new column for attendance percentage
        for i in range(len(newdf)):
            newdf["Attendance"].iloc[i] = str(int(round(newdf.iloc[i, 2:-1].mean() * 100)))+'%'    # Calculate and format attendance percentage
            #newdf.sort_values(by=['Enrollment'],inplace=True)
        newdf.to_csv(f"Attendance/{Subject}/attendance.csv", index=False)    # Save the combined attendance DataFrame to a CSV file

        # Create a tkinter window to display attendance
        root = tkinter.Tk()
        root.title("Attendance of "+Subject)
        root.configure(background="black")
        cs = f"Attendance/{Subject}/attendance.csv"    # Path to the attendance CSV file
        with open(cs) as file:
            reader = csv.reader(file)
            r = 0

            # Display the attendance data in a tkinter window
            for col in reader:
                c = 0
                for row in col:

                    label = tkinter.Label(
                        root,
                        width=10,
                        height=1,
                        fg="yellow",
                        font=("times", 15, " bold "),
                        bg="black",
                        text=row,
                        relief=tkinter.RIDGE,
                    )
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
        root.mainloop()
        print(newdf)

    subject = Tk()    # Create the main tkinter window for subject selection
    # windo.iconbitmap("AMS.ico")
    subject.title("Subject...")    # Set window title
    subject.geometry("580x320")    # Set window dimensions
    subject.resizable(0, 0)    # Disable window resizing
    subject.configure(background="black")    # Set window background color
    # subject_logo = Image.open("UI_Image/0004.png")
    # subject_logo = subject_logo.resize((50, 47), Image.ANTIALIAS)
    # subject_logo1 = ImageTk.PhotoImage(subject_logo)
    titl = tk.Label(subject, bg="black", relief=RIDGE, bd=10, font=("arial", 30))
    titl.pack(fill=X)
    # l1 = tk.Label(subject, image=subject_logo1, bg="black",)
    # l1.place(x=100, y=10)
    titl = tk.Label(
        subject,
        text="Which Subject of Attendance?",
        bg="black",
        fg="green",
        font=("arial", 25),
    )
    titl.place(x=100, y=12)

    def Attf():    # Define a function to open the folder containing attendance sheets
        sub = tx.get()
        if sub == "":
            t="Please enter the subject name!!!"
            #text_to_speech(t)    # Call text-to-speech function (commented out)
            print(t)
        else:
            os.startfile(
            f"Attendance/{sub}"
            )


    attf = tk.Button(
        subject,
        text="Check Sheets",
        command=Attf,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="yellow",
        height=2,
        width=10,
        relief=RIDGE,
    )
    attf.place(x=360, y=170)

    sub = tk.Label(
        subject,
        text="Enter Subject",
        width=10,
        height=2,
        bg="black",
        fg="yellow",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 15),
    )
    sub.place(x=50, y=100)

    tx = tk.Entry(
        subject,
        width=15,
        bd=5,
        bg="black",
        fg="yellow",
        relief=RIDGE,
        font=("times", 30, "bold"),
    )
    tx.place(x=190, y=100)

    fill_a = tk.Button(
        subject,
        text="View Attendance",
        command=calculate_attendance,
        bd=7,
        font=("times new roman", 15),
        bg="black",
        fg="yellow",
        height=2,
        width=12,
        relief=RIDGE,
    )
    fill_a.place(x=195, y=170)
    subject.mainloop()    # Start the main tkinter event loop for subject selection
