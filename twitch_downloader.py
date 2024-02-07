import yt_dlp
import time

def download_livestream(channel_url):
    return is_channel_live(channel_url, str(int(time.time()))+"_live.mp4")

def is_channel_live(channel_url, file_name):
    ydl_opts = {
        'outtmpl': f"../../livestreams/{file_name}",
        'fixup': 'never',
        'verbose': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([channel_url])
    except:
        print("Ninjacakeassassin is not currently online")
