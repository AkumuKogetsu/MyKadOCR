import cv2
import numpy as np
import pytesseract

# TESSERACT INSTALLED LOCATION
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 

img = cv2.imread('1.PNG')

def base_photo():
    # Hardcoded base_image (IC Photo)
    x = 626 # - kiri, + kanan
    y = 120 # - bwh, + ats
    h = 383 # Tinggi
    w = 275 # Lebar
    crop_img = img[y:y+h, x:x+w] # Create box
    cv2.imwrite('IC_Photo.PNG',crop_img) # Save selected box
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2) # Display rectangle onto image
    cv2.imwrite('Selected_Box.jpg', img)
    cv2.imshow("Source", img)

def base_ic():
    # Hardcoded base_image (IC Photo)
    x = 15 # - kiri, + kanan
    y = 110 # - atas, + bwh
    h = 63 # Tinggi
    w = 340 # Lebar
    crop_ic = img[y:y+h, x:x+w] # Create box

    # Convert image into gray
    def grayscale(crop_ic):
        return cv2.cvtColor(crop_ic, cv2.COLOR_BGR2GRAY)
    gray_ic = grayscale(crop_ic) # Convert into gray image
    thresh, bw_ic = cv2.threshold(gray_ic, 70, 255, cv2.THRESH_BINARY)
    #cv2.imwrite("gray.PNG", gray_image) # Save gray image
    cv2.imshow("BlackWhite_IC", bw_ic) # Display gray converted image
    
    print(pytesseract.image_to_string(bw_ic))
    cv2.imwrite('bw_ic.PNG',bw_ic) # Save selected box
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2) # Display rectangle onto image
    cv2.imshow("Source", img)

def base_nama():
    # Hardcoded base_image (IC Photo)
    x = 25 # - kiri, + kanan
    y = 370 # - atas, + bwh
    h = 43 # Tinggi
    w = 365 # Lebar
    crop_nama = img[y:y+h, x:x+w] # Create box

    # Convert image into gray
    def grayscale(crop_nama):
        return cv2.cvtColor(crop_nama, cv2.COLOR_BGR2GRAY)
    gray_nama = grayscale(crop_nama) # Convert into gray image
    thresh, bw_nama = cv2.threshold(gray_nama, 70, 255, cv2.THRESH_BINARY)
    #cv2.imwrite("gray.PNG", gray_nama) # Save gray image
    cv2.imshow("BlackWhite_Nama", bw_nama) # Display gray converted image
    
    print(pytesseract.image_to_string(bw_nama))
    #cv2.imwrite('IC_Photo.PNG',crop_img) # Save selected box
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2) # Display rectangle onto image
    cv2.imshow("Source", img)

def base_alamat():
    # Hardcoded base_image (IC Photo)
    x = 25 # - kiri, + kanan
    y = 445 # - atas, + bwh
    h = 130 # Tinggi
    w = 290 # Lebar
    crop_alamat = img[y:y+h, x:x+w] # Create box
    #cv2.imwrite('IC_Photo.PNG',crop_img) # Save selected box

    # Convert image into gray
    def grayscale(crop_alamat):
        return cv2.cvtColor(crop_alamat, cv2.COLOR_BGR2GRAY)
    gray_alamat = grayscale(crop_alamat) # Convert into gray image
    thresh, bw_alamat = cv2.threshold(gray_alamat, 70, 255, cv2.THRESH_BINARY)
    cv2.imwrite("bw_alamat.PNG", bw_alamat) # Save gray image
    cv2.imshow("Gray Alamat", bw_alamat) # Display gray converted image

    # Print text and display rectangle onto image
    print(pytesseract.image_to_string(bw_alamat))
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2) 
    cv2.imshow("Source", img)

def base_agama():
    # Hardcoded base_image (IC Photo)
    x = 610 # - kiri, + kanan
    y = 520 # - atas, + bwh
    h = 40 # Tinggi
    w = 90 # Lebar
    crop_agama = img[y:y+h, x:x+w] # Create box
    #cv2.imwrite('IC_Photo.PNG',crop_img) # Save selected box

    # Convert image into gray
    def grayscale(crop_agama):
        return cv2.cvtColor(crop_agama, cv2.COLOR_BGR2GRAY)
    gray_agama = grayscale(crop_agama) # Convert into gray image
    thresh, bw_agama = cv2.threshold(gray_agama, 70, 255, cv2.THRESH_BINARY)
    cv2.imwrite("bw_agama.PNG", bw_agama) # Save blackwhite image
    cv2.imshow("BlackWhite_Agama", bw_agama) # Display gray converted image

    # Print text and display rectangle onto image
    print(pytesseract.image_to_string(bw_agama))
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2) 
    cv2.imshow("Source", img)

def base_jantina():
    # Hardcoded base_image (IC Photo)
    x = 748 # - kiri, + kanan
    y = 520 # - atas, + bwh
    h = 40 # Tinggi
    w = 105 # Lebar
    crop_jantina = img[y:y+h, x:x+w] # Create box
    #cv2.imwrite('IC_Photo.PNG',crop_img) # Save selected box

    # Convert image into gray
    def grayscale(crop_jantina):
        return cv2.cvtColor(crop_jantina, cv2.COLOR_BGR2GRAY)
    gray_jantina = grayscale(crop_jantina) # Convert into gray image
    thresh, bw_jantina = cv2.threshold(gray_jantina, 70, 255, cv2.THRESH_BINARY)
    cv2.imwrite("bw_jantina.PNG", bw_jantina) # Save blackwhite image
    cv2.imshow("BlackWhite_Jantina", bw_jantina) # Display gray converted image

    # Print text and display rectangle onto image
    print(pytesseract.image_to_string(bw_jantina))
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2) 
    cv2.imshow("Source", img)

def henshin():
    base_photo()
    base_ic()
    base_nama()
    base_alamat()
    base_agama()
    base_jantina()

henshin()
