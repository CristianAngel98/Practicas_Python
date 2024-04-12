import lyricsgenius


genius = lyricsgenius.Genius("pqGge4vM4ugLoxlucw5k2yrPxpjn9sWry6091cwWvN-pe8f5PMWuEWST0d-6bEvS")
artist = genius.search_artist(input("Por favor ingrese un artista: "), max_songs= 0, sort = "title")
song = artist.song(input("Ingrese el nombre de la cancion de este artista: "))
#artist.save_lyrics()

print(song.lyrics)


