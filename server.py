# server.py
import socket
import threading


class ChatServer:
    def __init__(self, host='127.0.0.1', port=12344):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print(f"Server started on {host}:{port}")
        self.clients = {}  # Stores client sockets and their names

    def handle_client(self, client_socket):
        try:
            # Receive and store client name
            client_name = client_socket.recv(1024).decode('utf-8').strip()
            self.clients[client_name] = client_socket  # fill the client dictionary
            print(f"{client_name} has joined the chat.")

            while True:
                try:
                    # Receive message from client
                    msg = client_socket.recv(1024).decode('utf-8').strip()
                    if not msg:
                        break  # Client disconnected

                        # Check for "exit"
                    if msg.lower() == "exit":
                         print(f"{client_name} requested to exit.")
                         # Optionally notify other users or just break
                         break

                    # Message format validation
                    if ':' not in msg:
                        client_socket.send("[Invalid message format. Use 'name:message'.".encode('utf-8'))
                        continue

                    target, message = msg.split(":", 1)
                    target = target.strip()
                    message = message.strip()

                    if target in self.clients:
                        # Send message to the target client
                        self.clients[target].send(f"[{client_name} -> You]: {message}".encode('utf-8'))
                        # Notify the sender that the message was sent
                       # client_socket.send(f"[You -> {target}]: {message}".encode('utf-8'))
                    else:
                        # Notify the sender that the target client was not found
                        client_socket.send(f"[Server]: User {target} not found.".encode('utf-8'))
                except Exception as e:
                    print(f"Error handling message from {client_name}: {e}")
                    break
        except Exception as e:
            print(f"Error with client connection: {e}")
        finally:
            print(f"Connection with {client_name} lost.")
            if client_name in self.clients:
                del self.clients[client_name]
            client_socket.close()

    def start(self):
        print("Server is running and waiting for connections...")
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection established with {addr}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()


if __name__ == "__main__":
    server = ChatServer()
    server.start()
