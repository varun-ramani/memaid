import asyncio

import av
from av import AudioFrame
from av.frame import Frame

from aiortc.mediastreams import AUDIO_PTIME, MediaStreamError, MediaStreamTrack
import numpy as np

from queue import Queue

import pyaudio

import audioop

from transcription_service import start_recog_thread
audio = pyaudio.PyAudio()

RATE = 48000
CHUNK = 960
data_buffer = Queue()


async def consume_audio(track: MediaStreamTrack):
    while True:
        try:
            next_data: AudioFrame = await track.recv()

            next_data_arr: np.ndarray = next_data.to_ndarray()[0]
            next_data_bytes = b"".join([int(value).to_bytes(2, "little", signed=True) for value in next_data_arr])

            next_data_bytes = audioop.tomono(next_data_bytes, 2, 1, 0)
            data_buffer.put(next_data_bytes)

        except MediaStreamError:
            return

class AudioConsumer:
    def __init__(self):
        self.track = None

    def set_consume_track(self, track):
        self.track = track

    async def start(self):
        asyncio.ensure_future(consume_audio(self.track))
        start_recog_thread(RATE, CHUNK, data_buffer)