# Generated by Django 3.0.7 on 2020-06-30 06:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, null=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('sender', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by', models.CharField(max_length=70)),
                ('branch', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('real_sender', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yname', models.CharField(max_length=70)),
                ('branch', models.CharField(max_length=50)),
                ('skills', models.TextField()),
                ('suggestion', models.TextField()),
                ('real_sender', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MyPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='')),
                ('subject', models.CharField(max_length=200)),
                ('msg', models.TextField(blank=True, null=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=18, validators=[django.core.validators.MinValueValidator(18)])),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], default='female', max_length=20)),
                ('phone_no', models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator('^0?[5-9]{1}\\d{9}$')])),
                ('status', models.CharField(choices=[('single', 'single'), ('commited', 'commited'), ('complicated', 'complicated')], default='single', max_length=20)),
                ('registration_no', models.CharField(blank=True, max_length=12, null=True)),
                ('tagline', models.CharField(default='Hit me on Vitbook!', max_length=200)),
                ('city', models.CharField(default='Vitland', max_length=100)),
                ('college', models.CharField(choices=[('VIT Vellore', 'VIT Vellore'), ('VIT Chennai', 'VIT Chennai'), ('VIT Bhopal', 'VIT Bhopal'), ('VIT Amaravati', 'VIT Amaravati')], default='VIT Bhopal', max_length=100)),
                ('description', models.TextField(blank=True, default='Hi!, this is my default description.', null=True)),
                ('insta_profile', models.URLField(blank=True, null=True)),
                ('facebook_profile', models.URLField(blank=True, null=True)),
                ('linkedin_profile', models.URLField(blank=True, null=True)),
                ('github_profile', models.URLField(blank=True, null=True)),
                ('portfolio', models.URLField(blank=True, null=True)),
                ('pic', models.ImageField(blank=True, default='default_profile.png', null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_one', models.CharField(max_length=30)),
                ('option_two', models.CharField(max_length=30)),
                ('option_one_count', models.IntegerField(default=0)),
                ('option_two_count', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='social.MyProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Vithub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('code', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(choices=[('C', 'C'), ('C++', 'C++'), ('Python', 'Python'), ('Javascript', 'Javascript'), ('HTML/CSS', 'HTML/CSS'), ('Java', 'Java'), ('Golang', 'Golang'), ('Ruby', 'Ruby'), ('Kotlin', 'Kotlin'), ('Solidity', 'Solidity'), ('Other', 'Other')], default='Not provided', max_length=50)),
                ('domain', models.CharField(choices=[('Competitive Coding', 'Competitive Coding'), ('Web Development', 'Web Development'), ('App Development', 'App Development'), ('Blockchain', 'Blockchain'), ('Scripting', 'Scripting'), ('DSA', 'DSA'), ('Others', 'Others')], default='Not Provided', max_length=100)),
                ('uploaded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.MyProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PostLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('liked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.MyProfile')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.MyPost')),
            ],
        ),
        migrations.CreateModel(
            name='PollVoted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voted_by', to='social.MyProfile')),
                ('voted_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voted_on', to='social.Poll')),
            ],
        ),
        migrations.AddField(
            model_name='mypost',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.MyProfile'),
        ),
        migrations.CreateModel(
            name='FollowUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('followed_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to='social.MyProfile')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='social.MyProfile')),
            ],
        ),
        migrations.CreateModel(
            name='AddConfession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('by', models.CharField(max_length=100)),
                ('to', models.CharField(max_length=100)),
                ('confession', models.TextField(default='')),
                ('real', models.CharField(max_length=200)),
                ('confessioner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social.MyProfile')),
            ],
        ),
    ]
