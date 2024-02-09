# import necessary libraries
import csv
import os, cv2
import numpy as np
import pandas as pd
import datetime
import time



# take Image of user
def TakeImage(l1, l2, haarcasecade_path, trainimage_path, message, err_screen): 
    """
    Function to take image of user.
    Parameters:
    l1 (str): Enrollment Number of the user.
    l2 (str): Name of the user.
    haarcasecade_path (str): Path to the Haar Cascade classifier.
    trainimage_path (str): Path to save the training images.
    message (tkinter.Label): Label to display the message.
    err_screen (tkinter.Label): Label to display the error message.
    """    
    # check if both fields are empty
    if (l1 == "") and (l2==""):
        t='Please Enter the your Enrollment Number and Name.'
        print(t)
    # check if Enrollment Number field is empty
    elif l1=='':
        t='Please Enter the your Enrollment Number.'
        print(t)
    # check if Name field is empty
    elif l2 == "":
        t='Please Enter the your Name.'
        print(t)
    else:
        try:
            # initialize the camera and Haar Cascade classifier
            cam = cv2.VideoCapture(0)
            detector = cv2.CascadeClassifier(haarcasecade_path)
            # get the Enrollment Number and Name
            Enrollment = l1
            Name = l2
            # initialize the sample number and create a directory for the images
            sampleNum = 0
            total = 0
            directory = Enrollment + "_" + Name
            path = os.path.join(trainimage_path, directory)
            print(path)
            os.mkdir(path)
            # capture the images
            while True:
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    sampleNum = sampleNum + 1
                    total = total + 1
                    cv2.imwrite(
                        f"{path}/ "
                        + Name
                        + "_"
                        + Enrollment
                        + "_"
                        + str(total)
                        + ".jpg",
                        gray[y : y + h, x : x + w],
                    )
                    cv2.imshow("Frame", img)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
                elif sampleNum == 35:
                    print('change angle')
                    sampleNum = 0
                    time.sleep(5)
                elif total > 100: #increase sample size from 50 to 100
                    break
            cam.release()
            cv2.destroyAllWindows()
            # save the Enrollment Number and Name in the csv file
            row = [Enrollment, Name]
            with open(
                "StudentDetails/studentdetails.csv",
                "a+",
            ) as csvFile:
                writer = csv.writer(csvFile, delimiter=",")
                writer.writerow(row)
                csvFile.close()
            # display the message
            res = "Images Saved for ER No:" + Enrollment + " Name:" + Name
            message.configure(text=res)
            print(res)
        except FileExistsError as F:
            F = "Student Data already exists"
            print(F)
