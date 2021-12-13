#! /usr/bin/env python
from traceback import extract_stack
import rospy
from geometry_msgs.msg import Twist
import cv2

def intialize(msg):
    msg.linear.x=0.0
    msg.linear.y=0.0
    msg.linear.z=0.0
    msg.angular.x=0.0
    msg.angular.y=0.0
    msg.angular.z=0.0
if __name__ == '__main__':
    rospy.init_node('sumturtle_publisher')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    msg = Twist()
    # rate = rospy.Rate(100)
    intialize(msg)

    distance = 1
    cur_dist =0
    speed = 1

    # msg.linear.x =distance
    eita = 0.2
    cap = cv2.VideoCapture(0)
    while not rospy.is_shutdown() and cap.isOpened():
        # time0 = rospy.Time.now().to_sec()
        cur_dist =0
        while cur_dist < distance:#pro
            msg.linear.x=distance
            pub.publish(msg)
            # time1 = rospy.Time.now().to_sec()
            cur_dist += speed*eita
            print(cur_dist)
        intialize(msg)
        pub.publish(msg)
    
        # time0 = rospy.Time.now().to_sec()
        cur_dist =0        
        while cur_dist < distance:#back
            msg.linear.x=-distance
            pub.publish(msg)
            # time1 = rospy.Time.now().to_sec()
            cur_dist += speed*eita
            print(cur_dist)
        intialize(msg)
        pub.publish(msg)

        # time0 = rospy.Time.now().to_sec()
        cur_dist =0        
        while cur_dist < distance:#up
            msg.linear.y=distance
            pub.publish(msg)
            # time1 = rospy.Time.now().to_sec()
            cur_dist += speed*eita
            print(cur_dist)
        intialize(msg)
        pub.publish(msg)

        # time0 = rospy.Time.now().to_sec()
        cur_dist =0        
        while cur_dist < distance:#down
            msg.linear.y=-distance
            pub.publish(msg)
            # time1 = rospy.Time.now().to_sec()
            cur_dist += speed*eita
            print(cur_dist)
        intialize(msg)
        pub.publish(msg)
    
    # rate.sleep()
    
    # msg.linear.x=-5.0
    # pub.publish(msg)
    
    # rate.sleep()


    # while not rospy.is_shutdown():
    #     str = "hello publisher : %s " % rospy.get_time()
    #     pub.publish(str)
    #     rate.sleep()
    # pass