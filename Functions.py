# Generic greeting simple function
def greet_user():
    print("Hello LLunio!!!!")

    print("Welcome Llunio!!!!")

#more complext function with customizable greeting
def greet_user_by_name(name, greeting):
    print(greeting + "," + name)

#function seemingly based on intergers but name holders are simply proxys for a non defined but implied integer
def cube(base_number):
    cubed_value = base_number * base_number * base_number
    return cubed_value

#basically a print function displays parameters as defined above
greet_user()

greet_user_by_name(input("What is your name? : "),"Welcome")

eleven_cubed = cube(11)
print(eleven_cubed)

