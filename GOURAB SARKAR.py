def task1():
    # This initializes the name
    name = "Gourab"
    # This initializes the age
    age = 24
    # This prints a one-line greeting that includes the name and age
    print("My name is " + name + " and I am ", age, " years old.")

# Call the function to execute the code
task1()




# Task 2: Data Types and Type Conversion
def task2(num1, num2):

    #a variable num1 and assign an integer value to it.
    num1 = 10
    #a variable num2 and assign a float value to it.
    num2 = 10.5

    # Convert num1 to a float and store it in a new variable num1_float.
    num1_float = float(num1)
    # Convert num2 to an integer and store it in a new variable num2_int.
    num2_int = int(num2)

    # Print the original values of num1 and num2.
    print("num1:", num1)
    print("num1_float:", num1_float)
    print("num2:", num2)

# Call the function to execute the code 
    task2(num1, num2)




#Task 3: String Manipulation
def task3():
    # Create a string variable.
    sentence = "Python programming is fun!"

    # Print the length of the string.
    print("Length of the string:", len(sentence))

    # Print the 8th character (index 7) in the string.
    print("8th character:", sentence[7])

    # Create a substring from index 0 to 5 and store it in a new variable.
    substring = sentence[0:6]

    # Concatenate the string " I enjoy it!" with the substring.
    print("I enjoy it!" + substring)

# Call the function to execute the code.
task3()





#Task 4: Lists and List Manipulation
def task4():
    # Create a list fruits with the following items: "apple", "banana", "cherry", "date".
    fruits = ["apple", "banana", "cherry", "date"]

    # Add "grape" to the end of the list.
    fruits.append("grape")

    # Remove "banana" from the list.
    fruits.remove("banana")

    # Print the length of the list.
    print("Length of the fruits list:", len(fruits))

    # Create a new list sliced_fruits containing the second and third items from the fruits list.
    sliced_fruits = fruits[1:3]

    # Combine sliced_fruits with a new list extra_fruits containing "kiwi" and "lemon".
    extra_fruits = ["kiwi", "lemon"]
    combined_list = sliced_fruits + extra_fruits

    # Print the combined list.
    print("Combined list:", combined_list)

# Call the function to execute the list manipulation.
task4()





#Task 5: Conditional Statements
def task5():
    # Create a variable num and assign an integer value to it.
    num = 17

    # A conditional statement to check if num is even or odd.
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

# Call the function to execute the list manipulation.
task5()


#Task 6: Loops

def task6():
    # Print the numbers from 1 to 10 using a loop.
    for i in range(1, 11):
        print(i)

    # Calculate the sum of numbers from 1 to 100 using a loop.
    sum = 0
    for num in range(1, 101):
        sum = sum + num

    print(sum)

# Call the function to execute the list manipulation.
task6()







# Task 7: Functions

def task7():
    import math
    # a function calculate_square that takes a number as input and returns its square.
    def calculate_square(num):
        return num ** 2

    def is_prime(num):
        if num < 2:
            return False

        for n in range(2, int(math.sqrt(num)) + 1):
            if num % n == 0:
                return False

        return True

    print(is_prime(11))

    # Using the functions to find the square of 7 and check if 29 is prime
    print(calculate_square(7))
    print(is_prime(29))

# Call the function to execute the list manipulation.
task7()






#Task 8: Dictionaries
# a dictionary student with keys "name", "age", and "grade" with assign appropriate values.
def task8():
    # Create the student dictionary
    student = {
        "name": "Gourab",
        "age": 24,
        "grade": "A+"
    }

    # Add a new key "course" with a value of your choice
    student["course"] = "Data Science"

    # Print all the keys in the dictionary
    print("Keys in the dictionary student:", list(student.keys()))

    # Loop through the dictionary and print all key-value pairs
    print("All key-value pairs in the dictionary:")
    for key, value in student.items():
        print(key, ":", value)

# Call the function to execute the code
task8()






