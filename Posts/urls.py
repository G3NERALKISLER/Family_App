from django.urls import path
from . import views
app_name = "posts"
urlpatterns = [
    path('home/', views.Home_page, name='Homepage'),
    path('postpage/', views.Post_Page, name='postpage' ),
    path('newpost/', views.new_post, name='newpost' ),
    path('<slug:slug>', views.Post_Detail, name = 'page'),

]
