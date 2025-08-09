def priority_preemptive_no_arrival(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    process = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            pid, bt, pr = line.split()
            process.append([pid, int(bt), int(pr)])

    n = len(process)
    remaining_bt = [bt for _, bt, _ in process]
    complete = 0
    time = 0
    is_completed = [False] * n
    start_flag = [False] * n
    start_times = {}
    end_times = {}
    process_sequence = []

    wt = [0] * n
    tat = [0] * n
    ct = [0] * n

    while complete != n:
        idx = -1
        highest_priority = float('inf')
        for i in range(n):
            pid, bt, pr = process[i]
            if remaining_bt[i] > 0 and pr < highest_priority:
                highest_priority = pr
                idx = i

        if idx == -1:
            process_sequence.append("Idle")
            time += 1
            continue

        if not start_flag[idx]:
            start_flag[idx] = True
            start_times[process[idx][0]] = time

        process_sequence.append(process[idx][0])
        remaining_bt[idx] -= 1

        if remaining_bt[idx] == 0:
            complete += 1
            ct[idx] = time + 1
            tat[idx] = ct[idx]
            wt[idx] = tat[idx] - process[idx][1]
            end_times[process[idx][0]] = time + 1

        time += 1

    print("\nProcess\tBurst\tPriority\tWaiting\tTurnaround\tCompletion")
    for i in range(n):
        pid, bt, pr = process[i]
        print(f"{pid}\t{bt}\t{pr}\t\t{wt[i]}\t{tat[i]}\t\t{ct[i]}")

    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")

        # Proper Gantt Chart
    print("\nGantt Chart:")
    chart = "|"
    times = [0]  # Start from time 0

    for i in range(1, len(process_sequence)):
        if process_sequence[i] != process_sequence[i - 1]:
            chart += f" {process_sequence[i - 1]} |"
            times.append(i)
    # Add the last process
    chart += f" {process_sequence[-1]} |"
    times.append(len(process_sequence))

    print(chart)
    print("".join(f"{t:>5}" for t in times))

priority_preemptive_no_arrival("priority_preemptive_no_arrival.txt")
