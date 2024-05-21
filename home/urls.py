from django.urls import path
from .views import landing_page,GetTest

app_name = 'home'
urlpatterns =[
    path('',landing_page,name='landing_page'),
    path('testt/',GetTest.as_view(),name='test')
]