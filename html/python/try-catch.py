
user = input("Enter a username: ")
password = input("Enter a password: ")

try:
    if user != "admin" or password != "password123":
        raise ValueError("Invalid username or password.")
    # print(a)
    # raise ValueError("This is a custom error message.")
    # raise NameError("This is a custom error message.")
    #print(10 / 0)  
    # file = open("example.txt", "r")
except Exception as error:
    print(f"An error occurred: {error}")
else:
    print("Login successful!")
finally:
    print("This will always execute.")

# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except NameError:
#     print("Variable 'a' is not defined.")
# except FileNotFoundError:
#     print("The file 'example.txt' was not found.")
