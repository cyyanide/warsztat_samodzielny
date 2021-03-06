# Generated by Django 2.0.3 on 2018-11-28 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='group',
            field=models.ManyToManyField(to='phonebook.Group'),
        ),
        migrations.AlterField(
            model_name='address',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='phonebook.Person'),
        ),
        migrations.AlterField(
            model_name='email',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='phonebook.Person'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='phone',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='phonebook.Person'),
        ),
    ]
