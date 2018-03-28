import speech_recognition as sr
import sys
import os
import urllib
import bs4 as bs
import urllib.request
import re
import json
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import subprocess
import re
import os 




# Keine Datei angegeben (verwende Mikrofon)
if len(sys.argv) == 1:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Höre zu...")
		audio = r.listen(source)
else: # WAV-Datei ist als Kommandozeilen-Argument mitgegeben
	r = sr.Recognizer()
	with sr.AudioFile(sys.argv[1]) as source:
		audio = r.listen(source)

print(r.recognize_google(audio, language="de_DE"))
i= r.recognize_google(audio, language="de_DE")
print(i)


DEVELOPER_KEY = "Key eingeben"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))
      a= videos
    elif search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
    elif search_result["id"]["kind"] == "youtube#playlist":
      playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                    search_result["id"]["playlistId"]))

  print ("Videos:\n", "\n".join(videos), "\n")
  print ("Channels:\n", "\n".join(channels), "\n")
  print ("Playlists:\n", "\n".join(playlists), "\n")
  a= str(videos[1])
  b= a.split("(",1)[1]
  x= b[:-1]
  print(x)
  Link= "firefox"+ " "+ "https://www.youtube.com/watch?v="+ x
  print(Link)
  os.system(Link)




keyword= i # Suchwort nach Spracherkennung

if __name__ == "__main__":
  argparser.add_argument("--q", help="Search term", default= keyword) # insert default= "keyword", just make it a variable in order to make a proper search engine
  argparser.add_argument("--max-results", help="Max results", default=25)
  args = argparser.parse_args()

youtube_search(args)

        




        
