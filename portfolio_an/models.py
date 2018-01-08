from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from portfolio_an import LANGUAGES, LANGUAGE

class PortfolioUser(AbstractUser):
    language = models.CharField(verbose_name=_('taal'), max_length=10,
                                choices=LANGUAGES, default=LANGUAGE.DUTCH)

class Contact(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField()
    attachment = models.FileField(upload_to="attachements",
                                  help_text=_("Upload hier je document als je een offerte aanvraagt."),
                                  null=True, blank=True)

    date = models.DateTimeField(auto_created=True, auto_now=True)

    class Meta:
        ordering = ["-date"]
