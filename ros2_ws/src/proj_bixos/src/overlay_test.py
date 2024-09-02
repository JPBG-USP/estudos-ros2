#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Accel
from cv_bridge import CvBridge
import cv2

class ImageAccelOverlay(Node):
    def __init__(self):
        super().__init__('image_accel_overlay')

        # Criando assinaturas para os tópicos de imagem e aceleração
        self.image_subscriber = self.create_subscription(
            Image,
            'topico_camera',
            self.image_callback,
            10
        )
        self.accel_subscriber = self.create_subscription(
            Accel,
            'topico_acelerometro',
            self.accel_callback,
            10
        )

        self.bridge = CvBridge()
        self.current_accel = Accel()  # Inicializando com valores padrão

    def image_callback(self, msg):
        try:
            # Convertendo a imagem ROS para um objeto OpenCV
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

            # Escrever os valores de aceleração na imagem
            self.overlay_acceleration(cv_image)

            # Convertendo a imagem OpenCV de volta para ROS e publicando (opcional)
            ros_image = self.bridge.cv2_to_imgmsg(cv_image, encoding='bgr8')
            self.get_logger().info("Imagem com aceleração sobreposta.")
            
            # Exibir a imagem (opcional)
            cv2.imshow("Image with Acceleration", cv_image)
            cv2.waitKey(1)

        except Exception as e:
            self.get_logger().error(f'Erro ao processar imagem: {e}')

    def accel_callback(self, msg):
        # Atualizar os valores de aceleração
        self.current_accel = msg

    def overlay_acceleration(self, image):
        # Adicionar texto com os valores de aceleração na imagem
        text = (f"Linear Accel: x={self.current_accel.linear.x:.2f}, "
                f"y={self.current_accel.linear.y:.2f}, "
                f"z={self.current_accel.linear.z:.2f}\n"
                f"Angular Accel: x={self.current_accel.angular.x:.2f}, "
                f"y={self.current_accel.angular.y:.2f}, "
                f"z={self.current_accel.angular.z:.2f}")

        # Adicionar o texto na imagem
        cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    def __del__(self):
        cv2.destroyAllWindows()

def main(args=None):
    rclpy.init(args=args)
    node = ImageAccelOverlay()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
