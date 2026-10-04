from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('members', MemberViewSet)
router.register('transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/', RegisterView.as_view()),
    path('api/auth/login/', LoginView.as_view()),
    path('api/auth/me/', MeView.as_view()),
    path('api/dashboard/', DashboardView.as_view()),
    path('api/reports/', ReportsView.as_view()),
    path('api/', include(router.urls)),
]
