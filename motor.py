import keyboard
import time
import numpy as np
from robot import Robot
from dynamixel import Dynamixel


follower_dynamixel = Dynamixel.Config(baudrate=1_000_000, device_name='COM5').instantiate()
follower = Robot(follower_dynamixel, servo_ids=[1, 2, 3, 4])

goalPos = [2048, 1024, 2400, 3000]
follower.set_goal_pos(goalPos)

STEP_SIZE = [25, 25, 50, 50]
MIN_POS = 0
MAX_POS = 4096

current_pos = follower.read_position() 
time.sleep(2)
print(current_pos)

try:
    while True:
        if keyboard.is_pressed("q"):
            current_pos[0] = current_pos[0] + STEP_SIZE[0]
            follower.set_goal_pos(current_pos)
        elif keyboard.is_pressed("a"):
            current_pos[0] = current_pos[0] - STEP_SIZE[0]
            follower.set_goal_pos(current_pos)
        if keyboard.is_pressed("s"):
            current_pos[1] = current_pos[1] + STEP_SIZE[1]
            follower.set_goal_pos(current_pos)
        elif keyboard.is_pressed("w"):
            current_pos[1] = current_pos[1] - STEP_SIZE[1]
            follower.set_goal_pos(current_pos)
        if keyboard.is_pressed("e"):
            current_pos[2] = current_pos[2] + STEP_SIZE[2]
            follower.set_goal_pos(current_pos)
        elif keyboard.is_pressed("d"):
            current_pos[2] = current_pos[2] - STEP_SIZE[2]
            follower.set_goal_pos(current_pos)
        if keyboard.is_pressed("r"):
            current_pos[3] = current_pos[3] + STEP_SIZE[3]
            follower.set_goal_pos(current_pos)
        elif keyboard.is_pressed("f"):
            current_pos[3] = current_pos[3] - STEP_SIZE[3]
            follower.set_goal_pos(current_pos)
        if keyboard.is_pressed("esc"):
            raise KeyboardInterrupt

        time.sleep(0.05) 

except KeyboardInterrupt:
    follower._disable_torque()