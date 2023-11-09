import rclpy
from std_msgs.msg import String
import socket
import time

def enviar_comando(mensaje):
    # Crea un socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Dirección y puerto del servidor
    server_address = ('192.168.10.1', 8889)

    # Envía los datos al servidor
    client_socket.sendto(mensaje.encode(), server_address)

    # Cierra el socket
    client_socket.close()

def callback(msg):
    # Llamada a la función para enviar comandos
    enviar_comando("command")
    time.sleep(0.1)
    enviar_comando(msg.data)

def main():
    rclpy.init()
    node = rclpy.create_node('tello_controller_node')
    subscriber = node.create_subscription(String, 'comandos', callback, 10)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
