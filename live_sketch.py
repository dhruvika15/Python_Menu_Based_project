import cv2
import numpy as np
kernel = np.ones((5,5))
cap = cv2.VideoCapture(0)

while True:
    ret, photo = cap.read()
    photo = cv2.morphologyEx(photo, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Title" , photo)
    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()
