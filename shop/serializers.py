# shop.serializers.py

from rest_framework.serializers import(
    ModelSerializer,
    SerializerMethodField
)
from shop.models import Category, Product, Article


class CategorySerializer(ModelSerializer):

    products = SerializerMethodField
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'products',
            'date_created',
            'date_updated',
        ]

    def get_products(self, instance):
        queryset = instance.products.filter(active=True)
        serializer = ProductSerializer(queryset, many=True)
        return serializer.data

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'name',
            'description',
            'date_created',
            'date_updated',
        ]


class ArticleSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = [
            'id',
            'name',
            'price',
            'date_created',
            'date_updated',
        ]
