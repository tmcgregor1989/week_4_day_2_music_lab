from db.run_sql import run_sql

from models.album import Album
import repositories.artist_repository as artist_repository

def select_all():  
    albums = [] 

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], artist, row['genre'], row['id'] )
        albums.append(album)
    return album 

def save(album):
    sql = "INSERT INTO albums (title, artist, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.artist.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(album):
    sql = "UPDATE album SET (title, artist, genre) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.artist.id, album.genre, album.id]
    run_sql(sql, values)


def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], artist, result['genre'], result['id'])
    return album

