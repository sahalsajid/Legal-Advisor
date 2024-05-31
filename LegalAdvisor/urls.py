"""LegalAdvisor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from Administrator import views
from User import user_views
from Advocate import adv_views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('login/', views.login),
    path('adv_register/', views.adv_register),
    path('user_register/', views.user_register),
    path('user_bank/', views.user_bank),
    # path('chat/', views.chat),
    #-------------------------ADMIN-----------------------------------#
    path('admin_header_footer/', views.admin_header_footer),
    path('admin_home/', views.admin_home),
    path('advocate_list/', views.advocate_list),
    path('adv_request/', views.adv_request),
    path('action_adv/', views.action_adv),
    path('user_request/', views.user_request),
    path('user_list/', views.user_list),
    path('user_remove/', views.user_remove),
    path('action_user/', views.action_user),
    path('case_category/', views.case_category),
    path('cat_remove/', views.cat_remove),
    path('ipc_section/', views.ipc_section),
    path('ipc_remove/', views.ipc_remove),
    path('view_feedback/', views.view_feedback),
    path('phone_number/', views.phone_number),
    # path('gen_otp/', views.gen_otp),
    # path('otp/', views.otp),
    # path('sendsms1/', views.sendsms1),

    path('new_password/', views.new_password),

    #-------------------------User-----------------------------------#

    path('user_home/', user_views.user_home),
    path('user_header_footer/', user_views.user_header_footer),
    path('user_ipc/', user_views.user_ipc),
    path('user_adv_list/', user_views.user_adv_list),
    path('view_adv/', user_views.view_adv),
    path('add_case/', user_views.add_case),
    path('case_status/', user_views.case_status),
    path('user_view_case_status/', user_views.user_view_case_status),
    path('payment1/', user_views.payment1),
    path('payment2/', user_views.payment2),
    path('payment3/', user_views.payment3),
    path('payment4/', user_views.payment4),
    path('payment5/', user_views.payment5),
    path('user_feedback/', user_views.user_feedback),
    path('user_cat_list/', user_views.user_cat_list),
    path('add_rating/', user_views.add_rating),
    path('user_about/', user_views.user_about),
    path('user_profile/', user_views.user_profile),
    path('change_password/', user_views.change_password),
    path('change_number/', user_views.change_number),
    path('chat/', user_views.chat),

    #-------------------------Advocate-----------------------------------#
    path('adv_header_footer/', adv_views.adv_header_footer),
    path('adv_home/', adv_views.adv_home),
    path('adv_ipc/', adv_views.adv_ipc),
    path('adv_list/', adv_views.adv_list),
    path('adv_view_adv/', adv_views.adv_view_adv),
    path('adv_case_request/', adv_views.adv_case_request),
    path('view_case_request/', adv_views.view_case_request),
    path('status/', adv_views.status),
    path('status1/', adv_views.status1),
    path('case_ipc/', adv_views.case_ipc),
    path('add_fee/', adv_views.add_fee),
    path('adv_feedback/', adv_views.adv_feedback),
    path('adv_case_status/', adv_views.adv_case_status),
    path('view_case_status/', adv_views.view_case_status),
    path('add_doc/', adv_views.add_doc),
    path('rej_com_case/', adv_views.rej_com_case),
    path('adv_cat_list/', adv_views.adv_cat_list),
    path('advocate_profile/', adv_views.advocate_profile),
    path('adv_change_password/', adv_views.adv_change_password),
    


]
