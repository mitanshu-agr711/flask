from flask import Flask,render_template,redirect
import cv2

app=Flask(__name__)
camera=cv2.VideoCapture(0)  # 0 is the camera index  number

@app.route('/')
def index():
    return render_template('index.html')