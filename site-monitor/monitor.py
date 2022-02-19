import os
import smtplib
import requests
import logging

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

logging.basicConfig(filename='PATH_TO_DESIRED_LOG_FILE',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def notify_user():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'YOUR SITE IS DOWN!'
        body = 'Make sure the server restarted and it is back up'
        msg = f'Subject: {subject}\n\n{body}'

        logging.info('Sending Email...')
        smtp.sendmail(EMAIL_ADDRESS, 'RECIEVER_EMAIL_ADDRESS', msg)


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36"}
try:
    r = requests.get("https://amazon.in",headers=headers)

    if r.status_code != 200:
        logging.info('Website is DOWN!')
        notify_user()
    else:
        logging.info('Website is UP')
except Exception as e:
    logging.info('Website is DOWN!')
    notify_user()