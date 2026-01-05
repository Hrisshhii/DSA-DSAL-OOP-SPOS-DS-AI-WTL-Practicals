# ===========================================================
# Title : Implementation of Clock Synchronization (Lamport’s Clock)
# Author: (Your Name)
# ===========================================================
# Theory:
# Lamport’s Logical Clock maintains event ordering in distributed systems.
# Each process Pi maintains a counter Ci that is updated as follows:
#
# Formulas used:
# 1. For internal or send event:
#       Ci = Ci + 1
# 2. For receive event (message with timestamp Tm received):
#       Ci = max(Ci, Tm) + 1
#
# These rules ensure that if event a → b (a happens before b),
# then C(a) < C(b)
# ===========================================================

def lamport_logical_clock():
    print("\n===== Lamport’s Logical Clock Simulation =====")
    n = int(input("Enter number of processes: "))
    clocks = [0] * n

    e = int(input("Enter total number of events: "))

    for _ in range(e):
        print("\nEvent Types: 1 = Internal, 2 = Send, 3 = Receive")
        etype = int(input("Enter event type: "))

        if etype == 1:
            pid = int(input("Enter process ID (0 to n-1): "))
            # Internal event: Ci = Ci + 1
            clocks[pid] += 1
            print(f"Internal event at P{pid}: Ci = {clocks[pid]}")

        elif etype == 2:
            pid = int(input("Sender process ID: "))
            # Send event: Ci = Ci + 1
            clocks[pid] += 1
            print(f"Send event from P{pid}: Ci = {clocks[pid]}")
            sent = clocks[pid]

        elif etype == 3:
            pid = int(input("Receiver process ID: "))
            recv_time = int(input("Enter received timestamp (Tm): "))
            # Receive event: Ci = max(Ci, Tm) + 1
            clocks[pid] = max(clocks[pid], recv_time) + 1
            print(f"Receive event at P{pid}: Ci = max(C_local, Tm) + 1 = {clocks[pid]}")

        print("Current Clock Values:", clocks)

# Run simulation
lamport_logical_clock()
