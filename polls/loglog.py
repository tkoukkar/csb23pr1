from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver

from datetime import datetime

import logging

logger = logging.getLogger("django")


@receiver(user_logged_in)
def log_user_login(sender, user, **kwargs):
    """ log user login to user log """
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    msg = "[" + timestamp + "] Login by user " + user.username + " - OK"
    logger.info(msg)


@receiver(user_login_failed)
def log_user_login_failed(sender, user=None, **kwargs):
    """ log user login to user log """
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if user:
        msg = "[" + timestamp + "] Login attempt by user " + user.username + " - failed"
        logger.info(msg)
    else:
        msg = "[" + timestamp + "] Login attempt by unknown user - failed"
        logger.error(msg)


@receiver(user_logged_out)
def log_user_logout(sender, user, **kwargs):
    """ log user logout to user log """
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    msg = "[" + timestamp + "] Logout by user " + user.username
    logger.info(msg)