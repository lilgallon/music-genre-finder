from configparser import ConfigParser
from youtube.search import youtube_search
from youtube.info import video_info
from genre.genreFinder import find_genre

config = ConfigParser()


def main():
    # 1. Get the files to analyse
    # ... TODO
    musics = ["Bring Me The Horizon - Mother Tongue (Sub Focus Remix)",
             "Tantrum. Today - Amateur",
             "G-Eazy - Random (Official Audio)"]

    # 2. Find few channels for each music
    # ...
    result_amount = 5
    results_of_musics = []
    for music in musics:
        results = youtube_search(
            config["API"]["youtube_key"],
            music,
            result_amount)
        videos = results[0]
        results_of_musics.append((music, videos))

    # Results of musics looks like this:
    # [
    #    ("music title",
    #       ["video_title", "channel_id", "video_id"] , ... 5 times
    #       ["video_title", "channel_id", "video_id"] , ... 5 times
    #   ),
    #   ...
    # ]

    # 3. Find their genre
    # ...
    playlists = {}
    for results_of_music in results_of_musics:
        genre = find_genre(config["API"]["youtube_key"], results_of_music[1])
        if genre in playlists:  # if the genre already exist, we just need to append the video id
            playlists[genre].append(results_of_music[0])
        else:  # otherwise, we need to create a new key in the playlists dict
            playlists[genre] = [results_of_music[0]]

    # TODO: for the moment, playlists only contain the music name. It is used
    # to debug more easily. In the future, we will need all the information to
    # create playlists. Todo so, just change results_of_music[0] to
    # results_of_music[1] above. (Or even results_of_music if we want to keep
    # the original music name for logging).

    # 4. Create youtube playlists
    # ... TODO
    print(playlists)


if __name__ == "__main__":
    config.read('../config.ini')
    main()
