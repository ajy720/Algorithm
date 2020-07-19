import sys

input = sys.stdin.readline

class queue:
  arr = []
  head = 0
  def push(self, o):
    self.arr.append(o)
  
  def pop(self):
    if not self.empty():
      self.head += 1
      return self.arr[self.head-1]
    else:
      return -1

  def size(self):
    return len(self.arr) - self.head

  def empty(self):
    return 0 if len(self.arr) > self.head else 1
  
  def front(self):
    if not self.empty():
      return self.arr[self.head]
    else:
      return -1

  def back(self):
    if not self.empty():
      return self.arr[-1]
    else:
      return -1


if __name__ == "__main__":
  q = queue()
  for _ in ' '*int(input()):
    oper = input().split()

    if oper[0] == "push":
      q.push(oper[1])
    elif oper[0] == "pop":
      print(q.pop())
    elif oper[0] == "size":
      print(q.size())
    elif oper[0] == "empty":
      print(q.empty())
    elif oper[0] == "front":
      print(q.front())
    elif oper[0] == "back":
      print(q.back())
