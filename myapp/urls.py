"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from webapp import views
from django.conf import settings

urlpatterns = [
    url(r'^login/', views.login_page, name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'^$', views.index1, name='preface'),
    url(r'^webapp/', include('webapp.urls')),
    url(r'^webapp/line1station1/', include('webapp.urls')),
    url(r'^loglistquery/', views.loglist, name='loglist'),
    url(r'^loglist/log_list_station', views.loglist_station, name='loglist_station'),
    url(r'^loglist/log_list_search', views.loglist_search, name='loglist_search'),
    url(r'^showlog/(\w+)/$', views.showlog, name='show_log')
]
if settings.DEBUG:
    urlpatterns += [
        url(r'^admin/', include(admin.site.urls)),
    ]