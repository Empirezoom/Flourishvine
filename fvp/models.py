from django.db import models
# imported later 
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class CompanyProfile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    logo = models.ImageField(upload_to='logo')
    montheme = models.ImageField(upload_to='montheme')
    carousel1 = models.ImageField(upload_to='carousel1')
    carousel2 = models.ImageField(upload_to='carousel2')
    carousel3 = models.ImageField(upload_to='carousel3')
    carousel4 = models.ImageField(upload_to='carousel4')
    fb_link = models.CharField(max_length=50)
    insta_link = models.CharField(max_length=50)
    youtube_link = models.CharField(max_length=50)
    whatsapp_link = models.CharField(max_length=50)
    group_whatsapp = models.CharField(max_length=300, default="@flourish_whatsapp")
    thread_link = models.CharField(max_length=50,default='https://www.threads.net/@rccgfvp')
    developer_link = models.CharField(max_length=50)
    copyright = models.CharField(max_length=50)
    phone = models.CharField(max_length=50,default='070383993289')
    
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'CompanyProfile'
        managed = True
        verbose_name = 'CompanyProfile'
        verbose_name_plural = 'CompanyProfile'

class Features(models.Model):
    header = models.CharField(max_length=50)
    time = models.CharField(max_length=15,)
    fet_img = models.ImageField(upload_to='fet_img')
    openheaven_link = models.CharField(max_length=50)
    sunday_link = models.CharField(max_length=50)
    csr = models.TextField()
    mission = models.TextField()
    
    def __str__(self):
        return self.header
    class Meta:
        db_table = 'Features'
        managed = True
        verbose_name = 'Features'
        verbose_name_plural = 'Features'
    
class About(models.Model):
    sub_header = models.CharField(max_length=50)
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    team3 = models.CharField(max_length=50)
    img1 = models.ImageField(upload_to='team')
    img2 = models.ImageField(upload_to='team')
    img3 = models.ImageField(upload_to='team')
    txt1 = models.TextField()
    txt2 = models.TextField()
    txt3 = models.TextField()
    
    def __str__(self):
        return self.sub_header
    class Meta:
        db_table = 'About'
        managed = True
        verbose_name = 'About'
        verbose_name_plural = 'About'
    
class Testimonies(models.Model):
    testifier = models.CharField(max_length=50)
    passport = models.ImageField(upload_to='testifier')
    testimony = models.TextField()
    
    def __str__(self):
        return self.testifier
    class Meta:
        db_table = 'Testimony'
        managed = True
        verbose_name = 'Testimony'
        verbose_name_plural = 'Testimonies'
    
class Gallery(models.Model):
    g_title = models.CharField(max_length=50)
    g_img = models.ImageField(upload_to='gallery')
    span_info = models.TextField()
    land_right2 = models.BooleanField()
    land_left2 = models.BooleanField()
    portrait_center1 = models.BooleanField()
    
    
    def __str__(self):
        return self.g_title
    class Meta:
        db_table = 'Gallery'
        managed = True
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'
    
    
class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
    
class Give(models.Model):
    g_verse = models.CharField(max_length=100)
    g_head = models.CharField(max_length=100)
    offering_verse = models.CharField(max_length=100)
    offering_acc_no = models.CharField(max_length=100)
    tithe_verse = models.CharField(max_length=100)
    tithe_acc_no = models.CharField(max_length=100)
    Nehemiah_verse = models.CharField(max_length=100)
    Nehemiah_acc_no = models.CharField(max_length=100)
    slide1 = models.ImageField( upload_to='project')
    slide2 = models.ImageField( upload_to='project')
    slide3 = models.ImageField( upload_to='project')
    slide4 = models.ImageField( upload_to='project')


    def __str__(self):
        return self.g_verse
    
    class Meta:
        db_table = 'give'
        managed = True
        verbose_name = 'Give'
        verbose_name_plural = 'Give'


class Activity(models.Model):
    title = models.CharField(max_length=50, blank=True,null=True)
    slug = models.SlugField(unique=True)
    active = models.ImageField( upload_to='activities', )
    file = models.FileField(upload_to='file',blank=True,null=True)
    content = models.TextField(blank=True,null=True)
    updated = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, default=None,blank =True,related_name='liked')


    def __str__(self) :
        return self.title

    class Meta:
        db_table = 'activity'
        managed = True
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    
    def save(self,*arg,**kwargs):
        self.slug = slugify(self.title)
        super(Activity,self).save(arg,kwargs)
    
    def num_likes(self):
        return self.liked.all().count()

LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User,on_delete =models.CASCADE)
    post = models.ForeignKey(Activity,on_delete = models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like',max_length = 10)

    def __str__(self):
        return str(self.post)

class Comment(models.Model):
    commenter = models.ForeignKey(User,on_delete = models.CASCADE, related_name = 'comments')
    post = models.ForeignKey(Activity, on_delete = models.CASCADE,related_name = 'comments')
    body = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.commenter.username
    
class AdminInfo(models.Model):
    the_info = models.TextField()
    period = models.DateTimeField( auto_now=True,)

    def __str__(self):
        return self.the_info