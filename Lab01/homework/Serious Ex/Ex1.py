from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

# 1. Create connection
url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)

# 1.1 Download page
raw_data = conn.read()
html_content = raw_data.decode('utf-8')

# 2. Find ROI
soup = BeautifulSoup(html_content, "html.parser")
section = soup.find("section", "section chart-grid")

div = section.find("div", "section-content")

ul = div.find("ul")

li_list = ul.find_all("li")

song_list = []
list_song_name = []
for i in range(len(li_list)):
    li = li_list[i]
    h3 = li.h3.a
    h4 = li.h4.a

    song_name = h3.string
    artist_name = h4.string

    itunes = OrderedDict({
        "Song": song_name,
        "Artist": artist_name
    })
    song_list.append(itunes)
    list_song_name.append(song_name)

pyexcel.save_as(records=song_list, dest_file_name="itunes.xlsx")

options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 5, # Tell downloader to download only the first entry (audio)
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(list_song_name)