import qrcode
qr_data = input()
qr_img = qrcode.make(qr_data)
type(qr_img)
qr_img.save('qr.png')