# Image Steganography using Tkinter and OpenCV
Secure data hiding in image using steganography

## Description
This project is a simple **Image Steganography** application that allows users to hide secret messages inside images and retrieve them later. The project is built using **Python**, **Tkinter** for the GUI, **OpenCV** for image processing, and **PIL** (Pillow) for displaying images.

## Features
- Select an image to use for steganography.
- Encrypt a secret message into the image using **LSB (Least Significant Bit) encoding**.
- Secure encryption with a passcode.
- Decrypt the hidden message from the encrypted image using the correct passcode.
- View the encrypted image after message embedding.

## Technologies Used
- **Python** (Programming Language)
- **Tkinter** (Graphical User Interface)
- **OpenCV (cv2)** (Image Processing)
- **PIL (Pillow)** (Image Handling)


## Installation and Setup

### Prerequisites
Ensure you have Python installed on your system. You also need to install the required dependencies:

```sh
pip install opencv-python tkinter pillow
```

### Running the Application
1. Clone or download this repository.
2. Open a terminal or command prompt in the project directory.
3. Run the script using:
   ```sh
   python stego_gui.py
   ```
   

## How to Use
1. **Select an Image**: Click on the "Select Image" button and choose an image file.
2. **Encrypt Message**: Click on "Encrypt Message," enter your secret message and passcode.
3. **Decrypt Message**: Click on "Decrypt Message," enter the correct passcode to retrieve the message.
4. **Show Encrypted Image**: Click on "Show Encrypted Image" to view the modified image.

## Important Notes
- The message length is limited based on the image size.
- The passcode is required for decryption. If incorrect, the message cannot be retrieved.
- The encrypted image is saved as `encryptedImage.png` in the working directory.



