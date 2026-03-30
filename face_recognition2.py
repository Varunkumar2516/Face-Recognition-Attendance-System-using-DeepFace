import cv2
import os
from deepface import DeepFace
import mysql.connector
from dotenv import load_dotenv

# Load env
load_dotenv()

db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}

def face_recognition():

    # DB connection
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cap = cv2.VideoCapture(2,cv2.CAP_DSHOW)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            # DeepFace search
            results = DeepFace.find(
                img_path=frame,
                db_path="DATA",
                enforce_detection=False,
                silent=True,
                model_name="Facenet",          # better accuracy
                detector_backend="mtcnn",      # better face detection
            )

            if len(results[0]) > 0:
                # Best match path
                path = results[0].iloc[0]['identity']

                # Extract filename
                filename = os.path.basename(path)

                # Extract ID from "user.1.1.jpg"
                student_id = int(filename.split(".")[1])

                # Fetch from DB
                cursor.execute(
                    "SELECT department,name,class_roll_no,university_roll_no,year FROM student WHERE student_id=%s",
                    (student_id,)
                )
                result = cursor.fetchone()

                if result:
                    dep, name, classroll, univrollno, year = result

                    # Display
                    cv2.putText(frame, f"Name: {name}", (30,50),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 2)
                    cv2.putText(frame, f"Roll: {classroll}", (30,80),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 2)
                    cv2.putText(frame, f"Dept: {dep}", (30,110),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0), 2)
                else:
                    cv2.putText(frame, "Unknown", (30,50),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)

            else:
                cv2.putText(frame, "Unknown", (30,50),
                            cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)

        except Exception as e:
            cv2.putText(frame, "No Face", (30,50),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)

        cv2.imshow("DeepFace Recognition", frame)

        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()
    conn.close()