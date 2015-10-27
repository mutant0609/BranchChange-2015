# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151027_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Category',
            field=models.CharField(default='GE', max_length=5, choices=[('GE', 'GE'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST'), ('PwD', 'PwD')]),
        ),
        migrations.AddField(
            model_name='post',
            name='CurrentBranch',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AddField(
            model_name='post',
            name='Pref1',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AddField(
            model_name='post',
            name='Pref10',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AddField(
            model_name='post',
            name='Pref11',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AddField(
            model_name='post',
            name='Pref12',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AddField(
            model_name='post',
            name='Pref13',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AddField(
            model_name='post',
            name='Pref14',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AddField(
            model_name='post',
            name='Pref15',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AddField(
            model_name='post',
            name='Pref16',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AddField(
            model_name='post',
            name='Pref17',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AddField(
            model_name='post',
            name='Pref2',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AddField(
            model_name='post',
            name='Pref3',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AddField(
            model_name='post',
            name='Pref4',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AddField(
            model_name='post',
            name='Pref5',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AddField(
            model_name='post',
            name='Pref6',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AddField(
            model_name='post',
            name='Pref7',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AddField(
            model_name='post',
            name='Pref8',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AddField(
            model_name='post',
            name='Pref9',
            field=models.CharField(default='', max_length=18, choices=[('AE B.Tech', 'AE B.Tech'), ('CL B.Tech', 'CL B.Tech'), ('CE B.Tech', 'CE B.Tech'), ('CS B.Tech', 'CS B.Tech'), ('EE B.Tech', 'EE B.Tech'), ('EP B.Tech', 'EP B.Tech'), ('ME B.Tech', 'ME B.Tech'), ('MM B.Tech', 'MM B.Tech'), ('EE Dual Deg E1', 'EE Dual Deg E1'), ('EE Dual Deg E2', 'EE Dual Deg E2'), ('EN Dual Deg', 'EN Dual Deg'), ('EP Dual Deg N1', 'EP Dual Deg N1'), ('ME Dual Deg M2', 'ME Dual Deg M2'), ('MM Dual Deg Y1', 'MM Dual Deg Y1'), ('MM Dual Deg Y2', 'MM Dual Deg Y2'), ('CL Dual Deg', 'CL Dual Deg'), ('CH', 'CH'), ('None', '')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='Name',
            field=models.CharField(default='Enter your name here', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='Roll_Number',
            field=models.CharField(default='Valid 15XXXXXXX', help_text='Enter a valid 9 digit Roll Number starting with 15', max_length=100),
        ),
    ]
