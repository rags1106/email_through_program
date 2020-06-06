import smtplib
from email.message import EmailMessage

email= EmailMessage()
email['from']='Rajeshwari Jha'
email['to']='ravi62jha@gmail.com'
email['subject']='Hie from my python program'

email.set_content('Hie Papa')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('rajeshwarijha43@gmail.com','ragsdark@123')
	smtp.send_message(email)
	print('all good')