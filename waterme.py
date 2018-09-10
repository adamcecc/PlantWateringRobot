try:
	import time 
	from email.mime.text import MIMEText 
	import smtplib
	
except RuntimeError:
	print("Error importing time!")

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!") 


my_smtp_server = ""
my_smtp_login = ""
my_smtp_password = ""
to_email = ""
from_email = ""
subject_email = 'Plants watered %s' % time.strftime("%d/%m/%Y : %H:00")

body = "Watered"

class EmailMe(object):
	def __init__(self, smtpServer, smtpLogin, smtpPassword):
		self.smtpServer = smtpServer
		self.smtpLogin = smtpLogin
		self.smtpPassword = smtpPassword

	def sendEmail(self, toEmail, fromEmail, subject, body):
		msg = MIMEText(body.encode('utf-8'), 'plain', 'utf-8')
		msg['Subject'] = subject
		msg['From'] = fromEmail
		msg['To'] = toEmail

		s = smtplib.SMTP_SSL(self.smtpServer)
		s.login(fromEmail, self.smtpPassword)
		s.sendmail(fromEmail, [toEmail], msg.as_string())
		s.quit()

class WaterPlants:
	RelayLineOne = 11 
	chan_list = [RelayLineOne]
	RelayOn = GPIO.LOW
	RelayOff = GPIO.HIGH

	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.chan_list, GPIO.OUT)
		#Turn off warnings 
		GPIO.setwarnings(False)
	
	def turnOn(self):
		GPIO.output(self.chan_list, GPIO.LOW)

	def turnOff(self):
		GPIO.output(self.chan_list, GPIO.HIGH)
    
        def cleanUp(self):
                GPIO.cleanup()
            
wateringTime = 10  
waterMe = WaterPlants()
waterMe.turnOn()
time.sleep(wateringTime)
waterMe.turnOff() 

emailMe = EmailMe(my_smtp_server, my_smtp_login, my_smtp_password) 
emailMe.sendEmail(to_email, from_email, subject_email, body)


