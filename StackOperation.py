class Stack:
    def __init__(self):
        self.arr=[]
    def push(self,data):
        self.arr.append(data)
    def pop(self):
        return self.arr.pop(len(self.arr)-1) if len(self.arr)>0 else -1
    def show(self):
        return self.arr
    def is_Empty(self):
        return True if len(self.arr)<1 else False
    def search(self,data):
        loc= []
        for i in range(len(self.arr)):
            if self.arr.pop(len(self.arr)-1)==data:
                loc.append(i)
        return True if len(loc)>0 else False
    def sort(self):
        self.arr.sort()
        

    
        