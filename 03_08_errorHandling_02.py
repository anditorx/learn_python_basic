fruit_list = ["apple", "banana", "watermelon"]



def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: You can't divide by zero!"
    except TypeError:
        return "Error: Both arguments must be numbers!"
    else:
        return result

# Testing the function
print(divide_numbers(10, 2))  # Output: 5.0
print(divide_numbers(10, 0))  # Output: Error: You can't divide by zero!
print(divide_numbers(10, 'a'))  # Output: Error: Both arguments must be numbers!

print("")
print("---")
print("")

for fruit in fruit_list:
    print(fruit)
    
print("")
print("---")
print("")

def read_file(file_path):
    try:
        file = open(file_path, 'r')
        content = file.read()
    except FileNotFoundError:
        return "Error: File not found!"
    except IOError:
        return "Error: An I/O error occurred!"
    else:
        return content
    finally:
        if 'file' in locals() and not file.closed:
            file.close()

# Testing the function
print(read_file("existing_file.txt"))  # Output: Content of the file
print(read_file("non_existing_file.txt"))  # Output: Error: File not found!
