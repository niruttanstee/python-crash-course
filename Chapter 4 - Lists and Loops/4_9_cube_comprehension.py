# Use a list comprehension to generate a list of the first 10 cubes.
cubes = [value**2 for value in range(1, 11)]
for cube in cubes:
    print(cube)