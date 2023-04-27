class Node:

    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:

    def __init__(self):

        self.front=None
        self.rear=None
        self.size=0


    def push(self,data):
        node=Node(data)
        self.size += 1

        if self.rear is None:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node

    def pop(self):
        if self.size==0:
            return None
        self.size-=1

        temp=self.front
        self.front=temp.next

        if self.front is None:
            self.rear=None
        return temp.data
    def peek(self):
        return self.front.data

    def isempty(self):
        if self.size==0:
            return True
        return False

    def getallelements(self):
        if self.front is None:
            return []

        result=[]
        temp1=self.front
        while temp1 is not None:
            result.append(temp1.data)
            temp1=temp1.next
        return result

queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.pop())
print(queue.peek())
print(queue.isempty())

elements = queue.getallelements()
print(elements) # Output: [1, 2, 3]
