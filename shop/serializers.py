# shop.serializers.py

from rest_framework.serializers import ModelSerializer

from shop.models import Category, Product, Article


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


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
