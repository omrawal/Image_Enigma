import numpy as np
import cv2
import matplotlib.pyplot as plt
from steganography import Steganography
import time

steg_var=Steganography()

mask_img=cv2.imread("./Resources/mask.png")
secret_message_img=cv2.imread("./Resources/message_paint.png")
cypher=steg_var.embed_a_in_b(secret_message_img,mask_img)

filename='./encrypted_images/'+time.strftime("%Y%m%d-%H%M%S")+'.jpg'
# print(cv2.imwrite(filename, cypher))

cv2.imshow('mask',mask_img)
cv2.imshow('secret message',secret_message_img)
cv2.imshow('cypher image',cypher)
cv2.waitKey()


cypher=cv2.imread(r'D:\Code\Git stuff\Image-Enigma\encrypted_images\20210109-101236.jpg')
# print(cypher)
decyphered_image=steg_var.decrypt_image(cypher)

filename='./decrypted_images/'+time.strftime("%Y%m%d-%H%M%S")+'.jpg'
print(cv2.imwrite(filename, decyphered_image))

cv2.imshow('Decrypted image',decyphered_image)
cv2.waitKey()
