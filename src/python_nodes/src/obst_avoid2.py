#! /usr/bin/env python

import rospy

#import LaserScan data from turtlebot's LaserSensor. Subscribe to LaserScan data to build obstacle avoidance algorithm 
from sensor_msgs.msg import LaserScan

#import Twist to publish messages to turtlebot
from geometry_msgs.msg import Twist 

#define function called 'callback' that receives a parameter named message 
def callback(msg): 
    global move_cmd

#if distance to an obstacle in front of the robot is greater than 1m,robot will move forward

    # no obstacle within 0.5m the turtlebot to move forward by publishing to  linear.x 
    if msg.ranges[0] >0.5:
       move_cmd.linear.x = 0.5
       move_cmd.angular.z = 0.0

    #if there is obstacle detected within 0.5m we command turtlebot to turn by publishing to angular.z 
    else:
       move_cmd.linear.x = 0.0
       move_cmd.angular.z = 0.0 

    pub.publish(move_cmd)

rospy.init_node('obstacle_avoidance',anonymous=True) #create node called obstacle avoidance

#create a subscriber to subscribe to the /scan topic 
sub = rospy.Subscriber('/scan', LaserScan,callback) 

#create publisher to publish to '/cmd_vel_mux/input/teleop'
pub = rospy.Publisher('/cmd_vel_mux/input/teleop',Twist,queue_size=10) 

move_cmd = Twist()

rospy.spin()
