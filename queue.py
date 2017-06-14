class Queue(object):
	def __init__(self):
		self.__queue = []

	@property
	def view_all(self):
		if len(self.__queue) == 0:
			print("The Queue is empty")
		for i, val in enumerate(self.__queue):
			print(val)
			print("--")
	
	def push(self, val):
		self.__queue.append(val)
		return "added {} to the queue".format(val)

	@property
	def remove(self):
		if len(self.__queue) > 0:
			item = self.__queue.pop(0)
			print(" You just popped out: ", item)
		print("There is nothing to remove!")

	@property
	def size(self):
		print(len(self.__queue))

	@property
	def peek(self):
		print(self.__queue[0])