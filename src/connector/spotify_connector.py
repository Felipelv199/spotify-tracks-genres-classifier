import requests
import base64
import configparser


class ResponseGetTrackAudioFeatures:
    acousticness: float
    analysis_url: str
    danceability: float
    duration_ms: int
    energy: float
    id: str
    instrumentalness: float
    key: int
    liveness: float
    loudness: float
    mode: int
    speechiness: float
    tempo: float
    time_signature: int
    track_href: str
    type: str
    uri: str
    valence: float


class SpotifyConnector:
    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config.sections()
        config.read("../properties.ini")
        self.auth_token = config["spotify"]["access_token"]
        self.refresh_token = config["spotify"]["refresh_token"]
        self.client_id = config["spotify"]["client_id"]
        self.client_secret = config["spotify"]["client_secret"]
        self.refresh_access_token()

    def refresh_access_token(self):
        credentials = f"{self.client_id}:{self.client_secret}"
        credentials_bytes = bytes(credentials, "utf-8")
        authorization = base64.b64encode(credentials_bytes)
        authorization_str = authorization.decode("utf-8")
        h_payload = {
            "Authorization": f"Basic {authorization_str}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        d_payload = {"grant_type": "refresh_token", "refresh_token": self.refresh_token}
        response = requests.post(
            f"https://accounts.spotify.com/api/token", headers=h_payload, data=d_payload
        )
        if response.status_code == 200:
            response_json = response.json()
            self.auth_token = response_json["access_token"]
        else:
            print(response.content)

    def search_track(self, track_name: str, artist_name: str):
        query = f'track:"{track_name}"+artist:"{artist_name}"'
        p_payload = {"q": query, "type": "track"}
        h_payload = {"Authorization": f"Bearer {self.auth_token}"}
        return requests.get(
            "https://api.spotify.com/v1/search", params=p_payload, headers=h_payload
        )

    def get_tracks_audio_features(self, ids: str):
        h_payload = {"Authorization": f"Bearer {self.auth_token}"}
        p_payload = {"ids": ids}
        return requests.get(
            f"https://api.spotify.com/v1/audio-features",
            headers=h_payload,
            params=p_payload,
        )
