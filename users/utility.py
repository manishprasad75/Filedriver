from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import OTP
import time, uuid
from datetime import datetime, timedelta
from django.utils import timezone
now = timezone.now()


def isValidForm(context):
    # import pdb
    # pdb.set_trace()
    # print(context.get('firstname'), context.get('lastname'), context.get('username'), context.get('email'), context.get('password1'), context.get('password2'))
    if context.get('firstname') is None or len(context.get('firstname')) == 0:
        msg = "Error: First Name Not Provided"
        return False, msg
    if context.get('lastname') is None or len(context.get('lastname')) == 0:
        msg = "Error: Last Name Not Provided"
        return False, msg
    if context.get('username') is None or len(context.get('username')) == 0:
        msg = "Error: Email Not Provided"
        return False, msg

    # user = User.objects.filter(username=context.get('username')).first()
    #
    # if user is not None and user.is_active:
    #     msg = "Error: Email Already Exist"
    #     return False, msg

    if context.get('password1') is None or len(context.get('password1')) == 0:
        msg = "Error: Password Not Provided"
        return False, msg

    if context.get('password2') is None or len(context.get('password2')) == 0:
        msg = "Error: Conform Password Not Provided"
        return False, msg

    if context.get('password1') != context.get('password2'):
        msg = "Error: Password Does Not Matched"
        return False, msg

    return True, "Hello"


def sendMessage(user, otp):
    subject = "Email Verification"
    message = f'Thankyou {user.first_name}, for being a part of our startup. This means a lot for us. ' \
              f'<p>OTP</p><h1>{otp.value}</h1>'
    html_content = message
    message = strip_tags(html_content)
    (status, msg) = sendMessage1(subject, message, user.email, html_content)

    if not status:
        print(msg)
        return False
    else:
        return True

    # return redirect(request, 'varification.html', {'email': user.email, 'msg': msg, 'col': "info"})


def sendMessage1(subject, message, user_email, html_content):
    # import pdb
    # pdb.set_trace()
    subject = subject
    message = message
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email, ]
    if subject and message and recipient_list:
        try:
            send_mail(subject, message, email_from, recipient_list, html_message=html_content)
        except Exception as e:
            print(e)
            msg = "Error: Make sure Email is Valid"
            return False, msg
        msg = "Alert: Successfully Send OTP, Check your Email"
        return True, msg
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        msg = "Error: Make sure Email is Valid"
        return False, msg


def otpValidation(email, otp_val):
    user = User.objects.filter(username=email).first()
    if user is None:
        return False

    otp = OTP.objects.filter(value=otp_val).first()
    if otp is None:
        return False

    if otp.user_id_id != user.id:
        return False

    # import pdb;
    # pdb.set_trace()
    if datetime.now(otp.valid_upto.tzinfo) < otp.valid_upto:
        return True
    return False

def getOTPValue():
    value = uuid.uuid4().hex[:6].upper()
    return value