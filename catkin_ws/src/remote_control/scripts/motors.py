#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from robot.robot import RobotBot

speed = 90
turn_speed = 60
bot = RobotBot()

def command_callback(twist):
    left_speed = speed * twist.linear.x - turn_speed * twist.angular.z
    right_speed = speed * twist.linear.x + turn_speed * twist.angular.z
    bot.setMotor(left_speed, right_speed)

if __name__ == '__main__':
    print "Starting motor node"
    rospy.init_node('motors')
    rospy.Subscriber('cmd_vel', Twist, command_callback)
    rospy.spin()
