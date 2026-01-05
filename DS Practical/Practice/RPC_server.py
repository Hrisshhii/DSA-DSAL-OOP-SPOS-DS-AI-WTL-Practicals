from xmlrpc.server import SimpleXMLRPCServer

# Functions to expose
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

# Setup server
server = SimpleXMLRPCServer(("localhost", 9000))
print("RPC Server listening on port 9000...")

server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")

server.serve_forever()
