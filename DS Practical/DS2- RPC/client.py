# ===============================================
# Title: Implementation of RPC Mechanism (Client)
# Author: (Your Name)
# ===============================================

import socket
import pickle

def rpc_client():
    host = '127.0.0.1'
    port = 6000

    # Step 1: Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Step 2: Ask user for function and parameters
    print("Available functions: add, subtract, multiply, divide")
    func_name = input("Enter function name to call: ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    # Step 3: Pack function name and arguments
    data = (func_name, (a, b))
    client_socket.send(pickle.dumps(data))

    # Step 4: Receive result from server
    result = pickle.loads(client_socket.recv(1024))
    print(f"Result from server: {result}")

    # Step 5: Close connection
    client_socket.close()

if __name__ == "__main__":
    rpc_client()
