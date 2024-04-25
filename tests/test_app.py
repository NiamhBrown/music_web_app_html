from playwright.sync_api import Page, expect

def test_return_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/music_library.sql")
    page.goto(f"http://{test_web_address}/albums")
    h2_tags = page.locator("h2")
    para_tags = page.locator("p")
    expect(h2_tags).to_have_text(["title1", "title2"])
    expect(para_tags).to_have_text(["Released: 1111", "Released: 2222"])

def test_return_an_album_with_id(page, test_web_address, db_connection):
    db_connection.seed('seeds/music_library.sql')
    page.goto(f"http://{test_web_address}/albums/1")
    h2_tags = page.locator("h2")
    para_tags = page.locator("p")
    expect(h2_tags).to_have_text(["title1"])
    expect(para_tags).to_have_text(["Released: 1111"])

# POST /albums
# parameters:
#   title=Voyage
#   release_year=2022
#   artist_id=2
#  Expected response (200 OK):
"""
when i call POST /albums with some album info
the album is now in the list GET /albums
"""
# def test_add_album(web_client, db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post('/albums', data = {'title':'Voyage', 'release_year':'2022', 'artist_id':'2'})
#     assert post_response.status_code == 200
#     assert post_response.data.decode('utf-8') == 'Voyage (2022) has been added!'
#     get_response = web_client.get('/albums')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "[Album(1, title1, 1111, 1), Album(2, title2, 2222, 2), Album(3, Voyage, 2022, 2)]"


# def test_add_album_with_no_data(web_client, db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post('/albums')

#     assert post_response.status_code == 400
#     assert post_response.data.decode('utf-8') == "No data provided. Please enter some data!"

# def test_delete_album_by_id(web_client, db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     delete_response = web_client.delete('/albums/1')

#     assert delete_response.status_code == 200
#     assert delete_response.data.decode('utf-8') == "Album with id = 1 has been successfully deleted"

#     get_response = web_client.get('/albums')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "[Album(2, title2, 2222, 2)]"


# # POST /artists
# # parameters:
# #   name=David
# #   genre = pop
# #  Expected response (200 OK):
# """
# when i call POST /artist with some artist info
# the artist is now in the list GET /artists
# """

# def test_add_artist(web_client, db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post('/artists', data = {'name':'David', 'genre':'pop'})
#     assert post_response.status_code == 200
#     assert post_response.data.decode('utf-8') == 'David has been added as an artist!'

#     get_response = web_client.get('/artists')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "[Artist(1, Pixies, Rock), Artist(2, ABBA, Pop), Artist(3, Taylor Swift, Pop), Artist(4, Nina Simone, Jazz), Artist(5, David, pop)]"

# def test_add_artist_with_no_data(web_client, db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     post_response = web_client.post('/artists')

#     assert post_response.status_code == 400
#     assert post_response.data.decode('utf-8') == "No data provided. Please enter some data!"

# def test_delete_artist_by_id(web_client, db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     delete_response = web_client.delete('/artist/1')

#     assert delete_response.status_code == 200
#     assert delete_response.data.decode('utf-8') == "Artist with id = 1 has been successfully deleted"

#     get_response = web_client.get('/artists')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == "[Artist(2, ABBA, Pop), Artist(3, Taylor Swift, Pop), Artist(4, Nina Simone, Jazz)]"



