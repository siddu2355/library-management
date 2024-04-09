from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, BorrowerViewSet, TransactionViewSet, FineViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('borrowers', BorrowerViewSet)
router.register('transactions', TransactionViewSet)
router.register('fines', FineViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
