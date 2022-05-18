# YTDownloader
YTDownloader is a GUI program currently built off of [PYTube](https://github.com/pytube/pytube) and [breezypythongui](https://lambertk.academic.wlu.edu/breezypythongui/) (Tkinter). The purpose of this program is to quickly install any video from YouTube with all the available quality options. If you don’t already know when downloading from your YouTube dashboard, you don’t get all the quality options and it takes forever to download the files. In my experience the download takes substantially less time using this method.

Right now, there is no option to combined the Video and Audio files that are installed so you will need to do that by yourself either in a video editor, such as [DaVinci Resolve](https://www.blackmagicdesign.com/products/davinciresolve), [FFMPEG](https://ffmpeg.org/), or with [VLC](https://wiki.videolan.org/VLC_HowTo/Play_an_external_audio_track_for_a_video/). 


# Installation Instructions / Dependencies 

### Python Requirements
YTDownloader requires you to use [Python 3.X](https://www.python.org/).

### Program Installation
1.	Click on the green “Code” dropdown and click “Download ZIP”
2.	Extract the files where you want to an ease to find location on your computer
### Dependency Installation
The only external library needed is [PYTube](https://github.com/pytube/pytube).

After you have Python installed open your native command prompt. On Windows use CMD or PowerShell. 

Once open, copy and past the following command into the prompt and wait for PIP to finish installing PYTube.


      pip install pytube


# Intructions
To use YTDownloader do the following.

NOTE: When looking at the available files, pay attention to the ITAG, res, fps, and type.

1.	Run “Downloader_GUI.py” by double clicking on it.  
2.	Copy the URL of the YouTube video you want to download.
3.	In the box next to “Video Link” use the CTRL + V shortcut to past the URL.
4.	Click “View Files”
5.	Next look over the files shown in the Available Files window. Separated by Video Files  and Audio Files.
6.	Pay attention to the ITAG number for the quality option you want. You will need one for Video and one for Audio.
7.	Once you find the options you want enter the ITAG number into the designated boxes. If you want to choose itag=”136” just enter 136 (NOTE: YOU NEED A VIDEO AND AUDIO OPTION SELECTED)
8.	Click Download to install the files.

If this is your first time using YTDownloader, a new folder will appear called “video_files”. This file is where you videos will be installed.

# Future Plans
This program is in its early stages and many things will be changed to make it far more user friendly. I’m new to GUI programing.

1.	Add a “system message” panel and prevent the command prompt from appearing.
2.	Get rid of the flashbang mode (light mode) and replace it with a dark mode.
3.	Improve the Available Files panel format.
4.	Make ITAG selection based off a dropdown box and not typed in.
5.	Add an option to allow for Video or Audio file downloads. (Right now, you have to download both.)
6.	Add the ability to right click and not just use keyboard shortcuts.
7.	If possible, performance updates.
8.	Add the ability to download Twitch VODS/Clips.


# Disclaimer 
I am not your parent and can’t tell you how to “morally” use this program. Keep in mind that Copyright laws exist and that downloading content that isn’t yours can infringe on copyright laws. USE WITH YOUR OWN DISCRETION. I am not responsible for how you use this program and will NOT be dragged into your legal issues if you do something you shouldn’t.
