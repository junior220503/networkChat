import socket
import threading

def receber_mensagens(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024).decode('utf-8')
            print(mensagem)
        except:
            print("Você foi desconectado do servidor.")
            cliente.close()
            break

def enviar_mensagens(cliente):
    while True:
        mensagem = input("")
        cliente.send(mensagem.encode('utf-8'))

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(("127.0.0.1", 5555))

    thread_receber = threading.Thread(target=receber_mensagens, args=(cliente,))
    thread_receber.start()

    thread_enviar = threading.Thread(target=enviar_mensagens, args=(cliente,))
    thread_enviar.start()

if name == "main":
    main()