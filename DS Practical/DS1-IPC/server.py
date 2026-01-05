# ==============================
# Title: Multithreaded Echo Server
# Author: (Your Name)
# Aim: To implement IPC using socket programming in Python
# ==============================

import socket
import threading

# Function to handle each client connection
def handle_client(client_socket, client_address):
    print(f"[+] New connection from {client_address}")
    
    while True:
        data = client_socket.recv(1024)  # receive data from client
        if not data:
            break
        print(f"Received from {client_address}: {data.decode()}")
        client_socket.send(data)  # Echo the received data back
    
    print(f"[-] Connection closed for {client_address}")
    client_socket.close()


def main():
    host = '127.0.0.1'  # localhost
    port = 5000         # Port number

    # Step 1: Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("[*] Socket successfully created")

    # Step 2: Bind socket to host and port
    server_socket.bind((host, port))
    print(f"[*] Socket bound to {host}:{port}")

    # Step 3: Listen for incoming connections
    server_socket.listen(5)
    print("[*] Server is listening...")

    while True:
        # Step 4: Accept client connection
        client_socket, client_address = server_socket.accept()
        
        # Step 5: Create a new thread for each client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()
