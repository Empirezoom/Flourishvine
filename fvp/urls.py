from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('give',views.give,name='give'),
    path('register',views.register,name='register'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('profile',views.profile,name='profile'),
    path('profile_update',views.profile_update,name='profile_update'),
    path('message_center',views.message_center,name='message_center'),
    path('welcome',views.welcome,name='welcome'),
    path('event',views.event,name='event'),
    path('detail/<slug:theslug>',views.detail,name='detail'),
    path('post_like',views.post_like,name='post_like'),
    path('fvp_media_admin',views.fvp_media_admin,name='fvp_media_admin'),
    path('delete', views.delete, name='delete'),
    path('del_test', views.del_test, name='del_test'),
    path('del_notification', views.del_notification, name='del_notification'),
    path('search', views.search, name='search'),
    path('notification', views.notification, name='notification'),

]