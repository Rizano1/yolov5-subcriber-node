#!/usr/bin/env python3

import rospy 
from std_msgs.msg import String

def fungsi_callback(pesan):
    if pesan.data == "kanan":
        rospy.loginfo("belok kanan")
    elif pesan.data == "kiri":
        rospy.loginfo("belol kiri")
    else:
        rospy.loginfo("lurus")


def fungsi_dengar():
    rospy.init_node('sub_node', anonymous=False)
    rospy.Subscriber('yolo_topic', String, fungsi_callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        fungsi_dengar()
    except rospy.ROSInterruptException:
        pass