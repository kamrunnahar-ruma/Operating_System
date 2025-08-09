def preemptive_sjf_no_arrival(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    processes = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            pid, bt = line.split()
            processes.append((pid, int(bt)))

    n = len(processes)
    remaining_time = [bt for _, bt in processes]
    complete = 0
    time = 0
    process_sequence = []
    idle_time = 0

    wt = [0] * n
    tat = [0] * n
    ct = [0] * n

    while complete != n:
        shortest = -1
        min_rt = float('inf')

        for i in range(n):
            if remaining_time[i] > 0 and remaining_time[i] < min_rt:
                min_rt = remaining_time[i]
                shortest = i

        if shortest == -1:
            # CPU is idle
            process_sequence.append("Idle")
            idle_time += 1
            time += 1
            continue

        pid, bt = processes[shortest]
        process_sequence.append(pid)
        remaining_time[shortest] -= 1

        if remaining_time[shortest] == 0:
            complete += 1
            ct[shortest] = time + 1
            tat[shortest] = ct[shortest]
            wt[shortest] = tat[shortest] - bt

        time += 1

    # Output results
    print("\nProcess\tBurst\tWaiting\tTurnaround\tCompletion")
    for i in range(n):
        pid, bt = processes[i]
        print(f"{pid}\t{bt}\t{wt[i]}\t{tat[i]}\t\t{ct[i]}")

    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print(f"Total CPU Idle Time: {idle_time}")

    # Gantt chart
    print("\nGantt Chart:")
    chart = "|"
    times = [0]
    for t in range(1, len(process_sequence)):
        if process_sequence[t] != process_sequence[t - 1]:
            chart += f" {process_sequence[t - 1]} |"
            times.append(t)
    chart += f" {process_sequence[-1]} |"
    times.append(len(process_sequence))

    print(chart)
    print("".join(f"{str(t):>5}" for t in times))


# Run with input file
preemptive_sjf_no_arrival("input.txt")
