from django.urls import path
from bikes import views


app_name = 'bikes'


urlpatterns = [
    path('brand/', views.brand,name='brand'),
    path('base/',views.base,name='base'),
    path('other/',views.other,name='other')
]
