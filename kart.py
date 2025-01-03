class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0

    def append(self,data):
        self.size+=1
        new_node=node(data)

        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
    def push(self,data):
        self.size+=1
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node
    def print(self):
        temp=self.head
        while temp:
            print(temp.data,end=' ')
            temp=temp.next
    def insertAtpos(self,pos,data):
        if pos<1 or pos>self.size+1:
            return
        if pos==1:
            self.push(data)
            return
        if pos==self.size+1:
            self.append(data)
            return
        self.size+=1
        newnode=node(data)
        temp=self.head
        i=1
        while(i<pos-1):
            i+=1
            temp=temp.next
            rem=temp.next
        temp.next=newnode
        newnode.next=rem

    def deleteAtstart(self):
        if self.head is None:
            return
        self.head=self.head.next
        self.size-=1
    def deleteAtend(self):
        if self.head is None:
            return
        temp = self.head
        while temp.next and temp.next.next:
            temp=temp.next
        temp.next=None
        self.size-=1
        

        
LinkedList=LinkedList()
LinkedList.deleteAtend()
LinkedList.push(4)
LinkedList.push(5)
LinkedList.push(1)
LinkedList.push(6)
LinkedList.insertAtpos(5,77)
LinkedList.deleteAtend()
LinkedList.print()
            



'''LinkedList=LinkedList()
LinkedList.append(2)
LinkedList.append(8)
LinkedList.append(9)
LinkedList.append(12)
LinkedList.print() '''
            
            
                         
