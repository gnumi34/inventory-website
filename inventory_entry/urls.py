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
    path('review/inverter/<int:pk>/edit/', views.InverterEdit.as_view(), name='edit_inverter'),
    path('review/inverter/<int:pk>/delete/', views.InverterDelete.as_view(), name='delete_inverter'),
    path('review/inverter/<int:pk>/history/', views.InverterHistory.as_view(), name='history_inverter'),
    path('review/monitoring/', views.MonitoringListView.as_view(), name='review_monitoring'),
    path('review/monitoring/<int:pk>/edit/', views.MonitoringEdit.as_view(), name='edit_monitoring'),
    path('review/weather_station/', views.WeatherStationListView.as_view(), name='review_weather_station'),
    path('review/weather_station/<int:pk>/edit/', views.WeatherStationEdit.as_view(), name='edit_weather_station'),
    path('review/sensor/', views.SensorListView.as_view(), name='review_sensor'),
    path('review/sensor/<int:pk>/edit/', views.SensorEdit.as_view(), name='edit_sensor'),
    path('review/solarcc/', views.SolarCCListView.as_view(), name='review_solarcc'),
    path('review/solarcc/<int:pk>/edit/', views.SolarCCEdit.as_view(), name='edit_solarcc'),
    path('review/pv_module/', views.PVModuleListView.as_view(), name='review_pv_module'),
    path('review/pv_module/<int:pk>/edit/', views.PVModuleEdit.as_view(), name='edit_pv_module'),
    path('review/battery/', views.BatteryListView.as_view(), name='review_battery'),
    path('review/battery/<int:pk>/edit/', views.BatteryEdit.as_view(), name='edit_battery'),
    path('review/lv_panel/', views.LVPanelListView.as_view(), name='review_lv_panel'),
    path('review/lv_panel/<int:pk>/edit/', views.LVPanelEdit.as_view(), name='edit_lv_panel'),
    path('review/mv_panel/', views.MVPanelListView.as_view(), name='review_mv_panel'),
    path('review/mv_panel/<int:pk>/edit/', views.MVPanelEdit.as_view(), name='edit_mv_panel'),
    path('review/trafo/', views.TrafoListView.as_view(), name='review_trafo'),
    path('review/trafo/<int:pk>/edit/', views.TrafoEdit.as_view(), name='edit_trafo'),
    path('review/all_in_one/', views.AIOListView.as_view(), name='review_all_in_one'),
    path('review/all_in_one/<int:pk>/edit/', views.AIOEdit.as_view(), name='edit_all_in_one'),
    path('review/mounting/', views.MountingListView.as_view(), name='review_mounting'),
    path('review/mounting/<int:pk>/edit/', views.MountingEdit.as_view(), name='edit_mounting'),
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
