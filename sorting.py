def bubblesort(arr):
    """
    Description: Sorting an array using bubble sort

    Parameter: arr: unsorted array

    Return: Sorted array
    """

    arr_len=len(arr)
    for i in range(arr_len):
        for j in range(arr_len-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def insertionsort(arr):
    """
    Description: Sorting an array using insertion sort

    Parameter: arr: unsorted array

    Return: Sorted array
    """

    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1

        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    
    return arr

def selectionsort(arr):
    """
    Description: Sorting an array using selection sort

    Parameter: arr: unsorted array

    Return: Sorted array
    """

    n=len(arr)
    for i in range(n-1):
        min_val=i
        for j in range(i+1,n):
            if arr[j]<arr[min_val]:
                min_val=j
        
        arr[i],arr[min_val]=arr[min_val],arr[i]
    
    return arr

def mergesort(arr,left,right):
    """
    Description: Sorting an array using merge sort

    Parameter: arr: unsorted array
               left: value of splitting in left
               right: value of splitting in right

    Return: Sorted array
    """

    if left<right:
        mid=(left+right)//2

        mergesort(arr,left,mid)
        mergesort(arr,mid+1,right)
        merge(arr,left,mid,right)
    
    return arr

def merge(arr,left,mid,right):
    """
    Description: Function used for merging the values after splitting 

    Parameter: arr: unsorted array
               left: value of splitting in left
               mid: value of mid 
               right: value of splitting in right

    Return: None
    """

    n1=mid-left+1
    n2=right-mid
    l=[0]*n1
    r=[0]*n2

    for i in range(n1):
        l[i]=arr[left+i]

    for j in range(n2):
        r[j]=arr[mid+1+j]

    i=0
    j=0
    k=left

    while i<n1 and j<n2:
        if l[i]<=r[j]:
            arr[k]=l[i]
            i+=1
        else:
            arr[k]=r[j]
            j+=1
        k+=1

    while i<n1:
        arr[k]=l[i]
        i+=1
        k+=1
    
    while j<n2:
        arr[k]=r[j]
        j+=1
        k+=1
    
def quicksort(arr,low,high):
    """
    Description: Sorting an array using quick sort

    Parameter: arr: unsorted array
               low: value from which we start
               high: value from which we end

    Return: Sorted array
    """

    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
    
    return arr

def swap(arr,i,j):
    """
    Description: Function used for swapping values

    Parameter: i: index value used for swapping
               j: index value used for swapping

    Return: None
    """

    arr[i],arr[j]=arr[j],arr[i]

def partition(arr,low,high):
    """
    Description: Function used for creating partition on pivot and swapping the values

    Parameter: arr: unsorted array
               low: value from which we start
               high: value from which we end

    Return: None
    """

    pivot=arr[high]
    i=low-1

    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            swap(arr,i,j)
    
    swap(arr,i+1,high)
    return i+1

arr=[411,2,1,5,11,63,99]
print("Initital Array: ",arr)
choice=input("Enter the algo to sort with \n1.Bubble Sort\n2.Insertion Sort\n3.Selection Sort\n4.Merge Sort\n5.Quick Sort\nOption: ")
match choice:
    case "1":
        print(bubblesort(arr))
    
    case "2":
        print(insertionsort(arr))
    
    case "3":
        print(selectionsort(arr))
    
    case "4":
        print(mergesort(arr,0,len(arr)-1))
    
    case "5":
        print(quicksort(arr,0,len(arr)-1))
    
    case default:
        print("\nWrong Option")