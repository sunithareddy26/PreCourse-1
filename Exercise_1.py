class myStack:
     def __init__(self):
         self.list = []         
     def isEmpty(self):
         if len(self.list) <= 0:
	     return True
	 else:
	     return False         
     def push(self, item):
         self.list.append(item)

     def pop(self):
	 return self.list.pop()        
        
     def peek(self):
	 return self.list[-1]
        
     def size(self):
         return len(self.list)
         
     def show(self):
         for item in self.list:
             print("List item: %s" % (item ))
         

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())
