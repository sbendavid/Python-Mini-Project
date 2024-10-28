import qrcode
from PIL import Image


# img = qrcode.make('Some data here')
# type(img)  # qrcode.image.pil.PilImage
# img.save("some_file.png")

# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data('Some data')
# qr.make(fit=True)

# img = qr.make_image(fill_color="black", back_color="white")

# Create QR code instance with custom settings
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Higher error correction to allow embedding
    box_size=10,
    border=4,
)

# Define the vCard data
vcard = """BEGIN:VCARD
VERSION:4.0
FN:John Smith
ORG:Example Company
TITLE:CEO
TEL;TYPE=WORK,VOICE:(555) 555-5555
EMAIL;TYPE=PREF,INTERNET:john.smith@example.com
URL:https://www.example.com
END:VCARD"""

# Define the WiFi data
wifi = "WIFI:S:Example_Network;T:WPA;P:password123;;"

portfolio = "https://bendavid.pythonanywhere.com/"

# Add a YouTube video link
qr.add_data(portfolio)
qr.make(fit=True)

# Generate the QR code with fun colors
img = qr.make_image(fill_color="black", back_color="white")

# Optional: Embedding a small logo at the center of the QR code
logo = Image.open('youtube_logo.png')
logo = logo.resize((50, 50))

# Calculate position to place the logo at the center
# img_w, img_h = img.size
# logo_w, logo_h = logo.size
# pos = ((img_w - logo_w) // 2, (img_h - logo_h) // 2)

# img.paste(logo, pos)

# Save or show the image
img.show()
img.save("wifi_qr_code.png")
