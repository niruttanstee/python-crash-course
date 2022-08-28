# Think of something you could store in a list.
vowels = []
# Write a program that creates a list containing these item and then use each function introduced in this chapter at least once.
vowels.append('a')
vowels.append('e')
vowels.append('o')
vowels.append('u')
vowels.insert(2, 'i')

# Getting the item using index.
print(vowels[2])

# Popping the latest item.
print(f"This vowel was popped as it was the last: {vowels.pop()}")
print(vowels)

# Removing and item using value.
item_remove = 'a'
vowels.remove(item_remove)
print(f"Vowel {item_remove.title()} has been removed")
print(vowels)

# Adding the item back in its specific places.
vowels.append('u')
print(vowels)
vowels.insert(0, 'a')
print(vowels)

# Sorting list temporarily and also reversing it.
sorted_vowels = sorted(vowels)
print(sorted_vowels)
print(sorted(sorted_vowels, reverse=True))
