from pytube import YouTube
from getch import pause
import time

link = input("Enter the Youtube Link: ")
yt = YouTube(link)

time.sleep(1)
print("\n")
#Title of video
print("Title: ", yt.title)
#Number of views of video
print("Number of views: ",yt.views)
#Length of the video
print("Length of video: ", yt.length, "seconds")
#Description of video
print("Description: ", yt.description)
#Rating
print("Ratings: ", yt.rating)

#Grabbing highest resolution
stream = yt.streams.get_highest_resolution()

print("Downloading...")
print("\n")
stream.download('location')
time.sleep(1)
print("Download complete")
print("\n")
time.sleep(1)
pause("Press any key to exit")

