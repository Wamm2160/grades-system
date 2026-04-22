def save_data(data, filename):
    with open(filename, "w") as file:
        for item in data:
            file.write(str(item) + "\n")

def load_data(filename):
    try: 
        with open(filename, "r") as file:
            return [float(line.strip()) for line in file]
    except FileNotFoundError:
        return []

def add_item(items, item):
    items.append(item)
    return items
        
def total_sum(items):
    return  sum(items)

def get_average(items):
    if len(items) == 0:
        return 0
    return sum(items) / len(items)

def get_max(items):
    if not items:
        return None
    return max(items)

def count_items(items):
    return len(items)

def clear_all_items():
    return []