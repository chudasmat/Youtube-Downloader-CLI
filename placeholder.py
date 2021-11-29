#printing all the available streams
print(yt.streams)

#Printing only audio streams
print(yt.streams.filter(only_audio=True))
#Printing only video streams
print(yt.streams.filter(only_video=True))

#Enabling progressive streams
print(yt.streams.filter(progressive=True))