# Comparing two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print((num1 > num2) * "The first number is greater." +
      (num1 < num2) * "The second number is greater." +
      (num1 == num2) * "Both numbers are equal.")



condition1 = 5 > 3  # True
condition2 = 2 < 1  # False

print(condition1 or condition2)


