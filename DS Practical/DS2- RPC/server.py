# ===============================================
# Title: Implementation of RPC Mechanism (Server)
# Author: (Your Name)
# ===============================================

import socket
import pickle   # used for object serialization

# Step 1: Define server-side functions that can be called remotely
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"

# Step 2: Function to handle client requests
def rpc_server():
    host = '127.0.0.1'
    port = 6000

    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("[*] RPC Server is running and waiting for client connection...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[+] Connected to client: {addr}")

        # Step 3: Receive the function name and arguments from the client
        data = client_socket.recv(1024)
        func_name, args = pickle.loads(data)

        # Step 4: Execute the requested function
        if func_name in globals():
            result = globals()[func_name](*args)
        else:
            result = "Error: Function not found!"

        # Step 5: Send the result back to the client
        client_socket.send(pickle.dumps(result))
        client_socket.close()

if __name__ == "__main__":
    rpc_server()
