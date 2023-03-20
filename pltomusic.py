from pytube import Playlist , YouTube
plyList = input("ENter the playlist Link")
p = Playlist(plyList)
for url in p:
    yt =  YouTube(url)   
    x= yt.streams.filter(only_audio=True).order_by("abr").last()
    x.download()