# Triangle Classifier:
from inspect import classify_class_attrs

# Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

side1 = float(input("Enter the frist side of the triangle"))
side2 = float(input("Enter the second side of the triangle"))
side3 = float(input("Enter the third side of the triangle"))



def classify_tringle(a,b,c):
    if a == b == c:
        return "Equiletiral"
    elif a==b  or b==c or a==c:
        return "Isoceles"
    else:
        return "Scalene"

result = classify_tringle(side1, side2, side3)
print(f"The result of the triangle is: {result}")