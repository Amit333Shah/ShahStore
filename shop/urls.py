from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name="Index"),
    path('about/',views.about,name="About US"),
    path('contact/',views.contact,name="Contact Us"),
    path('tracker/',views.tracker,name="Traking Status"),
    path('search/',views.search,name="Search"),
    path('prodView/<int:myid>',views.prodView,name="Product"),
    path('checkout/',views.checkout,name="Checkout"),

]