"""inventory_entry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from data_entry import views
from accounts import views as accounts_views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('input/', views.input_page, name='input'),
    path('input/inverter/', views.input_inverter, name='inverter'),
    path('input/monitoring/', views.input_monitoring, name='monitoring'),
    path('input/weather_station/', views.input_weather_station, name='weather_station'),
    path('input/sensor/', views.input_sensor, name='sensor'),
    path('input/solarcc/', views.input_solarcc, name='solarcc'),
    path('input/pv_module/', views.input_pv_module, name='pv_module'),
    path('input/battery/', views.input_battery, name='battery'),
    path('input/lv_panel/', views.input_lv_panel, name='lv_panel'),
    path('input/mv_panel/', views.input_mv_panel, name='mv_panel'),
    path('input/trafo/', views.input_trafo, name='trafo'),
    path('input/all_in_one/', views.input_aio, name='all_in_one'),
    path('input/mounting/', views.input_mounting, name='mounting'),
    path('review/', views.review_page, name='review'),
    path('review/inverter/', views.InverterListView.as_view(), name='review_inverter'),
    path('review/inverter/<int:pk>/', views.InverterEdit.as_view(), name='edit_inverter'),
    path('review/inverter/<int:pk>/delete/', views.InverterDelete.as_view(), name='delete_inverter'),
    path('review/inverter/<int:pk>/history/', views.InverterHistory.as_view(), name='history_inverter'),
    path('review/monitoring/', views.review_monitoring, name='review_monitoring'),
    path('review/weather_station/', views.review_weather_station, name='review_weather_station'),
    path('review/sensor/', views.review_sensor, name='review_sensor'),
    path('review/solarcc/', views.review_solarcc, name='review_solarcc'),
    path('review/pv_module/', views.review_pv_module, name='review_pv_module'),
    path('review/battery/', views.review_battery, name='review_battery'),
    path('review/lv_panel/', views.review_lv_panel, name='review_lv_panel'),
    path('review/mv_panel/', views.review_mv_panel, name='review_mv_panel'),
    path('review/trafo/', views.review_trafo, name='review_trafo'),
    path('review/all_in_one/', views.review_aio, name='review_all_in_one'),
    path('review/mounting/', views.review_mounting, name='review_mounting'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', accounts_views.signup, name='signup'),
    re_path(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
    re_path(r'^reset/$', auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ),
        name='password_reset'
    ),
    re_path(r'^reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'
    ),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'
    ),
    re_path(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'
    ),
    re_path(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'
    ),
    re_path(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name="password_change_done.html"),
        name='password_change_done'
    ),
]
