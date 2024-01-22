#!/usr/bin/env python3

########## FILL HERE ##########
# NAME & SURNAME:Ekin Tasyurek
# STUDENT ID:150190108
###############################

########## DO NOT EDIT THESE LIBRARIES ##########
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
#################################################

########## ADD YOUR LIBRARIES HERE ##########
from math import pow, atan2, sqrt, pi

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

        self.pose = Pose()
        self.rate = rclpy.create_rate(10)
        self.clean_area(points)

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

        self.pose = msg

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

        twist = Twist()

        #We are checking if the movement is forward or backwards
        if(isForward):
            twist.linear.x = abs(speed)
        else:
            twist.linear.x = -abs(speed)

        #Since we only work on x-axis, the other axes are set to 0. Also, there's no turning so angular components are also set to 0.
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = 0

        initial_x = self.pose.x
        current_distance = 0

        #Using a loop, we move the turtle
        while current_distance < abs(distance):
            self.twist_publisher_.publish(twist)
            current_distance = abs(self.pose.x - initial_x)

        #After the loop, the robot is stopped
        twist.linear.x = 0 
        self.twist_publisher_.publish(twist)

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

        twist = Twist()

        #We convert the angle to radian and speed to angular speed.
        angular_speed = speed*2*pi/360
        relative_angle = angle*2*pi/360

         #Since we only work angular components, linear components are set to 0.
        twist.linear.x=0
        twist.linear.y=0
        twist.linear.z=0
        twist.angular.x = 0
        twist.angular.y = 0

        # Checking if our movement is clockwise or counter clockwise
        if isClockwise:
            twist.angular.z = -abs(angular_speed)
        else:
            twist.angular.z = abs(angular_speed)

        initial_angle = self.pose.theta
        current_angle = 0

        #Using a loop, we rotate the turtle
        while current_angle < abs(relative_angle):
            self.twist_publisher_.publish(twist)
            current_angle = abs(self.pose.theta - initial_angle)

        #After the loop, the robot is stopped
        twist.angular.z = 0
        self.twist_publisher_.publish(twist)

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

        twist = Twist()

        while self.euclidean_distance(point) >= 0.01:

            # Linear velocity in the x-axis.
            twist.linear.x = self.linear_vel(point, linear_speed)
            twist.linear.y = 0
            twist.linear.z = 0

            # Angular velocity in the z-axis.
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = self.angular_vel(point, angular_speed)

            self.twist_publisher_.publish(twist)
            self.rate.sleep()

        #After the movement, the robot is stopped
        twist.linear.x = 0
        twist.angular.z = 0
        self.twist_publisher_.publish(twist)

        pass
        ########################################

    ########## YOU CAN ADD YOUR FUNCTIONS HERE ##########

    def euclidean_distance(self, point):
        return sqrt(pow((point.x - self.pose.x), 2) +
                    pow((point.y - self.pose.y), 2))

    def linear_vel(self, point, linear_speed):
        return linear_speed * self.euclidean_distance(point)

    def steering_angle(self, point):
        return atan2(point.y - self.pose.y, point.x - self.pose.x)

    def angular_vel(self, point, angular_speed):
        return angular_speed * (self.steering_angle(point) - self.pose.theta)

    def clean_area(self, points):
        # The area is divided into grids, then each area is cleaned 
        # Grid boundaries are determined based on the given points
        grid_start = [min(p[0] for p in points), min(p[1] for p in points)]
        grid_end = [max(p[0] for p in points), max(p[1] for p in points)]
       
        cell_size = 0.5
        linear_speed = 5.0  
        angular_speed = 5.0 

        #We use 2 for loops to move inside the grid and visit each cell
        for x in range(int(grid_start[0] / cell_size), int(grid_end[0] / cell_size)):
            for y in range(int(grid_start[1] / cell_size), int(grid_end[1] / cell_size)):

                #We calculate the point which we want the robot to go to 
                goal_point = Pose()
                goal_point.x = x * cell_size
                goal_point.y = y * cell_size

                # We use go_to_a_goal function to move the robot
                self.go_to_a_goal(goal_point, linear_speed, angular_speed)
        pass

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