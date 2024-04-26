from lib.album import Album

def test_album_constructs():
    album = Album(1, "Test Title", 1234, 1 )
    assert album.id == 1
    assert album.title == "Test Title"
    assert album.release_year == 1234
    assert album.artist_id == 1

def test_album_formats_nicely():
    album = Album(1, "Test Title", 1234, 1)
    assert str(album) == "Album(1, Test Title, 1234, 1)"

def test_albums_are_equal():
    album1 = Album(1, "Test Title", 1234, 1)
    album2 = Album(1, "Test Title", 1234, 1)
    assert album1 == album2

def test_is_valid():
    album1 = Album(1, "", 1234, 1)
    album2 = Album(1, None, 1234, 1 )
    album3 = Album(1, "title", None, 1 )
    assert album1.is_valid() == False
    assert album2.is_valid() == False
    assert album3.is_valid() == False

def test_generate_errors():
    album1 = Album(1, "", 1234, 1)
    album2 = Album(1, "tttt", None, 1)
    album3 = Album(1, None, None, 1)
    assert album1.generate_errors() == "Title can't be blank"
    assert album2.generate_errors() == "Release year can't be blank"
    assert album3.generate_errors() == "Title can't be blank, Release year can't be blank"