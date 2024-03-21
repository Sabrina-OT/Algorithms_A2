#Sabrina Skoric: 100872613
#Algorithms and Data Structures Assignment 2

#ADD THE SOUNDS !!!!!!!!!!!!!!!!!

#TASK: accept an array of n integers, then perform either merge sort or quick sort. Ensure to print out each step

def main(): 
    print("\nWelcome to the Sorting Program!")
    print("\nPlease enter numbers for the array, or type EXIT to stop")
    
    # initialize some variables
    array = []
    counter = 0

    # get numbers from the user
    while counter == 0:
        number = input("Number: ")
        #ensure they are valid integers
        try:
            number = int(number)
            array.append(number)
        except:
            if number in ['EXIT', 'exit']:
                counter = 1
                break
            else:
                print("Invalid Input")

    #print out the array to users
    print("Here is your array: ", array)

    # let user decide sorting algorithm
    print("Which sorting algorithm would you like to use:")
    print("1 = MERGE SORT")
    print("2 = QUICK SORT")

    counter2 = 0
    # ensure the user enters a valid input
    while counter2 == 0:
        answer = input("Algorithm: ")

        try:
            # go to merge sort function
            if int(answer) == 1:
                MergeSort(array)
                print("Sorted: ", array)
                counter2 = 1

            # go to quick sort function
            elif int(answer) == 2:
                QuickSort(array, 0, len(array) - 1)
                print("Sorted: ", array)
                counter2 = 1

            else: 
                print("Number in invalid range")
        except:
            print("Invalid")
        print()

def MergeSort(array, depth=0):
    #calculate the indentation based on the recursion depth
    #this is done so that the output of the steps is more organized
    indent = "  " * depth 
    
    # print out the array currently being sorted
    print(indent + "Sorting array:", array) 

    if len(array) > 1:
        # Split array into left and right halves
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]

        # Recursively sort left and right halves
        MergeSort(left_array, depth + 1)
        MergeSort(right_array, depth + 1)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1
        
        #print the merged arrays
        print(indent + "Merging:", left_array, right_array) 


def QuickSort(arr, left, right):
    if left < right:
        #partition the arrat and get the position of the pivot
        partition_pos = partition(arr, left, right)
        
        #print the subarray that is being partitioned
        print("Partitioning array from index", left, "to", right, ": ", arr[left:right+1])
       
        #Recursively sort the left and right subarrays
        QuickSort(arr, left, partition_pos - 1)
        QuickSort(arr, partition_pos + 1, right)

def partition(arr, left, right):
    i = left
    j = right - 1

    #Choose the pivot as the last element
    pivot = arr[right]

    while i < j:
        # Move the left pointer until the value >= pivot
        while i < right and arr[i] < pivot:
            i += 1
        # Move the right pointer until the value < pivot
        while j > left and arr[j] >= pivot:
            j -= 1

        # Swap the elements at the left and right pointers if necessary
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Print the partitioned array
    print("Partitioned array:", arr[left:right+1], "Pivot:", pivot)

    # If the element is bigger than the pivot, then swap
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i
   
if __name__ == "__main__":
    main()