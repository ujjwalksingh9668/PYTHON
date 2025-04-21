# Program to calculate the sum of natural numbers up to n

# Solution:-
n = int(input("Enter a positive integer: "))

# Check if the number is positive
if n < 1:
    print("Please enter a positive integer.")
else:
    # Calculate the sum using the formula for sum of first n natural numbers
    sum_natural = n * (n + 1) // 2

    # Display the result
    print(f"The sum of first {n} natural numbers is: {sum_natural}")
