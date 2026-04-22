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