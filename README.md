# YMPO
Youtube Music Playlist Organizer, a simple Python application that uses `ytmusicapi` to help
user edit their playlists and organize in other playlists.

This is a personal project, I have built this to help me organize my music playlists. I am 
sharing my work in case anyone wants to use it. Enjoy!

#### Sample Use Case: 
If you have a cluttered playlist that you dump all the songs you like (like me), and you are
lazy to go over one by one and click all over Youtube to clean things up, then this is a really
simple app for you.

## Setup
There are not much dependencies so couple lines of setup will be enough (even if you have no idea
how to use python and/or unix).

Install Python if you don't have it [here](https://www.python.org/downloads/).
On your terminal/command prompt run;
```bash
pip install ytmusicapi
```

After installation we have two steps authentication instructions.
1. Copy authentication headers [-as decribed here-](https://ytmusicapi.readthedocs.io/en/latest/setup.html#copy-authentication-headers)
2. Run `setup.py`, paste the authentiaction header (step 1)
```python
python3 setup.py
```

## Run
The app is really simple and minimal. Go to your Youtube playlist and copy the id. 
Just run `ympo.py` and paste the id for the playlist you want to organize. 

```python
python3 ympo.py
```
