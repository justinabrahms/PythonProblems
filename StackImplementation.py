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

