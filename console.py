import pdb
from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

artist1 = Artist("Beyonce")
artist_repository.save(artist1)
artist2 = Artist("John Legend")
artist_repository.save(artist2)

album1 = Album("Lemonade", artist1, "Pop")
album_repository.save(album1)
album2 = Album("Get Lifted", artist2, "Pop")
album_repository.save(album2)

# album_repository.delete_all()
# artist_repository.delete_all()

artist_repository.select(5)


# print(artist_repository.select_all())

print(album_repository.select_all())