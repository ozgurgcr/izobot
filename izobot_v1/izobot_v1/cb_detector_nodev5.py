# 
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from std_msgs.msg import UInt16MultiArray
from sensor_msgs.msg import CompressedImage
import torch
import pandas
import cv2
import numpy as np
import time


class CbDetectorNode(Node):
    def __init__(self,model):
        super().__init__('cb_detector_nodev5')
        self.get_stream_node = self.create_subscription(CompressedImage, "my_stream", self.Cb_detect_callback,1)
        self.subscriptions
        self.cb_coordinate_publisher = self.create_publisher(UInt16MultiArray, 'cb_coordinates', 1)
        self.detected_publisher = self.create_publisher(CompressedImage, 'detected_stream',1)
        self.model = model
        self.bridge = CvBridge()
        self.get_logger().info("Cb detector node has been started.")


    def publish_cb_coordinates(self, cb_coordinates):
        self.get_logger().info("Cb coordinates has been publishing")
        self.cb_coordinate_publisher.publish(cb_coordinates)
        self.get_logger().info("Cb coordinates has been publishing1")

 
    def Cb_detect_callback(self,msg):
        self.get_logger().info("Cb detect callback function is called.")
        frame = self.bridge.compressed_imgmsg_to_cv2(msg)
        Detects = self.model(frame)
        self.get_logger().info("Frame processed by model")
        #Get the result frame as PIL Image
        #result_PILframe = Detects.render()
        #Convert PIL Image to NumPy array
        #self.get_logger().info("Cb publisher callback function is called3.")
        #result_npFrame = np.array(result_PILframe)
        #Convert NumPy array to CV2 image
        #self.get_logger().info("Cb publisher callback function is called4.")
        #result_cvFrame = cv2.cvtColor(result_npFrame, cv2.COLOR_BGR2RGB)
        #Convert CV2 Image to ROS2 Compressed_Img_msg
        #self.get_logger().info("Cb publisher callback function is called5.")
        #result_Img = self.bridge.cv2_to_compressed_imgmsg(cvim=frame, dst_format='jpg')
        #Publish the image to detected_stream so can be view at remote screen
        #self.get_logger().info("Cb publisher callback function is called6.")
        self.detected_publisher.publish(msg)
        self.get_logger().info("Frame is published as Detected Stream.")
        # 

        if len(Detects.pandas().xyxy)>0:
            Results_ = Detects.pandas().xyxy[0]     #this code returns a list that has object coordinates, index is the object index,
            print(Results_)
            if not Results_.empty:
                #print("Results:" ,Results_)
                self.get_logger().info("Cb publisher callback function is called4.")
                xmin =  Results_.iloc[0,0]               #pandas.core.frame.DataFrame members can be accessed by iloc attribute
                ymin =  Results_.iloc[0,1]
                xmax =  Results_.iloc[0,2]
                ymax =  Results_.iloc[0,3]
                center_x = xmin + (xmax - xmin)/2
                center_y = ymin + (ymax - ymin)/2
                self.get_logger().info("Cb publisher callback function is calledXXX.")
                cb_coordinates = UInt16MultiArray()  #[int(center_x), int(center_y)]
                cb_coordinates.data = [int(center_x), int(center_y)]
                print(cb_coordinates)
                #print(type(cb_coordinates))
                self.get_logger().info("Cb publisher callback function is called5.") 
                self.publish_cb_coordinates(cb_coordinates)
                self.get_logger().info("Cb publisher callback function is called6.")
            else: 
                print("Results_ is empty")
                cb_coordinates = UInt16MultiArray()  #[int(center_x), int(center_y)]
                cb_coordinates.data = [0, 0]
                self.publish_cb_coordinates(cb_coordinates)
        else:
            cb_coordinates = "None"
            print("No Cb Detected!")
            self.get_logger().info("Cb publisher callback function is called7.")
            ##############################################################

def main(args=None):
    rclpy.init(args=args)
    model = torch.hub.load('/home/rpi/python_workspace/yolov5/yolov5', 'custom', path='/home/rpi/python_workspace/yolov5/yolov5/best.pt', source = 'local')
    print("Yolov5 model has been loaded")
    model.conf = 0.7
    cb_detector_nodev5 = CbDetectorNode(model)
    rclpy.spin(cb_detector_nodev5)
    cb_detector_nodev5.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

