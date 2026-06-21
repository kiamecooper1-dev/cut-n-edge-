from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

BUSINESS_EMAIL = "cutnedgeatl@gmail.com"
SENDER_EMAIL = "cutnedgeatl@gmail.com"
SENDER_PASSWORD = "xtva sdfu rpdk nafz"

def send_email(name, phone, email, service, message):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = BUSINESS_EMAIL
    msg['Subject'] = f"New Quote Request from {name} - Cut N Edge Website"

    body = f"""
    NEW QUOTE REQUEST FROM YOUR WEBSITE

    Name:    {name}
    Phone:   {phone}
    Email:   {email}
    Service: {service}

    Message:
    {message}
    """

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    success = False

    if request.method == 'POST':
        name    = request.form.get('name')
        phone   = request.form.get('phone')
        email   = request.form.get('email')
        service = request.form.get('service')
        message = request.form.get('message')

        success = send_email(name, phone, email, service, message)

    return render_template('contact.html', success=success)

if __name__ == '__main__':
    app.run(debug=True)