# node structure
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

# class LinkedList
class LinkedList:
  def __init__(self):
    self.head = None

  #Add new element at the end of the list
  def push_back(self, newElement):
    newNode = Node(newElement)
    if(self.head == None):
      self.head = newNode
      return
    temp = self.head
    while(temp.next != None):
      temp = temp.next
    temp.next = newNode
    newNode.prev = temp

  # Inserts a new element at the given position
  def push_at(self, newElement, position):
      newNode = Node(newElement)
      if (position < 1):
          print("\nposition should be >= 1.")
      elif (position == 1):
          newNode.next = self.head
          self.head.prev = newNode
          self.head = newNode
      else:
          temp = self.head
          for i in range(1, position - 1):
              if (temp != None):
                  temp = temp.next
          if (temp != None):
              newNode.next = temp.next
              newNode.prev = temp
              temp.next = newNode
              if (newNode.next != None):
                  newNode.next.prev = newNode
          else:
              print("\nThe previous node is null.")

  # Delete an element at the given position
  def pop_at(self, position):
    if(position < 1):
      print("\nposition should be >= 1.")
    elif (position == 1 and self.head != None):
      nodeToDelete = self.head
      self.head = self.head.next
      nodeToDelete = None
      if (self.head != None):
        self.head.prev = None
    else:
      temp = self.head
      for i in range(1, position-1):
        if(temp != None):
          temp = temp.next
      if(temp != None and temp.next != None):
        nodeToDelete = temp.next
        temp.next = temp.next.next
        if(temp.next.next != None):
          temp.next.next.prev = temp.next
        nodeToDelete = None
      else:
        print("\nThe node is already null.")

  # display the content of the list
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

# testing the code
dllist = LinkedList()

# Add 4 elements at the end of the list.
dllist.push_back(5)
dllist.push_back(9)
dllist.push_back(13)
dllist.push_back(90)
dllist.PrintList()

#Insert an element at position 2
dllist.push_at(100, 2)
dllist.PrintList()

# Delete an element at position 2
dllist.pop_at(2)
dllist.PrintList()

# Add 1 element after the deletion.
dllist.push_back(99)
dllist.PrintList()
