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

    def delete(self, pos):
        last = self.start
        ch = 1
        while (last.next != None):
            last = last.next
            ch = ch + 1

        if pos == 1:
            self.start = self.start.next

        elif pos == ch:
            tmp = self.start
            while (tmp.next != None):
                pre = tmp
                tmp = tmp.next
            pre.next = None
            tmp.prev = None

        else:
            tmp = self.start
            for i in range(pos - 1):
                pre = tmp
                tmp = tmp.next
            pre.next = tmp.next
            tmp.next.prev = tmp

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
list.create(6)
list.create(4)
list.create(5)
list.create(6)
list.create(7)
list.display()
list.delete(4)
print("after deleting")
list.display()
