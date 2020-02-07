from django.urls import path
from . import views
app_name="blog"
urlpatterns = [
     
     path("", views.allblogs, name="allblogs"),
     path("create", views.create_blog, name="createblog"),
     path("<slug>", views.getsingleblog, name="singleblog"),
     path("category/<cat>",views.getcatblog,name="catblog")
 ]
 