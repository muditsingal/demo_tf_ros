#!/usr/bin/env python3
import roslib
roslib.load_manifest('demo_tf1')
import math

import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('fixed_tf_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        t = rospy.Time.now().to_sec() * math.pi
        br.sendTransform((2.0*math.cos(t), 2.0*math.sin(t), 0.0),
                         (0.0, 0.0, 0.0, 1.0),
                         rospy.Time.now(),
                         "moving_frame1",
                         "turtle1")
        rate.sleep()
