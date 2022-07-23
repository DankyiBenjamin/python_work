from pytube import YouTube
from sys import argv

link = argv[3]
yt = YouTube(link)


print("Title: ", yt.title)
print("Views: ", yt.views)