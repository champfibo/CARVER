#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String
class RobotNewStation(Node):
    
    def __init__(self):
        super().__init__("robot_new_station")

        self.publisher_ = self.create_publisher(String,"robot_news",10)
        self.timer_ = self.create_timer(0.5,self.publish_news)
        self.get_logger().info("Robot new station has been start")
    
    def publish_news(self):
        msg = String()
        msg.data ="Hello"   
        self.publisher_.publish(msg)     
        

def main(args=None):            
    rclpy.init(args=args)           #initialize Ros2 communications
    node = RobotNewStation()    # name of node
    
    rclpy.spin(node)  # run alway stop when ctrl+c
    rclpy.shutdown()

if __name__== "__main__":
        main()