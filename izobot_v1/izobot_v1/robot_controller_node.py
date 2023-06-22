import rclpy
from rclpy.node import Node
from std_msgs.msg import UInt16MultiArray
from geometry_msgs.msg import Twist
import math
import random
import time

class RobotControllerNode(Node):
    def __init__(self):
        super().__init__('robot_controller_node')
        self.subscription = self.create_subscription(
            UInt16MultiArray,
            'cb_coordinates',
            self.cb_coordinates_callback,
            10)
        self.subscription
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 1)
        self.get_logger().info("Robot Controller Node has been started.")
        # Create a Twist message to control the robot's movement
        self.twist_msg = Twist()
        self.target_x = 0.0
        self.target_y = 0.0
        
    def cb_coordinates_callback(self, msg):
        # Get the first CB coordinates from the message
        self.target_x = msg.data[0]
        self.target_y = msg.data[1]
        self.move_robot()

    def turn_right(self):
        self.twist_msg.angular.z = -2.0            # saga don 
        self.twist_msg.linear.x = 0.0
        print("Turning right...")
    def turn_left(self):
        self.twist_msg.angular.z = 2.0             # sola don
        self.twist_msg.linear.x = 0.0 
        print("Turning left...")
        
    def move_forward(self): 
        self.twist_msg.linear.x = -2.0              # ileri git 
        self.twist_msg.angular.z = 0.0
        print("Moving forward...")

 
    def move_robot(self):
        # Calculate the difference between the robot and target positions
        
        dx = self.target_x
        dy = self.target_y
        
        #eğer x ve y 0 olarak iletildiyse izmarit tespit edilememiştir. otonom hareket etmelidir.
        if dx == 0 and dy == 0:
            # List of functions
            functions = [self.turn_right, self.turn_left, self.move_forward]

            # Generate a random function caller
            random_function = random.choice(functions)

            # Call the random function
            random_function()
        else:
            if dx > 450:
                self.turn_right()
            if 0 < dx < 150:
                self.turn_left()
            if 0 < dy < 350:
                self.move_forward()
            if 400 > dy > 200:
                self.twist_msg.linear.x = -1.0              # az ileri git
                self.twist_msg.angular.z = 0.0 
                print("CB is close...")
            if 150 < dx < 450 and dy > 400:
                print("CB is here!!!")
                self.twist_msg.linear.x = -3.0
                self.twist_msg.angular.z = 0.0
        # Publish the Twist message to control the robot
        self.publisher.publish(self.twist_msg)

    

def main(args=None):
    rclpy.init(args=args)
    robot_controller_node = RobotControllerNode()
    rclpy.spin(robot_controller_node)
    robot_controller_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
