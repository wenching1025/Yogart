import cv2
from chair_pose import generate_framesD
from downward_facing_dog import generate_frameC
from full_boat_pose import generate_framesI
from half_moon_pose import generate_framesH
from happy_baby_pose import generate_framesJ
import mediapipe as mp
import threading
from flask import Flask, render_template, Response
from flask_socketio import SocketIO
from threading import Thread, Lock
from mountain_pose import generate_framesE
from tree_pose import generate_framesF
from triangle_pose import generate_framesG
from warrior_II_pose import generate_framesB
from warrior_I_pose import*
# from detect import *

app = Flask(__name__, static_url_path='/static')
socketio = SocketIO(app)

mp_drawing = mp.solutions.drawing_utils
detection_lock = Lock()
detection_ongoing = False

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.3, model_complexity=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/warrior_I_pose')
def run_warrior_I_pose():
    generate_framesA()
    return "Pose detection started."

@app.route('/warrior_II_pose')
def run_warrior_II_pose():
    generate_framesB()
    return "Pose detection started."

@app.route('/downward_facing_dog')
def run_downward_facing_dog():
    generate_frameC()
    return "Pose detection started."

@app.route('/chair_pose')
def run_chair_pose():
    generate_framesD()
    return "Pose detection started."

@app.route('/mountain_pose')
def run_mountain_pose():
    generate_framesE()
    return "Pose detection started."

@app.route('/tree_pose')
def run_tree_pose():
    generate_framesF()
    return "Pose detection started."

@app.route('/triangle_pose')
def run_triangle_pose():
    generate_framesG()
    return "Pose detection started."

@app.route('/half_moon_pose')
def run_half_moon_pose():
    generate_framesH()
    return "Pose detection started."

@app.route('/full_boat_pose')
def run_full_boat_pose():
    generate_framesI()
    return "Pose detection started."

@app.route('/happy_baby_pose')
def run_happy_baby_pose():
    generate_framesJ()
    return "Pose detection started."

# @app.route('/yolo')
# def run_yolo():
#     run()
#     return "started."

if __name__ == "__main__":
    app.run(debug=True)