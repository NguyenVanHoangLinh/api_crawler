from rest_framework import serializers
from .models import Article, ArticlePicture,Website
class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
class ArticlePictureSerializers(serializers.ModelSerializer):
    class Meta:
        model = ArticlePicture
        fields = '__all__'
class WebsiteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = '__all__'