# Generated by Django 4.1.5 on 2023-01-29 19:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Borrow_date', models.DateTimeField()),
                ('Expected_return_date', models.DateTimeField()),
                ('Actual_return_date', models.DateTimeField()),
                ('Book_id', models.ManyToManyField(to='book.book')),
                ('User_id', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='borrowing',
            constraint=models.CheckConstraint(check=models.Q(('Expected_return_date__gt', models.F('Borrow_date'))), name='Expected_return_date'),
        ),
        migrations.AddConstraint(
            model_name='borrowing',
            constraint=models.CheckConstraint(check=models.Q(('Actual_return_date__lte', models.F('Expected_return_date'))), name='Actual_return_date'),
        ),
    ]
