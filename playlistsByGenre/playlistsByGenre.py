from configparser import ConfigParser
from googleapiclient.errors import HttpError
from youtube.search import youtube_search

config = ConfigParser()


def main():
    results = search("surfing", 5)
    print(results)


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
