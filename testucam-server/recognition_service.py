from queue import Queue
from time import sleep
import cv2
import threading

import face_recognition
import numpy as np

CASC_PATH = "./haarcascade_frontalface_default.xml"
face_casc = cv2.CascadeClassifier(CASC_PATH)

largest_face_queue = Queue()

facial_encodings = []
names = []

def run_haar(input_image):
    img = input_image

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_casc.detectMultiScale(gray, 1.3, 5, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)

    if len(faces) == 0:
        return None

    return faces

def draw_bboxes(input_image, bounding_boxes):
    if bounding_boxes is not None:
        for (x, y, w, h) in bounding_boxes:
            cv2.rectangle(input_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    return input_image

def get_largest_face(input_image, bounding_boxes):
    if bounding_boxes is not None:
        largest_area = 0
        largest_face = None

        for (x, y, w, h) in bounding_boxes:
            area = w * h
            if area > largest_area:
                largest_area = area
                largest_face = input_image[y:y + h, x:x + w]

        return largest_face

    else:
        return None

def set_largest_face(face):
    if not largest_face_queue.empty():
        largest_face_queue.get()
        
    largest_face_queue.put(face)

def facial_recognition(input_image):
    print(names)
    print(input_image.shape)
    
    input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

    cv2.imwrite("test.png", input_image)

    encodings = face_recognition.face_encodings(input_image)
    if len(encodings) == 0:
        print("Failed to find valid encodings")
        return

    encoding = encodings[0]

    if len(facial_encodings):
        matches = face_recognition.compare_faces(facial_encodings, encoding)
        face_distances = face_recognition.face_distance(facial_encodings, encoding)

        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            pass
        else:
            facial_encodings.append(encoding)
            names.append("Bruh")
    else:
        facial_encodings.append(encoding)
        names.append("Bruh")

def start_recognition_service():
    while True:
        if not largest_face_queue.empty():
            next_face = largest_face_queue.get()
            facial_recognition(next_face)

        sleep(0.05)

recognition_service_thread = threading.Thread(target=start_recognition_service)
recognition_service_thread.start()
