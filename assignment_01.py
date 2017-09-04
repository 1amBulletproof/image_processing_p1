# python 2

import sys
import cv2

#Check and Read arguments
if len(sys.argv) < 4:
   print "ERROR: Missing Arguments"
   print "\tHOW: python %s image.jpg name last_name" % (sys.argv[0])
   sys.exit(1)

input_image = sys.argv[1]
name = sys.argv[2].upper()
last_name = sys.argv[3].upper()

#Read image
#COLOR:
img = cv2.imread(sys.argv[1],1)
#GRAYSCALE:
#img = cv2.imread(sys.argv[1],0)

#Write image
str_to_write = name + " " + last_name
font = cv2.FONT_HERSHEY_PLAIN
color = (255,255,255) #Red because OpenCV is BGR

#COLOR
rows,cols,depth = img.shape
#GRAYSCALE:
#rows,cols = img.shape

#cv2.putText(img, text, org(bottom_let_corner_of_string), fontFace, fontScale, color,thickness, line_type, bottomeLeftOrigin(true, img data origin @ bottom left)
cv2.putText(img,str_to_write,(rows/2-70,cols/4+35),font,2,color,1,cv2.LINE_AA)
#cv2.putText(img,str_to_write,(rows/10,cols/10),font,2,color,6,cv2.CV_AA)

#Show image and wait
cv2.imshow('Sheriff ' + name + ' ' + last_name ,img)
k = cv2.waitKey(0)

# wait for ESC key to exit
if k == 27:    
    cv2.destroyAllWindows()

# wait for 's' key to save and exit
elif k == ord('s'):
    output_file_name = last_name + "_output.jpg"
    cv2.imwrite(output_file_name, img)
    cv2.destroyAllWindows()
