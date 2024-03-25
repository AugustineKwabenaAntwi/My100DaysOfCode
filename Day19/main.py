class Node:
    #creating node first
    def __init__(self,data):
        self.data = data
        self.ref = None

#creating class to link list
class LinkedList:
    def __init__(self):
          self.head=None
# constructor for traversal
          #check if linked list is empty
          #if it is not empty
    def print_LL(self):
        if self.head is None:
            print("Linked List is empty")
        else: 
            n = self.head
            while self.head is not None:
                print(n.data,"-->",end=" ")
                n=n.ref

    def add_begin(self,data):
        new_node = Node(data) #creating the object from the node class
        new_node.ref = self.head #pointing the ref to the existing head node
        self.head = new_node #making new node the head node

    def add_end(self,data):
        new_node = Node(data) #creating the object from the node class

        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n=n.ref
            n.ref = new_node #outside the loop n.ref becomes newly created node

    def add_after(self,data,x):
        n = self.head       
        while n is not None: # two ways to come out of loop 1. when we search the entire till we get to null
            if x==n.data: # 2. use a break statement once we find x
                break
            n = n.ref

        if n is None:
            print("node is not present")
        # u have found the x (down)    
        else:
            new_node = Node(x)
            new_node.ref = n.ref
            n.ref = new_node