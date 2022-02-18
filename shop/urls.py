# shop.urls.py

from django.urls import path, include
from rest_framework import routers

from shop import views

router = routers.SimpleRouter()

router.register(
    r'admin/category',
    views.admin_category_view,
    basename='admin-category'
)
router.register(
    r'admin/article',
    views.admin_article_view,
    basename='admin-article'
)

router.register(
    r'category',
    views.category_view,
    basename='category'
)
router.register(
    r'product',
    views.product_view,
    basename='product'
)
router.register(
    r'article',
    views.article_view,
    basename='article'
)

urlpatterns = router.urls
