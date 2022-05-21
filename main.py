import cv2 
import cvzone

capture = cv2.VideoCapture(0)
     
cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

filtertypes = ['beard.png','cool.png','native.png','pirate.png','star.png','sunglass.png']

ind = 0

while True:
    _,frame = capture.read()
    
    filters = cv2.imread(filtertypes[ind],cv2.IMREAD_UNCHANGED)

    grey_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = cascade.detectMultiScale(grey_frame)

    for (x,y,h,w) in faces:
        #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),2)

        filterresize = cv2.resize(filters,(int(w*1.5),int(h*1.5)))

        frame = cvzone.overlayPNG(frame,filterresize,[x-45, y-75])

        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(frame, 
                    '1.Beard 2.Cool 3.Native 4.Pirate 5.Star 6.Sunglass q.Quit', 
                    (10 , 20), 
                    font, 0.5, 
                    (0,0,0), 
                    2, 
                    cv2.LINE_AA)


        cv2.imshow('filter',frame)

    if cv2.waitKey(10) == ord('1'):
        ind = 0
    if cv2.waitKey(10) == ord('2'):
        ind = 1
    if cv2.waitKey(10) == ord('3'):
        ind = 2
    if cv2.waitKey(10) == ord('4'):
        ind = 3
    if cv2.waitKey(10) == ord('5'):
        ind = 4
    if cv2.waitKey(10) == ord('6'):
        ind = 5
    if cv2.waitKey(10) == ord('q'):
        break
    
        






