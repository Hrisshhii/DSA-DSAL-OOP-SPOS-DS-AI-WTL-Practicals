class Process:
    def __init__(self, pid):
        self.pid = pid
        self.clock = 0

    def send(self, receiver):
        self.clock += 1
        timestamp = self.clock
        print(f"P{self.pid} sent message to P{receiver.pid} with timestamp {timestamp}")
        return timestamp

    def receive(self, sender_timestamp):
        self.clock = max(self.clock, sender_timestamp) + 1
        print(f"Message received, Clock updated to {self.clock}")

def menu():
    process=[]
    n=int(input("Enter number of processes: "))
    for i in range(n):
        pid=int(input(f"Enter Process {i+1} ID: "))
        process.append(Process(pid))
    while True:
        print("\nMenu:")
        print("1. Send Message")
        print("2. Exit")
        choice = int(input("Enter choice: "))
        if choice == 2:
            print("Exiting...")
            break
        elif choice == 1:
            sender_id = int(input("Enter Sender Process ID: "))
            receiver_id = int(input("Enter Receiver Process ID: "))
            sender = next((p for p in process if p.pid == sender_id), None)
            receiver = next((p for p in process if p.pid == receiver_id), None)
            if sender and receiver:
                timestamp = sender.send(receiver)
                receiver.receive(timestamp)
            else:
                print("Invalid Process IDs")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()

    