import os
from my_blog import mail
from flask_mail import Message
from flask import url_for, current_app
from os import urandom
from PIL import Image

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset request' , sender = "demo@gmail.com"  , recipients = [user.email])
    msg.body ="YOu can reset the password with this link. {}".format(url_for('reset_token' , token = token , _external =True))
    mail.send(msg)

def save_picture(form_picture):
    random_hex =urandom(8).hex()
    #random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn
