# Generated by Django 3.1.7 on 2021-03-26 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mines1', '0003_auto_20210319_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Denomination_Sociale', models.CharField(max_length=30)),
                ('Type_installation', models.IntegerField(null=True)),
                ('Localisation', models.TextField(max_length=30, null=True)),
                ('Adresse', models.CharField(max_length=30)),
                ('Date_inspection', models.IntegerField(null=True)),
                ('Inspecteurs', models.TextField(max_length=30, null=True)),
                ('Administration', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='send',
            name='Message',
            field=models.TextField(max_length=30, null=True),
        ),
    ]
