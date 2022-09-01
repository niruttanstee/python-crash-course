# Write a while loop that allows users to enter an album's artist and title.
# Once you have done that information, call make_album() with the user's
# input and print the dictionary that's created. Be sure to include a quit
# value in the while loop.

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

while True:
    print("\nPlease tell me the album information:")
    print("Enter (q) to quit the programme.")

    artist = input("Enter artist name: ")
    if artist == 'q':
        break
    title = input("Enter album title: ")
    if title == 'q':
        break
    songs = input("Enter number of songs, press enter by itself" + 
    " if you wish to not add an input: ")
    if songs == 'q':
        break
    
    if songs == '':
        album = make_album(artist_name=artist, album_title=title)
    else:
        songs = int(songs)
        album = make_album(artist_name=artist, album_title=title, 
        number_of_songs=songs)

    print(album)



