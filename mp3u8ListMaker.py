import sys
import os

# print('arguments: ', len(sys.argv))
# print('argument list: ', str(sys.argv))
# print('argument list: ', sys.argv[1])

listBegin = '#EXTM3U'
nextTrackBeginOnTop = '#EXTINF:'

listContent='';

listContent += listBegin + '\n'
# listContent += nextTrackBeginOnTop + '\n'

for index, path in enumerate(sys.argv,start=0):
     if(index != 0):
       listContent += nextTrackBeginOnTop + '\n'
       listContent += os.path.basename(sys.argv[index]) + '\n'


files_dir_path = os.path.dirname(sys.argv[1])
#print(files_dir_path)

m3u8ListFullName = files_dir_path+ '\\'
m3u8ListName = input("enter list name >: ")
m3u8ListName += ".m3u8"
m3u8ListFullName += m3u8ListName

# print(m3u8ListFullName)


mp3u9file = open(m3u8ListFullName,"w+")
mp3u9file.write(listContent)
mp3u9file.close()

# print(m3u8ListName);

input("Jobe Done Enjoy your list :):)")
# print(listContent)
# input("Czekam zebys zobaczyl co widzisz")