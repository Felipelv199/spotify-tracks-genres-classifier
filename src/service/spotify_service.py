from typing import Any, Callable, Dict
import pandas as pd
import time

from connector.spotify_connector import SpotifyConnector
from models.service.track_audio_feature_types import TrackAudioFeatureTypes


class SpotifyService:
    spotify_connector = SpotifyConnector()

    def get_track_id(self, response_json: Dict[str, Any]) -> str:
        response_tracks = response_json["tracks"]
        tracks_items = response_tracks["items"]
        spotify_id = pd.NA
        if len(tracks_items) != 0:
            track_item = tracks_items[0]
            spotify_id = track_item["id"]
        return spotify_id

    def get_spotify_track_id(self, track_name: str, artist_name: str) -> str:
        response = self.spotify_connector.search_track(track_name, artist_name)
        if response.status_code == 200:
            time.sleep(2)
            return self.get_track_id(response.json())
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

    def list_to_string(self, l: list) -> str:
        return ",".join(l)

    def get_track_audio_features_dict(
        self, response_json: Dict[str, Any]
    ) -> Dict[str, list]:
        track_audio_feature_dict = {
            "acousticness": [],
            "analysis_url": [],
            "danceability": [],
            "duration_ms": [],
            "energy": [],
            "spotify_id": [],
            "instrumentalness": [],
            "key": [],
            "liveness": [],
            "loudness": [],
            "mode": [],
            "speechiness": [],
            "tempo": [],
            "time_signature": [],
            "valence": [],
        }
        audio_features = response_json["audio_features"]
        for audio_feature in audio_features:
            i_audio_feature = TrackAudioFeatureTypes.json_to_instance(
                audio_feature)
            track_audio_feature_dict["acousticness"].append(
                i_audio_feature.acousticness
            )
            track_audio_feature_dict["analysis_url"].append(
                i_audio_feature.analysis_url
            )
            track_audio_feature_dict["danceability"].append(
                i_audio_feature.danceability
            )
            track_audio_feature_dict["duration_ms"].append(
                i_audio_feature.duration_ms)
            track_audio_feature_dict["energy"].append(i_audio_feature.energy)
            track_audio_feature_dict["spotify_id"].append(
                i_audio_feature.spotify_id)
            track_audio_feature_dict["instrumentalness"].append(
                i_audio_feature.instrumentalness
            )
            track_audio_feature_dict["key"].append(i_audio_feature.key)
            track_audio_feature_dict["liveness"].append(
                i_audio_feature.liveness)
            track_audio_feature_dict["loudness"].append(
                i_audio_feature.loudness)
            track_audio_feature_dict["mode"].append(i_audio_feature.mode)
            track_audio_feature_dict["speechiness"].append(
                i_audio_feature.speechiness)
            track_audio_feature_dict["tempo"].append(i_audio_feature.tempo)
            track_audio_feature_dict["time_signature"].append(
                i_audio_feature.time_signature
            )
            track_audio_feature_dict["valence"].append(i_audio_feature.valence)
        return track_audio_feature_dict

    def get_spotify_tacks_audio_features(self, batch: list) -> Dict[str, list]:
        spotify_ids = []
        for row in batch:
            spotify_id = row[0]
            spotify_ids.append(spotify_id)
        spotify_ids_string = self.list_to_string(spotify_ids)
        response = self.spotify_connector.get_tracks_audio_features(
            spotify_ids_string)
        if response.status_code == 200:
            time.sleep(2)
            return self.get_track_audio_features_dict(response.json())
        else:
            error_status = response.status_code
            error_message = str(response.content)
            if error_status == 401:
                self.spotify_connector.refresh_access_token()
                return self.get_spotify_tacks_audio_features(batch)
            else:
                exception_message = (
                    f"Error status {error_status} caused by: {error_message}"
                )
                raise Exception(exception_message)
