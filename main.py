import qrcode
data = 'Svitlana Derymova'
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='green', back_color='white')
img.save('/Users/svetlanaderymova/Documents/myqrcode/myqr1.png')
