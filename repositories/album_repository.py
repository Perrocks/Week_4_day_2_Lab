from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (name, artist_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.name, album.artist.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE  FROM albums"
    run_sql(sql)

def select_all():
    albums= []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['name'], artist, row['genre'], row['id'])
        albums.append(album)
    return albums