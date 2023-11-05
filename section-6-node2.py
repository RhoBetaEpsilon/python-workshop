#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int16

class Receiver:
    def __init__(self):
        '''Initialize the ROS node with name receiver'''

        '''Create a subscriber to topic sensor that listens for Int16 messages and sends them to handle_msg'''
        self.sensor = 0

        rospy.sleep(1)

    def handle_msg(self, msg: Int16):
        '''
        If the reading is above 50, let the user know the readins high.
        Otherwise, let the user know the reading is normal.
        '''
    
    def run(self):
        rospy.spin()

if __name__ == '__main__':
    Receiver().run()