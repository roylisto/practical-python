# bounce.py
#
# Exercise 1.5

height = 100
loop = 10

while loop > 0:
    height = (3 / 5) * height
    print(round(height, 4))
    loop = loop - 1
