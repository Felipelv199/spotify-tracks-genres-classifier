from __future__ import annotations
from typing import Any, Dict


class TrackAudioFeatureTypes:
    acousticness: float
    analysis_url: str
    danceability: float
    duration_ms: int
    energy: float
    spotify_id: str
    instrumentalness: float
    key: int
    liveness: float
    loudness: float
    mode: int
    speechiness: float
    tempo: float
    time_signature: int
    valence: float

    def json_to_instance(json: Dict[str, Any]) -> TrackAudioFeatureTypes:
        instance = TrackAudioFeatureTypes()
        instance.acousticness = json["acousticness"]
        instance.analysis_url = json["analysis_url"]
        instance.danceability = json["danceability"]
        instance.duration_ms = json["duration_ms"]
        instance.energy = json["energy"]
        instance.spotify_id = json["id"]
        instance.instrumentalness = json["instrumentalness"]
        instance.key = json["key"]
        instance.liveness = json["liveness"]
        instance.loudness = json["loudness"]
        instance.mode = json["mode"]
        instance.speechiness = json["speechiness"]
        instance.tempo = json["tempo"]
        instance.time_signature = json["time_signature"]
        instance.valence = json["valence"]
        return instance
