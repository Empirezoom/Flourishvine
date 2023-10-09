from django.contrib import admin
from . models import *

# Register your models here.
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ['id','name','logo']
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ['id','header','fet_img']
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ['id','header','fet_img']
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id','sub_header','team1','team2','team3']
class TestimoniesAdmin(admin.ModelAdmin):
    list_display = ['id','testifier','passport','testimony']
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id','g_title','land_right2','land_left2','portrait_center1']
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','full_name','message','sent']
class GiveAdmin(admin.ModelAdmin):
    list_display = ['id','offering_acc_no','Nehemiah_acc_no','slide1']
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id','title','active','updated']
    prepopulated_fields = {'slug':('title',)}
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id','user','post','value']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','commenter','post','body','status']
class AdminInfoAdmin(admin.ModelAdmin):
    list_display = ['id','the_info','period']






admin.site.register(CompanyProfile,CompanyProfileAdmin)
admin.site.register(Features,FeaturesAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Testimonies,TestimoniesAdmin)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(Give,GiveAdmin)
admin.site.register(Activity,ActivityAdmin)
admin.site.register(Like,LikeAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(AdminInfo,AdminInfoAdmin)



