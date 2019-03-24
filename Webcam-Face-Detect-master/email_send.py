import smtplib, ssl

message = """\
Subject: SECURITY ALERT

Your FunkyGrass security camera has detected the presence of a person."""

def send_email():

    global message

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "funkygrass.alert@gmail.com"  # Enter your address
    receiver_email = "funkygrass.alert@gmail.com"  # Enter receiver address
    password = "newhacks2019"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
