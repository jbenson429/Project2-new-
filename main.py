import functions
from functions import bubble_sort, merge_sort, quick_sort, run_sort_test, heap_sort
def main():
    while True:
        functions.main_menu()
        choice = input("Select a sorting algorithm (1-5): ")
        
        if choice == "1":
            run_sort_test(bubble_sort, "Bubble Sort")
        elif choice == "2":
            run_sort_test(merge_sort, "Merge Sort")
        elif choice == "3":
            run_sort_test(quick_sort, "Quick Sort")
        elif choice == "4":
            run_sort_test(heap_sort, "Heap Sort")
        elif choice == "5":
            print("Bye!")
            break
        else:
            print("Invalid input. Please choose a valid option.")

# Run the program
if __name__ == "__main__":
    main()