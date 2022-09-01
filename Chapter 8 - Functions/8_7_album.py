# Write a function called make_album() that builds a dictionary describing a
# music album. The function should take in an artist name and album title,
# and should return a dictionary containing these two pieces of information.

def make_album(artist_name, album_title, number_of_songs=None):
    """Return an album dictionary."""
    if number_of_songs:
        album = {
        'artist_name': artist_name,
        'album_title': album_title,
        'number_of_songs': number_of_songs,
        }
    else:
        album = {'artist_name': artist_name, 'album_title': album_title}
    return album

# Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing album
# information correctly.

print(make_album('callum scott', 'lost frequencies'))
print(make_album('boney m', 'rasputin'))
print(make_album('harry styles', 'adore you'))

# Use None to add an optional parameter to the function that allows you to
# store the number of songs on an album.

# If the calling line includes a value for the number of songs, add that value
# to the album's dictionary. Make at least one new function call that includes
# the number of songs on an album.

print(make_album("one republic", "i ain't worried", 1))