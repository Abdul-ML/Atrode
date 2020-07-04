#importing

import numpy as n
import cv2 as cv

#taking carbon copy of an image as an input
img='contr.jpeg'
Image = cv.imread(img)

#applying filter
cvtColor=cv.COLOR_BGR2GRAY
gray = cv.cvtColor(Image,cvtColor )
bin_thrsh=cv.THRESH_BINARY
_, Thrsh = cv.threshold(gray, 127,255, bin_thrsh)
R_tree=cv.RETR_TREE
c_approx=cv.CHAIN_APPROX_NONE

at_cont, _ = cv.findContours(Thrsh,R_tree ,c_approx )

cv.imshow("image", Image)

#calculating
count=0
for Atrodecontour in at_cont:
    arch=cv.arcLength(Atrodecontour, True)
    aprx = cv.approxPolyDP(Atrodecontour, 0.01* arch, True)
    cv.drawContours(Image, [aprx], 0, (0, 0, 0), 5)
    x = aprx.ravel()[0]
    y = aprx.ravel()[1] - 5
    if len(aprx) == 3:
        font=cv.FONT_HERSHEY_COMPLEX
        cv.putText(Image, "", (x, y),font , 0.5, (0, 0, 0))
    elif len(aprx) == 4:
        x1 ,y1, w, h = cv.boundingRect(aprx)
        aspct_Ratio = float(w)/h
        print(aspct_Ratio)
 #assigning the present roll numbers
    else:
        count=count+1

        font=cv.FONT_HERSHEY_COMPLEX
        cv.putText(Image, "Present", (x, y),font , 0.5, (0, 0, 0))

cv.putText(Image, f"Total present students = %d"%count, (10, 50),cv.FONT_ITALIC, 1, (0, 0, 255))


#output
print(count)
cv.imshow("Atrode", Image)
cv.waitKey(0)
cv.destroyAllWindows()