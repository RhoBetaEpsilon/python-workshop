#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int16
from random import randint

class Messenger:
    def __init__(self):
        '''Initialize the ROS node with name messenger'''

        '''Create a publisher for an Int16 message on topic sensor'''
        self.sensor = 0

        rospy.sleep(1)

    def run(self):
        '''Update the sensor reading with a random integer between 0 and 100'''
        '''Print the value to the terminal and publish it to the sensor topic'''
        '''Delay 2 seconds and repeat the above 10 times'''

if __name__ == '__main__':
    Messenger().run()