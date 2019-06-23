#!/usr/bin/python

# This sample executes a search request for the specified search term.
# Sample usage:
#   python search.py --q=surfing --max-results=10
# NOTE: To use the sample, you must provide a developer key obtained
#       in the Google APIs Console. Search for "REPLACE_ME" in this code
#       to find the correct place to provide that key..

from googleapiclient.discovery import build

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search(developer_key: str, term: str, max_results: int) -> list:
    """
    It performs a youtube search using google API.
    :param developer_key: google API key that supports youtube data v3,
    :param term: search term,
    :param max_results: number of results,
    :return: [videos, channels, playlists], with each being arrays of tuples formatted this way: (title, id).
    """
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=developer_key)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=term,
        part='id,snippet',
        maxResults=max_results
    ).execute()

    videos = []
    channels = []
    playlists = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append((search_result['snippet']['title'],
                           search_result['id']['videoId']))
        elif search_result['id']['kind'] == 'youtube#channel':
            channels.append((search_result['snippet']['title'],
                             search_result['id']['channelId']))
        elif search_result['id']['kind'] == 'youtube#playlist':
            playlists.append((search_result['snippet']['title'],
                              search_result['id']['playlistId']))

    return [videos, channels, playlists]
