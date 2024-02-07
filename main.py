import sys
import time
from twitch_downloader import download_livestream

twitch_link = "https://www.twitch.tv/bonus_daddies"

def parse_timer(v):
    try:
        result = int(v)
        return result
    except ValueError:
        print("Error: Unable to parse the string as an integer.")
        sys.exit(1)


def watcher(seconds):
    print("Watching twitch channel:", twitch_link)
    while True:
        # Do something
        print(download_livestream(twitch_link))

        time.sleep(seconds)


try:
    timer = sys.argv[1]  # First argument: Time in seconds to repeat the ping
except IndexError:
    print("Timer cannot be null")
    sys.exit(1)

timer = sys.argv[1]

timer = parse_timer(timer)

if (timer <= 0):
    print("Error: Time cannot be less than zero.")
    sys.exit(2)

watcher(seconds=timer)
sys.exit(0)