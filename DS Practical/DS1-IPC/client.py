# ==============================
# Title: Echo Client
# Author: (Your Name)
# ==============================

import socket

def main():
    host = '127.0.0.1'
    port = 5000

    # Step 1: Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Step 2: Connect to server
    client_socket.connect((host, port))
    print("[*] Connected to server")

    # Step 3: Send data to server
    while True:
        msg = input("Enter message (type 'exit' to quit): ")
        if msg.lower() == 'exit':
            break

        client_socket.send(msg.encode())          # Send message to server
        data = client_socket.recv(1024).decode()  # Receive echoed message
        print("Echoed from server:", data)

    # Step 4: Close connection
    client_socket.close()

if __name__ == "__main__":
    main()
