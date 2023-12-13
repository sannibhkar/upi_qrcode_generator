# upi_qrcode_generator
This script generates QR codes for UPI payments using different apps. It takes the UPI ID as input and creates four QR codes, one for each app. The user can scan the QR code and make the payment.
# UPI QR Code Generator

This is a python script that can generate QR codes for UPI payments using different apps such as PhonePe, Paytm, Google Pay, and Amazon Pay. The script takes the UPI ID of the user as input and creates four QR codes, one for each app. The user can then scan the QR code with their preferred app and make the payment.

## Requirements

To run this script, you need to have the following python packages installed:

- qrcode: This package can create QR codes from plain text.
- pillow: This package can save and display images.

You can install these packages using pip:

```bash
pip install qrcode
pip install pillow
```

## Usage

To run this script, simply execute it from the command line:

```bash
python upi_qr.py
```

The script will prompt you to enter your UPI ID, which should be in the format of `username@provider`. For example, `alice@phonepe`.

The script will then generate four QR codes, one for each app, and save them as PNG files in the same directory. The file names will be `phonepe_qr.png`, `paytm_qr.png`, `google_pay_qr.png`, and `amazon_pay_qr.png`.

The script will also display the QR codes on the screen using the pillow library. You can scan the QR code with your preferred app and make the payment.

## How it works

The script uses the `qrcode` package to create QR codes from plain text. The plain text is the UPI payment URL, which has the following format:

```
upi://pay2pa=UPI_ID&pn=Recipient%20Name&mc=1234
```

The UPI payment URL has the following parameters:

- pay2pa: This is the UPI ID of the recipient.
- pn: This is the name of the recipient.
- mc: This is the merchant code, which is optional.

The script uses the `f-string` syntax to insert the UPI ID of the user into the URL. The name of the recipient and the merchant code are hardcoded for simplicity, but they can be modified based on the payment app.

The script then uses the `qrcode.make()` function to create a QR code object from the URL. The QR code object has a `save()` method that can save the QR code as an image file. The script saves the QR code as a PNG file with the name of the app.

The script also uses the `qrcode.show()` method to display the QR code on the screen using the pillow library. The script does this for each app and creates four QR codes in total.
