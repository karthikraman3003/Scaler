class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class ll:

    def __init__(self):
        self.head=None
        self.length=0

    # def append(self,data):
    #     node=Node(data)
    #
    #     if self.head ==None:
    #         self.head=node
    #         return
    #
    #     lastnode=self.head
    #
    #     while lastnode.next:
    #         lastnode=lastnode.next
    #
    #     lastnode.next=node


    # 1->2->3
    # 1->2->5->3
    def insert_node(self,position, value):
        node = Node(value)
        if position==1:
            self.head=node
        else:
            position_node=self.head
            count=1
            while count<position-1:
                position_node=position_node.next
                count+=1
            curr=position_node.next
            position_node.next=node
            node.next=curr
        self.length+=1

    # def lenght(self):
    #     traversal=self.head
    #     count=0
    #     while traversal:
    #         count+=1
    #         traversal=traversal.next
    #     print('\n')
    #     return count
    # 1->2->3->4->5
    # 1->2->4->5
    def delete_node(self, position):
        if position > (self.length):
            return
        else:
            temp = self.head
            if position == 1:
                newHead = temp.next
                self.head = newHead

            else:
                count = 1
                while count < position - 1:
                    temp = temp.next
                    count += 1

                new_node = temp.next.next
                temp.next = new_node

            self.length -= 1

    def print_ll(self):

        curr_node=self.head

        while curr_node:
            print(str(curr_node.data),end=' ')

            curr_node=curr_node.next
        if curr_node:
            print(curr_node.data,end="")
        print()




obj=ll()
    #
    # obj.insert_node(1,1)
    # obj.insert_node(2, 2)
    # obj.insert_node(3, 3)
    # obj.insert_node(4, 4)
    # obj.insert_node(5, 5)
    # obj.insert_node(2,8)
    # obj.print()
    # obj.delete_node(1)
    # print('\n')
    # obj.print()
    # print('\n')
    # obj.delete_node(3)
    # obj.print()


ll = ll()

def insert_node(position, value):
    return ll.insert_node(position, value)


def delete_node(position):
    return ll.delete_node(position)


def print_ll():
    return ll.print_ll()
