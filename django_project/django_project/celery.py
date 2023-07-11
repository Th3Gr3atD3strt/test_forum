import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
from django.core.mail import send_mail
from django.urls import reverse

from django_project import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
app = Celery('django+project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

'''@app.task()
def send_verification_mail(user_id, email, username, ):
    msg = 'http://127.0.0.1:8000' + reverse('confirmation', kwargs={'confirmation_id': user_id,
                                                                    'username': username}
                                            )
    send_mail(subject=
              'Подтверждение аккаунта',
              message=msg,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[email])
              '''

