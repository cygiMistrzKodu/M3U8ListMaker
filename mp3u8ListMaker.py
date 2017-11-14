import sys
import os

def check_if_before_are_numbers_and_last_is_letter(listOfFirstTrackLetters):

    if  listOfFirstTrackLetters[-1].isdigit():
        return False

    for trackFirstLetter in listOfFirstTrackLetters[:-1]:
        if not trackFirstLetter.isdigit():
            return False

    return True

M3U8StartTag = '#EXTM3U'
M3U8StartTrackTag = '#EXTINF:'
CONST_FIRST_TRACK_LETTER_POSITION = 9

listOfTracks = []
listOfFirstTrackLetters = []

oneTrackEntry= '';
listOfTracks.append(M3U8StartTag + '\n')


for index, path in enumerate(sys.argv,start=0):
    if index != 0:
        oneTrackEntry += M3U8StartTrackTag + '\n'
        oneTrackEntry += os.path.basename(sys.argv[index]) + '\n'
        listOfFirstTrackLetters.append(oneTrackEntry[CONST_FIRST_TRACK_LETTER_POSITION])
        listOfTracks.append(oneTrackEntry)
        oneTrackEntry = ''

if check_if_before_are_numbers_and_last_is_letter(listOfFirstTrackLetters):

    lastTrack = listOfTracks.pop(-1)
    listOfTracks.insert(1, lastTrack)

finalListTrack = ''.join(listOfTracks)

files_dir_path = os.path.dirname(sys.argv[1])
m3u8ListFullName = files_dir_path+ '\\'
m3u8ListName = input("enter list name >: ")
m3u8ListName += ".m3u8"
m3u8ListFullName += m3u8ListName


mp3u9file = open(m3u8ListFullName,"w+")
mp3u9file.write(finalListTrack)
mp3u9file.close()

input("Job Done Enjoy your list :):)")
