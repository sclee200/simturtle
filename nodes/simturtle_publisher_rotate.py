import rospy
from geometry_msgs.msg import Twist



rospy.init_node('simturtle_pub_rotate')
pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(100)
twist = Twist()

# twist.angular.z = 3.14
# relative =3.14
current = 0
speed = 40
angle = 180
angular_speed = speed*2*3.14/360
relative_angle = angle*2*3.14/360

time0 = rospy.Time.now().to_sec()
twist.angular.z = angular_speed
while current < relative_angle:
    # rate.sleep()
    pub.publish(twist)
    time1 = rospy.Time.now().to_sec()
    # current = current*(time1-time0)
    current = angular_speed*(time1-time0)

    print('timediff :', (time1-time0), 'current : ',current, 'relative :', relative_angle)

twist.angular.z = 0.0