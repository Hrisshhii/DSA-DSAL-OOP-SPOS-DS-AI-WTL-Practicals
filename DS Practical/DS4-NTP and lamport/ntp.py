# ===========================================================
# Title : Implementation of Clock Synchronization (NTP)
# Author: (Your Name)
# ===========================================================
# Theory:
# Network Time Protocol (NTP) synchronizes the clock of a client
# with that of a time server by exchanging four timestamps:
#   T1 = time at which client sends request
#   T2 = time at which server receives request
#   T3 = time at which server sends reply
#   T4 = time at which client receives reply
#
# Formulas used:
#   Round-trip delay (δ) = (T4 - T1) - (T3 - T2)
#   Clock offset (θ)     = ((T2 - T1) + (T3 - T4)) / 2
# ===========================================================

import time
import random

def ntp_clock_sync():
    print("\n===== Network Time Protocol (NTP) Simulation =====")

    # Step 1: Client sends request at time T1
    T1 = time.time()
    print(f"T1 (Client send time): {T1:.6f}")

    # Step 2: Simulate transmission delay
    time.sleep(random.uniform(0.01, 0.05))

    # Step 3: Server receives request and records T2
    T2 = time.time()
    print(f"T2 (Server receive time): {T2:.6f}")

    # Step 4: Server processes and sends reply at T3
    time.sleep(random.uniform(0.01, 0.05))
    T3 = time.time()
    print(f"T3 (Server send time): {T3:.6f}")

    # Step 5: Client receives reply at T4
    time.sleep(random.uniform(0.01, 0.05))
    T4 = time.time()
    print(f"T4 (Client receive time): {T4:.6f}")

    # Step 6: Apply formulas
    # δ = (T4 - T1) - (T3 - T2)
    delay = (T4 - T1) - (T3 - T2)

    # θ = ((T2 - T1) + (T3 - T4)) / 2
    offset = ((T2 - T1) + (T3 - T4)) / 2

    print("\n--- Calculations ---")
    print(f"Round-trip delay (δ) = (T4 - T1) - (T3 - T2) = {delay:.6f} sec")
    print(f"Clock offset (θ) = ((T2 - T1) + (T3 - T4)) / 2 = {offset:.6f} sec")

    print(f"\nClient should adjust its clock by θ = {offset:.6f} seconds")

# Run the simulation
ntp_clock_sync()
