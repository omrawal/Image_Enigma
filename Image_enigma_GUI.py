import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from steganography import Steganography
import time
import cv2

def encrypt_image(message,mask,root):
    steg_var=Steganography()
    mask_img=cv2.imread(mask)
    secret_message_img=cv2.imread(message)
    cypher=steg_var.embed_a_in_b(secret_message_img,mask_img)
    filename='./encrypted_images/'+time.strftime("%Y%m%d-%H%M%S")+'.jpg'
    cv2.imwrite(filename, cypher)
    result_str='File saved at \"{}\"'.format(filename)
    messagebox.showinfo('SUCCESS!!!',result_str)
    cv2.imshow('cypher image',cypher)
    cv2.waitKey()

def decrypt_image(hidden,root):
    steg_var=Steganography()
    cypher=cv2.imread(hidden)
    decyphered_image=steg_var.decrypt_image(cypher)
    filename='./decrypted_images/'+time.strftime("%Y%m%d-%H%M%S")+'.jpg'
    cv2.imwrite(filename, decyphered_image)
    result_str='File saved at \"{}\"'.format(filename)
    messagebox.showinfo('SUCCESS!!!',result_str)
    cv2.imshow('Decrypted image',decyphered_image)
    cv2.waitKey()

root=tk.Tk()    
root.title("Image-Enigma")
root.geometry("500x700") #300x200
lbs = tk.Label(root, text = "Steganography", font=20)
lbs.place(x=180, y=5)
lbs1 = tk.Label(root, text = "Encryption: Hide one image into another", font=10)
lbs1.place(x=50, y=50)

lbs_message = tk.Label(root, text = "Secret Image:", font=10)
lbs_message.place(x=10, y=100)

message_entry=tk.Entry(root,font=10)
message_entry.place(x=150, y=100)

def browsefunc(ent):
    filename =askopenfilename(filetypes=([
                    ("image", ".jpeg"),
                    ("image", ".png"),
                    ("image", ".jpg"),
                ]))
    ent.insert(tk.END, filename) # add this

message_browse_button=tk.Button(root,text="Browse",font=10,command=lambda:browsefunc(message_entry))
message_browse_button.place(x=400, y=90)

lbs_mask = tk.Label(root, text = "Mask Image:", font=10)
lbs_mask.place(x=10, y=150)

mask_entry=tk.Entry(root,font=10)
mask_entry.place(x=150, y=150)

mask_browse_button=tk.Button(root,text="Browse",font=10,command=lambda:browsefunc(mask_entry))
mask_browse_button.place(x=400, y=140)

encrypt_button=tk.Button(root,font=("times", 16),text="Encrypt",command=lambda:encrypt_image(message_entry.get(),mask_entry.get(),root))
encrypt_button.place(x = 200, y = 200 )

lbs2 = tk.Label(root, text = "Decryption: Uncover the hidden message", font=10)
lbs2.place(x=50, y=280)

lbs_cypher = tk.Label(root, text = "Cypher Image:", font=10)
lbs_cypher.place(x=10, y=330)

cypher_entry=tk.Entry(root,font=10)
cypher_entry.place(x=150, y=330)

cypher_browse_button=tk.Button(root,text="Browse",font=10,command=lambda:browsefunc(cypher_entry))
cypher_browse_button.place(x=400, y=320)

decrypt_button=tk.Button(root,font=("times", 16),text="Decrypt",command=lambda:decrypt_image(cypher_entry.get(),root))
decrypt_button.place(x = 200, y = 400 )

root.mainloop()