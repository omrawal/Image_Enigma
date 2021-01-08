import tkinter as tk
from tkinter.filedialog import askopenfilename
def getInputs(ent1_val):
    print(ent1_val)
    print(type(ent1_val))
    pass

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
message_browse_button.place(x=410, y=90)

lbs_mask = tk.Label(root, text = "Mask Image:", font=10)
lbs_mask.place(x=10, y=150)

mask_entry=tk.Entry(root,font=10)
mask_entry.place(x=150, y=150)

mask_browse_button=tk.Button(root,text="Browse",font=10,command=lambda:browsefunc(mask_entry))
mask_browse_button.place(x=410, y=140)

log=tk.Button(root,font=("times", 16),text="Encrypt",command=lambda:getInputs(message_entry.get()))
log.place(x = 200, y = 200 )

root.mainloop()