# shop.serializers.py

from rest_framework.serializers import(
    ModelSerializer,
    ValidationError,
    SerializerMethodField
)
from shop.models import Category, Product, Article


class CategoryListSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'date_created',
            'date_updated',
        ]

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise ValidationError('Category already exists !')
        return value

    def validate(self, data):
        if data['name'] not in data['description']:
            raise ValidationError('Name must be in description')
        return data


class CategoryDetailSerializer(ModelSerializer):

    products = SerializerMethodField()
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
        serializer = ProductListSerializer(queryset, many=True)
        return serializer.data


class ProductListSerializer(ModelSerializer):
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

class ProductDetailSerializer(ModelSerializer):

    articles = SerializerMethodField()
    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'name',
            'articles',
            'description',
            'date_created',
            'date_updated',
        ]

    def get_articles(self, instance):
        queryset = instance.articles.filter(active=True)
        serializer = ArticleSerializer(queryset, many=True)
        return serializer.data

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

    def validate_price(self, value):
        if value < 1:
            raise ValidationError(
                'Price must be greater than 1'
            )
        return value

    def validate_product(self, value):
        if value.active is False:
            raise ValidationError('Inactive product')
        return value
