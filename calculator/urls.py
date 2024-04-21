from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    # when we keep the path empty, it is going to the root url of 127.0.0.1:8000
]    

# these urls must be given to the main project url
# there can be many urls but there will be only one url. The main url will be associated with all the views etc.
# we will be importing our views here