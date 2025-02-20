import csv

import keyboard
import time
import numpy as np
from robot import Robot
from dynamixel import Dynamixel


leader_dynamixel = Dynamixel.Config(baudrate=1_000_000, device_name='COM5').instantiate()
leader = Robot(leader_dynamixel, servo_ids=[1, 2, 3, 4, 6])


csvfile = open('leader_positions.csv', 'w', newline='')
writer = csv.writer(csvfile)

try:
    while True:
        writer.writerow(leader.read_position())
        time.sleep(0.05)
except KeyboardInterrupt:
    pass