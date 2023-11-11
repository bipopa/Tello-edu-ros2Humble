import rclpy
from rclpy.node import Node
import time

from std_msgs.msg import String  
standby=0
class MinimalPublisher(Node):

    def _init_(self):
        super()._init_('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'comandos', 10) 

    def get_user_input(self):

        global standby
        if standby==0 :
            stanby= input("Ingrese 1/0 para stanby ")  
        else

            msg = String()
            msg.data = 'command'
            
            self.publisher_.publish(msg)
            self.get_logger().info('Publicado: "%s"' % comando) 
            time.sleep(10)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    while rclpy.ok():
        minimal_publisher.get_user_input()

    minimal_publisher.destroy_node()
    rclpy.shutdown()

if _name_ == '_main_':
    main()