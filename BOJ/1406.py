import sys

input = sys.stdin.readline

class Node:
  def __init__(self, data):
    self.prev = None
    self.next = None
    self.data = data

class linkedList:
  def __init__(self, data):
    head = Node("head")
    self.head = head
    self.tail = head
    self.count = 0
    self.current = self.head

    for i, v in enumerate(data):
      self.append(v)


  def append(self, data):
    node = Node(data)
    node.prev = self.tail
    self.tail.next = node
    self.tail = node

    self.current = node

    self.count += 1

  def delete(self):
    pop_data = self.current

    if pop_data == self.head:
      self.head = self.current.next  
    elif pop_data == self.tail:
      self.tail = self.current.prev
    else:
      self.current.prev.next = self.current.next
      self.current.next.prev = self.current.prev
    
    self.current = self.current.prev
    
    self.count -= 1

    return pop_data
  
  def insert(self, data):  
    if self.current == self.tail:
      self.append(data)
      return

    nextNode = self.current.next
    node = Node(data)

    self.current.next = node
    node.prev = self.current

    nextNode.prev = node
    node.next = nextNode

    self.current = node

    self.count += 1
  

  def print(self):
    ret = ""
    node = self.head.next
    while node != None:
      ret += node.data
      node = node.next
    
    return ret


if __name__ == "__main__":
    arr = input().strip()
    ll = linkedList(arr)


    head = len(arr)

    for _ in ' '*int(input()):
      oper = input().split()

      if oper[0] == "L":
        if ll.current == ll.head:
          continue
        ll.current = ll.current.prev

      elif oper[0] == "D":
        if ll.current == ll.tail:
          continue
        ll.current = ll.current.next

      elif oper[0] == "B":
        if ll.current == ll.head:
          continue
        ll.delete()

      elif oper[0] == "P":
        ll.insert(oper[1])
    
    print(ll.print())