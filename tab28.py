s1, s2, s3 = 5, 5, 8
if s1 == s2 == s3:
    print("Equilateral")
elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Isosceles")
else:
    print("Scalene")
