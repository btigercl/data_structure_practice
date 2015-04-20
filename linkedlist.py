class Node(ojbect):
	#creates node 
	def __init__(self, data):
		self.data = data
		self.nextNode = nextNode

class linkedList(ojbect):
	#creates linked list
	def __init__(self, head=None):
		self.head = head

def insert(self, node):
	#insert into list by moving old head over one and makes new node the head
	if not self.head:
		self.head = node
	else:
	 	#set new nodes pointer to old head
	 	node.nextNode = self.head
	 	#reset head to new node
	 	self.head = node

def search(self, lList, Node):
	#searches each node for value O(n)
	if self.head == Node:
		return self.head
	else:
		if lList.head.nextNode:
			self.search(linkedList(lList.head.nextNode), Node)
		else :
			raise ValueError("Node not in Linked List")

def size(self):
	current = self.head
	size = 0
	while current is not None:
		size += 1
		current = current.nextNode
	return size 


def delete(self, node):
	if self.size() == 0:
		raise ValueError("List is empty")	
	else:
		current = self.head
		previous = None
		found = False
		while not found:
			if current == node:
				found = True
			elif current is None:
				raise ValueError("Node not in Linked List")
			else:
				previous = current
				current = current.nextNode
		if previous is None:
			self.head = current.nextNode
		else:
			previous.nextNode = current.nextNode


#Reverse Singly Linked List Python
class Node:
  def __init__(self,val,nxt):
    self.val = val
    self.nxt = nxt
 
def prnt(n):
  nxt = n.nxt
  print n.val
  if(nxt is not None):
    prnt(nxt)
 
#Iterative
def reverse(n):
  last = None
  current = n
 
  while(current is not None):
    nxt = current.nxt
    current.nxt = last 
    last = current
    current = nxt
 
  return last
 
#Recursive
def recurse(n,last):
  if n is None:
    return last
  nxt = n.nxt
  n.nxt = last
  return recurse(nxt, n)
 
 
n0 = Node(4,None)
n1 = Node(3,n0)
n2 = Node(2,n1)
n3 = Node(1,n2)
 
#l = reverse(n3)
prnt(n3)
result = recurse(n3, None)
prnt(result)
