from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Book, Member, Transaction


class BookSerializer(serializers.ModelSerializer):
    availability = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'isbn',
            'category',
            'total_copies',
            'available_copies',
            'created_at',
            'availability',
        ]

    def get_availability(self, obj):
        return 'Available' if obj.available_copies > 0 else 'Not Available'


class MemberSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Member
        fields = [
            'id',
            'name',
            'username',
            'email',
            'phone',
            'address',
            'joined_date',
            'active',
        ]

    def get_name(self, obj):
        full_name = obj.user.get_full_name()
        return full_name or obj.user.username


class TransactionSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(
        source='book.title',
        read_only=True
    )
    member_name = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = [
            'id',
            'book',
            'book_title',
            'member',
            'member_name',
            'issue_date',
            'return_date',
            'status',
        ]

    def get_member_name(self, obj):
        full_name = obj.member.user.get_full_name()
        return full_name or obj.member.user.username