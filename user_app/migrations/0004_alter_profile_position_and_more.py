# Generated by Django 4.1.2 on 2022-11-22 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_remove_profile_means_of_identifition_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(choices=[('CMD', 'CMD'), ('CMAC', 'CMAC'), ('HOD', 'HOD'), ('Consultant', 'Consultant'), ('Resident Doctor', 'Resident Doctor'), ('Accountant', 'Accountant'), ('Secretary', 'Secretary'), ('Admin Officer', 'Admin Officer'), ('Clerical Officer', 'Clerical Officer'), ('Medical Lab Scientist', 'Medical Lab Scientist'), ('Phermacist', 'Phermacist'), ('Scientific Officer', 'Scientific Officer')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_passport',
            field=models.ImageField(null=True, upload_to='staffImage/'),
        ),
    ]
