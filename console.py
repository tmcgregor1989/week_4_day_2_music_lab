import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


artist_1 = Artist("KISS")
artist_repository.save(artist_1)

artist_2 = Artist("Meatloaf")
artist_repository.save(artist_2)


album_1 = Album("Bat Out of Hell", artist_2, "power rock")
album_repository.save(album_1)

album_2 = Album("Bat Out of Hell II", artist_2, "power rock")
album_repository.save(album_2)

album_3 = Album("Love Gun", artist_1, "Glam Rock")
album_repository.save(album_3)

album_4 = Album("Bat Out of Hell III", artist_2, "power rock-ish")
album_repository.save(album_4)

album_repository.delete_all()

artist_repository.delete_all()

found_album = album_repository.select(1)

found_artist = artist_repository.select(1)

found_artists = artist_repository.select_all()

found_albums = album_repository.select_all()

# artist_1 = Artist("Metallica", 1)
# artist_repository.update(artist_1)

# album_1 = Album("Master of Puppets", 1, "Thrash Metal", 3)
# album_repository.update(album_1)

pdb.set_trace()