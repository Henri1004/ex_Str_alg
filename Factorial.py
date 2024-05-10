#Recursividad para calcular el factorial de un número.

def factorial(n):
    a = 1
    if n == 0:
        return a
    else:
        return n * factorial(n-1)

def main():
    print("=================================================================.")
    print("Test Case 1: Check the Factorial of 5.")
    print("=================================================================.")
    print("The factorial of 5 is: ", factorial(5))

if __name__ == "__main__":
    main()
    
