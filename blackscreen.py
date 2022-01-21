import cv2  
import numpy as np  
  
#Starting the webcam
video = cv2.VideoCapture(0) 
image = cv2.imread("Nobara.png") 
  
while True: 
    #reading the frames of the video
    ret, frame = video.read() 
    print(frame)
    #Resizing
    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480)) 
  
  #Creating an array of RGB of faint black color shade and dark shade of black 
  #Storing it in l_black and u_black respectively.
    u_black = np.array([104, 153, 70]) 
    l_black = np.array([30, 30, 0]) 
  
  #Creating a mask using cv’s inRange() function 
    mask = cv2.inRange(frame, l_black, u_black) 
    res = cv2.bitwise_and(frame, frame, mask = mask) 
  
  #Using np.where() function to return frame or image if the value of f is 0.
    f = frame - res 
    f = np.where(f == 0, image, f) 
  
  #Showing the real video and masked video
    cv2.imshow("video", frame) 
    cv2.imshow("mask", f) 
  
  #Breaking the loop if the user presses “Esc” or “Q”.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
  
#Releasing the video and closing the video windows.
video.release() 
cv2.destroyAllWindows() 