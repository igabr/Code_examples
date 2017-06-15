class Node(object):

	def __init__(self, data=None, pointer=None):
		self.__data = data
		self.__pointer = pointer

	def get_data(self):
		return self.__data

	def get_pointer(self):
		return self.__pointer

	def set_pointer(self, new_pointer):
		self.__pointer = new_pointer

class LinkedList(object):

	def __init__(self, root=None):
		self.__root = root

	def insert(self, data):
		new_node = Node(data)
		new_node.set_pointer(self.__root)
		self.__root = new_node

	@property
	def size(self):
		current = self.__root
		count = 0

		while current:
			count += 1
			current = current.get_pointer()
		return count
	
	def search(self, data):
		current = self.__root

		while current:
			if current.get_data() == data:
				return "item is in lst"
			else:
				current = current.get_pointer()
		return "Item not in lst"

	@property
	def print_lst(self):
		lst = []
		current = self.__root
		while current:
			lst.append(str(current.get_data()))
			current = current.get_pointer()
			print( '--'.join(lst))
