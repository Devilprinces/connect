from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('apost',views.apost,name='apost'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('serch', views.serch,name="serch"),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('delpost/<id>',views.delpost,name="delpost"),
    path('manage',views.manage,name='manage')
]
