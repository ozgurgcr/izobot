import rclpy
from rclpy.node import Node
import RPi.GPIO as GPIO 
from time import sleep
from geometry_msgs.msg import Twist


class VelocitySubscriber(Node):

    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.subscription = self.create_subscription(Twist,'turtle1/cmd_vel',self.cmd_to_pwm_callback,1)
        self.right_motor_a = 24
        self.right_motor_b = 23 
        self.right_motor_en = 25

        self.left_motor_a = 15 
        self.left_motor_b = 14
        self.left_motor_en = 4 

        GPIO.setmode(GPIO.BCM) 
        GPIO.setup(self.right_motor_a , GPIO.OUT)
        GPIO.setup(self.right_motor_b , GPIO.OUT)
        GPIO.setup(self.right_motor_en , GPIO.OUT)

        GPIO.setup(self.left_motor_a , GPIO.OUT)
        GPIO.setup(self.left_motor_b , GPIO.OUT)
        GPIO.setup(self.left_motor_en , GPIO.OUT) 

        self.pwm_r=GPIO.PWM(self.right_motor_en , 1000)
        self.pwm_l=GPIO.PWM(self.left_motor_en , 1000)

        self.pwm_r.start(50)
        self.pwm_l.start(50)
        
    # Robot Control can be made as if the linear.x > 0 go forward 
    #                               if the linear.x < 0 go back
    #                               if the angular.z > 0 turn right 
    #                               if the angular.z < 0 turn left 
    #
    # eğer msg.linear.x = 1 ise az ileri gitmelidir. 

    def cmd_to_pwm_callback(self, msg):
        if msg.linear.x == -1.0:

            right_wheel_vel = (msg.linear.x + msg.angular.z)/2
            left_wheel_vel = (msg.linear.x - msg.angular.z)/2

            print(left_wheel_vel ," / ", right_wheel_vel )
            # if right_wheel_vel > 0.50 and left_wheel_vel > 0.50 :
            #     self.pwm_r.ChangeDutyCycle(75)
            #     self.pwm_l.ChangeDutyCycle(75)
         
            GPIO.output(self.right_motor_a ,right_wheel_vel > 0 )
            GPIO.output(self.right_motor_b ,right_wheel_vel < 0 )
            GPIO.output(self.left_motor_a , left_wheel_vel > 0)
            GPIO.output(self.left_motor_b , left_wheel_vel < 0)
            sleep(0.2)
            GPIO.output(self.right_motor_a , 0 )
            GPIO.output(self.right_motor_b , 0 )
            GPIO.output(self.left_motor_a  , 0 )
            GPIO.output(self.left_motor_b  , 0 )
            sleep(1)
        elif msg.linear.x == -3.0:
            GPIO.output(self.right_motor_a , 0 )
            GPIO.output(self.right_motor_b , 0 )
            GPIO.output(self.left_motor_a  , 0 )
            GPIO.output(self.left_motor_b  , 0 )
            sleep(5)
        else: 
            right_wheel_vel = (msg.linear.x + msg.angular.z)/2
            left_wheel_vel = (msg.linear.x - msg.angular.z)/2

            print(left_wheel_vel ," / ", right_wheel_vel )
            # if right_wheel_vel > 0.50 and left_wheel_vel > 0.50 :
            #     self.pwm_r.ChangeDutyCycle(75)
            #     self.pwm_l.ChangeDutyCycle(75)
         
            GPIO.output(self.right_motor_a ,right_wheel_vel > 0 )
            GPIO.output(self.right_motor_b ,right_wheel_vel < 0 )
            GPIO.output(self.left_motor_a , left_wheel_vel > 0)
            GPIO.output(self.left_motor_b , left_wheel_vel < 0)
            sleep(0.5)
            GPIO.output(self.right_motor_a , 0 )
            GPIO.output(self.right_motor_b , 0 )
            GPIO.output(self.left_motor_a  , 0 )
            GPIO.output(self.left_motor_b  , 0 )
            sleep(2)
        

def main(args=None):
    rclpy.init(args=args)

    velocity_subscriber = VelocitySubscriber()
    rclpy.spin(velocity_subscriber)
    velocity_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()