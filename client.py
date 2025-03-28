import configparser
import socket
import time

def ejecutar_cliente():

    config = configparser.ConfigParser()
    config.read('config.conf')

    time.sleep(2)

    host = config['general']['host']
    port = config['general']['port']

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((host, port))

    message = input ("Ingresa tu mensaje: ")
    mensaje_modificado = str(message).lower() 
    client_socket.sendall(mensaje_modificado.encode('utf-8'))

    respuesta = client_socket.recv(1024)
    print(respuesta)


    client_socket.close()

if __name__ == "__main__":
    ejecutar_cliente()