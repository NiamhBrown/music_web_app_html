from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_get_all_records(db_connection): 
    db_connection.seed("seeds/music_library.sql") 
    repository = AlbumRepository(db_connection) 
    albums = repository.all() 
    assert albums == [Album(1, 'title1', 1111, 1), Album(2, 'title2', 2222, 2)]
"""
When we call AlbumRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new BookRepository
    repository.create(Album(None,'title3', '3333',3))
    result = repository.all()
    assert result == [Album(1, 'title1', 1111, 1),Album(2, 'title2', 2222,2), Album(3, 'title3', 3333,3)]

# """
# When we call BookRepository#find
# We get a single Book object reflecting the seed data.
# """
# def test_get_single_record(db_connection):
#     db_connection.seed("seeds/book_store.sql")
#     repository = BookRepository(db_connection)

#     book = repository.find(3)
#     assert book == Book(3, "Bluets", "Maggie Nelson")


# """
# When we call BookRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/book_store.sql")
#     repository = BookRepository(db_connection)
#     repository.delete(3) # Apologies to Maggie Nelson fans

#     result = repository.all()
#     assert result == [
#         Book(1, "Invisible Cities", "Italo Calvino"),
#         Book(2, "The Man Who Was Thursday", "GK Chesterton"),
#         Book(4, "No Place on Earth", "Christa Wolf"),
#         Book(5, "Nevada", "Imogen Binnie"),
#     ]
