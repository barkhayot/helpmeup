from django.urls import path
from . import views

urlpatterns = [
    path('getblogs/', views.GetBlogs, name='getblogs'),
    path('getprivateblogs/', views.GetPrivateBlogs, name='getprivateblogs'),
    path('createblog/', views.CreateBlog, name='createblog'),
    path('blogdetail/<int:pk>/', views.BlogDetail, name='blogdetail'),
    path('updateblog/<int:pk>/', views.UpdateBlog, name='updateblog'),
    path('privateblogdetail/<int:pk>/', views.PrivateBlogDetail, name='privateblogdetail'),
    path('blogdelete/<int:pk>/', views.BlogDelete, name='blogdelete'),
    path('userblog/', views.UserBlog, name='userblog'),
    path('forbidden/', views.Forbidden, name='forbidden')
]