# midterm-project

Midterm Project sent to ผศ.ดร. ยุทธนา เจวจินดา


## สารบัญ

- [ℹ️Introduction](#ℹ️introduction)
- [รายละเอียดอัลกอริธึม](#รายละเอียดอัลกอริธึม)
- [🪴Usage Example](#🪴usage-example)
- [👥Authors](#👥authors)

---

## ℹ️Introduction
ในระบบปฏิบัติการ (Operating System) ส่วนที่เรียกว่า "Scheduler" มีหน้าที่สำคัญในการตัดสินใจว่าจะให้โปรเซส (Process) ใดได้ใช้ CPU เป็นลำดับถัดไป เพื่อให้ระบบทำงานได้อย่างมีประสิทธิภาพและตอบสนองได้ดีที่สุด การสร้างโปรแกรมจำลอง Scheduler ที่สามารถจัดการคิวของโปรเซส, จัดลำดับความสำคัญ, และบันทึกประวัติการทำงาน

เป้าหมาย: พัฒนาระบบจำลองที่รับชุดคำสั่งของโปรเซสเข้ามา, จัดการด้วยคิว, จัดเรียงตามอัลกอริธึมที่กำหนด, และสามารถย้อนกลับสถานะการทำงานล่าสุดได้

---



## รายละเอียดอัลกอริธึม
- LinkedList Lecture 7
- Class and Object Lecture 6
- ADT and Stack Data Structure Lecture 6
- Recursive functions and Merge Sort Lecture 5
- function Lecture 3
- Basic Python Syntax Lecture 2
- Python Basics Lecture 1
---

## 🪴Usage Example
```bash
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
```

---

## 👥Authors
    670910566 นายเอกนฤน คนใหญ่
    670910778 นายกฤตภาส จงชาญสิทโธ
---
