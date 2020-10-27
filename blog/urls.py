from django.urls import path
from blog import views


app_name='blogs'

urlpatterns = [

    path('',views.Blog_home,name='bloghome'),
    path('<int:abc>',views.Blog_id,name='blogidlink'),

]
