import datetime
import time

class SubtitleLines:
    def __init__(self,id,time,subtitleText):
        self.id = id
        self.time = time
        self.Text = subtitleText

try:
    subtitleLocation = input("Enter Complete Location of the File with Extension (eg:C:\Movies\English\TopGun\TopGun.srt):")
    f=open(subtitleLocation, "r")
    fileLocationArray =subtitleLocation.split("\\")
    resyncedFileName = "(Resynced) " + fileLocationArray[len(fileLocationArray) - 1]
    del fileLocationArray[len(fileLocationArray) - 1]
    fResync= open("\\".join(fileLocationArray) + "\\" + resyncedFileName,"w+")
    contents = f.read()
    subtitleDelay = input("Enter delay for subtitle in secs:")
    myarray = contents.split("\n\n")
    subtitleLineArray = []
    for line in myarray:
        lineArray = line.split("\n")
        id = lineArray[0]
        time = lineArray[1]
        del lineArray[0]
        del lineArray[0]
        subLine = SubtitleLines(id, time, '\n'.join(lineArray))
        subtitleLineArray.append(subLine)
    for subtitleLine in subtitleLineArray:
        lineArray = subtitleLine.time.split(" ")
        strIncreasedTime1 = (datetime.datetime.strptime(lineArray[0].split(",")[0], '%H:%M:%S') + datetime.timedelta(seconds = int(subtitleDelay))).time().strftime("%H:%M:%S")
        finalTime1 = strIncreasedTime1+","+lineArray[0].split(",")[1]
        strIncreasedTime2 = (datetime.datetime.strptime(lineArray[2].split(",")[0], '%H:%M:%S') + datetime.timedelta(seconds = int(subtitleDelay))).time().strftime("%H:%M:%S")
        finalTime2 = strIncreasedTime2+","+lineArray[2].split(",")[1]
        subtitleResyncedTime = finalTime1+ " " + lineArray[1] + " " + finalTime2
        fResync.write(subtitleLine.id + "\n" + subtitleResyncedTime + "\n" + subtitleLine.Text +"\n\n")
    fResync.close()
    f.close()
except:
    print("\nPlease ensure you've given the entire file location with extensions specified. Also check the file do exist in that location")

    
