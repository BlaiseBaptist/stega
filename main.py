from PIL import Image


def gen_message():
    raw_message = """idk what to write here
just make sure to leave the 4 numbers in front as the length of the message
it makes it a lot easier to read them ngl"""
    header_v = str(len(raw_message) + 4)
    header_h = str("0" * (4 - len(header_v)))
    return header_h + header_v + raw_message


def main():
    message = make_im()
    message.show()


def make_im():
    message = iter_bits(bytearray(gen_message(), encoding='utf-8'))
    with Image.open("grayson.jpg") as im:
        im_bytes = im.tobytes()  # Convert image to raw bytes
        new_im_bytes = encode(im_bytes, list(message))
        return Image.frombytes('RGB', im.size, new_im_bytes)  # Make a new image


def encode(image, message):
    bits = list(iter_bits(image))
    bits[7:len(message) * 8:8] = message
    return bits_to_ints(bits)


def decode_im(image):
    bits = list(iter_bits(image.tobytes()))[7::8]
    try:
        message_len = int(bits_to_ints(bits[0:32]))
        message = bits_to_ints(bits[32:message_len * 8])
    except:
        message = bits_to_ints(bits)
    return message.decode('utf-8')


def bits_to_ints(bits):
    return bytearray([int("".join(str(x) for x in bits[i:i + 8]), 2) for i in range(0, len(bits), 8)])


def iter_bits(bytes):
    for b in bytes:
        for i in range(8):
            yield b >> (7 - i) & 1


main()
