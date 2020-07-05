from django.urls import path
from . import views
from blog import views as auth_view
urlpatterns=[
	path('',views.home,name="home"),
	path('about',auth_view. about,name='about'),
	path('printe',views.printe,name='printe'),
	path('playe',views.playe,name='playe')
]