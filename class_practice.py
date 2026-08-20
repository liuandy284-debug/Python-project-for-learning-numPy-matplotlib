import heapq

class Task:
    def __init__(self, name, priority, deadline):
        self.name = name
        self.priority = priority
        self.deadline = deadline

    def __lt__(self, other):   # def a comparison method to compare the priority of two tasks
        return self.priority < other.priority

    def __repr__(self):   # def what will be printed 
        return f"Task({self.name}, {self.priority}, {self.deadline})"

heap = []
task1 = Task("Task 1", 3, "2023-12-01")
task2 = Task("Task 2", 1, "2023-11-15")
task3 = Task("Task 3", 2, "2023-11-30")
task4 = Task("Task 4", 5, "2023-12-10")
task5 = Task("Task 5", 4, "2023-12-05")

heapq.heappush(heap, task1)
heapq.heappush(heap, task2)
heapq.heappush(heap, task3)
heapq.heappush(heap, task4)
heapq.heappush(heap, task5)

while(heap):   # Take out the tasks with lowest number each time
    task = heapq.heappop(heap)
    print(f"Task: {task.name}, Priority: {task.priority}, Deadline: {task.deadline}")