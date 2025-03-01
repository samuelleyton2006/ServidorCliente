import socket

def iniciar_cliente():
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_socket.connect(('127.0.0.1', 8080))

    print("Ya se conectó xd, escribe algo si quieres mandar al servidor")
    
    while True:
        msg = input("> ")
        if msg.lower() == 'cerrar cliente':
            break
        cliente_socket.send(msg.encode('utf-8'))
        response = cliente_socket.recv(1024).decode('utf-8')
        print(f"[Servidor] {response}")

    cliente_socket.close()

if __name__ == "__main__":
    iniciar_cliente()