import socket

server_socket=None
def openSocket():
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a specific address and port
    server_address = ('192.168.10.2', 8890)
    server_socket.bind(server_address)

    print(f'Escuchando en {server_address}')

def closeSocket():
    global server_socket
    if server_socket:
        server_socket.close()
        print("Socket cerrado")
    else:
        print("No hay socket abierto")


def getBateria():
    openSocket()
    # Recibe datos del cliente
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode()

    # Busca la etiqueta y extrae el valor correspondiente
    def get_value(tag):
        index = message.find(tag)
        if index != -1:
            return message[index:].split(';')[0].split(':')[-1]
        return None

    nivel_de_bateria = get_value('bat:')

    closeSocket()

    return nivel_de_bateria





def obtener_posicion_xyz():
    # Crea un socket UDP
    openSocket()

    # Recibe datos del cliente
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode()

    # Busca la etiqueta y extrae el valor correspondiente
    def get_value(tag):
        index = message.find(tag)
        if index != -1:
            return message[index:].split(';')[0].split(':')[-1]
        return None

    x = get_value('x:')
    y = get_value('y:')
    z = get_value('z:')

    # Cierra el socket
    closeSocket()

    return x, y, z

