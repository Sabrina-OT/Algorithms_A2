#Sabrina Skoric: 100872613
#Algorithms and Data Structures Assignment 2

#accept an array of n integers, then perform either merge sort or quick sort, ensure to print out each step

def main():
    array = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 0]
    MergeSort(array)
    print(array)

    """
    print("Welcome to the Sorting Program!")
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
                counter2 = 1

            # go to quick sort function
            elif int(answer) == 2:
                QuickSort(array)
                counter2 = 1

            else: 
                print("Number in invalid range")
        except:
            print("Invalid")
        print()

    """

def MergeSort(array):
    print("we are merging")

    print("LEGNTH: ", len(array))

    if len(array) > 1:
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2]

        #recursion
        MergeSort(left_array)
        MergeSort(right_array)

        #merge

        i = 0 #left index
        j = 0 #right index
        k = 0 #merged index

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

def QuickSort(array):
    print("We are quicking")
    print(array)
        
if __name__ == "__main__":
    main()