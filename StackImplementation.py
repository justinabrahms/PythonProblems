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


def paren_checker(string):
	
	stack = Stack()
	
	for char in string:
		if char == '(':
			stack.push(char)
		elif char == ')':
			if stack.isEmpty() == False:
				stack.pop()
			else:
				return 'Unbalanced'
	
	if stack.isEmpty() == False:
		return 'Unbalanced'
	else:
		return 'Balanced'


print 'Should be balanced: Is', paren_checker('(((())))(()((())()))')
print 'Should be unbalanced: Is', paren_checker('()))(()()(()')


