import numpy as np
import cv2
import matplotlib.pyplot as plt


class Steganography(object):
    def __init__(self):
        pass

    def binary_to_decimal(self, n):  # takes string input && returns integer
        return(int(n, 2))

    def decimal_to_binary(self, n):  # takes integer input && returns string
        return(format(n, '08b'))

    def hide(self, x, y):  # x is mask,  y in secret
        x_bin = self.decimal_to_binary(x)
        y_bin = self.decimal_to_binary(y)
        new_val_bin = x_bin[0:6]+y_bin[0:2]
        new_val_dec = self.binary_to_decimal(new_val_bin)
        return new_val_dec

    def hide_pixel(self, x, y):  # x,y is list of B,G,R  x is mask,  y in secret
        new_x = [self.hide(x, y)]
        return new_x

    def unhide_pixel(self, x):
        new_x = [self.unhide(x)]
        return new_x

    def unhide(self, x):
        x_bin = self.decimal_to_binary(x)
        new_val_bin = x_bin[6:]+'000000'
        new_val_dec = self.binary_to_decimal(new_val_bin)
        return new_val_dec

    def create_blank_image(self):
        blank_img = np.zeros([500, 500], dtype=np.uint8)
        blank_img.fill(255)  # or img[:] = 255
        return blank_img

    def embed_a_in_b(self, a, b):  # hide image a in b
        # mask=b
        # secret=a
        mask = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
        secret = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

        modified_mask = cv2.resize(mask, (500, 500))
        modified_secret = cv2.resize(secret, (500, 500))
        blank_img = self.create_blank_image()
        for x in range(0, modified_secret.shape[0], 1):
            for y in range(0, modified_secret.shape[1], 1):
                secret_coor = modified_secret[y, x]
                mask_coor = modified_mask[y, x]
                blank_img[y, x] = np.array(
                    self.hide_pixel(mask_coor, secret_coor))
        # ans=blank_img
        ans = cv2.cvtColor(blank_img, cv2.COLOR_GRAY2RGB)
        return ans

    def decrypt_image(self, a):  # unhide the secret image from the mask and return secret image
        gray_a = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
        decrypted_blank_img = self.create_blank_image()
        for x in range(0, gray_a.shape[0], 1):
            for y in range(0, gray_a.shape[1], 1):
                current_coor = gray_a[y, x]
                decrypted_blank_img[y, x] = np.array(
                    self.unhide_pixel(current_coor))
        # ans = decrypted_blank_img
        ans = cv2.cvtColor(decrypted_blank_img, cv2.COLOR_GRAY2RGB)
        return ans
