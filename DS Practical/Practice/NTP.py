def ntp():
    print("\nEnter timestamps (in seconds):")
    t1 = float(input("T1 (Client send time)  = "))
    t2 = float(input("T2 (Server receive time) = "))
    t3 = float(input("T3 (Server send time)  = "))
    t4 = float(input("T4 (Client receive time) = "))

    offset = ((t2 - t1) + (t3 - t4)) / 2
    delay = (t4 - t1) - (t3 - t2)

    print(f"\nComputed Clock Offset θ = {offset:.6f} seconds")
    print(f"Computed Round-trip Delay δ = {delay:.6f} seconds")
    print(f"Client should adjust clock by θ: new_time = time + {offset:.6f}\n")

def menu():
    while True:
        print("----- NTP Clock Simulation Menu -----")
        print("1. Enter timestamps and calculate offset/delay")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            ntp()
        elif choice == "2":
            print("Exiting simulation...")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    menu()
