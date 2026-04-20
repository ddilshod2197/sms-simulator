import random
import string
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class SMS_Sender:
    def __init__(self, sender_email, sender_password, recipient_number):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_number = recipient_number

    def generate_code(self):
        return ''.join(random.choices(string.digits, k=6))

    def send_sms(self, code):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = f'+{self.recipient_number}'
        msg['Subject'] = 'SMS Sender Simulyatsiya'
        body = f'SMS kod: {code}'
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.sender_email, self.sender_password)
        text = msg.as_string()
        server.sendmail(self.sender_email, f'+{self.recipient_number}', text)
        server.quit()

    def send_sms_with_code(self):
        code = self.generate_code()
        self.send_sms(code)
        return code

sender = SMS_Sender('sender_email', 'sender_password', 'recipient_number')
code = sender.send_sms_with_code()
print(f'Kod: {code}')
```

Kodni ishlatish uchun quyidagilar kerak:

1. `sender_email` va `sender_password` o'rniga o'zingizning Gmail yoki boshqa post-serverga kirish ma'lumotlarini kiritib qo'yin.
2. `recipient_number` o'rniga qabul qiluvchi raqamni kiritib qo'yin.
3. Kodni ishlatish uchun `sender` obyektini yaratib, `send_sms_with_code` metodi orqali SMS kodini oling.
4. Olingan kodni konsolga chiqarib ko'ring.
