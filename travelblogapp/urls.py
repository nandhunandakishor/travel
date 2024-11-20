from django.urls import path
from.import views

urlpatterns=[
    path('',views.welcomepage),
    path('register1',views.registerpage1,name='register1'),
    path('login1',views.loginpage2,name='login1'),
    path('welcome',views.welcomepage,name='welcome'),
    path('home1',views.homepage1, name='home1'),
    path('Add',views.reg),
    path('LOG',views.login1),
    path('kozhikode1',views.kozhikodepage,name='kozhikode1'),
    path('wayanad1',views.wayanadpage, name='wayanad1'),
    path('munnar1',views.munnarpage, name='munnar1'),
    path('beachpage',views.kozhikodebeachpage,name='beachpage'),
    path('sarovarampark',views.sarovaramparkpage,name='sarovarampark'),
    path('smstreet',views.smstreetpage,name='smstreet'),
    path('chembra',views.chembrapeakpage,name='chembra'),
    path('meenmutty',views.meenmuttypage,name='meenmutty'),
    path('forest',views.forestpage,name='forest'),
    path('anaimudi',views.anaimudipage,name='anaimudi'),
    path('home',views.homepage1,name='home'),
    path('about',views.aboutpage,name='about'),
    path('contact',views.contactpage,name='contact'),
    path('familypackage',views.familypackagepage,name='familypackage'),
    path('bachelorpackage',views.bachelorpackagepage,name='bachelorpackage'),
    path('sub',views.bachelor_package),
    # path('add/', views.add_view, name='add_view'),
    path('bookcalicut1',views.bookcalicutpage,name='bookcalicut1'),
    path('submit-booking', views.calicut_book),
    path('bookwayanad',views.bookwayandpage,name='bookwayanad'),
    path('bookmunnar',views.bookmunnarpage,name='bookmunnar'),
    path('payment1',views.paymentpage,name='payment1'),



]