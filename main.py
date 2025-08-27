class Process:
    def __init__(self, pid, task, priority, time):
        self._pid = pid
        self._task = task
        self._priority = priority
        self._time = time
        
    def __str__(self):
        return f"Process ID: {self._pid}"
    
class Node:
    def __init__(self, process):
        self._process = process
        self.next = None
    def get_process(self):
        return self._process
    def __str__(self):
        return str(self._process)
    
class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def add_process(self, process):
        newNodeProcess = Node(process)
        if self._tail is None:
            self._tail = newNodeProcess
            self._head = newNodeProcess
        else:
            self._tail.next = newNodeProcess
            self._tail = self._tail.next
            
    def add_processAtMain(self, process):
        newNodeProcess = Node(process)
        if self._head is None:
            self._head = newNodeProcess
            self._tail = newNodeProcess
        else:
            newNodeProcess.next = self._head
            self._head = newNodeProcess
    
    def remove_process(self):
        if self._head is not None:
            removed_process = self._head
            self._head = self._head.next
            
            if self._head is None:
                self._tail = None
                
            return removed_process
        return None
    
    def getAllProcesses(self):
        current = self._head
        processes = []
        while current is not None:
            processes.append(current.get_process())
            current = current.next
        return processes
    
class Stack:
    def __init__(self):
        self._size = 0
        self._processList = LinkedList()
        
    def push(self, process):
        self._processList.add_processAtMain(process)
        
    def pop(self):
        return self._processList.remove_process()
    
    def getAllProcesses(self):
        return self._processList.getAllProcesses()
    
class Queue:
    def __init__(self):
        self._size = 0
        self._processList = LinkedList()
        
    def enqueue(self, process):
        self._processList.add_process(process)
        self._size += 1
    
    def is_empty(self):
        return self._processList._head is None
    
    def dequeue(self):
        if not self.is_empty():
            inQueueProcess = self._processList.remove_process()
            if inQueueProcess is not None:
                self._size -= 1
                return inQueueProcess.get_process() if inQueueProcess else None
        return None
    
    def peek(self):
        if not self.is_empty():
            return self._processList._head.get_process()
        return None
    
    def getAllProcesses(self):
        return self._processList.getAllProcesses()
    
def prioritySort(processList):
    if len(processList) <= 1:
        return processList
    
    mid = len(processList) // 2
    left = prioritySort(processList[:mid])
    right = prioritySort(processList[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        # Lower priority number = higher priority
        # If same priority, sort by time (smaller time first)
        
        if (left[i]._priority < right[j]._priority) or (
            left[i]._priority == right[j]._priority and left[i]._time < right[j]._time):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result    

def runSimulation():
    # Create processes running in simulation the system
    processes = [
        Process(101, "explorer.exe", 5, 50),
        Process(102, "python_script.py", 4, 30),
        Process(103, "db_service", 0, 120), # High priority
        Process(104, "anti_virus_scan", 0, 300), # High priority
        Process(105, "idle_task", 2, 100), #priority = 106 and time = 106
        Process(106, "render_video.mov", 2, 100), #priority = 105 and time = 105
        Process(107, "email_client", 3, 80),
    ]
    
    # Create a queue and add all processes
    processQueue = Queue()
    for process in processes:
        processQueue.enqueue(process)
        
    # Create a stack for completed processes
    completedStack = Stack()
    
    # Simulation Display
    print("--- Initial Ready Queue ---")
    queueProcesses = processQueue.getAllProcesses() # see all processes in queue
    print(f"    [Queue: {', '.join(str(p) for p in queueProcesses)}]")
    print()
    
    print("    --- Running Simulation ---")
    print("    Sorting processes based on priority...") 
    # Get all processes from queue for sorting
    allProcesses = []
    while not processQueue.is_empty():
        allProcesses.append(processQueue.dequeue())
        
    sortedProcesses = prioritySort(allProcesses)
    
    # Execute processes in order
    for process in sortedProcesses:
        print(f"    Executing {process._task} (PID: {process._pid}, P:{process._priority}, T:{process._time})")
        completedStack.push(process)
    print()
    
    print("    --- Simulation Complete ---")
    print("    Ready Queue is empty.")
    completedProcesses = completedStack.getAllProcesses()
    print(f"    Completed Stack: [{', '.join(str(p) for p in completedProcesses)}]")
    print()
    
    print("    --- Performing Rollback ---")
    # Rollback the last completed process
    rolledBackProcess = completedStack.pop()._process
    print(f"    Rolled back {rolledBackProcess._task} (PID: {rolledBackProcess._task}). It is now back in the ready queue.")
    processQueue.enqueue(rolledBackProcess) # Simulation rollback
    print()
    
    print("    --- Final State ---")
    finalQueueProcesses = processQueue.getAllProcesses()
    print(f"    Ready Queue: [Queue: {', '.join(str(p) for p in finalQueueProcesses)}]")
    finalCompletedProcesses = completedStack.getAllProcesses()
    print(f"    Completed Stack: [{', '.join(str(p) for p in finalCompletedProcesses)}]")
                
if __name__ == "__main__":
    runSimulation()