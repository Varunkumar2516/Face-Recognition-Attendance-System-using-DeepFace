import cv2
import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}

def face_recognition():

    # DB connection (only once)
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    def draw_boundary(img, classifier, clf):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = classifier.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(100, 100)
        )

        for (x, y, w, h) in faces:

            # Ignore small detections
            if w < 80 or h < 80:
                continue

            face = gray[y:y+h, x:x+w]

            id, predict = clf.predict(face)
            confidence = int(100 - predict)

            print("ID:", id, "Confidence:", confidence)

            if confidence > 60:
                # Fetch student data
                cursor.execute(
                    "SELECT department, name, class_roll_no, university_roll_no, year FROM student WHERE student_id=%s",
                    (id,)
                )
                result = cursor.fetchone()

                if result:
                    dep, name, classroll, univrollno, year = result

                    # Green rectangle
                    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)

                    # Display details
                    cv2.putText(img, f"{name}", (x, y-40),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Roll: {classroll}", (x, y-20),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Year: {year}", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,255), 2)
                else:
                    # DB not found
                    cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 3)
                    cv2.putText(img, "Unknown", (x, y-10),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,255), 2)

            else:
                # Low confidence → Unknown
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 3)
                cv2.putText(img, "Unknown", (x, y-10),
                            cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,255), 2)

        return img

    # Load models
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("Classifier.yml")

    # Start camera
    cap = cv2.VideoCapture(0)

    while True:
        ret, img = cap.read()

        if not ret:
            break

        img = draw_boundary(img, faceCascade, clf)

        cv2.imshow("Face Recognition Attendance System", img)

        # Press Enter to exit
        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()
    conn.close()