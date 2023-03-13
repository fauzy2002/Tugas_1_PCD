# Nama : Mustafa Fauzy Tompoh
# NIM : F55121003
# Kelas : A

import cv2
import numpy as np

img = cv2.imread("fauzy.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar Fauzy Original", img)
cv2.imshow("Gambar Fauzy Greyscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
