


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