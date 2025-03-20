class Node:
    """Class Node used for creating nodes"""
    def __init__(self,data):
        """
        Description: Constructor used to assign the values of data and next

        Parameter: self=object
                   data=value of the node

        Return: None
        """

        self.data=data
        self.next=None

class linked_list():
    def __init__(self):
        """
        Description: Constructor used to assign the value of head

        Parameter: self=object

        Return: None
        """

        self.head=None
    
    def add_at_beginning(self,data):
        """
        Description: This function is used for add data to the beginning

        Parameter: self=object
                   data=value of the node

        Return: None
        """

        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head=new_node

    def add_at_end(self, data):
        """
        Description: This function is used for add data to the end

        Parameter: self=object
                   data=value of the node

        Return: None
        """

        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def add_at_position(self, data, index):
        """
        Description: This function is used for add data at the specific index
        
        Parameter: self=object
                   data=value of the node
                   index= position of the node

        Return: None
        """

        if index == 0:
            self.add_at_beginning(data)
            return
        new_node = Node(data)
        temp = self.head
        for _ in range(index - 1):
            if temp is None:
                raise IndexError("Index out of range")
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
    
    def search_and_remove(self, key):
        """
        Description: This function is used for remove the specific data

        Parameter: self=object
                   key=value of the node

        Return: None
        """

        temp = self.head
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if not temp:
            return "Item not found"
        if prev:
            prev.next = temp.next
        else:
            self.head = temp.next
    
    def remove_from_end(self):
        """
        Description: This function is used for remove the data at end

        Parameter: self=object

        Return: None
        """

        if not self.head:
            return "List is empty"
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def remove_from_front(self):
        """
        Description: This function is used for remove the data at front

        Parameter: self=object

        Return: None
        """

        if not self.head:
            return "List is empty"
        self.head = self.head.next

    def display(self):
        """
        Description: This function is used to display the list

        Parameter: self=object

        Return: None
        """

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

ll = linked_list()
ll.add_at_end(10)
ll.add_at_end(20)
ll.add_at_beginning(5)
ll.add_at_position(15, 2)
ll.display()

ll.search_and_remove(20)
ll.display()

ll.remove_from_end()
ll.display()

ll.remove_from_front()
ll.display()