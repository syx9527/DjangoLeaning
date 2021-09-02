# Generated by Django 3.2.6 on 2021-08-09 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_alter_book_book_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_market_price',
            field=models.DecimalField(decimal_places=2, max_digits=7, null=True, verbose_name='零价格'),
        ),
        migrations.AddField(
            model_name='book',
            name='pub',
            field=models.CharField(default='', max_length=50, verbose_name='出版社'),
        ),
        migrations.AlterField(
            model_name='author',
            name='author_age',
            field=models.IntegerField(default=1, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='author',
            name='author_email',
            field=models.EmailField(max_length=254, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterModelTable(
            name='author',
            table='author',
        ),
    ]
