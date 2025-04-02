


def add_sprinkles(func):
    def wrapper(*arg, **kwargs):
        print("Adding sprinkles!")
        func(*arg, **kwargs)
    return wrapper

def add_chocolate(func):
    def wrapper(*arg, **kwargs):
        print("Adding chocolate!")
        func(*arg, **kwargs)
    return wrapper

@add_chocolate
@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here's your {flavor} ice cream !")

get_ice_cream("vanilla")



# exceptions

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("You can't divide by zero!")
    except TypeError as e:
        print("Invalid type!")
    finally:
        print("Execution finished!")

print(divide(10, 0))
print(divide(10, "something"))
print(divide(10, 2))

