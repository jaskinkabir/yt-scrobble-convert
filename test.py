from ytmusicapi import YTMusic
import json

ytmusic = YTMusic()

# with open('watch-history.json', 'r', encoding='utf-8') as f:
#     history = json.load(f)

# listen_history = []

# for item in history:
#     if item['header'] == "YouTube Music":
#         listen_history.append(item)
# json.dump(listen_history, open('listen-history.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)

listen_history = json.load(open('listen-history.json', 'r', encoding='utf-8'))

def get_album(history_item: dict[str, str]) -> dict[str, str]:
    """Request album of a song from YouTube Music API

    Args:
        history_item (dict[str, str]): The item from the history.json file to get the album of

    Returns:
        dict[str, str]: The album name and browseid of the album
    """
    title = history_item["title"].split('Watched ')[1]
    search = ytmusic.search(
        query = title,
        filter='songs'
    )
    return [x for x in search if x['videoId'] == song_id][0]['album']


hist0 = listen_history[0]
url0 = hist0["titleUrl"]
title = hist0["title"].split('Watched ')[1]
song_id = url0.split('v=')[1]

search = ytmusic.search(
    query = title,
    filter='songs'
)
song = [x for x in search if x['videoId'] == song_id]
song = song[0]
print(song)