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