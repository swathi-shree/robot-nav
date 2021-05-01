#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    print('s1[0]')
    print msg.ranges[0]
	
    print('s2[90]')
    print msg.ranges[90]

    print('s3[100]') 
    print msg.ranges[100]

    print('s4[270]')
    print msg.ranges[270]
	
    print('s5[359]')
    print msg.ranges[359]
 
rospy.init_node('laser_data') #initiate node called laser_data 
sub = rospy.Subscriber('scan',LaserScan,callback) #create a subscriber to the the laser /scan topic 
rospy.spin()
