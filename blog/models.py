from django.db import models
from django.utils import timezone
from django.forms import RegexField
import re
PREF = (
	('AE B.Tech','AE B.Tech'),
	('CL B.Tech','CL B.Tech'),
	('CE B.Tech','CE B.Tech'),
	('CS B.Tech','CS B.Tech'),
	('EE B.Tech','EE B.Tech'),
	('EP B.Tech','EP B.Tech'),
	('ME B.Tech','ME B.Tech'),
	('MM B.Tech','MM B.Tech'),
	('EE Dual Deg E1','EE Dual Deg E1'),
	('EE Dual Deg E2','EE Dual Deg E2'),
	('EN Dual Deg','EN Dual Deg'),
	('EP Dual Deg N1','EP Dual Deg N1'),
	('ME Dual Deg M2','ME Dual Deg M2'),
	('MM Dual Deg Y1','MM Dual Deg Y1'),
	('MM Dual Deg Y2','MM Dual Deg Y2'),
	('CL Dual Deg','CL Dual Deg'),
	('CH','CH'),
        ('None',''),

	)

CAT=(
	('GE','GE'),
	('OBC','OBC'),
	('SC','SC'),
	('ST','ST'),
	('PwD','PwD'),

	)


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    Name = models.CharField(max_length=50, default='Enter your name here')
    Roll_Number = models.CharField(max_length=100, default='Valid 15XXXXXXX', help_text = 'Enter a valid 9 digit Roll Number starting with 15')
    CurrentBranch = models.CharField(max_length=18, choices=PREF, default='')
    Category = models.CharField(max_length=5, choices=CAT, default='GE')
  #  CPI = models.DecimalField(max_digits=4,decimal_places=2, default=10.00, help_text = 'Enter reasonable CPI atleast 8 for GE and OBC and atleast 7 for SC,ST and PwD')
    Pref1 = models.CharField(max_length=18, choices=PREF, default='')
    Pref2 = models.CharField(max_length=18, choices=PREF, default='')
    Pref3 = models.CharField(max_length=18, choices=PREF, default='')
    Pref4 = models.CharField(max_length=18, choices=PREF, default='')
    Pref5 = models.CharField(max_length=18, choices=PREF, default='')
    Pref6 = models.CharField(max_length=18, choices=PREF, default='')
    Pref7 = models.CharField(max_length=18, choices=PREF, default='')
    Pref8 = models.CharField(max_length=18, choices=PREF, default='')
    Pref9 = models.CharField(max_length=18, choices=PREF, default='')
    Pref10 = models.CharField(max_length=18, choices=PREF, default='')
    Pref11 = models.CharField(max_length=18, choices=PREF, default='')
    Pref12 = models.CharField(max_length=18, choices=PREF, default='')
    Pref13 = models.CharField(max_length=18, choices=PREF, default='')
    Pref14 = models.CharField(max_length=18, choices=PREF, default='')
    Pref15 = models.CharField(max_length=18, choices=PREF, default='')
    Pref16 = models.CharField(max_length=18, choices=PREF, default='')
    Pref17 = models.CharField(max_length=18, choices=PREF, default='')



    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
       return self.Name

# Create your models here.


class Document(models.Model):
    docfile = models.FileField(upload_to='documents')

# Create your models here.
