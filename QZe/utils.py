import json

def read(fileName):
    with open(fileName, 'rb') as f:
        data = json.load(f)
    
    return data

def write(fileName, data):
    with open(fileName, 'wb') as f:
        json.dump(data, f)

def extract_first_number(file_name):
    # Find the first sequence of digits in the file name
    digits = ""
    for char in file_name:
        if char.isdigit():
            digits += char
        elif digits:
            break
    return int(digits) if digits else float('inf')
