from typing import Dict
import time
import utils.spotify_utils as spotify_utils
import utils.list_utils as list_utils

from connector.spotify_connector import SpotifyConnector


class SpotifyService:
    spotify_connector = SpotifyConnector()
    sleep_seconds = 0.2

    def get_spotify_track_id(self, track_name: str, artist_name: str) -> str:
        response = self.spotify_connector.search_track(track_name, artist_name)
        if response.status_code == 200:
            time.sleep(self.sleep_seconds)
            return spotify_utils.get_track_id(response.json(), track_name, artist_name)
        else:
            error_status = response.status_code
            error_message = str(response.content)
            if error_status == 401:
                self.spotify_connector.refresh_access_token()
                return self.get_spotify_track_id(track_name, artist_name)
            else:
                exception_message = (
                    f"Error status {error_status} caused by: {error_message}"
                )
                raise Exception(exception_message)

    def get_spotify_tacks_audio_features(
        self, spotify_id_list: list[str]
    ) -> Dict[str, list]:
        spotify_ids_string = list_utils.list_to_string(spotify_id_list)
        response = self.spotify_connector.get_tracks_audio_features(spotify_ids_string)
        if response.status_code == 200:
            time.sleep(self.sleep_seconds)
            return self.get_track_audio_features_dict(response.json())
        else:
            error_status = response.status_code
            error_message = str(response.content)
            if error_status == 401:
                self.spotify_connector.refresh_access_token()
                return self.get_spotify_tacks_audio_features(spotify_id_list)
            else:
                exception_message = (
                    f"Error status {error_status} caused by: {error_message}"
                )
                raise Exception(exception_message)
