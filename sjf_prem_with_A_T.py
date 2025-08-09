def preemptive_sjf_with_arrival(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    processes = []  # (PID, ArrivalTime, BurstTime)
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            pid, at, bt = line.split()
            processes.append([pid, int(at), int(bt)])

    n = len(processes)
    remaining_bt = [bt for _, _, bt in processes]
    complete = 0
    time = 0
    is_completed = [False] * n
    start_flag = [False] * n
    start_times = {}
    end_times = {}
    process_sequence = []
    idle_time = 0

    wt = [0] * n
    tat = [0] * n
    ct = [0] * n

    while complete != n:
        idx = -1
        shortest_bt = float('inf')

        for i in range(n):
            pid, at, bt = processes[i]
            if at <= time and remaining_bt[i] > 0:
                if remaining_bt[i] < shortest_bt:
                    shortest_bt = remaining_bt[i]
                    idx = i
                elif remaining_bt[i] == shortest_bt:
                    if at < processes[idx][1]:
                        idx = i

        if idx == -1:
            process_sequence.append("Idle")
            time += 1
            idle_time += 1
            continue

        if not start_flag[idx]:
            start_flag[idx] = True
            start_times[processes[idx][0]] = time

        process_sequence.append(processes[idx][0])
        remaining_bt[idx] -= 1

        if remaining_bt[idx] == 0:
            complete += 1
            ct[idx] = time + 1
            tat[idx] = ct[idx] - processes[idx][1]
            wt[idx] = tat[idx] - processes[idx][2]
            end_times[processes[idx][0]] = time + 1
            is_completed[idx] = True

        time += 1

    print("\nProcess\tArrival\tBurst\tWaiting\tTurnaround\tCompletion")
    for i in range(n):
        pid, at, bt = processes[i]
        print(f"{pid}\t{at}\t{bt}\t{wt[i]}\t{tat[i]}\t\t{ct[i]}")

    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print(f"Total Idle Time: {idle_time}")

    # Gantt Chart
    print("\nGantt Chart:")
    chart = "|"
    times = [0]
    for i in range(1, len(process_sequence)):
        if process_sequence[i] != process_sequence[i - 1]:
            chart += f" {process_sequence[i - 1]} |"
            times.append(i)
    chart += f" {process_sequence[-1]} |"
    times.append(len(process_sequence))

    print(chart)
    print("".join(f"{str(t):>5}" for t in times))


# Run it
preemptive_sjf_with_arrival("arrive.txt")
0