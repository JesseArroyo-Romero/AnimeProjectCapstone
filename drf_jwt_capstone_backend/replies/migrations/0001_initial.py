# Generated by Django 3.2.8 on 2021-12-02 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Replies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.comments')),
            ],
        ),
    ]
