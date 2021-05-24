""" This File Contains Helper Function For Rad Views """

from developers.models import DeveloperUsers
from django.contrib.auth.models import User


def create_new_user(first_name: str, last_name: str, mail_address: str, password: str, confirm_password: str,
                    github_address: str, linkedin_address: str, twitter_address: str) -> bool:
    """
    This Function Creat New User In The Auth User Model
    :param first_name:
    :param last_name:
    :param mail_address:
    :param password:
    :param confirm_password:
    :param github_address:
    :param linkedin_address:
    :param twitter_address:
    :return:
    """
    if password == confirm_password:
        auth_user = User(
            first_name=first_name,
            last_name=last_name,
            username=mail_address,
            email=mail_address
        )
        auth_user.set_password(password)
        auth_user.save()

        developer_user = DeveloperUsers(
            first_name=first_name,
            last_name=last_name,
            mail_address=mail_address,
            github_address=github_address,
            linkedin_address=linkedin_address,
            twitter_address=twitter_address
        )
        developer_user.save()

        if auth_user and developer_user:
            return True
        else:
            return False
    else:
        return False
