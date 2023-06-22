#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node 
from sensor_msgs.msg import Image
from sensor_msgs.msg import CompressedImage
import cv2 
from cv_bridge import CvBridge


class displayVideoNode(Node):
    def __init__(self):
        super().__init__("display_detected_stream_node")
        self.display_video_node = self.create_subscription(CompressedImage, "detected_stream", self.display_callback, 2)
        self.subscriptions
        self.bridge=CvBridge()
        self.get_logger().info("Display stream has been started.")

    def display_callback(self, msg):
        frame = self.bridge.compressed_imgmsg_to_cv2(msg)
        # Display the frame using OpenCV
        cv2.imshow('CB Detected Video Stream', frame)
        cv2.waitKey(1)

def main(args = None):
    rclpy.init(args=args)
    node=displayVideoNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
