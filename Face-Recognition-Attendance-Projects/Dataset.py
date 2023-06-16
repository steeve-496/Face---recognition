import cv2

camera = cv2.VideoCapture(0)
face_detection = cv2.CascadeClassifier("face_model.xml")
user_id = input("Enter your username:")
count = 0
while count < 20:
    success, frame = camera.read()
    if success:
        frame = cv2.flip(frame, 1)
        faces = face_detection.detectMultiScale(frame, minNeighbors=6, minSize=(100, 100))
        print(faces)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imwrite(user_id + '.jpg', frame[y:y + h, x:x + w])
            count = count + 1
        cv2.imshow("Face", frame)
        end = cv2.waitKey(1)
        if end == ord("1"):
            break
