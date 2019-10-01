import json


def find_genre(developer_key: str, videos: str) -> str:
    with open("genre/genres.json", "r") as f:
        genres = json.load(f)

    # TODO: for the moment, we will only guess the genre by looking at the
    # channel ID. In the future we could look at the description and the tags
    # for example.

    # Here is how it works:
    # It loops over all the genres
    #   Then it gets the youtube channels that are concerned by this genre
    #       Finally, it checks if the YT channel is in the musics result
    #           If so, it adds a score to the concerned genre according to
    #           the accuracy of the channel for the given genre.

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

    # TODO: for the next step, we could return all the genres with their scores
    # so we can give a detailed output.

    # Now, we just need to get the most accurate genre we found
    more_accurate_genre = "unknown genre"
    best_accuracy = 0
    for genre in potential_genres.items():
        genre_name = genre[0]
        accuracy = genre[1]
        if accuracy > best_accuracy:
            accuracy = best_accuracy
            more_accurate_genre = genre[0]

    return more_accurate_genre
