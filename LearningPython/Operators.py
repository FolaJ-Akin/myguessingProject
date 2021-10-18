a = 12
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)  # ans = 4.0 - a floating point data type
print(a // b)  # ans = 4 integer division, rounded down towards minus infinity
print(a % b)  # 0 modulo: the remainder after integer division

print()
# a/b gives an error because you cannot use a float data type where an integer (int) should be used
for i in range(1, a // b):
    print(i)

# Lesson 25 - Operation Precedence
# Multiplication and division have equal precedence
# Addition and subtraction have equal precedence
# Python reads operators left from right in order of magnitude : BIDMAS
