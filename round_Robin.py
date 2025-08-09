def round_robin_scheduling_from_file(filename, time_quantum):
    # Step 1: Read input file
    with open(filename, 'r') as f:
        lines = f.readlines()

    processes = []  # [PID, BurstTime, RemainingTime]
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            pid, bt = line.split()
            processes.append([pid, int(bt), int(bt)])  # Remaining = BurstTime

    n = len(processes)

    waiting_time = {p[0]: 0 for p in processes}
    turnaround_time = {p[0]: 0 for p in processes}
    complete_time = {}
    ready_queue = processes.copy()
    gantt_chart = []
    time = 0

    # Step 2: Scheduling loop
    while any(p[2] > 0 for p in ready_queue):
        for current in ready_queue:
            pid, bt, rem = current
            if rem > 0:
                exec_time = min(time_quantum, rem)
                gantt_chart.append((pid, time, time + exec_time))
                time += exec_time
                current[2] -= exec_time
                if current[2] == 0:
                    complete_time[pid] = time

    # Step 3: Calculate turnaround and waiting times
    for pid, bt, _ in processes:
        turnaround_time[pid] = complete_time[pid]
        waiting_time[pid] = turnaround_time[pid] - bt

    # Step 4: Print table
    print("\nProcess\tBurst\tWaiting\tTurnaround")
    for pid, bt, _ in processes:
        print(f"{pid}\t{bt}\t{waiting_time[pid]}\t{turnaround_time[pid]}")

    avg_wt = sum(waiting_time.values()) / n
    avg_tat = sum(turnaround_time.values()) / n
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")

    # Step 5: Gantt chart
    print("\nGantt Chart:")
    chart = "| " + " | ".join(f"{pid}" for pid, _, _ in gantt_chart) + " |"
    timeline = str(gantt_chart[0][1]) + "".join(f"{' ' * 4}{end}" for _, _, end in gantt_chart)
    print(chart)
    print(timeline)


# Example run
round_robin_scheduling_from_file("input.txt", time_quantum=3)
