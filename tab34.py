import cmath
a, b, c = 1, -5, 6
d = (b**2) - (4*a*c)

root1 = (-b - cmath.sqrt(d)) / (2*a)
root2 = (-b + cmath.sqrt(d)) / (2*a)
print(f"Roots are: {root1} and {root2}")
