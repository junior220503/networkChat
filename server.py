import socket
import threading

clientes = []

def broadcast(mensagem, cliente_atual):
    for cliente in clientes:
        if cliente != cliente_atual:
            try:
                cliente.send(mensagem)
            except:
                cliente.close()
                if cliente in clientes:
                    clientes.remove(cliente)

def handle_cliente(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024)
            broadcast(mensagem, cliente)
        except:
            cliente.close()
            if cliente in clientes:
                clientes.remove(cliente)
            break

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(("127.0.0.1", 5555))
    servidor.listen()

    print("Servidor rodando e aguardando conexões...")

    while True:
        cliente, endereco = servidor.accept()
        print(f"Conectado com {str(endereco)}")

        clientes.append(cliente)
        cliente.send("Conectado ao servidor!".encode("utf-8"))

        thread = threading.Thread(target=handle_cliente, args=(cliente,))
        thread.start()

if name == "main":
    main()