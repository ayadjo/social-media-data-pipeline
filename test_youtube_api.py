import os
from googleapiclient.discovery import build

API_KEY = "YOUTUBE_API_KEY"
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

def test_youtube_connection():
    # Establishing a connection to the YouTube API
    youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)

    # Sending a test request (video search on "data engineering")
    request = youtube.search().list(
        part="snippet",
        q="data engineering",
        maxResults=1
    )
    response = request.execute()

    # Printing results
    print("API connection is successful! Video found:")
    print("-" * 50)
    item = response["items"][0]
    print(f"Naslov: {item['snippet']['title']}")
    print(f"Kanal: {item['snippet']['channelTitle']}")
    print(f"ID videa: {item['id']['videoId']}")

if __name__ == "__main__":
    test_youtube_connection()