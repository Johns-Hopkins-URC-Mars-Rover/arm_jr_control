import keyboard
import time
import numpy as np
from robot import Robot
from dynamixel import Dynamixel

follower_dynamixel = Dynamixel.Config(baudrate=1_000_000, device_name='COM5').instantiate()
follower = Robot(follower_dynamixel, servo_ids=[1, 2, 3, 4], auto=True)

keyboard_positions = {'init': [2048, 640, 2048, 2500],
                      'j': [2186, 1070, 1913, 2164],
                      'h': [2293, 1075, 1930, 2163],
                      'u': [2197, 1102, 1967, 2226], 
                      'space': [2639, 1047, 1890, 2155],
                      'r': [2413, 1309, 2257, 2120], 
                      'r_leave': [2393, 1199, 2206, 2119],
                      'c': [2543, 1098, 1949, 2229]}  

def reset_pos(goalPos):
    try:
        while True:
            current_pos = follower.read_position()
            
            atPos = True
            for i in range(4):
                if abs(current_pos[i] - goalPos[i]) > 50:
                    atPos = False
                    break

            if atPos:
                time.sleep(0.2)
                if goalPos == keyboard_positions['r']:
                    return
                follower.set_goal_pos(keyboard_positions['init'])
                time.sleep(2)
                return

            time.sleep(0.05) 

    except KeyboardInterrupt:
        follower._disable_torque()

follower.set_goal_pos(keyboard_positions['init'])

STEP_SIZE = [25, 25, 50, 50]
MIN_POS = 0
MAX_POS = 4096

current_pos = follower.read_position() 
time.sleep(2)

msg = ['j', 'h', 'u', 'space', 'u', 'r', 'r_leave', 'c']

for i in range(len(msg)):
    goalPos = keyboard_positions[msg[i]]
    follower.set_goal_pos(goalPos)
    reset_pos(goalPos)

follower._disable_torque()

