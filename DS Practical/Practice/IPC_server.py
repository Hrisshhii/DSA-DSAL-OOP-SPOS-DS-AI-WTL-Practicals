import socket
import threading

# Function to handle client connection
def handle_client(client_socket, addr):
    print(f"Connected to {addr}")
    while True:
        message = client_socket.recv(1024).decode()
        if not message or message.lower() == 'exit':
            break
        print(f"Received from {addr}: {message}")
        client_socket.send(f"ECHO: {message}".encode())
    print(f"Connection closed: {addr}")
    client_socket.close()

# Main server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))  # You can change port if needed
server.listen(5)
print("Server listening on port 12345...")

while True:
    client_sock, client_addr = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_sock, client_addr))
    client_thread.start()
