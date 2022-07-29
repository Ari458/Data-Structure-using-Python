class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
    def return_head(self):
        if self.head is None:
            return -1
        else:
            return self.head.data    
    def return_tail(self):
        if self.head is None:
            return -1
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            return temp.data    
    def length(self):
        count=0
        temp=self.head
        while temp!=None:
            temp=temp.next
            count+=1
        return count    
    def travarse(self):
        item=[]
        temp=self.head
        while temp!=None:
            item.append(temp.data)
            temp=temp.next
        return item    
    def add_Front(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head=newNode
    def add_End(self,data):
        newNode=node(data)
        if self.head==None:
            self.head=newNode
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode    
    def add_at(self,data,index):
        newNode=node(data)
        if index==1:
            self.add_Front(data)
        elif self.head is None:
             return -1
        else:
            if index>self.length():
                return -1
            else:
                temp2=self.head
                temp1=self.head
                for i in range(1,index):
                    temp1=temp2
                    temp2=temp2.next
                temp1.next=newNode
                newNode.next=temp2            
    def del_End(self):
        temp=self.head
        if temp==None:
            return -1
        else:
            p=temp
            while temp.next!=None:
                p=temp
                temp=temp.next
            temp_data=temp.data
            if p==temp:
                self.head=None
            else:
                p.next=None
            return temp_data
    def del_Front(self):
        if self.head is None:
            return -1
        else:
            temp_data=self.head.data
            self.head=self.head.next
            return temp_data
    def del_at(self,index):
        if self.head is None:
            return -1
        else:
            if index==1:
                self.del_Front
            elif index>self.length():
                return -1
            else:
                temp2=self.head
                for i in range(1,index):
                    temp1=temp2
                    temp2=temp2.next
                temp_data=temp2.data
                temp1.next=temp2.next
        return temp_data    
    def search(self,data):
        count=0
        pos=1
        loc=[]
        for i in self.travarse():
            if i==data:
                count+=1
                loc.append(pos)
            pos+=1    
        if count>0:
            return loc
        else:
            return -1        
    def del_by_val(self,data):
            temp1=temp2=self.head
            for i in range(1,self.length()+1):
                if temp2.data==data:
                    if i==1:
                        self.del_Front()
                    elif i==self.length():
                        self.del_End
                    else:    
                        temp1.next=temp2.next
                    return i
                else:    
                    temp1=temp2
                    temp2=temp2.next    
            return -1        




    

    