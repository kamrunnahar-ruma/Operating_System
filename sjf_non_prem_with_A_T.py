def sjf_with_arrival_time(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    processes = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            pid, at, bt = line.split()
            processes.append((pid, int(at), int(bt)))

    n = len(processes)
    complete = 0
    time = 0
    idle_time = 0
    is_completed = [False] * n
    gantt_chart = []
    wt = [0] * n
    tat = [0] * n
    ct = [0] * n

    while complete < n:
        idx = -1
        min_bt = float('inf')
        for i in range(n):
            pid, at, bt = processes[i]
            if at <= time and not is_completed[i]:
                if bt < min_bt:
                    min_bt = bt
                    idx = i
                elif bt == min_bt and at < processes[idx][1]:  
                    idx = i

        if idx == -1:
            gantt_chart.append(("Idle", time, time + 1))
            idle_time += 1
            time += 1
        else:
            pid, at, bt = processes[idx]
            gantt_chart.append((pid, time, time+bt))
            wt[idx] = time - at
            tat[idx] = wt[idx]+bt
            ct[idx] = time+bt
            time+=bt
            is_completed[idx] = True
            complete += 1

    print("\nProcess\tArrival\tBurst\tWaiting\tTurnaround\tCompletion")
    for i in range(n):
        pid, at, bt = processes[i]
        print(f"{pid}\t{at}\t{bt}\t{wt[i]}\t{tat[i]}\t\t{ct[i]}")

    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print(f"Total CPU Idle Time: {idle_time}")

    print("\nGantt Chart:")
    gantt_line = "| " + " | ".join(f"{pid}" for pid, _, _ in gantt_chart) + " |"
    time_line = str(gantt_chart[0][1]) + "".join(f"{' ' * 4}{end}" for _, _, end in gantt_chart)
    print(gantt_line)
    print(time_line)

sjf_with_arrival_time("arrive.txt")