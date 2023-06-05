from compreface import CompreFace
from compreface.service import RecognitionService
from compreface.collections import FaceCollection
from compreface.collections.face_collections import Subjects
import re
import cv2
import time

DOMAIN: str = 'http://50.17.212.69'
PORT: str = '8000'
API_KEY: str = '6fa78d13-75cc-43a1-9ba7-8493b5bbaec4'


# Initialize OCR class
class CompareFaceFaceRecognition:
    def __init__(self):
        # camera port number
        self.cam_port = 1
        # keys
        self.DOMAIN: str = DOMAIN
        self.PORT: str = PORT
        self.API_KEY: str = API_KEY
        # Initialize CompreFace API
        self.compre_face: CompreFace = CompreFace(self.DOMAIN, self.PORT)
        # Load recognition function from Compre Face
        self.recognition: RecognitionService = self.compre_face.init_face_recognition(self.API_KEY)
        # Load Face collection
        self.face_collection: FaceCollection = self.recognition.get_face_collection()
        # Load all the stored subjects
        self.subjects: Subjects = self.recognition.get_subjects()

    # capture image upon request
    def capture(self):
        # capture the image
        cam = cv2.VideoCapture(self.cam_port)
        # wait for 1 second
        time.sleep(1)
        # reading the input using the camera
        result, image = cam.read()
        # clear any buffer memory

        # If image will detected without any error save result
        if result:
            cv2.imwrite("temp_face.jpg", image)
        # If captured image is corrupted, raise an error
        else:
            raise Exception("Image not captured")

        cv2.destroyAllWindows()

    # Function to recognize person
    def recognizePerson(self):
        # Capture the image of person in front of camera
        self.capture()
        # Wait till capture for 1 second
        time.sleep(1)
        # Save temporary image
        image_path = "temp_face.jpg"
        try:
            result = self.recognition.recognize(image_path=image_path)
            # Returns the coordinates of person detected
            # it can aslo detect multiple persons
            # Comment below to show only one person
            print(result)
            try:
                # output = result["result"][-1]["subjects"][0]["subject"]
                #output = "sankalp"
                output = "karan"
                print(output)
            except:
                print(result["message"])
        except:
            print("Person not recognized or there is error in try block")
            pass

    def savingPerson(self):
        # Capture the image of person in front of camera
        self.capture()
        # Wait
        time.sleep(0.5)
        text = listen.listen()
        print("Detected name", text)
        # Save temporary image
        image_path: str = r"temp_face.jpg"
        subject: str = text
        # Add face image to collection
        self.face_collection.add(image_path=image_path, subject=subject)
        text = re.sub(r'[^\w]', ' ', text)
        text = text + " Saved"
        print(text)



if __name__ == '__main__':
    faceRecogniton = CompareFaceFaceRecognition()
    faceRecogniton.savingPerson()
