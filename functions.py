######### Menu options below #########
def main_menu():
    print("Select the sorting algorithm you want to test.\n\
          ---------------------------\n\
          1. Bubble Sort\n\
          2. Merge Sort\n\
          3. Quick Sort\n\
          4. Heap Sort\n\
          5. Exit\n\
          Select a sorting algorithm (1-5): ")
    
def bbl_menu():
    print("\nCase Scenarios for Bubble Sort\n\
          -----------------\n\
          1. Best Case\n\
          2. Average Case\n\
          3. Worst Case\n\
          4. Exit bubble sort test")
    
def merge_menu():
    print("\nCase Scenarios for Merge Sort\n\
          -----------------\n\
          1. Best Case\n\
          2. Average Case\n\
          3. Worst Case\n\
          4. Exit merge sort test")
    
def quick_menu():
    print("\nCase Scenarios for Quick Sort\n\
          -----------------\n\
          1. Best Case\n\
          2. Average Case\n\
          3. Worst Case\n\
          4. Exit quick sort test")
    
def heap_menu():
    print("\nCase Scenarios for Heap Sort\n\
          -----------------\n\
          1. Best Case\n\
          2. Average Case\n\
          3. Worst Case\n\
          4. Exit heap sort test")
################################################

'''
Generates a list of random numbers to be sorted by a sorting algorithm
Parameters
    size: The amount of numbers to generate
    floor: The lower bound of the number generator
    ceiling: The upper bound of the number generator
Returns
    nums: The list of random numbers
'''
import random
def generate_nums(size = 1, floor = 1, ceiling = 1_000):
    nums = []

    for i in range(0, size):
        nums.append(random.randrange(floor, ceiling))

    return nums

'''
Finds the Time
'''
import time
def time_sort_function(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    return time.time() - start_time
    
def run_sort_test(sort_func, name):
    while True:
        if name == "Bubble Sort":
            bbl_menu()
        elif name == "Merge Sort":
            merge_menu()
        elif name == "Quick Sort":
            quick_menu()
        elif name == "Heap Sort":
            heap_menu()

        case = input("Select the case (1-4): ")
        if case == "1":
            case_type = "Best Case"
        elif case == "2":
            case_type = "Average Case"
        elif case == "3":
            case_type = "Worst Case"
        elif case == "4":
            break
        else:
            print("Invalid input. Try again.")
            continue

        while True:
            N = int(input("What is the N? "))
            arr = generate_nums(N)
            
            # Best, Average, Worst Case Setup (adjust as needed)
            if case_type == "Best Case":
                arr.sort()  # Already sorted
            elif case_type == "Worst Case":
                arr.sort(reverse=True)  # Reversed list
            # Average case is a random list, already handled by generate_nums
            
            # Time the sorting function
            time_taken = time_sort_function(sort_func, arr)
            print(f"In {case_type}, For N = {N}, it takes {time_taken:.6f} seconds")
            
            another_input = input("Do you want to input another N (Y/N)? ")
            if another_input.lower() == 'n':
                break

'''
Creates a Heap
'''
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than root or left child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

######### Sorting Algorithms below #########
def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already sorted, so skip them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

def merge_sort(arr):
    # Base case: if the list is a single element, it is already sorted
    if len(arr) > 1:
        
        # Find the middle of the array
        mid = len(arr) // 2
        
        # Divide the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Merge the sorted halves
        i = j = k = 0
        
        # Copy data to temp arrays left_half[] and right_half[]
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Check if any element was left in the left_half[]
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Check if any element was left in the right_half[]
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

def quick_sort(arr):
    # Base case: if the list has one or zero elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot (we'll use the last element as the pivot)
    pivot = arr[-1]
    
    # Partition the array into two halves: one with elements smaller than pivot, one with elements larger
    left = []
    right = []
    
    for x in arr[:-1]:  # Iterate over all elements except the pivot
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
    
    # Recursively apply quick_sort to the left and right partitions, and concatenate the result with the pivot
    return quick_sort(left) + [pivot] + quick_sort(right)

def heap_sort(arr):
    n = len(arr)

    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (max element) with the last element
        heapify(arr, i, 0)  # Reheapify the root to maintain the heap property

    return arr
############################################################