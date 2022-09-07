
from django.urls import path
from .import views

urlpatterns = [
    
    path('',views.index,name='homepage'),
    path('about/',views.about,name='aboutpage'),
    path('blog/',views.blog,name='blogpage'),
    path('contact/',views.contact,name='contactpage'),
    path('gallery/',views.gallery,name='gallerypage'),
    path('rooms/',views.room,name='roompage'),
    path('rooms1/',views.room1,name='room1page'),
    path('booking/',views.book,name='bookingpage'),
    path('login1/',views.login1,name='loginpage'),
    path('login1/page',views.login2,name='loginhomepage'),
    path('logout/',views.logout,name='logoutpage'),
    path('reg',views.register,name='regpage'),
    path('confirm',views.booking,name='confirmpage'),
    path('comment/',views.comments,name="comment page"),
    path('contactus/',views.contactuspg,name="contactus"),
    
]