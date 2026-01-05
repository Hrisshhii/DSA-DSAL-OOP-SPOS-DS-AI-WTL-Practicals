import xmlrpc.client

# Connect to RPC server
proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")

print("Connected to RPC Server.")

while True:
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    choice = int(input("Enter choice: "))
    if choice == 5:
        print("Exiting...")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if choice == 1:
        print("Result:", proxy.add(a, b))
    elif choice == 2:
        print("Result:", proxy.subtract(a, b))
    elif choice == 3:
        print("Result:", proxy.multiply(a, b))
    elif choice == 4:
        print("Result:", proxy.divide(a, b))
    else:
        print("Invalid choice")
