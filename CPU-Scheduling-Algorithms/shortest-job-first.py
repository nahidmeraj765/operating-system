process_number = int(input("Total Number of Process: ")) # taking input for the number of total process

process_list = [] # defining an empty list to store the processes
burst_time_list = [] # defining an empty list to store the burst times

addition_flag = 0
total_flag = 0

for i in range(1,process_number+1):
    string_input,burst_time_input = input().split() # splitting both string and integer input with space
    burst_time = int(burst_time_input) # converting from string to integer
    process_list.append(string_input) # storing all process's (string) input into a list
    burst_time_list.append(burst_time) # storing all burst time's (integer) input into another list

process_list_length = len(process_list) # finding the length of the list named 'process_list'

# finding sorted burst time and process list respectively
for i in range(0,process_list_length):
    for j in range(i+1,process_list_length):
        if(burst_time_list[i]>burst_time_list[j]): # sorting the burst time list
            temp = burst_time_list[j]
            burst_time_list[j] = burst_time_list[i]
            burst_time_list[i] = temp

            temp1 = process_list[j] # sorting the process list based on the sorted burst time list
            process_list[j] = process_list[i]
            process_list[i] = temp1

# print(process_list)
# print(burst_time_list)

gantt_chart_string = "|0|"

for i in range(0,process_list_length): # generating loop for gantt-chart and waiting-time
    addition_flag += burst_time_list[i]
    gantt_chart_string += f"{process_list[i]}|" + f"{addition_flag}|"

    if i != process_number - 1: # skipping the last process
        total_flag += addition_flag

avg_waiting_time = total_flag/process_number

print("The gantt chart will be: ",gantt_chart_string)
print(f"The average waiting time will be: {avg_waiting_time:.2f} ms")

# 21 3 6 2

'''
4
p1 21
p2 3
p3 6
p4 2
'''
    

