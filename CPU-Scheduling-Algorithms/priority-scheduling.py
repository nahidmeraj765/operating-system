num_process = int(input("Enter the number of process: ")) # taking input for the number of total process

process_list = [] # defining an empty list to store the processes
time_list = [] # defining an empty list to store the burst times
priority_list = [] # defining an empty list to store the priorities

for i in range(0,num_process):
    process,time,priority = input().split() # splitting both string and integer input with space
    process_list.append(process) # storing all process's (string) input into a list
    time_list.append(int(time)) # storing all burst time's (integer) input into another list
    priority_list.append(int(priority)) # storing all priority's (integer) input into another list

length = len(priority_list)

# finding sorted process list,burst time list and priority list respectively
for i in range(0,length):
    for j in range(i+1,length):
        if(priority_list[i]>priority_list[j]):
            temp_Priority = priority_list[j] # sorting the priority list
            priority_list[j] = priority_list[i]
            priority_list[i] = temp_Priority

            temp_Process = process_list[j] # sorting the process list based on the sorted priority list
            process_list[j] = process_list[i]
            process_list[i] = temp_Process

            temp_time = time_list[j] # sorting the process list,burst time list based on the sorted priority list
            time_list[j] = time_list[i]
            time_list[i] = temp_time

start_count = 0
total_count = 0
gantt_chart_string = "|0|"

for k in range(0,length): # generating loop for gantt-chart and waiting-time
    start_count += time_list[k]
    gantt_chart_string += f"{process_list[k]}|" + f"{start_count}|"
    if(k!=length-1): # skipping the last process
        total_count += start_count

# print(total_count)
avg_waiting_time = total_count/num_process
print("The gantt chart will be: ",gantt_chart_string)
print(f"The average waiting time will be: {avg_waiting_time:.2f} ms")

# print(process_list)
# print(time_list)
# print(priority_list)

'''
4
p1 21 2
p2 3 1
p3 6 4
p4 2 3
'''