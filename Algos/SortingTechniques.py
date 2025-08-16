
def bubbleSort(arr,size):
    for i in range(size):
        for j in range(size-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(f"after bubble Sort{arr}")

def selectionSort(arr,size):
    for i in range(size):
        minPos = i
        for j in range(i, size):
            if arr[j]<arr[minPos]:
                minPos = j
        arr[i],arr[minPos] = arr[minPos],arr[i]
    print(f"after selection sort{arr}")
    
def insertionSort(arr,size):
    for i in range(size):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print(f"after insertion sort{arr}")
            

                     
if __name__ == "__main__":
    print("In main")
    size = int(input("enter the the size of the array"))
    print("now enter the elements one by one")
    list = []
    for i in range(size):
        list.append(input())
    print(f"Initial elements in the list are: {list}")
    size = len(list)
    bubble_list = list.copy()  
    bubbleSort(bubble_list, size)
    
 
    selection_list = list.copy()  
    selectionSort(selection_list, size)
    
    insertion_sort = list.copy()
    insertionSort(insertion_sort,size)
    
    list.sort() #builtin method 
    print(f"this is builtin method{list}")