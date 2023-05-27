import matplotlib.pyplot as plt

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.start_time = -1
        self.finish_time = -1

def read_processes_from_file(filename):
    processes = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            pid, arrival_time, burst_time, priority = line.split()
            arrival_time, burst_time, priority = int(arrival_time), int(burst_time), int(priority)
            processes.append(Process(pid, arrival_time, burst_time, priority))
    return processes

def sjf(processes):
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.start_time = current_time
        process.finish_time = current_time + process.burst_time
        current_time += process.burst_time

def round_robin(processes, time_quantum):
    current_time = 0
    queue = processes.copy()
    queue.sort(key=lambda x: x.arrival_time)
    while queue:
        current_process = queue.pop(0)
        if current_time < current_process.arrival_time:
            current_time = current_process.arrival_time
        execute_for = min(time_quantum, current_process.burst_time)
        current_process.burst_time -= execute_for
        if current_process.burst_time > 0:
            queue.append(current_process)
        current_time += execute_for
        if current_process.burst_time == 0:
            current_process.finish_time = current_time

def priority_scheduling(processes):
    processes.sort(key=lambda x: (x.arrival_time, -x.priority))
    current_time = 0
    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        process.start_time = current_time
        process.finish_time = current_time + process.burst_time
        current_time += process.burst_time

def draw_gantt_chart(processes):
    fig, ax = plt.subplots()
    ax.set_ylabel('Processes')
    ax.set_xlabel('Time units')
    ax.set_yticks(range(len(processes)))
    ax.set_yticklabels([p.pid for p in processes])
    ax.set_ylim(-1, len(processes))
    ax.grid(True)

    for i, process in enumerate(processes):
        ax.broken_barh([(process.start_time, process.finish_time - process.start_time)], (i-0.4, 0.8))

    plt.show()

filename = 'processes.txt'
processes = read_processes_from_file(filename)

sjf(processes)
draw_gantt_chart(processes)

# Reset start and finish times before running a different algorithm
for process in processes:
    process.start_time = -1
    process.finish_time = -1

round_robin(processes, 2)  # Example time quantum of 2
draw_gantt_chart(processes)

for process in processes:
    process.start_time = -1
    process.finish_time = -1

priority_scheduling(processes)
draw_gantt_chart(processes)
