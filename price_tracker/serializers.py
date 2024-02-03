# serializers.py
from rest_framework import serializers
from .models import Provider, Article, Price

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'name']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'name']

class PriceSerializer(serializers.ModelSerializer):
    # Ensure that provider_id and article_id are serialized as nested objects
    provider_id = serializers.PrimaryKeyRelatedField(queryset=Provider.objects.all())
    article_id = serializers.PrimaryKeyRelatedField(queryset=Article.objects.all())
    
    provider_name = serializers.StringRelatedField(source='provider_id.name', read_only=True)
    article_name = serializers.StringRelatedField(source='article_id.name', read_only=True)
    
    class Meta:
        model = Price
        fields = ['id', 'provider_id', 'provider_name', 'article_id', 'article_name', 'price', 'created_at', 'updated_at']
    
