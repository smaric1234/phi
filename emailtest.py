import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, body):
    # Set up the SMTP server
    smtp_server = "smtp.office365.com"
    smtp_port = 587

    # Create a MIMEText object to represent the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body of the email to the message
    msg.attach(MIMEText(body, 'plain'))

    # Start the SMTP session
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Close the SMTP session
    server.quit()

# Example usage
sender_email = "sasamaric_9@hotmail.com"
sender_password = "sasa1234"
receiver_email = "sasamaric_9@hotmail.com"
subject = "Test Email"
body = "This is a test email sent through Python."

send_email(sender_email, sender_password, receiver_email, subject, body)