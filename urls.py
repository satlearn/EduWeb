
from django.urls import path
from myapp import views

urlpatterns = [    
    path('index/',views.index,name='index.html'),
    path('about/',views.about,name='about.html'),
    path('courses/',views.courses,name='courses.html'),
    path('contact/',views.contact,name='contat.html'),
    path('home1/',views.home1,name='home1.html'),
    path('login/',views.login,name='login.html'),
    path('signup/',views.signup,name='signup.html'),
    path('signup_view/',views.signup_view,name='signup_view'),
    
]


