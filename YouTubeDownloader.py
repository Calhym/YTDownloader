# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:58:21 2022

@author: Calvin/Calhym
"""
# from pprint import pprint
import os
from pytube import YouTube


class VideoGrab(YouTube):
    """This class is to be used as an interface for pytube. A Python library
    that allows you to download YouTube videos."""
    
    def __init__(self, url):
        
        #Get's and stores the pytube object
        self.videoURL = url
        YouTube.__init__(self, self.videoURL)
        
        self.videoTitle = self.title
        self.fileTitle = ""
        
        #Variables that hold format selection.
        self.audioSelect = ""
        self.videoSelect = ""
    
    
    def fileNameSet(self):
        """Gets the video title and parses it to remove any unusable
        characters so that it can be used in file names."""
        
        title = self.videoTitle.split()
        cleanTitle = []
        
        for word in title:
            cleaned = word.strip("<>:/\|?*().\"")
            cleanTitle.append(cleaned)
        
        #Used to test for unusable characters.
        # for word in cleanTitle:
        #     print(word)
        
        self.fileTitle = "_".join(cleanTitle)
        
        
    def formatSelect(self, videoITAG, audioITAG):
        """This funcation takes two strings that represent ITAG numbers for
        video and audio. The ITAGs can be viewed in video and audio
        TypeViewer functions"""

        self.videoSelect = videoITAG
        self.audioSelect = audioITAG
        
    
    def videoTypeViewer(self):
        """This funcation returns a list of the video types that are available
        to be downloaded"""
        
        #Filters the "mime_types" to make it easier to select MP4 based files
        #Adaptive removes files options that have audio and video but capped at 720 30
        video = self.streams.filter(mime_type = "video/mp4", adaptive = True)
        
        videoFileList = []
        
        for stream in video:
            videoStream = str(stream)
            videoFileList.append(videoStream)
        
        return videoFileList
    
    def audioTypeViewer(self):
        """This funcation returns a list of the audio types that are available
        to be downloaded"""
        
        #Filters the "mime_types" to make it easier to select MP4 based files
        #Adaptive removes files options that have audio and video but capped at 720 30
        audio = self.streams.filter(mime_type = "audio/mp4", adaptive = True)
        
        audioFileList = []
        
        for stream in audio:
            audioStream = str(stream)
            audioFileList.append(audioStream)
        
        return audioFileList
        
    def directoryCheck(self):
        """This function checks to make sure that the directory used for
        storing the downloaded files exists and if it doesn't, it's created."""
        
        # Directory used to store the downloaded files.
        directory = 'video_files'
        
        pathCheck = os.path.isdir(directory)
        
        if pathCheck == False:
            os.mkdir(directory)
        else:
            pass
            
    
    def fileDownloader(self):
        """This function will create the directory and file names first. Then
        it will go through the process of downloading the selected files, and 
        creates a Text file that will hold video information."""

        videoFile = "video_{}.mp4".format(self.fileTitle)
        audioFile = "audio_{}.mp4".format(self.fileTitle)
        
        #Makes file directory for the video
        fileDirectory = "video_files/{}".format(self.fileTitle)
        
        # Insure that the download directory exists.
        self.directoryCheck()
        
        try:
            os.mkdir(fileDirectory)
            
            #Creates a text file to store the video URL, Title, and Thumbnail URL
            videoURLTXT = "{}/{}.txt".format(fileDirectory, "videoInfo")
            channelFile = open(videoURLTXT,'w+', encoding = "UTF-16" )
    
            channelFile.write("Video Title: " + self.videoTitle +
                              "\n\nVideo URL: " + self.videoURL + 
                              "\n\nThumbnail URL: " + self.thumbnail_url)
            channelFile.close()
            
            #Select the video and audio files wanted for download
            ysVideo = self.streams.get_by_itag(self.videoSelect)
            ysAudio = self.streams.get_by_itag(self.audioSelect)
    
            #Downloads the selected video and audio files.
            ysVideo.download(output_path = fileDirectory, filename = videoFile)
            ysAudio.download(output_path = fileDirectory, filename = audioFile)
            return("Complete")
        
                
        
        except FileExistsError:
            errorMessage = """\n[ERROR] \"{}" already exists.
        If you want to redownload this video, delete the old folder
        then rerun the program and make your selections as usual""".format(self.fileTitle)
            
            return(errorMessage)
            
        #Used for debugging for when a new exeption is being thrown.
        except Exception as ex:
            return(ex)


def main():
    
    #Ask for YouTube video from user
    videoInput = input("Enter a YouTube video URL: ")
    print()
    
    #Creates video instance
    video = VideoGrab(videoInput)
    
    #Show video files
    print("VIDEO FILES:")
    print(video.videoTypeViewer())
    print()
    
    #User Select Video file
    videoSelect = input("Select a video file using the ITAG: ")
    print()
        
    #Show audio files
    print("AUDIO FILES:")
    print(video.audioTypeViewer())
    print()
    
    #User Select Audio file
    audioSelect = input("Select a audio file using the ITAG: ")
    print()
    
    video.formatSelect(videoSelect, audioSelect)
    print("Video Selected\n")
    
    video.fileNameSet()
    print(video.fileDownloader())
    
    
if __name__ == "__main__":
    main()