def round_robin_with_arrival(filename, time_quantum):
    with open(filename, 'r') as f:
        lines = f.readlines()

    processes = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            pid, at, bt = line.split()
            processes.append([pid, int(at), int(bt), int(bt)])  

    n = len(processes)
    processes.sort(key=lambda x: x[1])  

    time = 0
    ready_queue = []
    gantt_chart = []
    complete = {}
    waiting_time = {}
    turnaround_time = {}
    i = 0  

    while True:
        while i < n and processes[i][1] <= time:
            ready_queue.append(processes[i])
            i += 1

        if ready_queue:
            current = ready_queue.pop(0)
            pid, at, bt, rem = current
            exec_time = min(rem, time_quantum)
            gantt_chart.append((pid, time, time + exec_time))
            time += exec_time
            current[3] -= exec_time

            while i < n and processes[i][1] <= time:
                ready_queue.append(processes[i])
                i += 1

            if current[3] > 0:
                ready_queue.append(current)
            else:
                complete[pid] = time
        else:
            if i < n:
                gantt_chart.append(("Idle", time, processes[i][1]))
                time = processes[i][1]
            else:
                break

    for pid, at, bt, _ in processes:
        tat = complete[pid] - at
        wt = tat - bt
        turnaround_time[pid] = tat
        waiting_time[pid] = wt

    print("\nProcess\tArrival\tBurst\tWaiting\tTurnaround")
    for pid, at, bt, _ in processes:
        print(f"{pid}\t{at}\t{bt}\t{waiting_time[pid]}\t{turnaround_time[pid]}")

    avg_wt = sum(waiting_time.values()) / n
    avg_tat = sum(turnaround_time.values()) / n
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")

    print("\nGantt Chart:")
    chart = "| " + " | ".join(f"{pid}" for pid, _, _ in gantt_chart) + " |"
    timeline = str(gantt_chart[0][1]) + "".join(f"{' ' * 4}{end}" for _, _, end in gantt_chart)
    print(chart)
    print(timeline)

round_robin_with_arrival("arrive.txt", time_quantum=3)
