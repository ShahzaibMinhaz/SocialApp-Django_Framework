from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('profile/<int:id>',views.profile,name='profile'),
    path('',views.home,name='home'),
    path('logout',views.logoutuser,name='logout'),
    path('MyPost',views.Mypost,name='mypost'),
    path('addcomments',views.addcomments,name='addcomments'),
    path('delete_comment',views.delete_comment,name='delete_comment'),
    path('findothers',views.findothers,name='findothers'),
    path('friendrequest/<int:user_id>/<int:friends_id>',views.sendfriendrequset,name='friendrequest'),
    path('getfriendrequest',views.getfriendrequest,name='getfriendrequest'),
    path('acceptfriendrequest/<int:friendstable_id>',views.accept_friendrequest,name='acceptfriendrequest'),
    path('unfriend/<int:friendstable_id>',views.unfriend,name='unfriend'),
    path('friends',views.friend,name='friends'),
    path('updatelike',views.updateLike,name='updatelike'),
    path('datafriends',views.datafriends,name='datafriends')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)