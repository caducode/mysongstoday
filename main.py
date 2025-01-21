import requests
import base64


CLIENT_ID = "595f1f75f77b4285becc1b5349fa6561"
CLIENTE_SECRECT = "5c75dac3cc8c4731873d24df4bb15bec"
URL_TOKEN = "https://accounts.spotify.com/api/token"
URL_API = "https://api.spotify.com/v1/"

convert_base64 = f"{CLIENT_ID}:{CLIENTE_SECRECT}"
string_bytes = convert_base64.encode('ascii')
base64_bytes = base64.b64encode(string_bytes)
string_base64 = base64_bytes.decode('ascii')


def get_token():

    url = URL_TOKEN
    headers = { 
                'Authorization': f'Basic {string_base64}',
                'Content-Type': 'application/x-www-form-urlencoded',
            }
    payload = {
    "grant_type": "client_credentials"
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    token = response.json()['access_token'] 
    return token


def get_recently_played(token):
    url = f"{URL_API}me/player/recently-played"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.request("GET", url, headers=headers)

    return response.json()

obj_musics = get_recently_played(get_token())
print(obj_musics)

