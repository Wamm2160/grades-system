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