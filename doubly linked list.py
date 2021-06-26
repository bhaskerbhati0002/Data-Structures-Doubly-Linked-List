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
    def delete(self):
        if (self.start == None):
            print('list is empty')
        else:
            self.start = self.start.next

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
list.display()