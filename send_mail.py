import smtplib 
from email.mime.text import MIMEText

def send_mail(customer, email, dealer, rating, comments):
    port = 2525
    smtp_server ="sandbox.smtp.mailtrap.io"
    login = "1daffc7bc8e0ec"
    password ="fa67061717f990"
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Email: {email}</li><li>Dealer: {dealer}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'adwai.yt31@gmail.com'
    receiver_email = 'surveadwai@gmail.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

        ## EMAIL USED OT LOGIN IN MAILTRAP.IO IS {adwai5840@gmail.com }
        ## heroku.com is used to deploy the website 