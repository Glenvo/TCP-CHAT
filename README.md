# TCP-CHAT
README
Overview
This is a multi-client chat application built with Python and TCP sockets. It has two components:

server.py: Accepts client connections, relays messages.
client.py: Connects to the server, sends/receives messages.

Key Features:
TCP communication (reliable).
Multi-threaded server (supports multiple clients).
Text-based interface with a simple message format: target_name: message.
Handles both graceful and unexpected disconnections.

Installation and Setup:
Clone/Download this project.
Ensure you have Python 

How to Run:
Start the Server
"python server.py"
You’ll see something like:
"Server started on 127.0.0.1:12344"
Server is running and waiting for connections...

Start the Client (in a different terminal)
"python client.py"
Enter your name when prompted.
You can run multiple clients in separate terminals, each with a unique name.
Example Usage
Client #1 (Gal):
Enter your name: Gal
[You]: Ido: Hello Ido!
Client #2 (Ido):
[Gal -> You]: Hello Ido!
[You]: Gal: Hi Gal, how are you?

Exiting:
Type exit in any client to disconnect.
The server removes that client from its active list.

Notes:
Invalid Format: If you omit the colon (:), the server responds with an error.
Unknown Target: If target_name doesn’t exist, you get a [Server]: User '...' not found. message.
Unexpected Disconnect: If a client terminates abruptly, the server detects it and removes them automatically.
Enjoy the chat!