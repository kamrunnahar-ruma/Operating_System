def fcfs_with_idle_time(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    process = []  
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):  
            pid, at, bt = line.split()
            process.append((pid, int(at), int(bt)))

    process.sort(key=lambda x: x[1])

    n = len(process)  
    start_time = 0
    wt = [0] * n
    tat = [0] * n
    ct = [0] * n
    idle_time = 0
    gantt_chart = []

    for i in range(n):
        pid, at, bt = process[i]
        if start_time < at:
            gantt_chart.append(("Idle", start_time, at))
            idle_time += at - start_time
            start_time = at

        wt[i] = start_time - at
        tat[i] = wt[i] + bt
        ct[i] = start_time + bt

        gantt_chart.append((pid, start_time, start_time + bt))
        start_time += bt

    print("\nProcess\tArrival\tBurst\tWaiting\tTurnaround\tCompletion")
    for i in range(n):
        pid, at, bt = process[i]
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

fcfs_with_idle_time("arrive.txt")