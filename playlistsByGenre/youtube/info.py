#!/usr/bin/python

from googleapiclient.discovery import build

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def video_info(developer_key: str, video_id: str) -> dict:
    """
    It retrieves the video information.
    :param developer_key: google API key that supports youtube data v3,
    :param video_id: the video id,
    :return: dict containing:
        - publishedAt
        - channelId
        - title
        - description
        - thumbnails
        - channelTitle
        - tags
        - categoryId
        - liveBroadcastContent
        - localized
        - defaultAudioLanguage
        You can get details by using this link: (replace VIDEO_ID and API_KEY).
         https://www.googleapis.com/youtube/v3/videos?part=snippet&id=VIDEO_ID&key=API_KEY
    """
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=developer_key)

    results = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()

    return results['items'][0]['snippet']

