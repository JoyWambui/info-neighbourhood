# Generated by Django 4.0 on 2022-01-09 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('neighbourhood', '0008_alter_business_business_neighbourhood'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='post_neighbourhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_neighbourhood', to='neighbourhood.neighbourhood'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AddField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=50, null=True, verbose_name='Post Title'),
        ),
    ]
