from django.conf.urls import url, include
from django.contrib import admin
from nightly_result import views
urlpatterns = [
        url(r'^$',views.upload_file)
        ]
