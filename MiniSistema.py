import services
import storage
numbers = storage.load_data("numbers.txt")


def menu():
    print("Mini Sistema")
    print("1. Add a number")
    print("2. Show total")
    print("3. Show Higher number")
    print("4. Count numbers")
    print("5. Exit")
    
#numbers = []
while True: 
    menu()
    try:
        option = int(input("Chosee an option: "))
    
        if option == 1:
            number = float(input("Type the number: "))
            numbers = services.add_item(numbers, number)
            storage.save_data(numbers, "numbers.txt")
            print("Number added successfully")
        
        elif option == 2:
            if not numbers:
                print("No numbers added yet")
            else:
                print("The total is:", services.total_sum(numbers))
        
        elif option == 3:
            if not numbers:
                print("No numbers added yet")
            else:
                print("The higher number is:", services.get_max(numbers))
        
        elif option == 4:
            print("The total numbers added:", services.count_items(numbers))
            
        
        elif option == 5:
            print("Bye")
            break
        
        else: 
            print("Invalid option")
    
    except ValueError:
        print("Type a valid number")

        
