#!/usr/bin/env python3

########## FILL HERE ##########
# NAME & SURNAME:
# STUDENT ID:
###############################

########## DO NOT EDIT THESE LIBRARIES ##########
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
#################################################

########## ADD YOUR LIBRARIES HERE ##########

###########################################

class TurtleCleaner(Node):
    def __init__(self, points):
        """
            Cleans the given area with the turtle

            Parameters:
                points (list): List of points that define the area
            Returns:
                None
        """

        ########## DO NOT EDIT ANYTHING HERE ##########
        # Initialize the node
        super().__init__('turtle_cleaner')
        self.area = points

        # Create the Twist publisher and Pose subscriber
        self.twist_publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.turtle_pose_sub_ = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.turtle_pose_sub_
        ###############################################

        ########## ADD YOUR CODE HERE ##########
        pass
        ########################################

    def pose_callback(self, msg):
        """
            Callback function for the Pose subscriber.

            Parameters:
                msg (Pose): Current turtle pose
            Returns:
                None
        """
        ########## ADD YOUR CODE HERE ##########
        pass
        ########################################

    def move(self, distance, speed, isForward):
        """
            Moves the turtle with the given speed for the given distance

            Parameters: 
                distance (float): Distance to move
                speed (float): Speed to move
                isForward (bool): Direction of the movement (True: Forward, False: Backward)

            Returns:
                None
        """
        ########## ADD YOUR CODE HERE ##########
        pass
        ########################################

    def rotate(self, angle, speed, isClockwise):
        """
            Rotates the turtle with the given speed for the given angle

            Parameters:
                angle (float): Angle to rotate in degrees
                speed (float): Speed to rotate
                isClockwise (bool): Direction of the rotation (True: Clockwise, False: Counter Clockwise)

        """
        ########## ADD YOUR CODE HERE ##########
        pass
        ########################################

    def go_to_a_goal(self, point, linear_speed, angular_speed):
        """
            Moves the turtle to the given point with the given speeds

            Parameters:
                point (list): Point to go
                linear_speed (float): Speed to move
                angular_speed (float): Speed to rotate in degrees

            Returns:
                None
        """
        ########## ADD YOUR CODE HERE ##########
        pass
        ########################################
    
    ########## YOU CAN ADD YOUR FUNCTIONS HERE ##########
    pass
    #####################################################


########## DO NOT EDIT ANYTHING BELOW THIS LINE ##########
def main(args=None):
    rclpy.init(args=args)
    points =[[7.0, 7.0], [7.0, 4.0], [4.0, 4.0], [4.0, 7.0]]
    turtle_cleaner = TurtleCleaner(points)
    rclpy.spin(turtle_cleaner)
    rclpy.shutdown()

if __name__ == '__main__':
    main()