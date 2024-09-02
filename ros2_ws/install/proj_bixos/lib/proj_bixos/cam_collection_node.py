#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class Camera_node(Node):
    def __init__(self, node_name_, topic_name_, timer_period_, video_capture):
        super().__init__(node_name=node_name_)
        self.cam_publisher = self.create_publisher(msg_type=Image, topic=topic_name_, qos_profile=10)
        self.cap = cv2.VideoCapture(video_capture)
        self.bridge = CvBridge()
        self.timer = self.create_timer(timer_period_, self.cam_publish_func)

        if not self.cap.isOpened():
            self.get_logger().error("Não foi possível abrir a câmera.")
            rclpy.shutdown()

    def cam_publish_func(self):
        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().error("Falha ao capturar imagem.")
            return
        
        ros_image = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
        self.cam_publisher.publish(ros_image)
        
    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()
    
def main(args=None):
    rclpy.init(args=args)
    node = Camera_node('no_camera', 'topico_camera', 0.05, 0)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()