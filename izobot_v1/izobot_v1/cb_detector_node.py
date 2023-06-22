import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import UInt16
from sensor_msgs.msg import CompressedImage
import torch
import cv2

class CBDetectorNode(Node):
    def __init__(self):
        super().__init__('cb_detector_node')
        self.subscription = self.create_subscription(
            CompressedImage,
            'my_stream',
            self.image_callback,
            10)
        self.subscription
        self.publisher = self.create_publisher(UInt16, 'cb_coordinates', 10)
        self.bridge = CvBridge()

    def image_callback(self, msg):
        try:
            cv_image = self.bridge.compressed_imgmsg_to_cv2(msg)
            cb_coordinates = self.detect_cbs_yolov5(cv_image)
            self.publish_cb_coordinates(cb_coordinates)
        except Exception as e:
            self.get_logger().error(f'Error processing image: {str(e)}')

    def detect_cbs_yolov5(self, image):
        # Load the YOLOv5 model
        model = torch.hub.load('/home/rpi/python_workspace/yolov5/yolov5', 'custom', path='/home/rpi/python_workspace/yolov5/yolov5/best.pt', source = 'local')
        model.conf = 0.7
        # Perform object detection
        Detects = model(image)
        if len(Detects.pandas().xyxy)>0:
            Results_ = Detects.pandas().xyxy[0]     #this code returns a list that has object coordinates, index is the object index,

            xmin = Results_.iloc[0,0]               #pandas.core.frame.DataFrame members can be accessed by iloc attribute
            ymin =  Results_.iloc[0,1]
            xmax =  Results_.iloc[0,2]
            ymax =  Results_.iloc[0,3]

            center_x = xmin + (xmax - xmin)/2
            center_y = ymin + (ymax - ymin)/2
            cb_coordinates = [UInt16(center_x), UInt16(center_y)] 

            return cb_coordinates

        else:
            cb_coordinates = "None"
            print("No Cb Detected!")


    def publish_cb_coordinates(self, cb_coordinates):
        msg = UInt16(data=cb_coordinates.flatten().tolist())
        self.publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    cb_detector_node = CBDetectorNode()
    rclpy.spin(cb_detector_node)
    cb_detector_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

