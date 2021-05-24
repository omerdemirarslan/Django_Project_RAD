from django.db import models


# Create your models here.


class DeveloperUsers(models.Model):
    """
    This Class Create Information Model For Developers
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)
    user_name = None
    mail_address = models.EmailField(max_length=50, unique=True)
    USERNAME_FIELD = 'mail_address'
    REQUIRED_FIELDS = []
    twitter_address = models.CharField(max_length=150, verbose_name="Twitter Profile",
                                       help_text="Please Share Your Twitter Profile Address", blank=True, null=True)
    linkedin_address = models.CharField(max_length=150, verbose_name="Linkedin Profile",
                                        help_text="Please Share Your Linkedin Profile Address", blank=True, null=True)
    github_address = models.CharField(max_length=150, verbose_name="Github Profile",
                                      help_text="Please Share Your Github Profile Address", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "developer_user"
        verbose_name_plural = "Developer User Information"
        ordering = ('-created_at',)

    def __str__(self):
        return "User Name: {user_name}, Name: {name}, Surname: {surname}, Twitter: {twitter}, Linkedin: {linkedin}, " \
               "Github: {github}".format(user_name=self.mail_address, name=self.first_name, surname=self.last_name,
                                         twitter=self.twitter_address, linkedin=self.linkedin_address,
                                         github=self.github_address
                                         )
