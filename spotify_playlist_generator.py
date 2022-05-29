from colorama import init, Fore, Back, Style
import json
import requests
import argparse
import webbrowser
import os
from dotenv import load_dotenv
from main import decorator
load_dotenv()


token = os.getenv('SPOTIFY_TOKEN')
user_id = os.getenv('SPOTIFY_USER_ID')

market = "US"
seed_genres = "holidays"
uris = []
seed_artists = '0XNa1vTidXlvJ2gHSsRi4A'
seed_tracks = '55SfSsxneljXOk5S3NVZIW'


# parser = argparse.ArgumentParser()
# parser.add_argument('--count')
# parser.add_argument('--danceability')
# parser.add_argument('--acoustic')
# parser.add_argument('--liveness')
# args = parser.parse_args()
# count = args.count
# target_danceability = args.danceability
# min_acousticness = args.acoustic
# target_liveness = args.acoustic

init()
count = 20


@decorator
def main():
    print(Back.GREEN + 'SPOTIFY PLAYLIST GENERATOR')
    print(Style.RESET_ALL)
    print('*********************************************\n\n')

    min_acousticness = input(
        Fore.CYAN + "Enter value for accoustics: ")
    target_liveness = input(
        Fore.BLUE + "Enter value for liveness: ")
    target_danceability = input(
        Fore.MAGENTA + "Enter value for danceability: ")

    print(Style.RESET_ALL)
    endpoint_url = "https://api.spotify.com/v1/recommendations?"
    # PERFORM THE QUERY
    query = f'{endpoint_url}count={count}&market={market}&seed_genres={seed_genres}&target_danceability={target_danceability}&min_acousticness={min_acousticness}'
    query += f'&seed_artists={seed_artists}'
    query += f'&seed_tracks={seed_tracks}'

    response = requests.get(query,
                            headers={"Content-Type": "application/json",
                                     "Authorization": f"Bearer {token}"})
    json_response = response.json()
    print("response", response)
    print('Recommended Songs:')
    for i, j in enumerate(json_response['tracks']):
        uris.append(j['uri'])
        print(f"{i + 1}) \"{j['name']}\" by {j['artists'][0]['name']}")

    endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    request_body = json.dumps({
        "name": "CLI generated music player",
        "description": ".",
        "public": False
    })
    response = requests.post(url=endpoint_url, data=request_body, headers={"Content-Type": "application/json",
                                                                           "Authorization": f"Bearer {token}"})

    url = response.json()['external_urls']['spotify']
    playlist_id = response.json()['id']
    endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    request_body = json.dumps({"uris": uris})
    response = requests.post(url=endpoint_url, data=request_body, headers={"Content-Type": "application/json",
                                                                           "Authorization": f"Bearer {token}"})

    print(f'Your playlist is ready at {url}')
    webbrowser.open(url)


main()
