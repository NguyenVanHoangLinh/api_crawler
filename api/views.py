from rest_framework import serializers
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from django.contrib import admin, auth
from .serializers import ArticleSerializers, ArticlePictureSerializers , WebsiteSerializers
from .models import Article, ArticlePicture, Website
from rest_framework.views import APIView
from django.http import Http404
from django.shortcuts import render
class ArticleAPI(APIView):
    def get(self, request):
        article = Article.objects.all()
        article_serializer = ArticleSerializers(article, many=True)
        return Response(article_serializer.data)
    def post(self, request):
        article_serializers = ArticleSerializers(data = request.data)
        if article_serializers.is_valid():
            article_serializers.save()
            return Response(article_serializers.data, status=status.HTTP_201_CREATED)
        return Response(article_serializers.errors, status=status.HTTP_400_BAD_REQUEST)
class ArticlePictureAPI(APIView):
    def get(self, request):
        article_picture = ArticlePicture.objects.all()
        article_picture_serializer = ArticlePictureSerializers(article_picture, many=True)
        return Response(article_picture_serializer.data)
    def post(self, request):
        article_picture_serializers = ArticlePictureSerializers(data = request.data)
        if article_picture_serializers.is_valid():
            article_picture_serializers.save()
            return Response(article_picture_serializers.data, status=status.HTTP_201_CREATED)
        return Response(article_picture_serializers.errors, status=status.HTTP_400_BAD_REQUEST)  
class WebsiteAPI(APIView):
    def get(self, request):
        website = Website.objects.all()
        website_serializer = WebsiteSerializers(website, many=True)
        return Response(website_serializer.data)