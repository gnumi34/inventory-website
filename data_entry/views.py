import requests
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from .models import *
from django.views.generic import ListView

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def input_page(request):
    return render(request, 'input.html')

@login_required
def review_page(request):
    return render(request, 'review.html')

@login_required
def input_inverter(request):
    if request.method == 'POST':
        form = InverterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Item Submission Successful!')
            inverter = form.save(commit=False)
            inverter.entry_by = request.user
            if inverter.kurs == '$':
                response = requests.get('https://api.exchangeratesapi.io/latest', params={'base': 'USD'})
                rates = response.json()['rates']
                inverter.idr_value = rates['IDR'] * inverter.value
            else:
                response = requests.get('https://api.exchangeratesapi.io/latest', params={'base': 'EUR'})
                rates = response.json()['rates']
                inverter.idr_value = rates['IDR'] * inverter.value
            inverter.save()
            return redirect('inverter')
    else:
        form = InverterForm()
    return render(request, 'input_inverter.html', {'form': form})

@login_required
def input_monitoring(request):
    if request.method == 'POST':
        form = MonitoringForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Item Submission Successful!')
            monitoring = form.save(commit=False)
            monitoring.entry_by = request.user
            monitoring.save()
            return redirect('monitoring')
    else:
        form = MonitoringForm()
    return render(request, 'input_monitoring.html', {'form': form})

@login_required
def input_weather_station(request):
    if request.method == 'POST':
        form = WSForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Item Submission Successful!')
            weather_station = form.save(commit=False)
            weather_station.entry_by = request.user
            weather_station.save()
            return redirect('weather_station')
    else:
        form = WSForm()
    return render(request, 'input_weather.html', {'form': form})

@login_required
def input_sensor(request):
    if request.method == 'POST':
        form = SensorForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Item Submission Successful!')
            sensor = form.save(commit=False)
            sensor.entry_by = request.user
            sensor.save()
            return redirect('sensor')
    else:
        form = SensorForm()
    return render(request, 'input_sensor.html', {'form': form})

@login_required
def input_solarcc(request):
    if request.method == 'POST':
        form = SCCForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Item Submission Successful!')
            scc = form.save(commit=False)
            scc.entry_by = request.user
            if scc.kurs == '$':
                response = requests.get('https://api.exchangeratesapi.io/latest', params={'base': 'USD'})
                rates = response.json()['rates']
                scc.idr_value = rates['IDR'] * scc.value
            else:
                response = requests.get('https://api.exchangeratesapi.io/latest', params={'base': 'EUR'})
                rates = response.json()['rates']
                scc.idr_value = rates['IDR'] * scc.value
            scc.save()
            return redirect('solarcc')
    else:
        form = SCCForm()
    return render(request, 'input_inverter.html', {'form': form})

@login_required
def input_pv_module(request):
    if request.method == 'POST':
        form = PVModuleForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Item Submission Successful!')
            pv_module = form.save(commit=False)
            pv_module.entry_by = request.user
            pv_module.save()
            return redirect('pv_module')
    else:
        form = PVModuleForm()
    return render(request, 'input_pv_module.html', {'form': form})

@login_required
def input_battery(request):
    if request.method == 'POST':
        form = BatteryForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Item Submission Successful!')
            battery = form.save(commit=False)
            battery.entry_by = request.user
            if battery.kurs == '$':
                response = requests.get('https://api.exchangeratesapi.io/latest', params={'base': 'USD'})
                rates = response.json()['rates']
                battery.idr_value = rates['IDR'] * battery.value
            else:
                response = requests.get('https://api.exchangeratesapi.io/latest', params={'base': 'EUR'})
                rates = response.json()['rates']
                battery.idr_value = rates['IDR'] * battery.value
            battery.save()
            return redirect('battery')
    else:
        form = BatteryForm()
    return render(request, 'input_battery.html', {'form': form})

@login_required
def input_lv_panel(request):
    if request.method == 'POST':
        form = LVPanelForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Item Submission Successful!')
            lv_panel = form.save(commit=False)
            lv_panel.entry_by = request.user
            lv_panel.save()
            return redirect('lv_panel')
    else:
        form = LVPanelForm()
    return render(request, 'input_lv_panel.html', {'form': form})

@login_required
def input_mv_panel(request):
    if request.method == 'POST':
        form = MVPanelForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Item Submission Successful!')
            mv_panel = form.save(commit=False)
            mv_panel.entry_by = request.user
            mv_panel.save()
            return redirect('mv_panel')
    else:
        form = MVPanelForm()
    return render(request, 'input_mv_panel.html', {'form': form})

@login_required
def input_trafo(request):
    if request.method == 'POST':
        form = TrafoForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Item Submission Successful!')
            trafo = form.save(commit=False)
            trafo.entry_by = request.user
            trafo.save()
            return redirect('trafo')
    else:
        form = TrafoForm()
    return render(request, 'input_trafo.html', {'form': form})

@login_required
def input_aio(request):
    if request.method == 'POST':
        form = AIOForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Item Submission Successful!')
            all_in_one = form.save(commit=False)
            all_in_one.entry_by = request.user
            if all_in_one.kurs == '$':
                response = requests.get('https://api.exchangeratesapi.io/latest', params={'base': 'USD'})
                rates = response.json()['rates']
                all_in_one.idr_value = rates['IDR'] * all_in_one.value
            else:
                response = requests.get('https://api.exchangeratesapi.io/latest', params={'base': 'EUR'})
                rates = response.json()['rates']
                all_in_one.idr_value = rates['IDR'] * all_in_one.value
            all_in_one.save()
            return redirect('all_in_one')
    else:
        form = AIOForm()
    return render(request, 'input_aio.html', {'form': form})

@login_required
def input_mounting(request):
    if request.method == 'POST':
        form = MountingForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Item Submission Successful!')
            mounting = form.save(commit=False)
            mounting.entry_by = request.user
            mounting.save()
            return redirect('mounting')
    else:
        form = MountingForm()
    return render(request, 'input_mv_panel.html', {'form': form})

@method_decorator(decorator=login_required, name='dispatch')
class InverterListView(ListView):
    model = Inverter
    template_name = "review_inverter.html"

@login_required
def review_monitoring(request):
    return render(request, 'review_monitoring.html')

@login_required
def review_weather_station(request):
    return render(request, 'review_wss.html')

@login_required
def review_sensor(request):
    return render(request, 'review_sensor.html')

@login_required
def review_solarcc(request):
    return render(request, 'review_solarcc.html')

@login_required
def review_pv_module(request):
    return render(request, 'review_pv_module.html')

@login_required
def review_battery(request):
    return render(request, 'review_battery.html')

@login_required
def review_lv_panel(request):
    return render(request, 'review_lv_panel.html')

@login_required
def review_mv_panel(request):
    return render(request, 'review_mv_panel.html')

@login_required
def review_trafo(request):
    return render(request, 'review_trafo.html')

@login_required
def review_aio(request):
    return render(request, 'review_aio.html')

@login_required
def review_mounting(request):
    return render(request, 'review_mounting.html')