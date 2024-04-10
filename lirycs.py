
import lyricsgenius
#from lyricsgenius import Genius

genius = lyricsgenius.Genius("pqGge4vM4ugLoxlucw5k2yrPxpjn9sWry6091cwWvN-pe8f5PMWuEWST0d-6bEvS")
artist = genius.search_artist("Billie Elish", max_songs= 0, sort = "title")
song = artist.song("lovely")
#artist.save_lyrics()



with open("lovely.txt", "w", encoding= "utf-8") as l:
    l.write(song.lyrics)

"""
import lyricsgenius

# Inicializar el cliente de LyricsGenius con tu token de acceso
genius = lyricsgenius.Genius("pqGge4vM4ugLoxlucw5k2yrPxpjn9sWry6091cwWvN-pe8f5PMWuEWST0d-6bEvS")

# Buscar la letra de una canción específica
cancion = genius.search_song("Flawless", "Beyonce")

# Imprimir la letra si la canción fue encontrada
if cancion:
    with open("Lyrics.txt", "w", encoding="utf-8") as l:
        l.write(cancion.lyrics)
    print("La letra de 'Flawless' by Beyonce ha sido guardada en el archivo 'letra_flawless.txt'.")
else:
    print("La canción no fue encontrada.")
"""
