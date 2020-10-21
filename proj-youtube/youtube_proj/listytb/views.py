import requests

from isodate import parse_duration

from django.conf import settings
from django.shortcuts import render, redirect

def index(request):
    
    itens_url = 'https://www.googleapis.com/youtube/v3/playlistItems'

    itens_params = {
        'playlistId' : 'PL8H85HKySx21UaDs0qoY5N-yTTU8R_4Qg',
        'key' : settings.YOUTUBE_DATA_API_KEY,
        'part' : 'snippet,contentDetails',
        'maxResults' : 7
    }

    r = requests.get(itens_url, params=itens_params)

    results = r.json()['items']
    
    
    video_ids = []
    for result in results:
        video_ids.append(result['snippet'])

    print(r.text)
    
   
  
    videos = []
    for result in results:
        video_data = {
            'title' : result['snippet']['title'],
            'id' : result['contentDetails']['videoId'],
            'url' : 'https://www.youtube.com/watch?v=%s' % (result['contentDetails']['videoId']),
            #'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
            'thumbnail' : result['snippet']['thumbnails']['high']['url']
        }

        videos.append(video_data)

    
    context = {
        'videos' : videos
    }

    return render(request, 'index.html', context)
