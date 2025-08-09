def fcfs_scheduling_from_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    process = []  

    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):  
            pid, bt = line.split()  
            process.append((pid, int(bt)))  

    n = len(process)  
    wt = [0] * n  
    tat = [0] * n  
    start_time = 0  
    gantt_chart = []  

    for i in range(n):
        pid, bt = process[i]
        wt[i] = start_time  
        tat[i] = wt[i] + bt  
        gantt_chart.append((pid, start_time, start_time + bt))  
        start_time += bt  

    print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        pid, bt = process[i]
        print(f"{pid}\t{bt}\t\t{wt[i]}\t\t{tat[i]}")

    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n

    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")

    print("\nGantt Chart:")
    gantt_line = "| " + " | ".join(f"{pid}" for pid, _, _ in gantt_chart) + " |"
    time_line = "0" + "".join(f"{' ' * 4}{end}" for _, _, end in gantt_chart)
    print(gantt_line) 
    print(time_line)

fcfs_scheduling_from_file("input.txt")