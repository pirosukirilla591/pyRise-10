import qrcode
data = "https://vk.com/piroschock.frilance.work"
filename = "Sound's/qrcode.png"
img = qrcode.make(data)
img.save(filename)