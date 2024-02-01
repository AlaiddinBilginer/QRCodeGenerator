import pyqrcode
import png
from pyqrcode import QRCode

link = "https://github.com/AlaiddinBilginer"

url = pyqrcode.create(link)

url.png("MyQRCode.png", scale=6)