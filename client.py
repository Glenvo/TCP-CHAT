#this is client
# client.py
import socket
import threading


class ChatClient:
    def __init__(self, host='127.0.0.1', port=12344):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def send_messages(self):
        while True:
            msg = input("[You]: ")
            self.client_socket.send(msg.encode('utf-8'))
            if msg.lower() == "exit":
                print("[Client]: Exiting chat...")
                break

    def receive_messages(self):
        while True:
            try:
                msg = self.client_socket.recv(1024).decode('utf-8')
                if not msg:
                    break  # Server closed connection
                print(msg)
            except Exception as e:
                print("[Client]: Connection to the server lost.")
                break

    def start(self):
        client_name = input("Enter your name: ")
        self.client_socket.send(client_name.encode('utf-8'))

        # Start threads for sending and receiving messages
        threading.Thread(target=self.receive_messages).start()
        self.send_messages()


if __name__ == "__main__":
    client = ChatClient()
    client.start()
