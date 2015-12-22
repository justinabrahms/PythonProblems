# Algorithms & Data Structures: Implementing a Stack
# 12.21.15
# @totallygloria


class Stack():
	
	def __init__(self):
		self.items = []
		
	def push(self, item):
		self.items.append(item)
		return self.items
	
	def pop(self):
		return self.items.pop()
		
	def peek(self):
		return self.items[-1]
		
	def isEmpty(self):
		return self.items == []
		
	def size(self):
		return len(self.items)


def rev_string(inputString):
	
	stack = Stack()
	new_string = str()
	
	for char in inputString:
		stack.push(char)
	
	while stack.isEmpty() == False:
		new_string += stack.pop()
		
	return new_string	


if rev_string('weener') == 'reneew':
	print "string reversed:", rev_string('weener')
else:
	print "something's fucked"
