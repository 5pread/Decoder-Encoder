import pybase64

def EncodeText():
    text = input('Text to encode >>')
    text = text.encode()
    encoded_text = pybase64.standard_b64encode(text)
    encoded_text = str(encoded_text)
    encoded_text = encoded_text[2:][:-1]
    print(f'Your encoded text >> {encoded_text}')

def DecodeText():
    string = input('Text to decode >>')
    decoded_text = pybase64.standard_b64decode(string)
    decoded_text = str(decoded_text)[2:][:-1]
    print(f'Your decoded text >> {decoded_text}')

answ = input("""
                E for encode, D for decoding\n""")

if answ == "E":
    EncodeText()
else:
    DecodeText()
