# Changing an element in the list.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

# Appending the elements to the end of the list using the append() method.
motorcycles.append('honda')
print(motorcycles)

# Appending an empty list.
bikes = []
bikes.append('ducati')
bikes.append('honda')
bikes.append('yamaha')
print(bikes)

# Inserting an element into specific position in the list.
bikes.insert(0, 'suzuki') 
# adds element to the front the list shifting every other element to the right or up.
print(bikes)