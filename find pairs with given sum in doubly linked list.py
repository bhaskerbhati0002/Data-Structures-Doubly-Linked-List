a=[]
class node():
    def __init__(self,data):
        self.data=data
        self.next=None

class ll:
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

    def sumpair(self,value):
        first=self.start
        while first.data<value:
            second=first.next
            while second.data<value:
                if first.data+second.data==value:
                    print(f"({first.data},{second.data})")
                second=second.next
            first=first.next

    def display(self):
        tmp=self.start
        while(tmp!=None):
            print(tmp.data,end='<->')
            tmp=tmp.next
        print("NULL")

list=ll()
list.create(1)
list.create(2)
list.create(3)
list.create(4)
list.create(5)
list.create(6)
list.create(8)
list.create(9)
list.display()
list.sumpair(7)