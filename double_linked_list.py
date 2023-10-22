class Node:

  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None


class Dll:

  def __init__(self):
    self.head = None

  def display(self):
    if self.head is None:
      print("Empty List")
    else:
      temp = self.head
      while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next


L = Dll()

n1 = Node(10)
L.head = n1
n2 = Node(20)
n1.next = n2
n2.prev = n1
n3 = Node(30)
n2.next = n3
n3.prev = n2
n4 = Node(40)
n3.next = n4
n4.prev = n3
n5 = Node(50)
n4.next = n5
n5.prev = n4
L.display()
