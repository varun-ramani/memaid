import asyncio

import av
from av import AudioFrame
from av.frame import Frame

from aiortc.mediastreams import AUDIO_PTIME, MediaStreamError, MediaStreamTrack
import numpy as np

from queue import Queue

import pyaudio

from streamaudio import start_recog_thread
audio = pyaudio.PyAudio()

# streamOut = audio.open(format=pyaudio.paFloat32, channels=1,
#                        rate=48000, output=True, input_device_index=0,
#                        frames_per_buffer=960)

RATE = 48000
CHUNK = 960
data_buffer = Queue()


async def consume_audio(track: MediaStreamTrack):
    while True:
        try:
            next_data: AudioFrame = await track.recv()

            next_data_arr: np.ndarray = next_data.to_ndarray()
            data_buffer.put(next_data_arr)

            # print(f"{next_data.format.name} {next_data.sample_rate} {next_data.samples} {next_data_arr}")
            # print(len(data_buffer.queue))

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