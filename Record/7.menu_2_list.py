list1 = input("Enter the first list of integers (separated by spaces): ").split()
list1 = list(map(int, list1))

list2 = input("Enter the second list of integers (separated by spaces): ").split()
list2 = list(map(int, list2))

while True:
    print("\nMenu:")
    print("1. Check if lists are of same length")
    print("2. Check if lists sum to same value")
    print("3. Check if any value occurs in both lists")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        if len(list1) == len(list2):
            print("The lists are of the same length.")
        else:
            print("The lists are of different lengths.")
    elif choice == '2':
        if sum(list1) == sum(list2):
            print("Both lists sum to the same value.")
        else:
            print("The lists do not sum to the same value.")
    elif choice == '3':
        common_elements = set(list1).intersection(set(list2))
        if common_elements:
            print(f"Common elements in both lists: {common_elements}")
        else:
            print("There are no common elements in both lists.")
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
