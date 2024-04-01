from django.urls import path
from .views import all_posts, posts_by_category,post_detail,post_created,post_update,post_delate,category_detail,category_created,category_ubdate,category_delete



urlpatterns = [
    path('', all_posts, name='index'),
    path('category/<int:category_id>/', posts_by_category, name='bolim'),
    path('detail/<int:pk>/',post_detail,name='post_detail'),
    path('category_detail/<int:pk>/',category_detail,name='category_detail'),
    path('add/',post_created,name='post_created'),
    path('category_add',category_created,name='category_created'),
    path('update/<int:pk>/',post_update,name='post_update'),
    path('category_update/<int:pk>/',category_ubdate,name='category_update'),
    path('delete/<int:pk>/',post_delate,name='post_delete'),
    path('category_delete/<int:pk>/',category_delete,name='category_delete'),
]