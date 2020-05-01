import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def sendMail(files):
	fromAddr = 'scharfgustavo@gmail.com'
	toAddr = 'scharfgustavo@gmail.com, ecocraftgus@gmail.com'

	msg = MIMEMultipart()

	msg['From'] = fromAddr
	msg['To'] = toAddr
	msg['Subject'] = "Today's Report"

	body = 'Body of the email. Test 123 321'

	msg.attach(MIMEText(body,'plain'))
	for file in files:
		filename = file
		attachment = open(filename,'rb')

		p = MIMEBase('application','octet-stream')
		p.set_payload((attachment).read())
		encoders.encode_base64(p)

		p.add_header('Content-Disposition','attachment; filename=%s' %filename)
		msg.attach(p)

	s = smtplib.SMTP('smtp.gmail.com',587)
	s.starttls()
	s.login('scharfgustavo@gmail.com','hvqwfdvnknampggk')
	text = msg.as_string()
	toList = ['scharfgustavo@gmail.com','ecocraftgus@gmail.com']
	s.sendmail('scharfgustavo@gmail.com',toList,text)
	s.quit()

sendMail(['test.xlsx','test2.xlsx'])