# Generated by Django 5.0.1 on 2024-04-08 17:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('phone_no', models.CharField(max_length=10, unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('department', models.CharField(blank=True, choices=[('Architecture and Planning', 'Architecture and Planning'), ('Bioengineering and Biotechnology', 'Bioengineering and Biotechnology'), ('Chemical Engineering', 'Chemical Engineering'), ('Center for Food Engineering and Technology', 'Center for Food Engineering and Technology'), ('Chemistry', 'Chemistry'), ('Civil and Env Engineering', 'Civil and Env Engineering'), ('Computer Science and Engg', 'Computer Science and Engg'), ('Centre for Quantitative Economics and Data Science', 'Centre for Quantitative Economics and Data Science'), ('Electrical and Electronics Engg', 'Electrical and Electronics Engg'), ('Electronics and Communication Engg', 'Electronics and Communication Engg'), ('Hotel Management and Catering Tech', 'Hotel Management and Catering Tech'), ('Humanities and Social Science', 'Humanities and Social Science'), ('Management', 'Management'), ('Mathematics', 'Mathematics'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Pharmaceutical Sciences and Tech', 'Pharmaceutical Sciences and Tech'), ('Physics', 'Physics'), ('Production and Industrial Engineering', 'Production and Industrial Engineering'), ('Remote Sensing', 'Remote Sensing'), ('Space Engineering and Rocketry', 'Space Engineering and Rocketry')], max_length=150, null=True)),
                ('collegeId', models.CharField(blank=True, max_length=5, null=True, unique=True)),
            ],
        ),
    ]
