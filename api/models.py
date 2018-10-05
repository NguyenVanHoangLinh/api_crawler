from django.db import models
# Create your models here.
class Article(models.Model):
    class Meta:
        verbose_name_plural = "Article"
        verbose_name = "Article"
    type = models.CharField(max_length=256, null=True)
    name = models.CharField(max_length=256, null=True)
    title = models.CharField(max_length=256, null=True)
    address = models.TextField(null=True)
    city = models.CharField(max_length=256, null=True)
    price = models.CharField(max_length=256,null=True)
    area = models.CharField(max_length=256,null=True)
    description = models.TextField(null=True)
    sell_date = models.TextField(null=True)
    expired_date = models.TextField(null=True)
    website = models.ForeignKey('Website', on_delete=models.CASCADE,default=1,null=True)
    website_uuid = models.CharField(max_length=256, null=True)
    seller_name = models.CharField(max_length=256, null=True)
    seller_address = models.CharField(max_length=256, null=True)
    seller_phone = models.CharField(max_length=256, null=True)
    seller_mobile = models.CharField(max_length=256, null=True)
    seller_email = models.CharField(max_length=256, null=True)
    seller_picture = models.TextField(null=True)
    project_name = models.CharField(max_length=256,null=True)
    project_investor = models.CharField(max_length=256,null=True)
    extended_data = models.TextField(null=True)

    def __str__(self):
         return self.id
class Website(models.Model):
    class Meta:
        verbose_name_plural = "Website"
        verbose_name = "Website"
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256,null=True)
    url = models.TextField(null=True)
    
    def __str__(self):
        return self.id
class ArticlePicture(models.Model):
    class Meta:
        verbose_name_plural = "ArticlePicture"
        verbose_name = "ArticlePicture"
    
    id = models.AutoField(primary_key=True)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    url = models.TextField(null=True)   
    
    def __str__(self):
        return self.id

