class Node:
    def __init__(self,value):
        self.next = None
        self.value = value
        self.prev = None


class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next=self.tail
        self.tail.prev = self.head
        


    def isEmpty(self) -> bool:
        return self.head.next == self.tail
        

    def append(self, value: int) -> None:
        newnode = Node(value)
        lastnode = self.tail.prev

        lastnode.next = newnode
        newnode.prev = lastnode
        newnode.next = self.tail
        self.tail.prev = newnode
        

    def appendleft(self, value: int) -> None:
        newnode = Node(value)
        firstnode = self.head.next
        
        self.head.next = newnode
        newnode.prev = self.head
        newnode.next = firstnode
        firstnode.prev = newnode
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        lastnode = self.tail.prev
        value = lastnode.value
        prevnode = lastnode.prev

        prevnode.next = self.tail

        self.tail.prev = prevnode
        return value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        firstnode = self.head.next
        value = firstnode.value

        nextval = firstnode.next

        nextval.prev = self.head
        self.head.next = nextval

        return value
        
