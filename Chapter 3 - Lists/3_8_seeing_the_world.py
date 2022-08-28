# Think of at least 5 places you want to visit.

# 1. Store the locations in a list. Make sure the list is not alphabetically ordered.
locations = ['california', 'norway', 'germany', 'iceland', 'egypt', 'china']

# 2. Print your list in its original order.
print(locations)

# 3. Use sorted() method to print your list in alphabetical order without modifying the actual list.
print(sorted(locations))

# 4. Show that the list is still in the original order by printing it.
print(locations)

# 5. Use sorted to print the list in reverse alphabetically without changing the order of the original list.
sorted_reverse_locations = sorted(locations, reverse=True) 
# sorted() also has reverse argument
print(sorted_reverse_locations)

# 6. Show that the list is still in its original order by printing it again.
print(locations)

# 7. Use reverse() method to change the order of your list, then print to show the changed list.
locations.reverse()
print(locations)

# 8. Use reverse() method to the order of the list again, print to show the list is back to its original order.
locations.reverse()
print(locations)

# 9. Use sort() method to change your list so it's stored in alphabetical order, then print to show the order has been changed.
locations.sort()
print(locations)

# 10. Use sort() to change the list so it's stored in reverse alphabetical order, then print the list to show that its order has changed.
locations.sort(reverse=True)
print(locations)