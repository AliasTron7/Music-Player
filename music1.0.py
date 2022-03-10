# importing nessecery libs
from base64 import decode
import subprocess
import urllib.request as ur
from bs4 import BeautifulSoup
import re
import datetime

# time code
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
month = date.strftime("%M")
day = date.strftime("%D")

# variables
countForYoutubeTitles = 0

# Taking the user song input  and converting it to url stream .
songName = input("Enter the song name : ")
songNameUrlString = songName.replace(" ", "+")

# Youtube Url resource
searchUrl = rf"https://www.youtube.com/results?search_query={songNameUrlString}"

# Taking the response and letting the user choose from the titles of the videos

html = ur.urlopen(searchUrl)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
while countForYoutubeTitles < 3:  # we are going to print first 3 title of the youtube videos we get from the user input search len(video_ids)
    videoUrl = "https://www.youtube.com/watch?v=" + \
        video_ids[countForYoutubeTitles]
    html = ur.urlopen(videoUrl)
    soup = BeautifulSoup(html.read().decode(), 'html.parser')
    rawTitle = str(soup.get_text()).replace(
        f' - YouTubeAboutPressCopyrightContact usCreatorAdvertiseDevelopersTermsPrivacyPolicy & SafetyHow YouTube worksTest new features© {year} Google LLC',
        '')
    print(f"{countForYoutubeTitles+1}. {rawTitle}")
    countForYoutubeTitles += 1

choice = int(input("Enter the Video number : "))
videoUrl = "https://www.youtube.com/watch?v=" + video_ids[choice - 1]

subprocess.Popen(
    "start /b " + ".\\mpv-x86_64-20220306-git-1c49d57\\mpv " + videoUrl +
    " --no-video --loop=inf --input-ipc-server=\\\\.\\pipe\\mpv-pipe > output.txt",
    shell=True)
