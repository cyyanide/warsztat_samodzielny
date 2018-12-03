"""workshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from phonebook.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', AllPersonsDisplay.as_view()),
    re_path(r'^new$', AddPerson.as_view()),
    re_path(r'^show/(?P<id>\d+)$', PersonDetails.as_view()),
    re_path(r'^modify/(?P<id>\d+)$', PersonModify.as_view()),
    re_path(r'^delete/(?P<id>\d+)$', PersonDelete.as_view()),
    re_path('^modify/(?P<id>\d+)/addaddress$', AddAddress.as_view()),
    re_path('^modify/(?P<id>\d+)/addphone$', AddPhone.as_view()),
    re_path('^modify/(?P<id>\d+)/addemail$', AddEmail.as_view()),
    re_path('^modify/(?P<id>\d+)/deleteaddress$', AddressDelete.as_view()),
    re_path('^modify/(?P<id>\d+)/deletephone$', PhoneDelete.as_view()),
    re_path('^modify/(?P<id>\d+)/deleteemail$', EmailDelete.as_view()),
    re_path('^group/(?P<group_id>\d+)/show$', ShowGroup.as_view()),
    re_path('^group/create$', CreateGroup.as_view()),
    re_path('^group/(?P<group_id>\d+)/addmembers$', AddGroupMember.as_view()),





]
