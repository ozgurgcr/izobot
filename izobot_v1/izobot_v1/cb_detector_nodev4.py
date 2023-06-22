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
        super().__init__('cb_detector_nodev4')
        self.cb_coordinate_publisher = self.create_publisher(UInt16MultiArray, 'cb_coordinates', 2)
        self.detected_publisher = self.create_publisher(CompressedImage, 'detected_stream',2)
        self.timer_=self.create_timer(0.01, self.Cb_Publisher_callback)
        self.model = model
        self.bridge = CvBridge()
        self.get_logger().info("wait is started.")
        time.sleep(5)
        self.get_logger().info("wait is stopped.")
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.get_logger().info("Camera stream has been started.")


    def publish_cb_coordinates(self, cb_coordinates):
        self.publisher.publish(cb_coordinates)
        self.get_logger().info("Cb coordinates has been publishing")

 
    def Cb_Publisher_callback(self):
        self.get_logger().info("Cb publisher callback function is called.")
        ret, frame = self.capture.read()
        if ret:
            self.get_logger().info("Video Captured.")
            Detects = self.model(frame)
            #Get the result frame as PIL Image
            self.get_logger().info("Frame Processed by model.")
            #result_PILframe = Detects.render()
            #Convert PIL Image to NumPy array
            #self.get_logger().info("Cb publisher callback function is called3.")
            #result_npFrame = np.array(result_PILframe)
            #Convert NumPy array to CV2 image
            #self.get_logger().info("Cb publisher callback function is called4.")
            #result_cvFrame = cv2.cvtColor(result_npFrame, cv2.COLOR_BGR2RGB)
            #Convert CV2 Image to ROS2 Compressed_Img_msg
            #self.get_logger().info("Cb publisher callback function is called5.")
            result_Img = self.bridge.cv2_to_compressed_imgmsg(cvim=frame, dst_format='jpg')
            #Publish the image to detected_stream so can be view at remote screen
            #self.get_logger().info("Cb publisher callback function is called6.")
            self.detected_publisher.publish(result_Img)
            self.get_logger().info("Frame is published as Detected Stream.")
            # 

            if len(Detects.pandas().xyxy)>0:
                Results_ = Detects.pandas().xyxy[0]     #this code returns a list that has object coordinates, index is the object index,
                print(Results_)
                if not Results_.empty:
                    print("Results:" ,Results_)
                    self.get_logger().info("Cb publisher callback function is called4.")
                    xmin =  Results_.iloc[0,0]               #pandas.core.frame.DataFrame members can be accessed by iloc attribute
                    ymin =  Results_.iloc[0,1]
                    xmax =  Results_.iloc[0,2]
                    ymax =  Results_.iloc[0,3]
                    center_x = xmin + (xmax - xmin)/2
                    center_y = ymin + (ymax - ymin)/2
                    self.get_logger().info("Cb publisher callback function is calledXXX.")
                    cb_coordinates = 1 #[int(center_x), int(center_y)]
                    #cb_coordinates = UInt16MultiArray(data=[cb_coordinates])

                    self.get_logger().info("Cb publisher callback function is called5.") 
                    #self.publish_cb_coordinates(cb_coordinates)
                    self.get_logger().info("Cb publisher callback function is called6.")
                else: 
                    print("Results_ is empty")
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
    cb_detector_nodev4 = CbDetectorNode(model)
    rclpy.spin(cb_detector_nodev4)
    cb_detector_nodev4.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

