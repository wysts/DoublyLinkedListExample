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
