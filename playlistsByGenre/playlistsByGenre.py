import argparse

from configparser import ConfigParser
from googleapiclient.errors import HttpError
from playlistsByGenre.youtube.search import youtube_search

config = ConfigParser()


def main():
    print('h')


def search():
    parser = argparse.ArgumentParser()
    parser.add_argument('--q', help='Search term', default='Google')
    parser.add_argument('--max-results', help='Max results', default=25)
    args = parser.parse_args()

    try:
        youtube_search(config['API']['key'], args)
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))


if __name__ == "__main__":
    global config  # Needed to modify global copy of config
    config.read('config.ini')
    main()
