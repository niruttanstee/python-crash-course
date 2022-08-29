# Using get() to access values are better as if a key does not exist in the
# dictionary we can assign a default value without calling an error.
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# If we leave the value empty as the second argument Python will interpret as
# value None.