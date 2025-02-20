import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Image Steganography")
root.geometry("500x500")


encrypted_img_path = "encryptedImage.png"
image_path = ""
password = ""  


def select_image():
    global image_path
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if image_path:
        messagebox.showinfo("Image Selected", f"Image selected: {image_path}")
    else:
        messagebox.showinfo("Image Selection Cancelled", "No image was selected.")


def encrypt_message():
    global image_path, password
    if not image_path:
        messagebox.showerror("Error", "Please select an image first!")
        return

    msg = simpledialog.askstring("Input", "Enter the secret message:")
    password = simpledialog.askstring("Input", "Enter a passcode:", show="*")

    if not msg or not password:
        messagebox.showerror("Error", "Message and password cannot be empty!")
        return

    img = cv2.imread(image_path)
    if img is None:
        messagebox.showerror("Error", "Could not read the image. It might be corrupted.")
        return

    # Check if the message is too long for the image
    max_bytes = img.shape[0] * img.shape[1] * 3 // 8  # Calculate maximum bytes
    if len(msg) > max_bytes - 1: # Subtract 1 for the delimiter
        messagebox.showerror("Error", f"Message too long. Maximum {max_bytes - 1} characters allowed.")
        return

    # Convert message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in msg)
    binary_message += '11111111'  # Add a delimiter

    # Embed the message
    index = 0
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            for color in range(3):  # Iterate through RGB channels
                if index < len(binary_message):
                    # Modify the least significant bit (LSB)
                    img[row, col, color] = (img[row, col, color] & 254) | int(binary_message[index])
                    index += 1
                else:
                    break  # Message embedded
            else:
                continue
            break
        else:
            continue
        break

    cv2.imwrite(encrypted_img_path, img)
    messagebox.showinfo("Success", "Message encrypted successfully!")


def decrypt_message():
    global password
    if not os.path.exists(encrypted_img_path):
        messagebox.showerror("Error", "No encrypted image found!")
        return

    try:
        img = cv2.imread(encrypted_img_path)
        if img is None:
            messagebox.showerror("Error", "Could not read the encrypted image. It might be corrupted.")
            return

        entered_pass = simpledialog.askstring("Input", "Enter passcode for decryption:", show="*")

        if entered_pass != password:
            messagebox.showerror("Error", "Incorrect passcode!")
            return

        binary_message = ""
        # Iterate through the image pixels in the same order as in encryption
        for row in range(img.shape[0]):
            for col in range(img.shape[1]):
                for color in range(3):
                    binary_message += str(img[row, col, color] & 1)

        decoded_message = ""
        byte = ""
        for bit in binary_message:
            byte += bit
            if len(byte) == 8:
                if byte == '11111111':  # Delimiter found
                    break
                decoded_message += chr(int(byte, 2))
                byte = ""

        messagebox.showinfo("Decryption Successful", f"Hidden message: {decoded_message}")

    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed: {e}")

        

def show_encrypted_image():
    if not os.path.exists(encrypted_img_path):
        messagebox.showerror("Error", "No encrypted image found!")
        return

    try:
        new_window = tk.Toplevel(root)
        new_window.title("Encrypted Image")

        img = Image.open(encrypted_img_path)
        img = img.resize((300, 300))  
        img_tk = ImageTk.PhotoImage(img)

        label = tk.Label(new_window, image=img_tk)
        label.image = img_tk  
        label.pack()
    except Exception as e:
        messagebox.showerror("Error", f"Error displaying image: {e}")


# GUI Layout
btn_select = tk.Button(root, text="Select Image", command=select_image, width=20, height=2)
btn_encrypt = tk.Button(root, text="Encrypt Message", command=encrypt_message, width=20, height=2)
btn_decrypt = tk.Button(root, text="Decrypt Message", command=decrypt_message, width=20, height=2)
btn_show_img = tk.Button(root, text="Show Encrypted Image", command=show_encrypted_image, width=20, height=2)

btn_select.pack(pady=10)
btn_encrypt.pack(pady=10)
btn_decrypt.pack(pady=10)
btn_show_img.pack(pady=10)

root.mainloop()