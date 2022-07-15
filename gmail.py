import smtplib
server = smtplib.SMTP("rishaansingh360@gmail.com", 360)
server.ehlo()
server.starttls()
server.login("rishaansingh360@gmail.com", "Rishaanisranz10")
server.sendmail("rishaansingh360@gmail.com", "rishaansingh360@gmail.com", "hello")
server.close()