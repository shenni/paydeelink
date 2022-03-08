from project import app, mail
from datetime import date, time, datetime, timedelta
from flask import current_app, render_template, redirect, url_for, flash, request, send_file, send_from_directory, safe_join, abort, Response
from flask_mail import Message



@app.route('/', methods=['GET', 'POST'])
def home():
    return "OK"

@app.route('/thank_you/', defaults={'email': ""}, methods=['GET', 'POST'])
@app.route('/thank_you/<email>', methods=['GET', 'POST'])
def thank_you(email):


    if len(email) > 0: 

        req = f"Hi," + "\n\n"
        req = req + f"Request:PaydeeLink Tour " + "\n\n"
        req = req + f"Here is your login detail." + "\n"
        req = req + f"  Email: {email}" + "\n"

        msg = Message("PaydeeLink tour request",
                    sender="team@paydee.co",
                    recipients=["yokesan@paydee.co"])
        #,
        #bcc=[app.config['GOLIVE_TEAM_EMAIL']])
        msg.body = req
        mail.send(msg)

        print("email sent")

    return render_template('thankyou.html', email=email)
