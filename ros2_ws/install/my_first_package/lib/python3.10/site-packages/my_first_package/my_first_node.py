#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

nodeName = 'my_first_node'
info_active_timer = 15

# O nosso nó é definido como uma classe, que herda as caracteristicas da classe Node do rclpy
class MyNode(Node):
    def __init__(self):
        super().__init__(node_name=nodeName) # Super é para pegar funções da classe Node, o parametro que a gente coloca é o nome do nó
        self.get_logger().info(nodeName + " has been started.")
        self.seconds_active = info_active_timer
        self.create_timer(15.0, self.active_timer_callback)

    def active_timer_callback(self):
        second_str = str(self.seconds_active)
        self.get_logger().info(nodeName + " active " + second_str + " seconds ago.")
        self.seconds_active += info_active_timer

def main(args=None):
    rclpy.init(args=args) # Iniciando o nó em ROS2

    node = MyNode()  # Cria o objeto do nó
    rclpy.spin(node) # Mantem o nó ativo até que seja encerrado

    rclpy.shutdown() # Encerrando o nó em ROS2

if __name__ == '__main__':
    main()
