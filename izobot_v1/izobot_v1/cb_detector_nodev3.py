# 
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import UInt16
from sensor_msgs.msg import CompressedImage
import torch
import pandas
import cv2
import numpy as np

class CBDetectorNode(Node):
    def __init__(self):
        super().__init__('cb_detector_nodev3')
        self.publisher = self.create_publisher(UInt16, 'cb_coordinates', 10)
        self.detected_publisher = self.create_publisher(CompressedImage, 'detected_stream',10)
        self.timer_=self.create_timer(0.1, self.image_callback)
        self.bridge = CvBridge()

    def image_callback(self):
        try:
            cb_coordinates = self.detect_cbs_yolov5()
            self.publish_cb_coordinates(cb_coordinates)
        except Exception as e:
            self.get_logger().error(f'Error processing image: {str(e)}')

    def detect_cbs_yolov5(self):
        # Load the YOLOv5 model
        model = torch.hub.load('/home/rpi/python_workspace/yolov5/yolov5', 'custom', path='/home/rpi/python_workspace/yolov5/yolov5/best.pt', source = 'local')
        model.conf = 0.7
        # Perform object detection
        Detects = model(0)
        ##########################13.06.23####################3#####
        #Get the result frame as PIL Image
        result_PILframe = Detects.render()

        #Convert PIL Image to NumPy array
        result_npFrame = np.array(result_PILframe)

        #Convert NumPy array to CV2 image
        result_cvFrame = cv2.cvtColor(result_npFrame, cv2.COLOR_BGR2RGB)

        #Convert CV2 Image to ROS2 Compressed_Img_msg
        result_Img = self.bridge.cv2_to_compressed_imgmsg(cvim=result_cvFrame, dst_format='jpg')

        #Publish the image to detected_stream so can be view at remote screen
        self.detected_publisher.publish(result_Img)

        ##########################13.06.23####################3#####

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
    cb_detector_nodev3 = CBDetectorNode()
    rclpy.spin(cb_detector_nodev3)
    cb_detector_nodev3.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

