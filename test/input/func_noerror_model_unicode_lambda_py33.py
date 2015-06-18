"""
Ensures that django models without a __unicode__ method are flagged
"""
#  pylint: disable=C0111

from django.db import models


class SomeModel(models.Model):
    something = models.CharField(max_length=255)
    __str__ = lambda s: str(s.something)
