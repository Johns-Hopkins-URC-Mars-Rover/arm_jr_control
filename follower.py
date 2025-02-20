import csv

import keyboard
import time
import numpy as np
from robot import Robot
from dynamixel import Dynamixel


follower_dynamixel = Dynamixel.Config(baudrate=1_000_000, device_name='COM5').instantiate()
follower = Robot(follower_dynamixel, servo_ids=[1, 2, 3, 4, 6])

file = open('leader_positions.csv', 'r', newline='')
reader = csv.reader(file)

try:
    for row in reader:
        pos = [int(i) for i in row]
        follower.set_goal_pos(pos)
        time.sleep(0.05)
        print(follower.read_position())
    raise SystemExit
except KeyboardInterrupt and SystemExit:
    time.sleep(2)
    follower._disable_torque()