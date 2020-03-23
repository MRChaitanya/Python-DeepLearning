from apiclient.discovery import build
from firebase import firebase

# Arguments that need to passed to the build function
DEVELOPER_KEY = "AIzaSyCWrBmvhU0lK7lvJDVNtsC7m5dXH91mPHw"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

firebase = firebase.FirebaseApplication('https://news4u-e0844.firebaseio.com/', None)

# creating Youtube Resource Object
youtube_object = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                       developerKey=DEVELOPER_KEY)


def youtube_search_keyword(query, max_results):
    # calling the search.list method to
    # retrieve youtube search results
    search_keyword = youtube_object.search().list(q=query, part="id, snippet",
                                                  maxResults=max_results).execute()

    # extracting the results from search response
    results = search_keyword.get("items", [])

    # empty list to store video,
    # channel, playlist metadata
    videos = []
    playlists = []
    channels = []


    # extracting required info from each result object
    for result in results:
        # video result object
        #print(result)
        if result['id']['kind'] == "youtube#video":
            videos.append("% s (% s) (% s) (% s)" % (result["snippet"]["title"],
                                                     result["id"]["videoId"], result['snippet']['description'],
                                                     result['snippet']['thumbnails']['default']['url']))
            print("The following video is about:", result['snippet']['title'])
            print("The youtube URL for the video is: https://www.youtube.com/watch?v=" + result['id']['videoId'])
            print("The following video is published at:", result['snippet']['publishedAt'])
            data = {
                'URL': "https://www.youtube.com/watch?v=" + result['id']['videoId'],
                'Channel Name': channelname,
                'PublishedAt': result['snippet']['publishedAt'],
                'videotitle': result["snippet"]["title"],
                'videoid': result['id']['videoId']
            }
            chalo = firebase.post('/Videos/', data)
            print(chalo)
            print('Firebase Updated')



        # playlist result object
        elif result['id']['kind'] == "youtube#playlist":
            playlists.append("% s (% s) (% s) (% s)" % (result["snippet"]["title"],
                                                        result["id"]["playlistId"],
                                                        result['snippet']['description'],
                                                        result['snippet']['thumbnails']['default']['url']))
            print("playlist id:", result['id']['playlistId'])


        # channel result object
        elif result['id']['kind'] == "youtube#channel":
            channels.append("% s (% s) (% s) (% s)" % (result["snippet"]["title"],
                                                       result["id"]["channelId"],
                                                       result['snippet']['description'],
                                                       result['snippet']['thumbnails']['default']['url']))
            if result['id']['channelId'] == 'UCrKevLQTcgUp2kZ-WE0pWZQ':
                channelname = "Janasena Party"
                print("The videos from" "\t" + channelname + " are as follows:")
            elif result['id']['channelId'] == 'UC_2irx_BQR7RsBKmUV9fePQ':
                channelname = "ABN Andhra Jyothi"
                print("The videos from" "\t" + channelname + " are as follows:")
            else:
                channelname = "Sakshi TV"
                print("The videos from" "\t" + channelname +" are as follows:")
            print("ChannelId:", result['id']['channelId'])





if __name__ == "__main__":
    youtube_search_keyword('JanaSena', max_results=3)
    youtube_search_keyword('Sakshi TV', max_results=3)
    youtube_search_keyword('ABN Andhrajyothi', max_results=3)

