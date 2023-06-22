import cv2
from cv_bridge import CvBridge
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from sensor_msgs.msg import Image
import torch
import pandas

class myCameraNode(Node):
    def __init__(self):
        super().__init__('my_camera_node')
        self.publisher = self.create_publisher(CompressedImage, 'my_stream', 1)
        self.timer_=self.create_timer(0.1, self.publish_image)
        self.get_logger().info("Camera stream has been started.")
        self.bridge = CvBridge()
        self.capture = cv2.VideoCapture(0)

    def publish_image(self):
            ret, frame = self.capture.read()
            if ret: 
                # Convert CV2 image to ROS2 Image message
                image_msg = self.bridge.cv2_to_compressed_imgmsg(cvim=frame, dst_format='jpg')
                # 
                # Publish the image message
                self.publisher.publish(image_msg)
                print("stream publishing...")

def main(args=None):
    rclpy.init(args=args)
    image_publisher = myCameraNode()
    rclpy.spin(image_publisher)
    image_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
