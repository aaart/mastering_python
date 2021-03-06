# this one is like your scripts with argv
def print_sth(*args):
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")
    print(f"(...) = {args}")

# ok, that *args is actually pointless, we can just do this
def print_two(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_sth("Zed","Shaw", "trololo")
print_two("Zed","Shaw")
print_one("First!")
print_none()
