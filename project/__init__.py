'''
Fix:
# python -m pip install --upgrade pip
# python -m pip install --no-use-pep517 flask-bcrypt
'''
from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisisfirstflaskapp'
app.config['MAIL_SERVER']='mail.asb.com.my'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'yokesan@asb.com.my'
app.config['MAIL_PASSWORD'] = 'shenni@2000'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
#app.config['MAIL_DEBUG'] = True

mail = Mail(app)

from project import routes
