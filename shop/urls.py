# shop.urls.py

from django.urls import path, include
from rest_framework import routers

from shop.views import category_view, product_view, article_view

router = routers.SimpleRouter()
router.register(r'category', category_view, basename='category')
router.register(r'product', product_view, basename='product')
router.register(r'article', article_view, basename='article')

urlpatterns = router.urls
