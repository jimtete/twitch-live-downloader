# Twitch live downloader

### Description
This tool tries to download a twitch's channel current live if the channel is online.
It utilizes the [yt-dlp library](https://github.com/yt-dlp/yt-dlp/releases)
as a python package and uses it to try and parse the channel's livestream.

### Requirements
```Python 3, yt-dlp```

### How it works
The algorithm does these steps:
* Parse the first argument as an integer. Null or non-integer values will make it fail. Values below 0 will also result in an error.
* The first argument represents the frequency in seconds which the tool has to wait in order to re-try parsing the livestream. The variable is called ```timer```.
* After the successful validation of the timer variable, then the tool enters an endless loop where it tries every ```timer``` seconds to download the livestream. The download code is saved in `twitch_downloader.py` file.
* `twitch_downloader.py` tries to download the livestream using the yt-dlp library. If the channel is not currently online, it will fail not throwing an exception and will re-try in ```timer``` seconds. If the channel is online, it will download the livestream as long as the tool runs and save it with the name of _xxxxxxxxx_live.mp4_ where _xxxxxxxxx_ represents the timestamp in seconds which the tool started parsing the livestream.
* The twitch channel is saved in `main.py` in ```twitch_link``` global variable at the top of the file.

### How to use
1. Change the ```twitch_link``` variable to the channel that you want to download its livestream.
2. Run ```python3 main.py 30``` or ```python main.py 30``` in the command line in the folder where the `main.py` file is saved. This will run the script in order to download and save the livestream as mentioned above. `30` represents the amount of seconds that you want the script to wait before re-trying to download the livestream.

### Optional
I highly suggest to use this script in a remote machine that will work on low power usage or on a cheap cloud server. The script doesn't require a lot of memory but a generous amount of space is highly suggested.

Additionally, in order to have access to the machine out of the running script, try using applications that allow multiple terminal sessions such as [screen](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-screen-on-an-ubuntu-cloud-server).

