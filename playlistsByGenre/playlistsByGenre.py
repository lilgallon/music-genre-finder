from configparser import ConfigParser
from googleapiclient.errors import HttpError
from youtube.search import youtube_search
from youtube.info import video_info

config = ConfigParser()


def main():
    print('main')


def info(video_id: str) -> dict:
    """
    It retrieves the video information.
    :param video_id: the video ID.
    :return: None if an HttpError is caught, otherwise a dict containing:
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
    results = None
    try:
        results = video_info(config['API']['key'], video_id)
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
    return results


def search(term: str, max_results: int) -> list:
    """
    It performs a youtube search.
    :param term: the thing to look for,
    :param max_results: maximum number of results,
    :return: None if an HttpError is caught, the result otherwise: [videos, channels, playlists].
    """
    results = None
    try:
        results = youtube_search(config['API']['key'], term, max_results)
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
    return results


if __name__ == "__main__":
    config.read('../config.ini')
    main()
