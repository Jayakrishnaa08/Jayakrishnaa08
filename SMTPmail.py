from smtplib import SMTP


HOST = "smtp-mail.outlook.com"
PORT = 587


FROM_EMAIL = "ENTER THE SENDER E-MAIL ID"
TO_EMAIL = "ENTER THE RECEIVER E-MAIL ID"
PASSWORD = "SENDER E-MAIL ID PASSWORD"
MESSAGE = """Subject: This is a system generated MAIL..."""


smtp = SMTP(HOST,PORT)
status_code, response = smtp.starttls()
print(f"[*] Starting TLS connection: {status_code} {response}")


status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"[*] Logging in : {status_code} {response}")


smtp.sendmail(from_addr=FROM_EMAIL,to_addrs=TO_EMAIL,msg=MESSAGE)
print("Mail Sent Successfully")

smtp.quit()