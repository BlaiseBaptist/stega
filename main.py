from PIL import Image


def main():
    with Image.open("awesome.png") as im:
        im_bytes = im.tobytes()  # Convert image to raw bytes
        print(im_bytes[0:49])
        print(len(im_bytes)/3)  # Length of im_bytes should be divisible by 3.
        new_im_bytes = bytearray(len(im_bytes))  # Make a byte array to store my modified data
        for i, b in enumerate(im_bytes):
            if i%3 == 0:
                new_im_bytes[i] = b  # Modify each byte
            else:
                new_im_bytes[i] = b  # Modify each byte
        new_im = Image.frombytes('RGB', im.size, new_im_bytes)  # Make a new image
        new_im.show()  # Let's see what we did!


if __name__ == '__main__':
    main()
