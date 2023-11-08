import socket
def enviar_comando(mensaje):
    # Crea un socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Dirección y puerto del servidor
    server_address = ('192.168.10.1', 8889)

    # Envía los datos al servidor
    client_socket.sendto(mensaje.encode(), server_address)

    # Cierra el socket
    client_socket.close()

# Llamamos a la función para enviar el mensaje "takeoff"
