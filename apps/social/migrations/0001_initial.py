# Generated by Django 5.2.3 on 2025-06-21 13:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('facebook', 'Facebook'), ('twitter', 'Twitter'), ('instagram', 'Instagram'), ('linkedin', 'LinkedIn'), ('pinterest', 'Pinterest'), ('youtube', 'YouTube'), ('tiktok', 'TikTok')], max_length=20, unique=True)),
                ('icon', models.CharField(blank=True, max_length=50)),
                ('api_version', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('media_url', models.URLField(blank=True, null=True)),
                ('scheduled_time', models.DateTimeField()),
                ('is_published', models.BooleanField(default=False)),
                ('published_time', models.DateTimeField(blank=True, null=True)),
                ('post_id', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostAnalytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.PositiveIntegerField(default=0)),
                ('comments', models.PositiveIntegerField(default=0)),
                ('shares', models.PositiveIntegerField(default=0)),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('impressions', models.PositiveIntegerField(default=0)),
                ('engagement_rate', models.FloatField(default=0.0)),
                ('saved_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='analytics', to='social.scheduledpost')),
            ],
        ),
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=255)),
                ('account_id', models.CharField(max_length=255)),
                ('access_token', models.TextField()),
                ('refresh_token', models.TextField(blank=True, null=True)),
                ('token_expires', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_accounts', to=settings.AUTH_USER_MODEL)),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='social.socialplatform')),
            ],
            options={
                'unique_together': {('user', 'platform', 'account_id')},
            },
        ),
        migrations.AddField(
            model_name='scheduledpost',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_posts', to='social.socialaccount'),
        ),
    ]
