#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    
    def __init__(self):
        super().__init__("py_test")
        self.get_logger().info("Hello 123456789101111110") 
        self.counter_ = 0
        self.create_timer(0.5, self.timer_callback)
    
    def timer_callback(self):
        self.counter_ +=1
        self.get_logger().info("Hello2 " + str(self.counter_)) 

def main(args=None):            
    rclpy.init(args=args)           #initialize Ros2 communications
    node = MyNode()    # name of node
    #  node.get_logger().info("Hello")    # print
    rclpy.spin(node)  # run alway stop when ctrl+c
    rclpy.shutdown()

if __name__== "__main__":
        main()