import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_api.settings')
django.setup()

from django.contrib.auth.models import User
from library_api.models import Book, Member, Transaction


def create_admin():
    user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@library.com',
            'first_name': 'Library',
            'last_name': 'Admin',
        },
    )

    user.is_staff = True
    user.is_superuser = True
    user.set_password('Admin@123')
    user.save()

    return user


def create_members():
    members = [
        {
            'username': 'student1',
            'password': 'Member@123',
            'first_name': 'Ananya',
            'last_name': 'Reddy',
            'email': 'ananya@example.com',
            'phone': '9876543210',
            'address': 'Chennai',
        },
        {
            'username': 'student2',
            'password': 'Member@123',
            'first_name': 'Rahul',
            'last_name': 'Kumar',
            'email': 'rahul@example.com',
            'phone': '9876543211',
            'address': 'Hyderabad',
        },
        {
            'username': 'student3',
            'password': 'Member@123',
            'first_name': 'Priya',
            'last_name': 'Sharma',
            'email': 'priya@example.com',
            'phone': '9876543212',
            'address': 'Bangalore',
        },
    ]

    created_members = []

    for data in members:
        user, created = User.objects.get_or_create(
            username=data['username'],
            defaults={
                'email': data['email'],
                'first_name': data['first_name'],
                'last_name': data['last_name'],
            },
        )

        if created:
            user.set_password(data['password'])
            user.save()

        member, _ = Member.objects.get_or_create(
            user=user,
            defaults={
                'phone': data['phone'],
                'address': data['address'],
            },
        )

        created_members.append(member)

    return created_members


def create_books():
    books = [
        {
            'title': 'Python Programming',
            'author': 'Mark Lutz',
            'isbn': '9781449355739',
            'category': 'Programming',
            'total_copies': 5,
        },
        {
            'title': 'Clean Code',
            'author': 'Robert C. Martin',
            'isbn': '9780132350884',
            'category': 'Programming',
            'total_copies': 4,
        },
        {
            'title': 'The Alchemist',
            'author': 'Paulo Coelho',
            'isbn': '9780061122415',
            'category': 'Fiction',
            'total_copies': 3,
        },
        {
            'title': 'Database System Concepts',
            'author': 'Abraham Silberschatz',
            'isbn': '9780078022159',
            'category': 'Database',
            'total_copies': 3,
        },
        {
            'title': 'Computer Networks',
            'author': 'Andrew S. Tanenbaum',
            'isbn': '9780132126953',
            'category': 'Networking',
            'total_copies': 2,
        },
    ]

    created_books = []

    for data in books:
        book, created = Book.objects.get_or_create(
            isbn=data['isbn'],
            defaults={
                'title': data['title'],
                'author': data['author'],
                'category': data['category'],
                'total_copies': data['total_copies'],
                'available_copies': data['total_copies'],
            },
        )

        created_books.append(book)

    return created_books


def main():
    admin = create_admin()
    members = create_members()
    books = create_books()

    print('Library seed data created successfully.')
    print(f'Admin user: {admin.username}')
    print(f'Members: {len(members)}')
    print(f'Books: {len(books)}')


if __name__ == '__main__':
    main()