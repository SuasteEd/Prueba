from pytube import Playlist

p = Playlist('https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')

print(f'Downloading: {p.title}')
Downloading: Python Tutorial for Beginers (For Absolute Beginners)
for video in p.videos:
video.streams.first().download()
