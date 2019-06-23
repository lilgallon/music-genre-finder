# Playlists by genre
![opissues](https://img.shields.io/github/issues/N3ROO/playlistsByGenre.svg) 
![clissues](https://img.shields.io/github/issues-closed/N3ROO/playlistsByGenre.svg)

🔎 It looks at music filenames, 🎵 detects the genre, and ▶ creates playlists.

**Why this project?**
I am subscribed to a lot of music channels on youtube. Since 2012, I kept the best ones, and now
I have a total of ~7300 mp3 files of all genres:
- 2012: 198 musics
- 2013: 444 musics
- 2014: 769 musics
- 2015: 923 musics
- 2016: 2 043 musics
- 2017: 1 337 musics
- 2018: 1 101 musics
- 2019: 382 musics (in progress)

I decided that I would create youtube playlists for each genre, so I can listen to them anywhere. Here is my [youtube
channel](https://www.youtube.com/channel/UCEmXg3VBFGn7dN52OMA-inQ?view_as=subscriber) where the playlists will be published.

**How to detect the music genre?**
I saw that there are a lot of IA-based projects to detect the music genre, but it only covers *"big"* music genres.
I mean that "pop" as a ton of sub genres, as well as "rock".

I want to detect very specific genres like **neurofunk**, which is a sub genre of **drum and bass**, which is a sub
genre of **electronic music**. To do so, I will look at the youtube video information to retrieve the genre.
There are few approaches: 
- Looking for the channel name (UKF Dubstep, House nation),
- Looking for key words in the description,
- Looking for the video tags.

If youtube API is not enough, there are soundcloud, spotify, and deezer API for example.

## 1. Getting started
### 1.1 Prerequisites
It works with python 3.7.3, and should be working for older versions (3+).
Then, open a terminal and type `pip install -r requirements.txt` to install the needed libraries.

### 1.2 How to use it
*Still in development*

### 1.3 Setting up your dev environment
There is nothing special to do once that you match the prerequisites. You can use any IDE.

## 2. Miscellaneous
### 2.1 Changelog
The changelog is available [here](CHANGELOG.md).

### 2.2 Authors
- **N3ROO** - *Initial work* - [Github](https://github.com/N3ROO) [Website](https://n3roo.github.io/)

### 2.3 License
This project is licensed under the GPL-3.0 license - see the [LICENSE](LICENSE) file for details