import configparser
import socket
import subprocess 
import threading


config = configparser.ConfigParser()
config.read('config.conf')

def iniciar_servidor():

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = config['general']['host']
    puerto = config['general']['port']

    try:
        servidor.bind((host, puerto))
        print(f"Servidor escuchando en {host}:{puerto}")
    except Exception as e:
        print(f"Error al enlazar el puerto: {e}")
        return
    
    servidor.listen(5)

    while True:
        try:            
            cliente, direccion = servidor.accept()            
            
            datos = cliente.recv(1024)
            print(datos)
            if datos:
                mensaje_recibido = datos.decode()
                print(f"Datos recibidos: {mensaje_recibido}")
                if mensaje_recibido == "desconexion":
                    print("Desconectando")
                    print(f"Conexión cerrada con {direccion}")
                    cliente.close()
                    
                else:
                    respuesta = "Hola cliente"        
                respuesta = "HTTP/1.1 200 OK\r\n"
                respuesta += "Content-Type: text/plain\r\n"                                
                respuesta += "Servidor ha recibido el mensaje."

                cliente.send(respuesta.encode())
                        

        except Exception as e:
            print(f"Error durante la conexión o el manejo de datos: {e}")

def ejecutar_cliente():
       
    subprocess.run(["python", config['general']['directorio']])

servidor_thread = threading.Thread(target=iniciar_servidor)
servidor_thread.start()

ejecutar_cliente()
