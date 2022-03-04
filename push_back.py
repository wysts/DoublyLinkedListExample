# Add new element at the end of the list
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
