def ring_election(processes, failed_id=None):
    """
    processes: list of process IDs in the ring
    failed_id: ID of the failed coordinator (optional)
    """
    print("Processes in ring:", processes)
    
    if failed_id is None:
        print("No failure detected. Current coordinator is max ID:", max(processes))
        return max(processes)
    
    print(f"\nCoordinator {failed_id} failed. Starting election...")
    
    # Start election from the next process after failed coordinator
    start_idx = (processes.index(failed_id) + 1) % len(processes)
    election = []
    
    idx = start_idx
    while True:
        election.append(processes[idx])
        idx = (idx + 1) % len(processes)
        if idx == start_idx:
            break
    
    new_coordinator = max(election)
    print("Election message passed around the ring:", election)
    print("New coordinator elected:", new_coordinator)
    return new_coordinator

# Example usage
processes = [1, 3, 5, 2, 4]  # Process IDs
failed_id = 5                # Suppose process 5 (current coordinator) fails
ring_election(processes, failed_id)
