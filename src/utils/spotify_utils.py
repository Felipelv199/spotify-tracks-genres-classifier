from typing import Any, Dict
import pandas as pd

from models.track_audio_feature_types import TrackAudioFeatureTypes


def is_valid_track(track, track_name: str, artist_name: str) -> bool:
    tn = track["name"]
    artists = track["artists"]
    artist_name_list = []
    for artist in artists:
        artist_name_list.append(artist["name"])
    an = ", ".join(artist_name_list)
    return track_name == tn and artist_name == an

def get_track_id(response_json: Dict[str, Any], track_name: str, artist_name: str) -> str:
    response_tracks = response_json["tracks"]
    tracks_items = response_tracks["items"]
    spotify_id = pd.NA
    if len(tracks_items) != 0:
        for track in tracks_items:
            if is_valid_track(track, track_name, artist_name):
                return track["id"]
    return spotify_id

def get_track_audio_features_dict(response_json: Dict[str, Any]) -> Dict[str, list]:
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
        i_audio_feature = TrackAudioFeatureTypes.json_to_instance(audio_feature)
        track_audio_feature_dict["acousticness"].append(
            i_audio_feature.acousticness
        )
        track_audio_feature_dict["analysis_url"].append(
            i_audio_feature.analysis_url
        )
        track_audio_feature_dict["danceability"].append(
            i_audio_feature.danceability
        )
        track_audio_feature_dict["duration_ms"].append(i_audio_feature.duration_ms)
        track_audio_feature_dict["energy"].append(i_audio_feature.energy)
        track_audio_feature_dict["spotify_id"].append(i_audio_feature.spotify_id)
        track_audio_feature_dict["instrumentalness"].append(
            i_audio_feature.instrumentalness
        )
        track_audio_feature_dict["key"].append(i_audio_feature.key)
        track_audio_feature_dict["liveness"].append(i_audio_feature.liveness)
        track_audio_feature_dict["loudness"].append(i_audio_feature.loudness)
        track_audio_feature_dict["mode"].append(i_audio_feature.mode)
        track_audio_feature_dict["speechiness"].append(i_audio_feature.speechiness)
        track_audio_feature_dict["tempo"].append(i_audio_feature.tempo)
        track_audio_feature_dict["time_signature"].append(
            i_audio_feature.time_signature
        )
        track_audio_feature_dict["valence"].append(i_audio_feature.valence)
    return track_audio_feature_dict
