class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new):
        new = Node(new)
        new.next = self.head
        self.head = new

    def append(self,new):
        new = Node(new)
        cur_node = self.head
        if (cur_node is None) :
            self.head = new
            return
        while(cur_node.next):
            cur_node = cur_node.next
            print(cur_node.data)
        cur_node.next = new

    def printList(self):
        cur_node = self.head
        while(cur_node):
            print(cur_node.data,end=" ")
            cur_node = cur_node.next
        print('')

if __name__ =='__main__':
    node = LinkedList()
    node.append(3)
    node.append(4)
    node.printList()
