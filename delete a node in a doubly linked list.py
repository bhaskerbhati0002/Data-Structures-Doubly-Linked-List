class node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dll:
    def __init__(self):
        self.start=None
    def create(self,value):
        newnode=node(value)
        if(self.start==None):
            self.start = newnode
        else:
            tmp=self.start
            while (tmp.next != None):
                tmp = tmp.next
            tmp.next = newnode
            newnode.prev=tmp
    def delete(self, value):
        tmp=self.start
        while(tmp.next!=None):
            pre=tmp
            tmp=tmp.next

        if (self.start.data == value):#if data is at first pos
            self.start=self.start.next

        elif (tmp.data==value):#if data is at last pos
            pre.next=None

        else:
            tmp=self.start
            while(tmp.data!=value):
                pre=tmp
                tmp=tmp.next
            pre.next=tmp.next
            tmp.next.prev=pre


    def display(self):
        tmp=self.start
        while(tmp!=None):
            print(tmp.data,end='<->')
            tmp=tmp.next
        print("NULL")

list=dll()
list.create(1)
list.create(2)
list.create(3)
list.create(4)
list.create(5)
list.create(6)
list.display()
list.delete(4)
print("after deleting 4")
list.display()
list.delete(1)
print("after deleting 1")
list.display()
list.delete(6)
print("after deleting 6")
list.display()