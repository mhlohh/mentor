def greet(function):
    return function("Hello")

def uppercase(text):
    return text.upper()

print(greet(uppercase))