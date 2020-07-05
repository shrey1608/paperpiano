from django.urls import path
from . import views
from blog import views as auth_view
urlpatterns=[
	path('',views.home,name="blog-home"),
	path('about',auth_view.about,name='about'),
	path('next',views.nextp,name="next-p"),
]