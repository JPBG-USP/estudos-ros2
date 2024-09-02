#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import rclpy.publisher
from geometry_msgs.msg import Accel
import random

class data_collection_node(Node):
    def __init__(self, node_name_, topic_name_, time_period_):
        super().__init__(node_name=node_name_) 
        self.data_publisher = self.create_publisher(msg_type=Accel, topic=topic_name_, qos_profile=10)
        self.timer = self.create_timer(timer_period_sec= time_period_, callback=self.publish_data)
        
    def publish_data(self):
        msg = Accel() 
        
        msg.linear.x = random.random()
        msg.linear.y = random.random()
        msg.linear.z = random.random()
        
        msg.angular.x = random.random()
        msg.angular.y = random.random()
        msg.angular.z = random.random()
        
        self.data_publisher.publish(msg=msg)
        self.get_logger().info(f'Published: linear=({msg.linear.x}, {msg.linear.y}, {msg.linear.z}), '
                               f'angular=({msg.angular.x}, {msg.angular.y}, {msg.angular.z})')


def main(args=None):
    rclpy.init(args=args)
    node = data_collection_node('no_acelerometro', 'topico_acelerometro', 0.5)
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
