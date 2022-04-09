# take in image data and return the name of the face in the image if available
import face_recognition
from hashlib import sha512
import json
import language_processing

face_encodings = {}

def restore_saved_data():
    with open("encodings.json", "r") as infile:
        face_encodings = json.load(infile)

# take array of face coordinates and return the index of the largest face
def find_prominent_face(faces):
    #find the maximum image area from face array
    max_area = 0
    max_index = 0
    for i in range(len(faces)):
        x_len = abs(faces[i][2] - faces[i][0])
        y_len = abs(faces[i][3] - faces[i][1])
        if x_len * y_len > max_area:
            max_area = x_len * y_len
            max_index = i

    return max_index

# 
def find_face_vector(image_file):
    face_encodings = {}
    #get the location of the faces in the image
    image = face_recognition.load_image_file(image_file)
    face_locations = face_recognition.face_locations(image)

    # find the index of the most prominent image
    max_index = find_prominent_face(face_locations)
    #get the face encoding of the most prominent face
    max_face_encoding = face_recognition.face_encodings(image)[max_index]
    #convert the face encoding to a list
    max_face_encoding.tolist()
    print(type(max_face_encoding))

    #generate a hash for the face encoding
    hex_face = sha512(max_face_encoding)

    # check if the face encoding is already in the database
    # if so, return the name, else add it and return the name
    if hex_face.hexdigest() in face_encodings:
        return face_encodings[hex_face.hexdigest()]
    else:
        new_name = language_processing.get_name()
        face_encodings[hex_face.hexdigest()] = new_name
        # save the face encodings to a file
        with open("encodings.json", "w") as outfile:
            json.dump(face_encodings, outfile)
        return new_name

    