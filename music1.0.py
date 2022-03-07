# importing nessecery libs
from base64 import decode
import urllib.request as ur
from bs4 import BeautifulSoup
import re

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
while countForYoutubeTitles < len(video_ids):
    videoUrl = "https://www.youtube.com/watch?v=" + \
        video_ids[countForYoutubeTitles]
    html = ur.urlopen(videoUrl)
    soup = BeautifulSoup(html.read().decode(), 'html.parser')
    rawTitle = str(soup.get_text()).replace(
        ' - YouTubeAboutPressCopyrightContact usCreatorAdvertiseDevelopersTermsPrivacyPolicy & SafetyHow YouTube worksTest new features© 2022 Google LLC', '')
    print(f"{countForYoutubeTitles+1}. {rawTitle}")
    countForYoutubeTitles += 1

choice = int(input("Enter the Video number : "))
videoUrl = "https://www.youtube.com/watch?v=" + video_ids[choice-1]



