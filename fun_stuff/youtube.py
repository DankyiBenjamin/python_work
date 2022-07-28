from pytube import YouTube
yt = YouTube('https://youtu.be/7N3fQBuve3Y')
yt.filter(progressive = True, file_extension = 'mp4')
yt.order_by('resolution')
yt.streams.download()