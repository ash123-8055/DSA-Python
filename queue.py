class Queue:
    """This class consists the operations on queue for enqueue, dequeue, peek and front"""
    def __init__(self):
        """
        Description: Constructor for initiating the queue

        Parameter: self: Object
        
        Return: None
        """

        self.__num_list=[]

    def enqueue(self,data):
        """
        Description: Function for adding a data to the queue at end 

        Parameter: self: Object
                   data: Value of queue data
        
        Return: None
        """

        self.__num_list.append(data)

    def dequeue(self):
        """
        Description: Function for removing data from the beginning

        Parameter: self: Object
        
        Return: None
        """

        if not self.__num_list:
            print("The Queue is empty!Cant Remove anything!!")
        else:
            self.__num_list.pop(0)
    
    def peek(self):
        """
        Description: Function for printing the value at the end of queue

        Parameter: self: Object
        
        Return: None
        """

        if not self.__num_list:
            print("Queue is empty")
        else:
            print(self.__num_list[-1])

    def front(self):
        """
        Description: Function for printing the value at the front of queue

        Parameter: self: Object
        
        Return: None
        """

        if not self.__num_list:
            print("Queue is empty")
        else:
            print(self.__num_list[0])

q=Queue()
q.enqueue(10)
q.enqueue(30)
q.enqueue(20)
q.peek()
q.front()
q.dequeue()
q.dequeue()
q.peek()
q.front()
q.dequeue()
q.peek()
q.dequeue()


        
