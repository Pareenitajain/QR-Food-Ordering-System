import qrcode

# ✅ Use YOUR actual IP address
your_ip = "172.8.5.65"
url = f"http://{your_ip}:5000/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_code.png")

print(f"✅ QR Code Generated Successfully!")
print(f"📱 Menu URL: {url}")
print(f"🖼️  QR Code saved as: qr_code.png")

