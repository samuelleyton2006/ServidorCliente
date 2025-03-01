import socket

def iniciar_servidor():
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind(('0.0.0.0', 8080))
    servidor_socket.listen(5)

    print("Servidor iniciado y esperando conexiones...")

    while True:
        cliente_socket, direccion = servidor_socket.accept()
        print(f"Cliente conectado desde {direccion}")

        while True:
            try:
                mensaje = cliente_socket.recv(1024).decode('utf-8')
                if not mensaje:
                    break
                print(f"[Cliente {direccion}] {mensaje}")
                cliente_socket.send("Mensaje recibido".encode('utf-8'))
            except:
                break
        
        print(f"Cliente {direccion} desconectado")
        cliente_socket.close()

if __name__ == "__main__":
    iniciar_servidor()