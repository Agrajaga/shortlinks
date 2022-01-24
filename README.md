# Bitly url shortener

Creates a URL shortened through [Bitly](https://bitly.com/); ideal for sharing in social posts and other communications due to its neat and compact size.  
Also returns the number of clicks on shortened links.

## Usages

To shorten URL (for example, https://www.youtube.com/watch?v=dQw4w9WgXcQ)
```
$ python main.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
Shortlink: https://bit.ly/3FRWkIx
```
To get the number of clicks
```
$ python main.py https://bit.ly/3FRWkIx
Clicks: 1
```

## How to install

You must be registered on [bitly.com](https://bitly.com/)  and have an [access token](https://app.bitly.com/settings/api/).  
Create a file `.env` and put youre access token in it
```
BITLY_API_TOKEN=<youre_access_token>
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).