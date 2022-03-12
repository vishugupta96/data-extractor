from django.db import models
from django.contrib.auth.models import User

# from django.db.models.fields import CharField

# Create your models here.

class Client(models.Model):
    username = models.CharField(max_length=50,unique=True , blank = False)
    created_at = models.DateTimeField(auto_now=True , blank=False)

    youtube_url = models.URLField( blank=False)

    twitter_title=models.CharField(max_length=100 , blank=False)
    twitter_consumer_key = models.CharField(max_length=100 , blank = False)
    twitter_consumer_secret = models.CharField(max_length=100, blank = False)
    twitter_access_token = models.CharField(max_length=100, blank = False)
    twitter_access_token_secret = models.CharField(max_length=100 , blank = False)
    twitter_bearer_token = models.CharField(max_length=200, blank = False)
    
    
    instagram_title=models.CharField(max_length = 50, blank = False)
    facebook_title = models.CharField(max_length=50, blank = False)
    fb_access_token = models.CharField(max_length=250 , blank = False)
    fb_client_id = models.CharField(max_length=50, blank = False)
    fb_client_secret = models.CharField(max_length = 100,blank = False)
    fb_graph_domain = models.CharField(max_length = 100,default='https://graph.facebook.com/')
    fb_graph_version = models.CharField(max_length = 50,default='v12.0')
    fb_page_id = models.CharField(max_length=50,blank = False)
    fb_instagram_account_id = models.CharField(max_length=50,blank = False)
    fb_ig_username = models.CharField(max_length=50 ,blank = False)
    instagram_business_id = models.CharField(max_length=50,blank= False)


    linkedIn_title = models.CharField(max_length=50,blank=False )
    linkedIn_title_username = models.CharField(max_length=100, blank = False)
    linkedIn_title_password = models.CharField(max_length=100,blank = False)
    # c = Client.objects.get(id = '4')
    # c.allowed_users.all()
    allowed_users = models.ManyToManyField(User, blank = False , related_name='c_users',through='Link')

    twetter_file= models.FileField(blank=True,null=True)
    twitter_file_url = models.URLField(blank= True,null=True)


    def assigned_to(self):
        return ",".join([str(p) for p in self.allowed_users.all()])

    def __str__(self):
        return self.username

class Link(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete= models.CASCADE)