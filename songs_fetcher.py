from rauth import OAuth2Service
import bot
from lyricsgenius import Genius

token = bot.token
genius = Genius(token)
artist = genius.search_artist('Oxxxymiron', max_songs=1)

songs_ids = open("names_of_songs", "w")


page = 1
songs = []
while page:
    request = genius.artist_songs(artist.id,
                                  sort='popularity',
                                  per_page=50,
                                  page=page,
                                  )
    songs.extend(request['songs'])
    page = request['next_page']

print(songs)
for x in songs:
    songs_ids.write(x['api_path'] + "\n")

songs_ids.close()    

