# youtube-cropper
Crop YouTube videos and convert them to various formats

***IMPORTANT:*** You have to fix pytube in order to use this script or else it won't work. It is a bug in pytube.
https://github.com/nficano/pytube/issues/642#issuecomment-637671478

Go to this folder: `C:\Users\{YOUR_USER}\AppData\Local\Programs\Python\Python38-32\Lib\site-packages\pytube`
Open `extract.py` and change the old cipher_url to the new cipher_url
**OLD:**
```
cipher_url = [
                parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
            ]
```
**NEW:**
```
cipher_url = [
                parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats)
            ]
```

You can edit the settings in the file. You can set the video url, a file name, a start time, an end time and an fps which is used for cropping. There is an example on the end of the file.

Requirements:
- Python 3.8
- moviepy
- pytube
- **pytube fix**
