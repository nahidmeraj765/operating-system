num_process = int(input("Enter the number of processes: ")) # taking input for the number of total process

process_list = [] # defining an empty list to store the processes
time_list = [] # defining an empty list to store the burst times

quantum = int(input("Enter the time quantum: ")) # taking input for the quantum number

for i in range(0,num_process):
    process, burst_time = input().split() # splitting both string and integer input with space
    process_list.append(process) # storing all process's (string) input into a list
    time_list.append(int(burst_time)) # storing all burst time's (integer) input into another list

# variables to store remaining times and waiting times
remaining_time = time_list.copy()  # remaining burst time for each process
waiting_time = [0] * num_process   # initializing the waiting time as [0,0,0,0]
time = 0                           # current time

gantt_chart_string = "|0|" # gantt chart representation

# Loop through the processes
while True:
    done = True  # assuming all processes are done

    for i in range(num_process):
        if remaining_time[i] > 0:
            done = False  # process is not done yet
            
            # if process burst time is greater than quantum
            if remaining_time[i] > quantum:
                time += quantum  # will increase the current time by quantum
                remaining_time[i] -= quantum  # reducing the remaining time by quantum
            else:
                time += remaining_time[i]  # adding the remaining burst time
                waiting_time[i] = time - time_list[i]  # calculating the waiting time
                remaining_time[i] = 0  # selected process is finished
            
            # updating the Gantt chart
            gantt_chart_string += f"{process_list[i]}|{time}|"

    if done:  # will exit the loop if all processes are finished
        break

total_waiting_time = sum(waiting_time)
avg_waiting_time = total_waiting_time / num_process

print("The Gantt chart will be:", gantt_chart_string)
print(f"The average waiting time will be: {avg_waiting_time:.2f} ms")

'''
4
p1 21
p2 3
p3 6
p4 2
Quantum = 5
'''
