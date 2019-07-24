import json

def find_genre(developer_key: str, videos: str) -> str:
    with open("genre/genres.json", "r") as f:
        genres = json.load(f)

    # TODO: for the moment, we will only guess the genre by looking at the
    # channel ID. In the future we could look at the description and the tags
    # for example.

    potential_genres = {}
    for genre in genres.items():
        genre_name = genre[0]
        channels = genre[1]
        potential_genres[genre_name] = 0

        for channel in channels:
            channel_id = channel["id"]
            channel_accuracy = channel["accuracy"]

            for video in videos:
                video_channel = video[1]

                if channel_id == video_channel:
                    potential_genres[genre_name] += channel_accuracy

    more_accurate_genre = "unknown genre"
    best_accuracy = 0
    for genre in potential_genres.items():
        genre_name = genre[0]
        accuracy = genre[1]
        if accuracy > best_accuracy:
            accuracy = best_accuracy
            more_accurate_genre = genre[0]

    return more_accurate_genre
