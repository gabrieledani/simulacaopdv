# Generated by Django 4.1.2 on 2022-11-01 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdvSimulations', '0005_simulacao_aprovada_simulacao_observacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulacao',
            name='vlr_verba1',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='simulacao',
            name='vlr_verba2',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='simulacao',
            name='vlr_verba3',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='simulacao',
            name='vlr_verba4',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='simulacao',
            name='vlr_verba5',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
