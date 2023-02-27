# Generated by Django 4.1.2 on 2022-11-14 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=11, null=True, unique=True)),
                ('email', models.EmailField(max_length=50, null=True, unique=True)),
                ('date_of_birth', models.DateField(max_length=50, null=True)),
                ('nationality', models.CharField(choices=[('Nigeria', 'Nigeria'), ('Ghana', 'Ghana'), ('United Kindom', 'UK'), ('USA', 'USA')], max_length=50, null=True)),
                ('state', models.CharField(choices=[('Nigeria', 'Nigeria'), ('Ghana', 'Ghana'), ('United Kindom', 'UK'), ('USA', 'USA')], max_length=50, null=True)),
                ('means_of_identifition', models.ImageField(null=True, unique=True, upload_to='identityImage/')),
                ('particular', models.ImageField(null=True, upload_to='particularsImage/')),
                ('profile_passport', models.ImageField(null=True, upload_to='staffimage/')),
                ('position', models.CharField(choices=[('CMD', 'CMD'), ('CMAC', 'CMAC'), ('Consultant', 'Consultant'), ('Resident Doctor', 'Resident Doctor'), ('Accountant', 'Accountant'), ('Secretary', 'Secretary'), ('Admin Officer', 'Admin Officer'), ('Clerical Officer', 'Clerical Officer'), ('Medical Lab Scientist', 'Medical Lab Scientist'), ('Phermacist', 'Phermacist'), ('Scientific Officer', 'Scientific Officer')], max_length=25, null=True)),
                ('department', models.CharField(choices=[('Internal medical', 'Internal medical'), ('Surgery', 'Surgery'), ('O&G', 'O&G'), ('Peadiatrics', 'Peadiatrics'), ('Nursing', 'Nursing'), ('Accounting', 'Accounting')], max_length=40, null=True)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorce', 'Divorce'), ('Complicated', 'Complicated')], max_length=20, null=True)),
                ('staff', models.BooleanField(default=False)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('O+', 'O+'), ('AB+', 'AB+'), ('A-', 'A-'), ('B-', 'B-'), ('O-', 'O-'), ('AB+', 'AB+')], max_length=4, null=True)),
                ('next_of_kin', models.CharField(max_length=20, null=True, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
