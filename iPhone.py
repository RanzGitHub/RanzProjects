import cv2
import tkinter as tk
import time as iTime
from datetime import datetime
from tkinter import * #imports all tkinter packages
from PIL import Image, ImageTk
iCam = cv2.VideoCapture(0)
Screen = tk.Tk(className="iPhone")
now = datetime.now()
text = Text(Screen)
photo = PhotoImage(file = "applelogo2007.png")
Screen.iconphoto(False, photo)
Screen.geometry("320x480")
Earth = Image.open('Earth.jpg')
Earth_img = ImageTk.PhotoImage(Earth)
label = tk.Label(Screen, text="iPhone", image=Earth_img)
label.config(fg="#FFFFFF")
label.pack()
#text.insert(INSERT, now.strftime('%I:%M'))
#text.pack()
Screen.mainloop()
#while iCam.isOpened():
    #ret, camera = iCam.read()
    #cv2.imshow("Camera", camera