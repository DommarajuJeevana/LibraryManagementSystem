from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import transaction as db_transaction
from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, Member, Transaction
from .serializers import BookSerializer, MemberSerializer, TransactionSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        username=request.data.get('username','').strip(); password=request.data.get('password',''); email=request.data.get('email','')
        first=request.data.get('first_name','').strip(); last=request.data.get('last_name','').strip(); phone=request.data.get('phone','').strip()
        if not username or not password: return Response({'detail':'Username and password are required.'},status=400)
        if User.objects.filter(username=username).exists(): return Response({'detail':'Username already exists.'},status=400)
        user=User.objects.create_user(username=username,password=password,email=email,first_name=first,last_name=last)
        Member.objects.create(user=user,phone=phone)
        token=Token.objects.create(user=user)
        return Response({'token':token.key,'user':{'username':user.username,'name':user.get_full_name() or user.username}},status=201)

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        user=authenticate(username=request.data.get('username'),password=request.data.get('password'))
        if not user: return Response({'detail':'Invalid username or password.'},status=401)
        token,_=Token.objects.get_or_create(user=user)
        return Response({'token':token.key,'user':{'id':user.id,'username':user.username,'name':user.get_full_name() or user.username,'is_staff':user.is_staff}})

class MeView(APIView):
    def get(self,request):
        u=request.user
        return Response({'id':u.id,'username':u.username,'name':u.get_full_name() or u.username,'is_staff':u.is_staff})

class BookViewSet(viewsets.ModelViewSet):
    queryset=Book.objects.all().order_by('title'); serializer_class=BookSerializer
    def get_queryset(self):
        qs=super().get_queryset(); q=self.request.query_params.get('search','').strip()
        if q: qs=qs.filter(title__icontains=q) | qs.filter(author__icontains=q) | qs.filter(isbn__icontains=q) | qs.filter(category__icontains=q)
        return qs

class MemberViewSet(viewsets.ModelViewSet):
    queryset=Member.objects.select_related('user').all().order_by('-joined_date'); serializer_class=MemberSerializer
    def create(self, request, *args, **kwargs):
        username=request.data.get('username','').strip(); password=request.data.get('password','') or 'Member@123'; first=request.data.get('first_name','').strip(); last=request.data.get('last_name','').strip(); email=request.data.get('email','').strip(); phone=request.data.get('phone','').strip(); address=request.data.get('address','').strip()
        if not username: return Response({'detail':'Username is required.'},status=400)
        if User.objects.filter(username=username).exists(): return Response({'detail':'Username already exists.'},status=400)
        user=User.objects.create_user(username=username,password=password,first_name=first,last_name=last,email=email)
        member=Member.objects.create(user=user,phone=phone,address=address)
        return Response(MemberSerializer(member).data,status=201)
    def destroy(self, request, *args, **kwargs):
        member=self.get_object(); member.user.delete(); return Response(status=204)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset=Transaction.objects.select_related('book','member__user').all().order_by('-issue_date'); serializer_class=TransactionSerializer
    @db_transaction.atomic
    def create(self,request):
        book_id=request.data.get('book_id'); member_id=request.data.get('member_id')
        try: book=Book.objects.select_for_update().get(id=book_id); member=Member.objects.get(id=member_id)
        except (Book.DoesNotExist,Member.DoesNotExist): return Response({'detail':'Book or member not found.'},status=404)
        if book.available_copies < 1: return Response({'detail':'Book is not available.'},status=400)
        if Transaction.objects.filter(book=book,member=member,status='ISSUED').exists(): return Response({'detail':'This member already has this book.'},status=400)
        tx=Transaction.objects.create(book=book,member=member); book.available_copies-=1; book.save(update_fields=['available_copies'])
        return Response(TransactionSerializer(tx).data,status=201)

    @action(detail=True, methods=['post'], url_path='return')
    @db_transaction.atomic
    def return_book(self,request,pk=None):
        try: tx=Transaction.objects.select_for_update().select_related('book').get(pk=pk,status='ISSUED')
        except Transaction.DoesNotExist: return Response({'detail':'Active transaction not found.'},status=404)
        tx.status='RETURNED'; tx.return_date=timezone.now(); tx.save(update_fields=['status','return_date'])
        tx.book.available_copies=min(tx.book.total_copies,tx.book.available_copies+1); tx.book.save(update_fields=['available_copies'])
        return Response(TransactionSerializer(tx).data)

class DashboardView(APIView):
    def get(self,request):
        return Response({'total_books':Book.objects.count(),'total_copies':sum(Book.objects.values_list('total_copies',flat=True)),'available_copies':sum(Book.objects.values_list('available_copies',flat=True)),'total_members':Member.objects.count(),'active_issues':Transaction.objects.filter(status='ISSUED').count(),'returned':Transaction.objects.filter(status='RETURNED').count()})

class ReportsView(APIView):
    def get(self,request):
        tx=Transaction.objects.select_related('book','member__user').all().order_by('-issue_date')
        return Response({'transactions':TransactionSerializer(tx,many=True).data})
