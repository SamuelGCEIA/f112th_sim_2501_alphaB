#!/usr/bin/env python3
import rclpy 
from rclpy.node import Node
import xacro
import os
import xml.etree.ElementTree as ET
from sensor_msgs.msg import LaserScan

class LdrCntrl(Node):
    def __init__(self):
        super().__init__("ldr_cntrl_listener")
        self.subscription = self.create_subscription(LaserScan, "/scan", self.ldr_callback, 10)
        self.subscription

    def ldr_callback(self, msg):
        min_range = min(msg.ranges)
        self.get_logger().info(f"Min range: {min_range:.2f} m")

def main(args=None):
    rclpy.init(args=args)
    node = LdrCntrl()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()