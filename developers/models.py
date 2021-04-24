from django.db import models

# Create your models here.


class DeveloperUser(models.Model):
    """
    This Class Create Information Models For Developers
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, unique=True)
    mail_address = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=250)
    linkedin_address = models.CharField(max_length=150, verbose_name="Linkedin Profile",
                                        help_text="Please Share Your Linkedin Profile Address", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "developer_users"
        verbose_name_plural = "Developer User Information"
        ordering = ('-created_at',)

    def __str__(self):
        return "User Name:{user_name}, Name:{name}, Surname:{surname}, Linkedin:{linkedin}".format(
            user_name=self.user_name, name=self.name, surname=self.surname, linkedin=self.linkedin_address
        )
