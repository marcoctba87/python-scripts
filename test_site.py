import smtplib
import os
import requests

SITES = ['http://www.site1.com.br','https://www.site2.com.br','https://www.site3.com.br']
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_NOTIFY = ['email1@gmail.com','email2@hotmail.com']
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

## TESTE VARIAVEIS DE AMBIENTE ##
#print(EMAIL_ADDRESS, EMAIL_PASSWORD)

def notify_user():
	server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	subject = 'Site ' + SITE + ' esta fora do ar'
	body = "Verifique se o servidor esta no ar e o apache esta rodando\n\nSite afetado: " + SITE
	msg = f'Subject: {subject}\n\n{body}'
	server.sendmail(EMAIL_ADDRESS, EMAIL_NOTIFY, msg)
	server.quit()

for SITE in SITES:
	try:
		print(SITE)
		r = requests.get(SITE, timeout=5)

		if r.status_code != 200:
			notify_user()

		else:
			print('Tude certo')

	except Exception as e:
			notify_user()
