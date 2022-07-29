class Queue:
    def __init__(self): #initializing queue
        self.arr=[]
    def enqueue(self,data):     #add item in queue
        self.arr.append(data)
    def dequeue(self):              #delete item from queue
        if len(self.arr)!=0:
            return self.arr.pop(0)    
        else: return -1
    def show(self):         #show queue elements
        return self.arr
    def isEmpty(self):      #check either queue is empty or not
        if len(self.arr)<1:
            return True
        else: 
            return False
    def search(self,data):  #search item in queue
        loc=[]
        for i in range(len(self.arr)):
            if self.arr.pop(0)==data:
               loc.append(i)
        if len(loc)>0:
            return loc
        else: 
            return False
    def sort(self):
        self.arr.sort()