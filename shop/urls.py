from django.urls import path
from . import views

urlpatterns={
     path('',views.index,name='index'),
     path('register/',views.register,name='register'),
     path('foodrecom/',views.foodrecom,name='foodrecom'),
     path('menu/',views.menu,name='menu'),
     path('breakfastveg/',views.breakfastveg,name='breakfastveg'),
     path('breakfastnon/',views.breakfastnon,name='breakfastnon'),
     path('lunchveg/',views.lunchveg,name='lunchveg'),
     path('lunchnon/',views.lunchnon,name='lunchnon'),
     path('dinnerveg/',views.dinnerveg,name='dinnerveg'),
     path('dinnernon/',views.dinnernon,name='dinnernon'),
     path('signup/',views.signup,name='signup'),
     path('contact/',views.contact,name='contact'),
     path('cart/',views.cart,name='cart'),
     path('chatsveg/',views.chatsveg,name='chatsveg'),
     path('juice/',views.juice,name='juice'),
     path('soups/',views. soups,name=' soups'),
     path('starters/',views. starters,name=' starters'),
     path('combo/',views. combo,name=' combo'),
     path('about/',views.about,name='about'),
     
     
}