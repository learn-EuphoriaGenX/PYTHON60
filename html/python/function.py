
def imp_calculator(x=10, y=10): # parameter
    a = x
    b = y
    ans1 = a + b 
    ans2 = a - b 
    ans3 = a * b 
    final_ans = ans1 + ans2 + ans3
    return final_ans

print(imp_calculator(12, 14) + 10) # arguments
print(imp_calculator() + 14)
print(imp_calculator( 0, 12) + 78)


# def printDetalils
def print_details (name, age, address, country = "INDIA"):
    print(f'Hello {name}')
    print(f'Your age is {age}')
    print(f'Your address is {address}')
    print(f'You are from {country}')

print_details("Hello", "23", "Kolkata", "INDIA")
print_details("hello", "29", "Bihar")

# call by refference | Call by object reference
def add_item(item, ls=[]): # params 
    ls.append(item)
    return ls

print(add_item(1)) # -> [1]
print(add_item(2)) # -> [1, 2]
print(add_item(3)) # -> [1, 2, 3]


def remote():
    return "AC Remote"

def remote():
    return "TV Remote"

print(remote())


def test():
    print("Test1")

print(test())




def outer():
    def inner():
        return "In inner Function"
    return inner()

print("In inner Function")


def fn_1234():
    return 1, 2, 3, 3, 4

ans = fn_1234()

print(ans)


def spoon(arr = []):
    arr.append(1)
    return arr

print(spoon())
print(spoon())











