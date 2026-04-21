
def add_numbers(numbers, number):
    numbers.append(number)
    return numbers
        
def total_sum(numbers):
    return  sum(numbers)

def max_number(numbers):
    if not numbers:
        return None
    return max(numbers)

def total_number_added(numbers):
    return len(numbers)

def menu():
    print("Mini sistema basic")
    print("1. Add a number")
    print("2. Show total")
    print("3. Show Higher number")
    print("4. Count numbers")
    print("5. Exit")
    
numbers = []
while True: 
    menu()
    try:
        option = int(input("Chosee an option: "))
    
        if option == 1:
            number = float(input("Type the number: "))
            numbers = add_numbers(numbers, number)
            print("Number added successfully")
        
        elif option == 2:
            if not numbers:
                print("No numbers added yet")
            else:
                print("The total is:", total_sum(numbers))
        
        elif option == 3:
            if not numbers:
                print("No numbers added yet")
            else:
                print("The higher number is:", max_number(number))
        
        elif option == 4:
            print("The total numbers added:", total_number_added(numbers))
            
        
        elif option == 5:
            print("Bye")
            break
        
        else: 
            print("Invalid option")
    
    except ValueError:
        print("Type a valid number")

        
