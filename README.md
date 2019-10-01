# Music genre finder
![opissues](https://img.shields.io/github/issues/N3ROO/music-genre-finder.svg) 
![clissues](https://img.shields.io/github/issues-closed/N3ROO/music-genre-finder.svg)

🔎 It looks at music files and detects their genre.

## 0. How does it work?
There are a lot of IA-based projects to detect the genre of songs, but it only covers "big" music genres (*pop*, *rock* and *jazz* for example).

This project consists in detecting very specific genres like *neurofunk*, *dubstep*, *lofi*, and *rap*. To do so, the program uses YouTube API
to get videos matching the song name. Then, with these videos, we can find useful information by taking a look at:
- the channel name (UKF Dubstep, House nation),
- some key words in the description,
- the tags.

If youtube API is not enough, we could use soundcloud, spotify, and deezer APIs.

## 1. Getting started
### 1.1 Prerequisites
- **python**: It works with python 3.7.3, and should be working for older versions (3+).
- **libraries**: Open a terminal and type `pip install -r requirements.txt` to install the needed libraries.
- **api key**: You need a Google API key that supports YouTube Data v3. Follow what is said in this link: https://developers.google.com/youtube/v3/getting-started

### 1.2 Setting up your dev environment
Put your Google API Key inside config.ini:
```
youtube_key = your_api_key_without_quotes
```

### 1.3 How to use it
For the moment, you can only use it by typing `python musicGenreFinder.py` in a terminal that is inside *musicGenreFinder* folder. It will be more "user-friendly" in the future.

## 2. Miscellaneous
### 2.1 Changelog
The changelog is available [here](CHANGELOG.md).

### 2.2 Authors
- **N3ROO** - *Initial work* - [Github](https://github.com/N3ROO) [Website](https://n3roo.github.io/)

### 2.3 License
This project is licensed under the GPL-3.0 license - see the [LICENSE](LICENSE) file for details