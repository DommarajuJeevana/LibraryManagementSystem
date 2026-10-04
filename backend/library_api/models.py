from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member_profile')
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    joined_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    def __str__(self): return self.user.get_full_name() or self.user.username

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=30, unique=True)
    category = models.CharField(max_length=100, blank=True)
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title

class Transaction(models.Model):
    STATUS = [('ISSUED','Issued'),('RETURNED','Returned')]
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='transactions')
    member = models.ForeignKey(Member, on_delete=models.PROTECT, related_name='transactions')
    issue_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='ISSUED')
    def __str__(self): return f'{self.book.title} - {self.member}'
