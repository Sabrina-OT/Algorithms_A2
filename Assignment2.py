#Sabrina Skoric: 100872613
#Algorithms and Data Structures Assignment 2

#accept an array of n integers, then perform either merge sort or quick sort, ensure to print out each step

def main(): 
    print("\nWelcome to the Sorting Program!")
    print("\nPlease enter numbers for the array, or type EXIT to stop")
    
    array = []
    counter = 0

    # get numbers from the user
    while counter == 0:
        number = input("Number: ")
        try:
            number = int(number)
            array.append(number)
        except:
            if number in ['EXIT', 'exit']:
                counter = 1
                break
            else:
                print("Invalid Input")

    print("Here is your array: ", array)

    # let user decide sorting algorithm
    print("Which sorting algorithm would you like to use:")
    print("1 = MERGE SORT")
    print("2 = QUICK SORT")

    counter2 = 0
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
    indent = "  " * depth  # Calculate indentation based on recursion depth
    print(indent + "Sorting array:", array)  # Print the array being sorted

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
        
        print(indent + "Merging:", left_array, right_array)  # Print the merged arrays


def QuickSort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        print("Partitioning array from index", left, "to", right, ": ", arr[left:right+1])
        QuickSort(arr, left, partition_pos - 1)
        QuickSort(arr, partition_pos + 1, right)

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    print("Partitioned array:", arr[left:right+1], "Pivot:", pivot)
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    return i
   
if __name__ == "__main__":
    main()