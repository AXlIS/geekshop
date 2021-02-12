from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.products, name='index'),
    path('page/<int:page>/<int:category_id>', mainapp.products, name='page'),
]

