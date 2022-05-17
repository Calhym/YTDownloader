# -*- coding: utf-8 -*-
"""
Created on Wed May 11 19:50:04 2022

@author: Calvin
"""

import YouTubeDownloader as YD
from breezypythongui import EasyFrame

class DowloaderGUI(EasyFrame):
    
    def __init__(self):
        EasyFrame.__init__(self, "Video Downloader")
        self.setSize(width = 1000, height = 300)
        
        linkPanel = self.addPanel(row = 0, column = 0)
        linkPanel.addLabel("Video Link (use the paste shortcut. ex: CTRL+V ):",
                           row = 0, column = 0, sticky = "NE")
        
        #Get's the video URL
        self.videoLink = linkPanel.addTextField("", row = 0, column = 1, sticky = "NESW")
        
        self.textPanel = self.addPanel(row = 1, column = 0)
        self.textPanel.addLabel("Available Files", row = 0, column = 0, sticky = "NESW")
        self.availableFiles = self.textPanel.addTextArea("", row = 1, column = 0, height = 10,columnspan = 2)
        
        self.selectPanel = self.addPanel(row = 2, column = 0)
        self.selectPanel.addLabel("Video ITAG: ", row = 0, column = 0, sticky = "E")
        self.videoITAG = self.selectPanel.addTextField("", row = 0 , column = 1, sticky = "W")
        self.selectPanel.addLabel("Audio ITAG: ", row = 0, column = 2, sticky = "E")
        self.audioITAG = self.selectPanel.addTextField("", row = 0 , column = 3, sticky = "W")
        
        self.buttonPanel = self.addPanel(row = 3, column = 0)
        self.buttonPanel.addButton("View Files", row = 1, column = 0, 
                                   command = self.formatViewer)
        self.buttonPanel.addButton("Download", row = 1 , column = 1, command = self.download)
        
        #Used to store the VideoGrab object. Which returns a stream.
        self.videoGrab = None
        
    def formatViewer(self):
        """This funcation takes the VIDEO URL and get's streams that can be
        downloaded. The streams are then displayed in the text area"""
        
        #Clears the text area
        self.availableFiles.setText("")
        
        #Sets the VideoGrab object
        videoURL = str(self.videoLink.getText())
        self.videoGrab = YD.VideoGrab(videoURL)
        
        #Shows the available file tpypes
        videoFileList = self.videoGrab.videoTypeViewer()
        self.availableFiles.appendText("VIDEO FILES: \n")
        
        for file in videoFileList:
            self.availableFiles.appendText(file)
            self.availableFiles.appendText("\n")
        
        audioFileList = self.videoGrab.audioTypeViewer()
        self.availableFiles.appendText("\nAUDIO FILES: \n")
        
        for file in audioFileList:
            self.availableFiles.appendText(file)
            self.availableFiles.appendText("\n")
    
    def download(self):
        self.videoGrab.fileNameSet()
        
        videoITAG = self.videoITAG.getText()
        audioITAG = self.audioITAG.getText()

        self.videoGrab.formatSelect(videoITAG, audioITAG)
        x = self.videoGrab.fileDownloader()
        print(x)
        
        
        self.videoITAG.setText("")
        self.audioITAG.setText("")
        self.videoLink.setText("")

def main():
    
   DowloaderGUI().mainloop()
    
    
if __name__ == "__main__":
    main()