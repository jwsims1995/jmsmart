# Generated by Django 3.0.8 on 2020-07-23 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=64, verbose_name='아이디')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('username', models.CharField(max_length=64, verbose_name='사용자명')),
                ('postcode', models.CharField(max_length=64, verbose_name='우편번호')),
                ('address', models.CharField(max_length=64, verbose_name='주소')),
                ('phone', models.CharField(max_length=64, verbose_name='전화번호')),
                ('e_mail', models.CharField(max_length=64, verbose_name='이메일')),
            ],
        ),
    ]
