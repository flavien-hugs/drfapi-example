# shop.views.py

from rest_framework.viewsets import(
    ModelViewSet, ReadOnlyModelViewSet
)
from shop.mixins import MultipleSerializerMixin
from shop.models import Category, Product, Article
from shop.serializers import(
    CategoryListSerializer, CategoryDetailSerializer,
    ProductListSerializer, ProductDetailSerializer,
    ArticleSerializer,
)


class AdminCategoryViewSet(MultipleSerializerMixin, ModelViewSet):

    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset


admin_category_view = AdminCategoryViewSet


class CategoryViewSet(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        queryset = Category.objects.filter(active=True)
        return queryset


category_view = CategoryViewSet


class ProductViewSet(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
        queryset = Product.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset


product_view = ProductViewSet


class ArticleViewSet(ReadOnlyModelViewSet):

    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.filter(active=True)
        product_id = self.request.GET.get('product_id')
        if product_id is not None:
            queryset = queryset.filter(product_id=product_id)
        return queryset


article_view = ArticleViewSet


class AdminArticleViewSet(ModelViewSet):

    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all()
        return queryset


admin_article_view = AdminArticleViewSet
