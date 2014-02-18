from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from portfolio_an import LANGUAGES, LANGUAGE

class PortfolioUser(AbstractUser):
    language = models.CharField(verbose_name=_('language'), max_length=10,
                                choices=LANGUAGES, default=LANGUAGE.DUTCH)
