class Stack():
    def __init__(self):
        self.arr=[]
    def Push(self,data):
        self.arr.insert(0,data)
    def Pop(self):
        return self.arr.pop(0)
    def isEmpty(self):
        if self.arr:
            return False
        else:
            return True
    def Peek(self):
        return(self.arr[0])
