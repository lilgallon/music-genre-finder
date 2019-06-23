from configparser import ConfigParser
from youtube.search import youtube_search
from genre.genreFinder import find_genre

config = ConfigParser()


def main():
    # 1. Get the files to analyse
    # ...
    files = ["Bring Me The Horizon - Mother Tongue (Sub Focus Remix)",
             "Tantrum. Today - Amateur",
             "G-Eazy - Random (Official Audio)"]

    # 2. Find their video ID
    # ...
    video_ids = []
    for file in files:
        results = youtube_search(config["API"]["youtube_key"], file, 1)
        videos = results[0]
        video = videos[0]
        video_id = video[1]
        video_ids.append(video_id)

    # 3. Find their genre
    # ...
    playlists = {}
    for video_id in video_ids:
        genre = find_genre(config["API"]["youtube_key"], video_id)
        if genre in playlists:  # if the genre already exist, we just need to append the video id
            playlists[genre].append(video_id)
        else:  # otherwise, we need to create a new key in the playlists dict
            playlists[genre] = [video_id]

    # 4. Create youtube playlists
    # ...
    print(playlists)


if __name__ == "__main__":
    config.read('../config.ini')
    main()
