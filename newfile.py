import qrcode

#Taking UPI IDs as input
upi_id = input("Enter your UPI ID = ")

#upi://pay2pa=UPI_ID&apn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#There are different payment URLs based on the UPI ID and the app you're using. It can be modified based on the payment app.

phonepe_url = f'upi://pay2pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay2pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay2pa={upi_id}&pn=Recipient%20Name&mc=1234'
amazon_pay_url = f'upi://pay2pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)
amazon_pay_qr = qrcode.make(amazon_pay_url)

#Saving the QRCode image as an image file
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')
amazon_pay_qr.save('amazon_pay_qr.png')

#Displaying the QRCode by installing Pil/Pillow library
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
amazon_pay_qr.show()