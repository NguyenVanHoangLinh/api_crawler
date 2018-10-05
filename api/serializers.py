from rest_framework import serializers
from .models import Article, ArticlePicture
class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
class ArticlePictureSerializers(serializers.ModelSerializer):
    class Meta:
        model = ArticlePicture
        fields = '__all__'