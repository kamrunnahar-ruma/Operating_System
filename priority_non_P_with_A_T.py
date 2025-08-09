def priority_scheduling_with_arrival(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    process = [] 
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            pid, at, bt, pr = line.split()
            process.append((pid, int(at), int(bt), int(pr)))

    n = len(process)
    complete = 0
    time = 0
    is_completed = [False] * n
    gantt_chart = []
    wt = [0] * n
    tat = [0] * n
    ct = [0] * n
    idle_time = 0

    while complete != n:
        idx = -1
        highest_priority = float('inf')
        for i in range(n):
            pid, at, bt, pr = process[i]
            if at <= time and not is_completed[i]:
                if pr < highest_priority:
                    highest_priority = pr
                    idx = i
                elif pr == highest_priority:
                    if at < processes[idx][1]:
                        idx = i

        if idx == -1:
            gantt_chart.append(("Idle", time, time + 1))
            time += 1
            idle_time += 1
        else:
            pid, at, bt, pr = process[idx]
            wt[idx] = time - at
            tat[idx] = wt[idx]+bt
            ct[idx] = time+bt
            gantt_chart.append((pid, time, time+bt))
            is_completed[idx] = True
            complete += 1
            time +=bt

    print("\nProcess\tArrival\tBurst\tPriority\tWaiting\tTurnaround\tCompletion")
    for i in range(n):
        pid, at, bt, pr = process[i]
        print(f"{pid}\t{at}\t{bt}\t{pr}\t\t{wt[i]}\t{tat[i]}\t\t{ct[i]}")

    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print(f"Total Idle Time: {idle_time}")

    print("\nGantt Chart:")
    gantt_line = "| " + " | ".join(f"{pid}" for pid, _, _ in gantt_chart) + " |"
    time_line = str(gantt_chart[0][1]) + "".join(f"{' ' * 4}{end}" for _, _, end in gantt_chart)
    print(gantt_line)
    print(time_line)

priority_scheduling_with_arrival("priority_preemptive.txt")