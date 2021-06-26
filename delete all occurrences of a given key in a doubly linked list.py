a=[]
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
        last=self.start
        ch=1
        while(last.next!=None):
            last=last.next
            ch=ch+1

        if pos==1:
            self.start=self.start.next

        elif pos==ch:
            tmp=self.start
            while(tmp.next!=None):
                pre=tmp
                tmp=tmp.next
            pre.next=None
            tmp.prev=None

        else:
            tmp = self.start
            for i in range(pos - 1):
                pre = tmp
                tmp = tmp.next
            pre.next = tmp.next
            tmp.next.prev = tmp



    def removeoccurence(self,value):
        tmp=self.start
        ch=1
        while(tmp!=None):
            if (tmp.data==value):
                a.append(ch)
                tmp=tmp.next
                ch=ch+1
            else:
                tmp=tmp.next
                ch=ch+1
        a.reverse()
        for i in a:
            list.delete(i)


    def display(self):
        tmp=self.start
        while(tmp!=None):
            print(tmp.data,end='<->')
            tmp=tmp.next
        print("NULL")

list=dll()
list.create(2)
list.create(2)
list.create(10)
list.create(8)
list.create(4)
list.create(2)
list.create(5)
list.create(2)
list.display()
list.removeoccurence(2)
list.display()