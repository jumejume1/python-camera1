#!/usr/bin/env python
import cv2

#cv2.CAP_DSHOW
cap=cv2.VideoCapture(1,cv2.CAP_DSHOW)

while(1):
	_, img = cap.read()
	    
	
	cv2.imshow("Original Image",img)	
    	 
	if cv2.waitKey(1)== ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
