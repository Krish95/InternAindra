class Node:
    """
    A node in the linked list.
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    """
    Represents the Linked list.
    """
    def __init__(self):
        """
        Create a new LL in constant time.
        """
        self.head = None
        self.last = None

    def __repr__(self):
        """
        Prints the list in O(n)
        """
        nodes = []
        current = self.head
        while current and current!=self.last:
            nodes.append(repr(current))
            current = current.next
        nodes.append(repr(self.last))
        return '[' + ', '.join(nodes) + ']'

    def append(self, data):
        """
        Insert an element at the end of the list in O(1).
        """
        if not self.head:
            self.head = Node(data=data)
            self.last = self.head
            return

        self.last.next = Node(data=data)
        self.last = self.last.next

    def insertAtPos(self,data, pos):
        """
        Inserts a new node at pos(0 indicates head). Return -1 if invalid.
        """
        i = 0
        newNode = Node(data=data)

        if pos== 0:
            if self.head:
                newNode.next = self.head
                self.head = newNode
                return self.head
            else:
                self.head = newNode
                self.last = newNode
                return self.head

        if pos == self.findlen():
            self.last.next = newNode
            self.last = self.last.next
            return self.last

        if pos > self.findlen():
            return -1
            
        curr = self.head
        previous = curr
        next = curr.next
        while i < pos - 1:
            current = current.next
            i+= 1
            previous = current
            next = curr.next

        previous.next = newNode
        newNode.next = next
        return self.head
    
    
    def createcycle(self,data):
        """
        This method allows to modify the 'next' of the last node. Returns -1 if data is invalid else returns head.
        """
        link = self.find(data)
        if link:
            self.last.next = link
            return self.head
        else:
            return -1

    def prepend(self, data):
        """
        Insert an element at the head in constant time.
        """
        if self.head is None: 
        	self.head = Node(data=data)
        	self.last = self.head
        else:
	        self.head = Node(data=data, next=self.head)


    def find(self, key):
        """
        Search for 'key'. Returns it or `None` if absent in O(n) time.
        """
        current = self.head
        while current and current.data != key:
            if current==self.last: 
               return None
            current = current.next
            
        return current  

    def delete(self, key):
        """
        Remove the first 'key' in the list in O(n).
        """
        #find node
        current = self.head
        previous = None
        while current and current.data != key:
            if current == self.last:
                return
            previous = current
            current = current.next

        if not current or current.data != key:
            return None

        if current == self.last:  
            self.last = previous
    
        #unlink
        if previous is None:
            self.head = current.next
            if self.head == current:
                self.head = None
        elif current:
            previous.next = current.next
            current.next = None

        return current
        
    def detectCycleLen(self):
        """
        Finds the length of a cycle if present else returns 0.
        """
        len = 0
        nodeset = set()
        temp = self.head
        start = None
        while(temp):
            if(temp in nodeset):
                start = temp
                break

            nodeset.add(temp)
            temp = temp.next

        if start is not None:
            temp = start.next   
            len = 1
            while(temp!=start):      
                len+=1
                temp = temp.next  

        return len

    def findlen(self):
        """
        Finds the number of nodes present in the list.
        """
        len=0
        temp = self.head
        if self.head: len=1
        while temp and temp!=self.last:
            len+=1
            temp = temp.next
        return len

