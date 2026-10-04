from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings

class Migration(migrations.Migration):
    initial=True
    dependencies=[migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations=[
        migrations.CreateModel(name='Book',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('title',models.CharField(max_length=200)),('author',models.CharField(max_length=150)),('isbn',models.CharField(max_length=30,unique=True)),('category',models.CharField(blank=True,max_length=100)),('total_copies',models.PositiveIntegerField(default=1)),('available_copies',models.PositiveIntegerField(default=1)),('created_at',models.DateTimeField(auto_now_add=True))]),
        migrations.CreateModel(name='Member',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('phone',models.CharField(blank=True,max_length=20)),('address',models.CharField(blank=True,max_length=255)),('joined_date',models.DateField(auto_now_add=True)),('active',models.BooleanField(default=True)),('user',models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,related_name='member_profile',to=settings.AUTH_USER_MODEL))]),
        migrations.CreateModel(name='Transaction',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('issue_date',models.DateTimeField(auto_now_add=True)),('return_date',models.DateTimeField(blank=True,null=True)),('status',models.CharField(choices=[('ISSUED','Issued'),('RETURNED','Returned')],default='ISSUED',max_length=20)),('book',models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,related_name='transactions',to='library_api.book')),('member',models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,related_name='transactions',to='library_api.member'))])
    ]
