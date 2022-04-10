# take in image data and return the name of the face in the image if available
import face_recognition
from hashlib import sha512
import json
import language_processing
import cv2

face_encodings = []
names = []


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
    global face_encodings
    #get the location of the faces in the image
    face_locations = []
    image = face_recognition.load_image_file(image_file)
    # cv2.imshow("obama", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    if image.shape[1] > 1200 or image.shape[0] > 1500:
        small_frame = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow("resized", small_frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        rgb_small_frame = small_frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
    else:
        rgb_small_frame = image[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_small_frame)
    
    # find the index of the most prominent image
    if len(face_locations) == 0:
        print("Here")
        return None
    
    max_index = find_prominent_face(face_locations)
    print(max_index)
    #get the face encoding of the most prominent face
    max_face_encoding = face_recognition.face_encodings(image)[max_index]
    #convert the face encoding to a list
    max_face_encoding.tolist()
    #print(type(max_face_encoding))
    print(max_face_encoding)
    #generate a hash for the face encoding
    #new_name = language_processing.get_name()
    new_name = "Obama"
    return new_name

if __name__ == "__main__":
    restore_saved_data()
    print(find_face_vector("./test-images/obama.jpg"))
    end_time = time.time()
    print(start_time - end_time)
    #print(find_face_vector("./test-images/theboys.jpg"))
    #print(find_face_vector("./test-images/ramani1.jpg"))

