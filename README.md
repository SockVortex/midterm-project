# midterm-project

Midterm Project sent to ผศ.ดร. ยุทธนา เจวจินดา


## Table of Contents

- [ℹ️Introduction](#ℹ️introduction)
- [📝Algorithm Details](#📝algorithm-details)
- [🧑‍💻Explain code](#🧑‍💻explain-code)
- [🪴Usage Example](#🪴usage-example)
- [👥Authors](#authors)

---

## ℹ️Introduction
ในระบบปฏิบัติการ (Operating System) ส่วนที่เรียกว่า "Scheduler" มีหน้าที่สำคัญในการตัดสินใจว่าจะให้โปรเซส (Process) ใดได้ใช้ CPU เป็นลำดับถัดไป เพื่อให้ระบบทำงานได้อย่างมีประสิทธิภาพและตอบสนองได้ดีที่สุด การสร้างโปรแกรมจำลอง Scheduler ที่สามารถจัดการคิวของโปรเซส, จัดลำดับความสำคัญ, และบันทึกประวัติการทำงาน

เป้าหมาย: พัฒนาระบบจำลองที่รับชุดคำสั่งของโปรเซสเข้ามา, จัดการด้วยคิว, จัดเรียงตามอัลกอริธึมที่กำหนด, และสามารถย้อนกลับสถานะการทำงานล่าสุดได้

---



## 📝Algorithm Details
- LinkedList Lecture 7
- Class and Object Lecture 6
- ADT and Stack Data Structure Lecture 6
- Recursive functions and Merge Sort Lecture 5
- function Lecture 3
- Basic Python Syntax Lecture 2
- Python Basics Lecture 1
---

## 🧑‍💻Explain code
```bash
class Process:
    def __init__(self, pid, task, priority, time):
        self._pid = pid
        self._task = task
        self._priority = priority
        self._time = time
        
    def __str__(self):
        return f"Process ID: {self._pid}"
```
จากโค้ดในส่วนนี้เป็นการใช้ 
- Class and Object ADT and Stack Data Structure Lecture 6

เป็นการสร้าง Class ที่ชื่อว่า Process โดยเมธอด__init__ทำหน้าที่นำค่าที่รับเข้ามาผ่าน Parameters (พารามิเตอร์) ไปเก็บไว้เป็น Attribute (คุณสมบัติ) ของ Object ซึ่งจากโค้ด Class Process จะมี Attribute (คุณสมบัติ)
- pid = หมายเลขประจำตัวโพรเซส
- task = ชื่องานหรือคำอธิบายของโพรเซส
- priority = ระดับความสำคัญ **ยิ่งค่าระดับความสำคัญน้อย ระดับความสำคัญจะสูงมาก**
- time (ms) = เวลาที่โพรเซสต้องใช้ในการทำงาน **มีหน่วยเป็น ms**

__str__เป็นเมธอดพิเศษ หน้าที่ของมันคือการกำหนดว่า เมื่อ Object นี้ถูกแปลงเป็นข้อความ (String) ควรจะแสดงผลออกมาเป็นอย่างไร แล้วในที่นี้มันจะแสดงออกมาเป็น
    
    Output: Process ID: xxx
---
```bash
class Node:
    def __init__(self, process):
        self._process = process
        self.next = None
    def get_process(self):
        return self._process
    def __str__(self):
        return str(self._process)
```
จากโค้ดในส่วนนี้เป็นการใช้
- LinkedList Lecture 7

คลาส Node นี้ทำหน้าที่เป็น "กล่อง" หรือ "ตู้คอนเทนเนอร์สำหรับเก็บข้อมูล" แต่ความสามารถมันถูกออกแบบมาเพื่อ เชื่อมต่อกันเป็นสาย โดยเมธอด__init__ทำหน้าที่นำค่าที่รับเข้ามาผ่าน Parameters (พารามิเตอร์) ไปเก็บไว้เป็น Attribute (คุณสมบัติ) ของ Object ซึ่งจากโค้ด Class Node จะมี Attribute (คุณสมบัติ)
- self._process = process
    - นำ Process object ที่รับเข้ามาเก็บไว้ใน Attribute
- self.next = None
    - นี่เป็นส่วนสำคัญ สร้าง Attribute ที่ชื่อว่า next ขึ้นมาเพื่อใช้เป็น "ข้อต่อ" หรือ "ตัวชี้" (Pointer/Reference) ไปยัง Node ตัวถัดไป
---
```bash
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
```
จากโค้ดในส่วนนี้เป็นการใช้
- LinkedList Lecture 7

Class LinkedList นี้เป็นส่วนที่น่าสนใจที่สุดเพราะมันคือการนำ Node มาประกอบร่างสร้างเป็นโครงสร้างข้อมูล
ที่ทำหน้าที่เป็น "อินเทอร์เฟซ" (Interface) หรือเป็นตัวกลางให้เราสามารถทำงานกับโครงสร้างข้อมูลที่ซับซ้อน (อย่าง Linked List) ได้ง่ายๆ โดยที่เราไม่จำเป็นต้องไปยุ่งกับ Node หรือ .next โดยตรงในโค้ดหลักของเรา
- มีเมธอด (Method)
    - add_process: เป็นการนำ process ใหม่มาพ่วงต่อท้ายขบวน
    - add_processAtMain: เป็นการนำ process ใหม่มาเสียบที่หัวขบวน
    - remove_process: เป็นการถอด process ที่หัวขบวนออกไป

อธิบายโค้ด remove_process เพิ่มเติม
```bash
def remove_process(self):
        # if self._head is not None:
        #     removed_process = self._head
        #     self._head = self._head.next
            
            if self._head is None:
                self._tail = None
                
        #     return removed_process
        # return None
```
ตรงนี้เป็นส่วนที่หน้าสนใจหลังจากเลื่อน _head ไปแล้ว ให้ตรวจสอบว่า _head กลายเป็น None หรือไม่? ซึ่งจะเกิดขึ้นเมื่อ List มี Node แค่ตัวเดียวพอเอาออกไป _head ก็จะชี้ไปที่ None

self._tail = None: ถ้าเป็นกรณีนี้จริง แสดงว่า List ได้กลายเป็นว่างเปล่าแล้ว จึงต้องอัปเดต "ท้ายขบวน" (_tail) ให้เป็น None ด้วย เพื่อรักษาสถานะของ List ให้ถูกต้อง
    
- - getAllProcesses: เป็นการดู process ทั้งหมดในขบวน

อธิบายโค้ด getAllProcesses เพิ่มเติม
```bash
def getAllProcesses(self):
        current = self._head
        processes = []
        while current is not None:
            processes.append(current.get_process())
            current = current.next
        return processes
```
เมธอดนี้ใช้สำหรับ ดึงข้อมูล Process ทั้งหมด ที่อยู่ใน List ออกมาเป็น Python List ธรรมดา

---
```bash
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
```
จากโค้ดในส่วนนี้เป็นการใช้
- LinkedList Lecture 7
- ADT and Stack Data Structure Lecture 6

คลาส Stack เป็นการนำสิ่งที่สร้างไว้ก่อนหน้า (LinkedList) มาสร้างเป็นโครงสร้างข้อมูลอีกชนิดหนึ่ง หลักการสำคัญของ Stack คือ "เข้าทีหลัง ออกก่อน" หรือ LIFO (Last-In, First-Out)
- มีเมธอด(Method)
    - push: เป็นการวางข้อมูลลงบนสุดของ Stack
    - pop: เป็นการหยิบข้อมูลจากบนสุดของ Stack
    - getAllProcesses: เป็นการดูข้อมูลทั้งหมดใน Stack

จุดหน้าสนใจของ getAllProcesses ส่งต่องานนี้ไปให้ LinkedList

---
```bash
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
```
จากโค้ดในส่วนนี้เป็นการใช้
- LinkedList Lecture 7
- ADT and Stack Data Structure Lecture 6

class Queue เป็นอีกหนึ่งโครงสร้างข้อมูลที่สำคัญ โค้ดนี้แสดงให้เห็นถึงการนำ LinkedList มาประยุกต์คลาส Queue นี้จำลองโครงสร้างข้อมูลที่เรียกว่า "คิว" หรือ "แถวคอย" ซึ่งเป็นสิ่งที่เราคุ้นเคยกันดีในชีวิตประจำวัน เช่น การต่อแถวซื้อตั๋วหนัง หรือการรอคิวชำระเงินหลักการสำคัญของ Queue คือ "เข้าก่อน ออกก่อน" หรือ FIFO (First-In, First-Out)
- มีเมธอด(Method)
    - enqueue: เป็นการเข้าคิว
    - is_empty: ตรวจสอบว่าคิวว่างหรือไม่
    - dequeue: การออกจากคิว
    - peek: ดูหัวคิว
    - getAllProcesses: ดูข้อมูลทั้งหมดในคิว

---
```bash
def prioritySort(processList):
    if len(processList) <= 1:
        return processList
    
    mid = len(processList) // 2
    left = prioritySort(processList[:mid])
    right = prioritySort(processList[mid:])
    
    return merge(left, right)
```
จากโค้ดในส่วนนี้เป็นการใช้
- Recursive functions and Merge Sort Lecture 5

prioritySort เป็นฟังก์ชันที่ใช้หลักการ "แบ่งและเอาชนะ" (Divide and Conquer) เพื่อจัดเรียงข้อมูลใน processList

---
```bash
def merge(left, right):
    result = [] #list ว่างสำหรับเก็บผลลัพธ์ที่ผสานกันแล้ว 
    #สร้าง indexหรือ "ตัวชี้" สำหรับ list left (i) และ right (j)
    # โดยเริ่มที่ตำแหน่งแรกสุดของทั้งสอง list
    i = j = 0
    
    # วนลูปเพื่อเปรียบเทียบ item จาก left และ right
    # ลูปจะทำงานตราบใดที่ยังมี item ให้เปรียบเทียบเหลืออยู่ใน *ทั้งสอง* list
    while i < len(left) and j < len(right):
        # Lower priority number = higher priority
        # If same priority, sort by time (smaller time first)
        
        # เงื่อนไขที่ 1: priority ของ item ใน left น้อยกว่า  ของ right หรือไม่?
        # เงื่อนไขที่ 2: หรือถ้า priority เท่ากันให้ดูที่ time: time ของ item ใน left น้อยกว่า (มาก่อน) ของ right หรือไม่?
        if (left[i]._priority < right[j]._priority) or (
            left[i]._priority == right[j]._priority and left[i]._time < right[j]._time):
            # ถ้าเงื่อนไขเป็นจริง (item จาก left สำคัญกว่า)
            # ให้นำ item จาก left[i] ไปต่อท้ายใน result
            result.append(left[i])
            # แล้วเลื่อนตัวชี้ของ list left ไปยังตำแหน่งถัดไป
            i += 1
        else:
        # ถ้าเงื่อนไขเป็นเท็จ (หมายความว่า item จาก right สำคัญกว่าหรือเท่ากัน)
            # ให้นำ item จาก right[j] ไปต่อท้ายใน result
            result.append(right[j])
            # แล้วเลื่อนตัวชี้ของ list right ไปยังตำแหน่งถัดไป
            j += 1

    #นำ item ที่เหลือทั้งหมดใน list left (ถ้ามี) ไปต่อท้าย result       
    result.extend(left[i:])
    # นำ item ที่เหลือทั้งหมดใน list right (ถ้ามี) ไปต่อท้าย result
    result.extend(right[j:])
    #คืนค่า list ใหม่ที่ผ่านการผสานและเรียงลำดับเรียบร้อยแล้ว
    return result  
```
จากโค้ดในส่วนนี้เป็นการใช้
- Recursive functions and Merge Sort Lecture 5

ฟังก์ชัน merge เป็นส่วนประกอบที่สำคัญที่สุดของอัลกอริทึมการจัดเรียงข้อมูลที่เรียกว่า Merge Sort ทำหน้าที่รับ list ที่ผ่านการเรียงลำดับมาแล้ว 2 list โดยเงื่อนไขการจัดเรียง
1) จัดเรียงตาม priority(ระดับความสำคัญ) ยิ่งค่าระดับความสำคัญน้อย ระดับความสำคัญจะสูงมาก จะต้องมาก่อน
2) ถ้าระดับความสำคัญเท่ากัน ให้เรียงจากเวลาน้อยที่สุด

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

## Output

---

## Authors
- 👤670910535 นายธนพนธ์ เจริญสุข

- 👤670910566 นายเอกนฤน คนใหญ่

- 👤670910778 นายกฤตภาส จงชาญสิทโธ

---
