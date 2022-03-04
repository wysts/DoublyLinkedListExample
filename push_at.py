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
