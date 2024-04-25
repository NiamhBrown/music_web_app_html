import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods=['POST'])
def add_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    if not request.form:
        return "No data provided. Please enter some data!", 400

    new_album = Album(None, request.form['title'],request.form['release_year'], request.form['artist_id'])
    repository.create(new_album)
    return f"{request.form['title']} ({request.form['release_year']}) has been added!"

@app.route('/albums', methods=['GET'])
def return_albums():

    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return str(repository.all())
    # albums = repository.all()
    # album_list = [{'id': album.id, 'title': album.title, 'release_year': album.release_year, 'artist_id': album.artist_id} for album in albums]
    # print("hereeee")
    # print(album_list)
    # return album_list

@app.route('/albums/<int:id>', methods=['DELETE'])
def delete_album_by_id(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.delete(id)
    return f"Album with id = {id} has been successfully deleted"

@app.route('/artists', methods=['GET'])
def return_artists():

    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    return str(repository.all())

@app.route('/artists', methods=['POST'])
def add_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    if not request.form:
        return "No data provided. Please enter some data!", 400

    new_artist = Artist(None, request.form['name'],request.form['genre'])
    repository.create(new_artist)
    return f"{request.form['name']} has been added as an artist!"

@app.route('/artist/<int:id>', methods=['DELETE'])
def delete_artist_by_id(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    repository.delete(id)
    return f"Artist with id = {id} has been successfully deleted"

# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
