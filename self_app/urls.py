from django.urls import path

from self_app import views


app_name = 'self_app'

urlpatterns = [
    path('houtarou/',views.Houtarou,name="houtarou"),
    path('namjoohyuk/', views.Namjoohyuk, name='namjoohyuk')

]   