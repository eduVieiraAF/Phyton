from pytube import YouTube

# URL of the video
url = "https://www.youtube.com/watch?v=jnfTN5c41Ug"

# Create a YouTube object
yt = YouTube(url)

# Play the video
yt.streams.first().download()

