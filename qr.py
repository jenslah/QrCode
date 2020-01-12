import qrcode

image = qrcode.make("https://www.spiegel.de")
image.save("qr.png", "PNG")
