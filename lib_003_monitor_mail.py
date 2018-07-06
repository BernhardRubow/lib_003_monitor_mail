import smtplib
from lib_004_config_reader import nvp_config_reader as config_reader

# sample config file
# config = {
#   'subject': "your subject",
#   'from': 'sender email address',
#   'to': 'receiver email address',
#   'smtpServer': 'smtp server address or dns name',
#   'port': 666,
#   'userName': 'username for login',
#   'password': 'password for login'
# }

def sent_monit_mail(text_template, state='HEALTHY', string_to_append='no custom message'):
    config = config_reader.read_config_file('config.json')

    # Import the email modules we'll need
    from email.message import EmailMessage

    # Open the plain text file whose name is in textfile for reading.
    with open(text_template) as fp:
        # Create a text/plain message
        msg = EmailMessage()
        content = fp.read()
        content += string_to_append
        msg.set_content(content)

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = config["subject"] + state
    msg['From'] = config["from"]
    msg['To'] = config['to']

    server = smtplib.SMTP_SSL(config['smtpServer'], config['port'])
    server.login(config['userName'], config['password'])
    server.send_message(msg)
    server.quit()

    print("eMail send")
