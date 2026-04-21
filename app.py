
def add_grade(grades, grade):
    if grade < 0 or grade > 10: 
        raise ValueError("Grade must be between 0 and 10")
    grades.append(grade)
    return grades

def calculate_average(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

def get_max_grade(grades):
    if len(grades) == 0:
        return 0
    return max(grades)

def numbers_of_grades(grades):
    return len(grades)

def clear_all_grades():
    return []

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
            grades = add_grade(grades, grade) 
            print("Grade added successfully.")
        except ValueError:
            print("Invalid input. Try again.")
            
    elif option == "2":
        print("Average:", calculate_average(grades))
    
    elif option == "3":
        print ("Max grade:", get_max_grade(grades))
    
    elif option == "4":
        if len(grades) == 0:
            print("No grade added yet.")
        else:
            print("Number of grades added:", numbers_of_grades(grades))
    
    elif option == "5":
        grades = clear_all_grades()
        print("All grades cleared.")
        
    elif option == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid option")

