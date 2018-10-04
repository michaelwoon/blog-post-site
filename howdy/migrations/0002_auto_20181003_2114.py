# Generated by Django 2.0.2 on 2018-10-04 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('howdy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='relatedOne',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_article', to='howdy.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='relatedThree',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_article', to='howdy.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='relatedTwo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_article', to='howdy.Post'),
        ),
    ]