from PIL import ImageGrab
import numpy as np
import cv2
import win32gui

methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

def click_event(event, x, y, flags, params):
 
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img_np, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('tripletown', img_np)
 
    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)

hwnd = win32gui.FindWindow(None, 'BlueStacks App Player')
arrayX = 0
arrayY = 0
itemSize = 65
while True:
    try :
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    except :
        print("can't find the window")
        break
    img = ImageGrab.grab(bbox = (left, top, right+66, bottom+50))
    img_np = np.array(img)
    nextItem = img_np[125:180, 5:64]
    workplace = img_np[295:295+itemSize*6, 25:25+itemSize*6]
    # workplace = cv2.rectangle(workplace, (arrayX*itemSize,arrayY*itemSize), 
    #     (arrayX*itemSize+itemSize,arrayY*itemSize+itemSize), (0,0,255), 3)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("tripletown", img_np)
    cv2.imshow("workplace", workplace)
    dice = workplace[arrayX*itemSize:arrayX*itemSize+itemSize,
     arrayY*itemSize:arrayY*itemSize+itemSize]
    # cv2.imshow("nextItem", nextItem)
    cv2.imwrite('./temp/dice' + str(arrayX) + str(arrayY) + '.jpg', dice)
    cv2.imwrite('./temp/nextItem.jpg', nextItem)
    cv2.imwrite('./temp/workplace.jpg', workplace)
    if(arrayX >= 5):
        arrayX = 0
        arrayY = arrayY + 1
        if(arrayY >= 6):
            arrayY = 0
    else:
        arrayX = arrayX + 1
    
    cv2.setMouseCallback('tripletown',click_event)
    k = cv2.waitKey(500)&0xFF #64bits! need a mask
    if k ==27:
        cv2.destroyAllWindows()
        break