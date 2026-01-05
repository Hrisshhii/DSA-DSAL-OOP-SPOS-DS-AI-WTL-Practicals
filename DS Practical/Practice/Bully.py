def bully_algorithm(processes, failed_id):
    """
    processes: list of process IDs
    failed_id: current coordinator that failed
    """
    print("Processes:", processes)
    print(f"Coordinator {failed_id} failed. Starting election...")

    # Find processes higher than the one that detected failure
    for p in sorted(processes):
        if p > failed_id:
            print(f"Process {failed_id} sends election message to {p}")
    
    # New coordinator is the process with the highest ID
    new_coordinator = max(processes)
    print("New coordinator elected:", new_coordinator)
    return new_coordinator

# Example usage
processes = [1, 3, 5, 2, 4]  # Process IDs
failed_id = 3                # Suppose current coordinator (3) fails
bully_algorithm(processes, failed_id)
