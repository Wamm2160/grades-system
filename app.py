import services
def menu():
    print("\n--- Grade System ---")
    print("1. Add Grade")
    print("2. Show Average")
    print("3. Show max grade")
    print("4. Show how many grades have been added")
    print("5. Clear all grades")
    print("6. Exit")



grades = []

while True:
    menu()
    option = input("choose an option: ")
    
    if option == "1":
        try:
            grade = float(input("Enter grade (0-10): "))
            grades = services.add_item(grades, grade) 
            print("Grade added successfully.")
        except ValueError:
            print("Invalid input. Try again.")
            
    elif option == "2":
        print("Average:", services.get_average(grades))
    
    elif option == "3":
        print ("Max grade:", services.get_max(grades))
    
    elif option == "4":
        if len(grades) == 0:
            print("No grade added yet.")
        else:
            print("Number of grades added:", services.count_items(grades))
    
    elif option == "5":
        grades = services.clear_all_items()
        print("All grades cleared.")
        
    elif option == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option")

