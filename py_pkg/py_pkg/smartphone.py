#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class SmartphoneNode(Node):
    
    def __init__(self):
        super().__init__("smartphone")

        self.subscriber_ = self.create_subscription(String,"robot_news", self.callback_robot_news,10)
        
        self.get_logger().info("Smartphone has been start")
    
    def callback_robot_news(self,msg):
        self.get_logger().info(msg.data)
    
          
        

def main(args=None):            
    rclpy.init(args=args)           #initialize Ros2 communications
    node = SmartphoneNode()    # name of node
    
    rclpy.spin(node)  # run alway stop when ctrl+c
    rclpy.shutdown()

if __name__== "__main__":
        main()