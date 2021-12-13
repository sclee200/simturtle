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

def rotateControl(pub, msg, angle):
    current = 0
    speed = angle
    angle = 180
    angular_speed = speed*2*3.14/360
    relative_angle = angle*2*3.14/360

    time0 = rospy.Time.now().to_sec()
    msg.angular.z = angular_speed
    while current < relative_angle:
        # rate.sleep()
        pub.publish(msg)
        time1 = rospy.Time.now().to_sec()
        # current = current*(time1-time0)
        current = angular_speed*(time1-time0)

        print('timediff :', (time1-time0), 'current : ',current, 'relative :', relative_angle)

    msg.angular.z = 0.0

def keyControl(pub, msg):
    key=cv2.waitKeyEx(1)
    if key > -1:
        print('key : ', key)
   
    # key = input('please input command')   

    if key ==ord("l"):
        
        intialize(msg)
        msg.linear.x=1
        pub.publish(msg)
    if key ==ord("j"):
        
        intialize(msg)
        msg.linear.x=-1
        pub.publish(msg)
    elif key == ord("i"):
        intialize(msg)
        msg.linear.y=1
        pub.publish(msg)
    elif key == ord("k"):
        intialize(msg)
        msg.linear.y=-1
        pub.publish(msg)
    elif key == ord("a"):
        intialize(msg)
        rotateControl(pub, msg, 40)
    return key

img = cv2.imread('./flying-drone.jpg')  

if __name__ == '__main__':
    rospy.init_node('sumturtle_publisher')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    msg = Twist()
     
 
    while not rospy.is_shutdown():
        cv2.imshow('flying drone',img)
        key= keyControl(pub, msg)  
        if key == ord('q'):
            break
  
cv2.destroyAllWindows()