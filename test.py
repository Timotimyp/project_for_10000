import base64
from binascii import a2b_base64
import urllib

encoded = base64.b64encode(open("image.jpg", "rb").read())
print(type(encoded))
print(encoded)
encoded = str(encoded)
w = open('e.txt', 'w')
print(encoded, file=w)

