class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.length = k
        self.front_pointer = 0
        self.rear_pointer = 0
        

    def enQueue(self, value: int) -> bool:
        if self.q[self.rear_pointer] is None:
            self.q[self.rear_pointer] = value
            self.rear_pointer = (self.rear_pointer + 1) % self.length
            return True
        else:
            return False
        

    def deQueue(self) -> bool:
        if self.q[self.front_pointer] is None:
            return False
        else:
            self.q[self.front_pointer] = None
            self.front_pointer = (self.front_pointer + 1) % self.length
            return True
        

    def Front(self) -> int:
        return -1 if self.q[self.front_pointer] is None else self.q[self.front_pointer]

    
    def Rear(self) -> int:
        return -1 if self.q[self.rear_pointer-1] is None else self.q[self.rear_pointer-1]
    

    def isEmpty(self) -> bool:
        return self.front_pointer == self.rear_pointer and self.q[self.front_pointer] is None
        

    def isFull(self) -> bool:
        return self.front_pointer == self.rear_pointer and self.q[self.front_pointer] is not None
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()