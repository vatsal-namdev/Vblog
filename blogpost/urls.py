from django.urls import path
from . import views
from .views import UpdatePostView, LikeView, UpdateProfileView, DeletePostView

urlpatterns = [
    path('',views.index,name='index'),
    path('post/<slug>',views.post,name='post'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('ad',views.ad,name='ad'),
    path('save',views.save,name='save'),
    path('search',views.search,name='search'),
    path('post/update/<slug>',UpdatePostView.as_view(),name='update'),
    path('like/<slug>', LikeView, name='like'),
    path('post/<slug>/delete',DeletePostView.as_view(),name='delete_post'),
    path('update_profile/<slug:username>/<int:pk>',UpdateProfileView.as_view(),name='update_profile'),
    path('about',views.about,name='about')
]