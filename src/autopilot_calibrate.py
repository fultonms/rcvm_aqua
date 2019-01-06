#! /usr/bin/python

import sys, math, threading
from time import sleep
from math import pi

import rospy

from aquacore.msg import AutopilotModes
from rcvm_pilot_client import RCVMPilotClient

params = {}
#params['mode'] = AutopilotModes.AP_GLOBAL_ANGLES_FIXED_DEPTH
params['mode'] = AutopilotModes.AP_GLOBAL_ANGLES_LOCAL_THRUST
pc = RCVMPilotClient(params)


#Straight motion
d = pc.current_depth

rads = pc.get_rpy_of_imu_in_global()
degs = (rads[0] * 180/pi, rads[1] * 180/pi, rads[2] * 180/pi)
pc.do_straight_line(2, degs, d, 0.3, 0)
pc.do_straight_line(2, degs, d, 0.3, 0.2)

#Depth change
pc.do_relative_depth_change(1, 0, 0.1)

#Global angles
pc.goto_target_orientation([0,0,0], 1, 0,0)
pc.goto_target_orientation([90,90,90], 1, 0, 0)
pc.goto_target_orientation([0,0,0], 1, 0, 0)

#Relative angles
pc.do_relative_angle_change([45,0,0], pc.current_depth, 0, 0)
pc.do_relative_angle_change([-90,0,0], pc.current_depth, 0, 0)
pc.do_relative_angle_change([45,0,0], pc.current_depth, 0, 0)

pc.do_relative_angle_change([0, 45,0], pc.current_depth, 0, 0)
pc.do_relative_angle_change([0, -90,0], pc.current_depth, 0, 0)
pc.do_relative_angle_change([0, 45,0], pc.current_depth, 0, 0)

pc.do_relative_angle_change([0, 0, 45], pc.current_depth, 0, 0)
pc.do_relative_angle_change([0,0,-90], pc.current_depth, 0, 0)
pc.do_relative_angle_change([0,0,45], pc.current_depth, 0, 0)



