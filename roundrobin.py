

#real life example - 'public feast'


def findWaitingTime(processes,n,burstTime,waitingTime,quantum):
    remainingBurstTime = burstTime.copy()
    time = 0
    gantt = []
    while (1): #this loop ensures we move about the list 'processes' in a round robin fashion
        done = True
        for i in range(n): #iterating through all the processes
            if (remainingBurstTime[i] > 0):
                #no else condition needed as if it's = 0 then the process if finished
                done = False
                gantt.append(processes[i])
                if (remainingBurstTime[i] > quantum):
                    time += quantum
                    remainingBurstTime[i] -= quantum
                else:
                    time += remainingBurstTime[i]
                    waitingTime[i] = time - burstTime[i]
                    remainingBurstTime[i] = 0
        if (done == True): #which means all remaining burst times are 0
            break #breaking out of the forever while loop
    return gantt

def findTurnAroundTime(n,burstTime,waitingTime,turnAroundTime):
    for i in range(n):
        turnAroundTime[i] = burstTime[i] + waitingTime[i]
    return turnAroundTime

def Calculate(processes,n,burstTime,quantum):
    waitingTime = [0,0,0,0,0]
    turnAroundTime = [0,0,0,0,0]
    totalWaitingTime = 0
    totalTurnAroundTime = 0
    gantt = findWaitingTime(processes,n,burstTime,waitingTime,quantum)
    findTurnAroundTime(n,burstTime,waitingTime,turnAroundTime)
    print('*'*75)
    print("| processes         | Burst Time        |Waiting Time        | Turn Around Time")
    for i in range(n):
        totalWaitingTime += waitingTime[i]
        totalTurnAroundTime += turnAroundTime[i]
        print("*"*75)
        print("| "+processes[i]+"                | "+str(burstTime[i])+"                | "+str(waitingTime[i])+"                   | "+str(turnAroundTime[i]))
    print('*'*75)
    print("\n")
    print(" Average Waiting Time :- ",totalWaitingTime/n)
    print(" Total Turn Around Time :- ",totalTurnAroundTime/n)
    print(" Gantt chart: ",gantt)
    

def main():
    processes = ['P1','P2','P3','P4','P5']
    n = len(processes)
    burstTime = [4,5,6,3,8]
    quantum = 4
    Calculate(processes,n,burstTime,quantum)

main()
