import cv2
cap = cv2.VideoCapture(0)
print("Press q to take selfie")
while True:
    _, frame = cap.read()
    cv2.imshow("Selfie", frame)
    if cv2.waitKey(10) == ord("q"):
        print("Selfie Taken")
        break