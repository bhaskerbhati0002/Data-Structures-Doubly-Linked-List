class node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dll:
    def __init__(self):
        self.start=None

    def sortedinsert(self,value):
        newnode=node(value)
        if(self.start==None):
            self.start = newnode
        elif newnode.data<=self.start.data:
            newnode.next=self.start
            self.start=newnode
        else:
            tmp=self.start
            while tmp.next!=None and tmp.next.data<newnode.data:
                tmp=tmp.next
            newnode.next=tmp.next
            newnode.prev=tmp
            tmp.next = newnode

    def display(self):
        tmp=self.start
        while(tmp!=None):
            print(tmp.data,end='<->')
            tmp=tmp.next
        print("NULL")

list=dll()
list.sortedinsert(3)
list.sortedinsert(2)
list.sortedinsert(5)
list.sortedinsert(8)
list.sortedinsert(1)
list.sortedinsert(10)
list.sortedinsert(12)
list.display()
list.sortedinsert(9)
print("after inserting")
list.display()