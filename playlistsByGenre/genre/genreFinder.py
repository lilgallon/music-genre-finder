import json

def find_genre(developer_key: str, videos: str) -> str:
    with open("genre/genres.json") as f:
        genres = json.load(f)

    # TODO: for the moment, we will only guess the genre by looking at the
    # channel ID. In the future we could look at the description and the tags
    # for example.

    return 'unknown genre'
