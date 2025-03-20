class Stack:
    """The class stack has the functions for pushing, popping and checking top on a stack"""
    def __init__(self):
        """
        Description: Constructor for initiating the stack

        Parameter: self: object

        return: none
        """

        self.__num_stack=[]

    def num_pop(self):
        """
        Description: Function to remove the value on top of the stack

        Parameter: self: object

        return: none
        """

        if not self.__num_stack:
            print("The Stack is empty!Cant Remove any value")
        else:
            self.__num_stack.pop()
    
    def top(self):
        """
        Description: Function to show the value on top

        Parameter: self: object

        return: none
        """

        if not self.__num_stack:
            print("The Stack is empty")
        else:
            print(self.__num_stack[-1])
    
    def push(self,data):
        """
        Description: Function to push a value on top the stack

        Parameter: self: object
                   data: value to pushed to the stack

        return: none
        """

        self.__num_stack.append(data)



s=Stack()
s.top()
s.num_pop()
s.push(10)
s.push(20)
s.top()
s.num_pop()
s.top()
s.push(30)
s.top()
s.num_pop()
s.top()