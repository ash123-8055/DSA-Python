from collections import defaultdict

def binarysearch(arr,low,high,x):
    """
    Description: Searching for a element using binary search

    Parameter: arr: intial array
               low: value from which we start
               high: value at which we end
               x: value to be searched
    
    Return: return False element if not found and index if element was found
    """

    while low<=high:
        mid=(low+high)//2

        if arr[mid]==x:
            return mid
        
        elif arr[mid]<x:
            low=mid+1
        
        else:
            high=mid-1
    
    return -1

def linearsearch(arr,x):
    """
    Description: Searching for a element using linear search

    Parameter: arr: intial array
               x: value to be searched
    
    Return: return False element if not found and index if element was found
    """

    arr_len=len(arr)
    found=False

    for i in range(0,arr_len):
        if arr[i]==x:
            return i
            found=True
            break

    if found==False:
        return False

class Graph:
    """Graph used for bfs and dfs"""

    def __init__(self):
        """
        Description: Constructor for initiating the Graph

        Parameter: self: object

        Return: None 
        """

        self.graph=defaultdict(list)

    def add_edge(self,u,v):
        """
        Description: Function for inintiating the edge and vertex

        Parameter: self: object
                   u: edge
                   v: vertex

        Return: None 
        """

        self.graph[u].append(v)

    def bfs(self,s):
        """
        Description: Function for breadth first search

        Parameter: self: object
                   s: value to be searched

        Return: True
        """

        visited= [False] * (max(self.graph)+1)
        queue=[]
        queue.append(s)
        visited[s]=True

        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i]=True
    
    def dfs(self, v):
        """
        Description: Function for Depth first search

        Parameter: self: object
                   s: value to be searched

        Return: True
        """

        visited = set()
        stack = [v]
    
        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                stack.extend(reversed(self.graph[node]))

def main():
    """
    Description: Driver Code
    """

    arr=[1,3,6,8,12,16,19]
    x=12
    if binarysearch(arr,0,len(arr)-1,x) != False:
        print(f"The Element was found at index {binarysearch(arr,0,len(arr)-1,x)}.")
    else:
        print("Element was not found")

    if linearsearch(arr,x) != False:
        print(f"The Element was found at index {linearsearch(arr,x)}.")
    else:
        print("Element was not found")

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.bfs(2)
    print()
    g.dfs(2)



if __name__=="__main__":
    main()
