import rclpy
from std_msgs.msg import String
import socket


## coloque aqui las ip de los drones
selector=1
drone1_ip_address='192.168.137.110'
drone2_ip_address='192.168.137.110'
drone3_ip_address='192.168.137.110'
command="land"

def enviar_comando(mensaje, ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (ip, 8889)

    client_socket.sendto(mensaje.encode(), server_address)
    client_socket.close()

def case_1():
    enviar_comando("command")
    time.sleep(0.05)
    enviar_comando(command, drone1_ip_address)

def case_2():
    enviar_comando("command")
    time.sleep(0.05)
    enviar_comando(command, drone2_ip_address)

def case_3():
    enviar_comando("command")
    time.sleep(0.05)
    enviar_comando(command, drone3_ip_address)

def case_4():
    for ip in [drone1_ip_address, drone2_ip_address, drone3_ip_address]:
        enviar_comando("command")
        time.sleep(0.05)
        enviar_comando(command, ip)

def switch_case(argument):
    switcher = {
        1: case_1,
        2: case_2,
        3: case_3,
        4: case_4
    }
    func = switcher.get(argument, lambda: print("Valor de dronselect no válido"))
    func()

def callback_command(msg):
    # Llamada a la función para enviar comandos
    global command
    command = msg.data
    switch_case(selector)


def callback_drone_select(msg):
    global selector
    selector = int(msg.data)

def main():
    rclpy.init()
    node = rclpy.create_node('tello_controller_node')
    subscriber_commands= node.create_subscription(String, 'comandos', callback_command, 10)
    subscriber_swarm_select=node.create_subscription(String, 'drone_select', callback_drone_select, 10)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
