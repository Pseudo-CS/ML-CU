import requests
import cv2
import numpy as np

# define the url of the IP camera
url = "http://192.168.0.6:8080/shot.jpg"

# infinite loop to capture images from the IP camera
while True:
    # send a GET request to the IP camera to capture an image
    cam = requests.get(url)
    # convert the captured image from bytes to a numpy array
    imgNp = np.array(bytearray(cam.content), dtype=np.uint8)
    # decode the numpy array to an image
    img = cv2.imdecode(imgNp, -1)
    # display the captured image in a window
    cv2.imshow("cam", img)
    
    # break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
