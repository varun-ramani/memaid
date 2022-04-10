import argparse
import asyncio
import atexit
import json
import logging
import os
import uuid
import face_recognition
import cv2

from aiohttp import web
from av import VideoFrame
import aiohttp_cors
from aiortc import MediaStreamTrack, RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaBlackhole, MediaPlayer, MediaRecorder, MediaRelay

ROOT = os.path.dirname(__file__)

logger = logging.getLogger("pc")
pcs = set()
relay = MediaRelay()

# from pathlib import Path
# data_json_path = Path("data.json")
# if data_json_path.exists():
#     with open("data.json", "r") as f:
#         data_storage = json.load(f)
# else:
#     data_storage = {}
faces = []
names = []

class VideoTransformTrack(MediaStreamTrack):
    """
    A video stream track that transforms frames from an another track.
    """

    kind = "video"

    def __init__(self, track, transform):
        super().__init__()  # don't forget this!
        self.track = track
        self.transform = transform

    async def recv(self):
        global faces
        global names
        frame = await self.track.recv()

        img = frame.to_ndarray(format="bgr24")
        
        # whatever you do here
        face_locations = face_recognition.face_locations(img)
        max_area = 0
        max_index = 0
        for i in range(len(faces)):
            x_len = abs(faces[i][2] - faces[i][0])
            y_len = abs(faces[i][3] - faces[i][1])
            if x_len * y_len > max_area:
                max_area = x_len * y_len
                max_index = i
        
        max_face_encoding = face_recognition.face_encodings(image)[max_index]
        
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        face_distances = face_recognition.face_distance(faces, max_face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            print("Duplicate face")
        else:
            faces.append(max_face_encoding)
            names.append("Ramani")

        for (top, right, bottom, left), name in zip(face_locations, names):
            cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        transform_output = img
        new_frame = VideoFrame.from_ndarray(img, format="bgr24")
        new_frame.pts = frame.pts
        new_frame.time_base = frame.time_base

        return new_frame

async def offer(request):
    params = await request.json()
    offer = RTCSessionDescription(sdp=params["sdp"], type=params["type"])

    pc = RTCPeerConnection()
    pc_id = "PeerConnection(%s)" % uuid.uuid4()
    pcs.add(pc)

    def log_info(msg, *args):
        logger.info(pc_id + " " + msg, *args)

    log_info("Created for %s", request.remote)

    # prepare local media
    player = MediaPlayer(os.path.join(ROOT, "demo-instruct.wav"))
    recorder = MediaBlackhole()

    @pc.on("datachannel")
    def on_datachannel(channel):
        @channel.on("message")
        def on_message(message):
            if isinstance(message, str) and message.startswith("ping"):
                channel.send("pong" + message[4:])

    @pc.on("connectionstatechange")
    async def on_connectionstatechange():
        log_info("Connection state is %s", pc.connectionState)
        if pc.connectionState == "failed":
            await pc.close()
            pcs.discard(pc)

    @pc.on("track")
    def on_track(track):
        log_info("Track %s received", track.kind)
        print(f"Got new track {track.kind}")

        if track.kind == "audio":
            pc.addTrack(player.audio)
            recorder.addTrack(track)
        elif track.kind == "video":
            pc.addTrack(
                VideoTransformTrack(
                    relay.subscribe(track), transform=params["video_transform"]
                )
            )

        @track.on("ended")
        async def on_ended():
            log_info("Track %s ended", track.kind)
            await recorder.stop()

    # handle offer
    await pc.setRemoteDescription(offer)
    await recorder.start()

    # send answer
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)

    return web.Response(
        content_type="application/json",
        text=json.dumps(
            {"sdp": pc.localDescription.sdp, "type": pc.localDescription.type}
        ),
    )


async def on_shutdown(app):
    # close peer connections
    coros = [pc.close() for pc in pcs]
    await asyncio.gather(*coros)
    pcs.clear()


app = web.Application()
cors = aiohttp_cors.setup(app)
app.on_shutdown.append(on_shutdown)
app.router.add_post("/offer", offer)

for route in list(app.router.routes()):
    cors.add(route, {
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
            allow_methods="*"
        )
    })

# def persist_data():
#     with open("data.json", "w") as f:
#         json.dump(data_storage, f)

atexit.register(persist_data)

if __name__ == "__main__":
    web.run_app(
        app, access_log=None, host="0.0.0.0", port=8080, ssl_context=None
    )