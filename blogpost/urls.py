from django.urls import path
from . import views
from .views import UpdatePostView, LikeView, UpdateProfileView, DeletePostView

urlpatterns = [
    path('',views.index,name='index'),
    path('post/<int:pk>',views.post,name='post'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('ad',views.ad,name='ad'),
    path('save',views.save,name='save'),
    path('search',views.search,name='search'),
    path('post/update/<int:pk>',UpdatePostView.as_view(),name='update'),
    path('like/<int:pk>', LikeView, name='like'),
    path('post/<int:pk>/delete',DeletePostView.as_view(),name='delete_post'),
    path('update_profile/<slug:username>/<int:pk>',UpdateProfileView.as_view(),name='update_profile')
]