def show_info(func):
    def wrapper(*args, **kwargs):
        print("Calling function...")
        result = func(*args, **kwargs)
        print("Function executed.")
        return result
    return wrapper


@show_info
def square(num):
    return num * num


num = int(input("Enter a number: "))

print("Square =", square(num))