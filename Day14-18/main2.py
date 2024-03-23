#create nodes
#create linked list 
# Add nodes to linked list
#Print linked list

class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        

class LinkedList:
    def __init__(self):
        self.head = None #first head node must be empty

    def insert_at_beginning(self,data):
        node = Node(data, self.head)   #next value of node will be the current head
        self.head = node

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
# iterate over each element and print
        itr = self.head
        llstr=''
        while itr:
            llstr=llstr+str(itr.data)+'-->'
            itr = itr.next  

        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)    

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(8)
    ll.insert_at_beginning(89)
    ll.print()