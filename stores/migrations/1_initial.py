import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('store_type', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('opening_hour', models.TimeField(null=True)),
                ('closing_hour', models.TimeField(null=True)),
                ('city', models.CharField(max_length=50)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('address', models.CharField(max_length=100)),
                ('rating', models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('phone', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
