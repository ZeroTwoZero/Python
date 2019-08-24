from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from imdb import IMDb
import shutil
import time
import os

#Object Creations.

imdbObject = IMDb()
observer = Observer()

if __name__ == "__main__":
    pattern = "*"
    IgnorePatterns = ""
    IgnoreDirectories = True
    CaseSensitive = True

EventHandlerForMoviesFolder = PatternMatchingEventHandler(pattern, IgnorePatterns, IgnoreDirectories, CaseSensitive)

    
def On_Created(event):
    #shutil.move(event.src_path)
    #print(event.src_path)
    MoveFolderOrFileLocation(event.src_path)

def MoveFolderOrFileLocation(FileLocation):
    FileName= FileLocation.replace(".\\" , "")
    FileNameWithoutExtension= FileName.split(".")[0]
    movie = imdbObject.search_movie(FileNameWithoutExtension)
    if movie:
        movie_details = imdbObject.get_movie(movie[0].movieID)
        genres=""
        for genre in movie_details['genres']:
            if not genres:
                genres = genre
            else:
                genres = genres + "_" + genre
        if not os.path.exists(".\\" + genres + "\\"):
            os.mkdir(".\\" + genres + "\\")
        shutil.move(FileLocation, ".\\" + genres + "\\" + FileName)
                                   
EventHandlerForMoviesFolder.on_created = On_Created
path="."
RecursiveExecution = True

observer.schedule(EventHandlerForMoviesFolder, path, recursive=RecursiveExecution)
observer.start()

try:
    while True:
        time.sleep(0)
except KeyboardInterrupt:
    observer.stop()
observer.join()


