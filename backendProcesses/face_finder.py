# take in image data and return the name of the face in the image if available
import face_recognition

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
def find_face(image):
    #load image
    image = face_recognition.load_image_file(image)
    #find faces
    face_locations = face_recognition.face_locations(image)
    #select face
    return find_prominent_face(face_locations)