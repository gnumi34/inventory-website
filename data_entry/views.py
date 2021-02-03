import requests
from django.core.cache import cache
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, UpdateView, DeleteView
from django.db.models.query_utils import Q
from django.utils import timezone
from django.urls import reverse_lazy
from .forms import *
from .models import *

# Place basic function here
def get_idr_conversion_value(kurs):
    if kurs == '$':
        response = requests.get('https://api.exchangeratesapi.io/latest', params={'base': 'USD'})
        rates = response.json()['rates']
        return rates['IDR']
    else:
        response = requests.get('https://api.exchangeratesapi.io/latest', params={'base': 'EUR'})
        rates = response.json()['rates']
        return rates['IDR']

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
                inverter.idr_value = round(cache.get_or_set('kurs_usd', get_idr_conversion_value('$'), 3600) * inverter.value, 2)
            else:
                inverter.idr_value = round(cache.get_or_set('kurs_eur', get_idr_conversion_value('E'), 3600) * inverter.value, 2)
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
                scc.idr_value = round(cache.get_or_set('kurs_usd', get_idr_conversion_value('$'), 3600) * scc.value, 2)
            else:
                scc.idr_value = round(cache.get_or_set('kurs_eur', get_idr_conversion_value('E'), 3600) * scc.value, 2)
            scc.save()
            return redirect('solarcc')
    else:
        form = SCCForm()
    return render(request, 'input_scc.html', {'form': form})

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
                battery.idr_value = round(cache.get_or_set('kurs_usd', get_idr_conversion_value('$'), 3600) * battery.value, 2)
            else:
                battery.idr_value = round(cache.get_or_set('kurs_eur', get_idr_conversion_value('E'), 3600) * battery.value, 2)
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
                all_in_one.idr_value = round(cache.get_or_set('kurs_usd', get_idr_conversion_value('$'), 3600) * all_in_one.value, 2)
            else:
                all_in_one.idr_value = round(cache.get_or_set('kurs_eur', get_idr_conversion_value('E'), 3600) * all_in_one.value, 2)
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
    return render(request, 'input_mounting.html', {'form': form})


@method_decorator(decorator=login_required, name='dispatch')
class InverterListView(ListView):
    model = Inverter
    context_object_name = 'objects'
    template_name = "review_inverter.html"

    def get_queryset(self):
        merk_query = self.request.GET.get('merk')
        application_query = self.request.GET.get('application')
        phase_query = self.request.GET.get('phase')
        search_query = self.request.GET.get('search')
        if search_query or merk_query or application_query or phase_query:
            if search_query.isnumeric():
                queryset = self.model.objects.filter(
                    (Q(merk__icontains=search_query) | Q(aplikasi__icontains=search_query)
                    | Q(tipe__icontains=search_query) | Q(jenis__icontains=search_query) |
                    Q(kva=float(search_query))) & Q(merk__icontains=merk_query) & 
                    Q(aplikasi__icontains=application_query) & Q(phase__icontains=phase_query)
                )
            else:
                queryset = self.model.objects.filter(
                    (Q(merk__icontains=search_query) | Q(aplikasi__icontains=search_query)
                    | Q(tipe__icontains=search_query) | Q(jenis__icontains=search_query)) &
                    Q(merk__icontains=merk_query) & Q(aplikasi__icontains=application_query)
                    & Q(phase__icontains=phase_query)
                )
            return queryset
        else:
            queryset = self.model.objects.all()
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = InverterSearchForm(initial={
            'merk': self.request.GET.get('merk', ''),
            'phase': self.request.GET.get('phase', ''),
            'application': self.request.GET.get('application', ''),
            'search': self.request.GET.get('search', '')
        })
        return context


@method_decorator(decorator=login_required, name='dispatch')
class InverterEdit(UpdateView):
    model = Inverter
    form_class = InverterForm
    context_object_name = 'object'
    template_name = 'edit_inverter.html'
    success_url = reverse_lazy('review_inverter')

    def form_valid(self, form):
        messages.success(self.request, 'Item Succesfully Edited!')
        inverter = form.save(commit=False)
        inverter.updated_at = timezone.now()
        inverter.updated_by = self.request.user
        if inverter.kurs == '$':
            inverter.idr_value = round(cache.get_or_set('kurs_usd', get_idr_conversion_value('$'), 3600) * inverter.value, 2)
        else:
            inverter.idr_value = round(cache.get_or_set('kurs_eur', get_idr_conversion_value('E'), 3600) * inverter.value, 2)
        inverter.save()
        return redirect('review_inverter')
    

@method_decorator(decorator=login_required, name='dispatch')
class InverterDelete(DeleteView):
    model = Inverter
    template_name = 'delete_inverter.html'
    success_url = reverse_lazy('review_inverter')
    success_message = "Item Deleted Successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(InverterDelete, self).delete(request, *args, **kwargs)


@method_decorator(decorator=login_required, name='dispatch')
class InverterHistory(ListView):
    model = Inverter
    context_object_name = 'inverter'
    template_name = "history_inverter.html"

    def get_queryset(self):
        queryset = self.model.objects.get(pk=self.kwargs.get('pk'))
        return queryset


@method_decorator(decorator=login_required, name='dispatch')
class MonitoringListView(ListView):
    model = Monitoring
    context_object_name = 'objects'
    template_name = "review_monitoring.html"

    def get_queryset(self):
        merk_query = self.request.GET.get('merk')
        search_query = self.request.GET.get('search')
        if search_query or merk_query:
            queryset = self.model.objects.filter(
                (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                | Q(tipe__icontains=search_query)) & Q(merk__icontains=merk_query)
            )
            return queryset
        else:
            queryset = self.model.objects.all()
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MonitoringSearchForm(initial={
            'merk': self.request.GET.get('merk', ''),
            'search': self.request.GET.get('search', '')
        })
        return context


@method_decorator(decorator=login_required, name='dispatch')
class MonitoringEdit(UpdateView):
    model = Monitoring
    form_class = MonitoringForm
    context_object_name = 'object'
    template_name = 'edit_monitoring.html'
    success_url = reverse_lazy('review_monitoring')

    def form_valid(self, form):
        messages.success(self.request, 'Item Succesfully Edited!')
        monitoring = form.save(commit=False)
        monitoring.updated_at = timezone.now()
        monitoring.updated_by = self.request.user
        monitoring.save()
        return redirect('review_monitoring')


@method_decorator(decorator=login_required, name='dispatch')
class MonitoringDelete(DeleteView):
    model = Monitoring
    template_name = 'delete_monitoring.html'
    success_url = reverse_lazy('review_monitoring')
    success_message = "Item Deleted Successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MonitoringDelete, self).delete(request, *args, **kwargs)


@method_decorator(decorator=login_required, name='dispatch')
class WeatherStationListView(ListView):
    model = WeatherStation
    context_object_name = 'objects'
    template_name = "review_weather.html"

    def get_queryset(self):
        merk_query = self.request.GET.get('merk')
        search_query = self.request.GET.get('search')
        if search_query or merk_query:
            queryset = self.model.objects.filter(
                (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                | Q(tipe__icontains=search_query)) & Q(merk__icontains=merk_query)
            )
            return queryset
        else:
            queryset = self.model.objects.all()
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = WSSearchForm(initial={
            'merk': self.request.GET.get('merk', ''),
            'search': self.request.GET.get('search', '')
        })
        return context


@method_decorator(decorator=login_required, name='dispatch')
class WeatherStationEdit(UpdateView):
    model = WeatherStation
    form_class = WSForm
    context_object_name = 'object'
    template_name = 'edit_weather.html'
    success_url = reverse_lazy('review_weather_station')

    def form_valid(self, form):
        messages.success(self.request, 'Item Succesfully Edited!')
        wss = form.save(commit=False)
        wss.updated_at = timezone.now()
        wss.updated_by = self.request.user
        wss.save()
        return redirect('review_weather_station')


@method_decorator(decorator=login_required, name='dispatch')
class WeatherStationDelete(DeleteView):
    model = WeatherStation
    template_name = 'delete_weather.html'
    success_url = reverse_lazy('review_weather_station')
    success_message = "Item Deleted Successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(WeatherStationDelete, self).delete(request, *args, **kwargs)


@method_decorator(decorator=login_required, name='dispatch')
class SensorListView(ListView):
    model = Sensor
    context_object_name = 'objects'
    template_name = "review_sensor.html"

    def get_queryset(self):
        merk_query = self.request.GET.get('merk')
        search_query = self.request.GET.get('search')
        if search_query or merk_query:
            queryset = self.model.objects.filter(
                (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                | Q(tipe__icontains=search_query)) & Q(merk__icontains=merk_query)
            )
            return queryset
        else:
            queryset = self.model.objects.all()
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SensorSearchForm(initial={
            'merk': self.request.GET.get('merk', ''),
            'search': self.request.GET.get('search', '')
        })
        return context


@method_decorator(decorator=login_required, name='dispatch')
class SensorEdit(UpdateView):
    model = Sensor
    form_class = SensorForm
    context_object_name = 'object'
    template_name = 'edit_sensor.html'
    success_url = reverse_lazy('review_sensor')

    def form_valid(self, form):
        messages.success(self.request, 'Item Succesfully Edited!')
        sensor = form.save(commit=False)
        sensor.updated_at = timezone.now()
        sensor.updated_by = self.request.user
        sensor.save()
        return redirect('review_sensor')


@method_decorator(decorator=login_required, name='dispatch')
class SensorDelete(DeleteView):
    model = Sensor
    template_name = 'delete_sensor.html'
    success_url = reverse_lazy('review_sensor')
    success_message = "Item Deleted Successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(SensorDelete, self).delete(request, *args, **kwargs)


@method_decorator(decorator=login_required, name='dispatch')
class SolarCCListView(ListView):
    model = SolarCC
    context_object_name = 'objects'
    template_name = "review_solarcc.html"

    def get_queryset(self):
        merk_query = self.request.GET.get('merk')
        search_query = self.request.GET.get('search')
        if search_query or merk_query:
            queryset = self.model.objects.filter(
                (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                | Q(tipe__icontains=search_query)) & Q(merk__icontains=merk_query)
            )
            return queryset
        else:
            queryset = self.model.objects.all()
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SolarCCSearchForm(initial={
            'merk': self.request.GET.get('merk', ''),
            'search': self.request.GET.get('search', '')
        })
        return context


@method_decorator(decorator=login_required, name='dispatch')
class SolarCCEdit(UpdateView):
    model = SolarCC
    form_class = SCCForm
    context_object_name = 'object'
    template_name = 'edit_solarcc.html'
    success_url = reverse_lazy('review_solarcc')

    def form_valid(self, form):
        messages.success(self.request, 'Item Succesfully Edited!')
        scc = form.save(commit=False)
        scc.updated_at = timezone.now()
        scc.updated_by = self.request.user
        if scc.kurs == '$':
            scc.idr_value = round(cache.get_or_set('kurs_usd', get_idr_conversion_value('$'), 3600) * scc.value, 2)
        else:
            scc.idr_value = round(cache.get_or_set('kurs_eur', get_idr_conversion_value('E'), 3600) * scc.value, 2)
        scc.save()
        return redirect('review_solarcc')


@method_decorator(decorator=login_required, name='dispatch')
class SolarCCDelete(DeleteView):
    model = SolarCC
    template_name = 'delete_solarcc.html'
    success_url = reverse_lazy('review_solarcc')
    success_message = "Item Deleted Successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(SolarCCDelete, self).delete(request, *args, **kwargs)


@method_decorator(decorator=login_required, name='dispatch')
class PVModuleListView(ListView):
    model = PVModule
    context_object_name = 'objects'
    template_name = "review_pv_module.html"

    def get_queryset(self):
        merk_query = self.request.GET.get('merk')
        search_query = self.request.GET.get('search')
        kw_value_query = self.request.GET.get('kw_value')
        if search_query or merk_query or kw_value_query:
            if search_query.isnumeric():
                if kw_value_query == '':
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query) | Q(kw_value=float(search_query))) 
                        & Q(merk__icontains=merk_query) & Q(kw_value=float(kw_value_query))
                    )
                else:
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query) | Q(kw_value=float(search_query))) 
                        & Q(merk__icontains=merk_query)
                    )
            else:
                if kw_value_query == '':
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query)) & Q(merk__icontains=merk_query)
                    )
                else:
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query)) & Q(merk__icontains=merk_query)
                        & Q(kw_value=float(kw_value_query))
                    )
            return queryset
        else:
            queryset = self.model.objects.all()
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PVModuleSearchForm(initial={
            'merk': self.request.GET.get('merk', ''),
            'kw_value': self.request.GET.get('kw_value', ''),
            'search': self.request.GET.get('search', '')
        })
        return context


@method_decorator(decorator=login_required, name='dispatch')
class PVModuleEdit(UpdateView):
    model = PVModule
    form_class = PVModuleForm
    context_object_name = 'object'
    template_name = 'edit_pv_module.html'
    success_url = reverse_lazy('review_pv_module')

    def form_valid(self, form):
        messages.success(self.request, 'Item Succesfully Edited!')
        pv_module = form.save(commit=False)
        pv_module.updated_at = timezone.now()
        pv_module.updated_by = self.request.user
        pv_module.save()
        return redirect('review_pv_module')


@method_decorator(decorator=login_required, name='dispatch')
class PVModuleDelete(DeleteView):
    model = PVModule
    template_name = 'delete_pv_module.html'
    success_url = reverse_lazy('review_pv_module')
    success_message = "Item Deleted Successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PVModuleDelete, self).delete(request, *args, **kwargs)


@method_decorator(decorator=login_required, name='dispatch')
class BatteryListView(ListView):
    model = Battery
    context_object_name = 'objects'
    template_name = "review_battery.html"

    def get_queryset(self):
        merk_query = self.request.GET.get('merk')
        search_query = self.request.GET.get('search')
        v_per_cell_query = self.request.GET.get('v_per_cell')
        tipe_query = self.request.GET.get('tipe')
        if search_query or merk_query or v_per_cell_query or tipe_query:
            if search_query.isnumeric():
                if v_per_cell_query == '':
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query) | Q(keterangan__icontains=search_query)
                        | Q(capacity=float(search_query))) & Q(merk__icontains=merk_query)
                        & Q(tipe__icontains=tipe_query)
                    )
                else:
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query) | Q(keterangan__icontains=search_query)
                        | Q(capacity=float(search_query))) & Q(merk__icontains=merk_query)
                        & Q(v_per_cell=float(v_per_cell_query)) & Q(tipe__icontains=tipe_query)
                    )
            else:
                if v_per_cell_query == '':
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query) | Q(keterangan__icontains=search_query)) 
                        & Q(merk__icontains=merk_query) & Q(tipe__icontains=tipe_query)
                    )
                else:
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query) | Q(keterangan__icontains=search_query)) 
                        & Q(merk__icontains=merk_query) & Q(v_per_cell=float(v_per_cell_query)) 
                        & Q(tipe__icontains=tipe_query)
                    )
            return queryset
        else:
            queryset = self.model.objects.all()
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BatterySearchForm(initial={
            'merk': self.request.GET.get('merk', ''),
            'v_per_cell': self.request.GET.get('v_per_cell', ''),
            'tipe': self.request.GET.get('tipe', ''),
            'search': self.request.GET.get('search', '')
        })
        return context


@method_decorator(decorator=login_required, name='dispatch')
class BatteryEdit(UpdateView):
    model = Battery
    form_class = BatteryForm
    context_object_name = 'object'
    template_name = 'edit_battery.html'
    success_url = reverse_lazy('review_battery')

    def form_valid(self, form):
        messages.success(self.request, 'Item Succesfully Edited!')
        battery = form.save(commit=False)
        battery.updated_at = timezone.now()
        battery.updated_by = self.request.user
        if battery.kurs == '$':
            battery.idr_value = round(cache.get_or_set('kurs_usd', get_idr_conversion_value('$'), 3600) * battery.value, 2)
        else:
            battery.idr_value = round(cache.get_or_set('kurs_eur', get_idr_conversion_value('E'), 3600) * battery.value, 2)
        battery.save()
        return redirect('review_battery')


@method_decorator(decorator=login_required, name='dispatch')
class BatteryDelete(DeleteView):
    model = Battery
    template_name = 'delete_battery.html'
    success_url = reverse_lazy('review_battery')
    success_message = "Item Deleted Successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BatteryDelete, self).delete(request, *args, **kwargs)


@method_decorator(decorator=login_required, name='dispatch')
class LVPanelListView(ListView):
    model = LVPanel
    context_object_name = 'objects'
    template_name = "review_lv_panel.html"

    def get_queryset(self):
        merk_query = self.request.GET.get('merk')
        search_query = self.request.GET.get('search')
        if search_query or merk_query:
            queryset = self.model.objects.filter(
                (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                | Q(tipe__icontains=search_query)) & Q(merk__icontains=merk_query)
            )
            return queryset
        else:
            queryset = self.model.objects.all()
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LVPanelSearchForm(initial={
            'merk': self.request.GET.get('merk', ''),
            'search': self.request.GET.get('search', '')
        })
        return context


@method_decorator(decorator=login_required, name='dispatch')
class LVPanelEdit(UpdateView):
    model = LVPanel
    form_class = LVPanelForm
    context_object_name = 'object'
    template_name = 'edit_lv_panel.html'
    success_url = reverse_lazy('review_lv_panel')

    def form_valid(self, form):
        messages.success(self.request, 'Item Succesfully Edited!')
        lv_panel = form.save(commit=False)
        lv_panel.updated_at = timezone.now()
        lv_panel.updated_by = self.request.user
        lv_panel.save()
        return redirect('review_lv_panel')


@method_decorator(decorator=login_required, name='dispatch')
class LVPanelDelete(DeleteView):
    model = LVPanel
    template_name = 'delete_lv_panel.html'
    success_url = reverse_lazy('review_lv_panel')
    success_message = "Item Deleted Successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(LVPanelDelete, self).delete(request, *args, **kwargs)


@method_decorator(decorator=login_required, name='dispatch')
class MVPanelListView(ListView):
    model = MVPanel
    context_object_name = 'objects'
    template_name = "review_mv_panel.html"

    def get_queryset(self):
        merk_query = self.request.GET.get('merk')
        search_query = self.request.GET.get('search')
        if search_query or merk_query:
            queryset = self.model.objects.filter(
                (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                | Q(tipe__icontains=search_query)) & Q(merk__icontains=merk_query)
            )
            return queryset
        else:
            queryset = self.model.objects.all()
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MVPanelSearchForm(initial={
            'merk': self.request.GET.get('merk', ''),
            'search': self.request.GET.get('search', '')
        })
        return context


@method_decorator(decorator=login_required, name='dispatch')
class MVPanelEdit(UpdateView):
    model = MVPanel
    form_class = MVPanelForm
    context_object_name = 'object'
    template_name = 'edit_mv_panel.html'
    success_url = reverse_lazy('review_mv_panel')

    def form_valid(self, form):
        messages.success(self.request, 'Item Succesfully Edited!')
        mv_panel = form.save(commit=False)
        mv_panel.updated_at = timezone.now()
        mv_panel.updated_by = self.request.user
        mv_panel.save()
        return redirect('review_mv_panel')


@method_decorator(decorator=login_required, name='dispatch')
class MVPanelDelete(DeleteView):
    model = Inverter
    template_name = 'delete_mv_panel.html'
    success_url = reverse_lazy('review_mv_panel')
    success_message = "Item Deleted Successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MVPanelDelete, self).delete(request, *args, **kwargs)


@method_decorator(decorator=login_required, name='dispatch')
class TrafoListView(ListView):
    model = Trafo
    context_object_name = 'objects'
    template_name = "review_trafo.html"

    def get_queryset(self):
        merk_query = self.request.GET.get('merk')
        search_query = self.request.GET.get('search')
        year_query = self.request.GET.get('year')
        kva_value_query = self.request.GET.get('kva_value')
        if search_query or merk_query or year_query or kva_value_query:
            if search_query.isnumeric():
                if kva_value_query == '':
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query) | Q(kva_value=float(search_query)))
                        & Q(merk__icontains=merk_query) & Q(year__icontains=year_query)
                    )
                else:
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query) | Q(kva_value=float(search_query))) 
                        & Q(merk__icontains=merk_query) & Q(year__icontains=year_query) 
                        & Q(kva_value=float(kva_value_query))
                    )
            else:
                if kva_value_query == '':
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query)) & Q(merk__icontains=merk_query)
                        & Q(year__icontains=year_query)
                    )
                else:
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query)) & Q(merk__icontains=merk_query)
                        & Q(year__icontains=year_query) & Q(kva_value=float(kva_value_query))
                    )
            return queryset
        else:
            queryset = self.model.objects.all()
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TrafoSearchForm(initial={
            'merk': self.request.GET.get('merk', ''),
            'kva_value': self.request.GET.get('kva_value', ''),
            'year': self.request.GET.get('year', ''),
            'search': self.request.GET.get('search', '')
        })
        return context


@method_decorator(decorator=login_required, name='dispatch')
class TrafoEdit(UpdateView):
    model = Trafo
    form_class = TrafoForm
    context_object_name = 'object'
    template_name = 'edit_trafo.html'
    success_url = reverse_lazy('review_trafo')

    def form_valid(self, form):
        messages.success(self.request, 'Item Succesfully Edited!')
        trafo = form.save(commit=False)
        trafo.updated_at = timezone.now()
        trafo.updated_by = self.request.user
        trafo.save()
        return redirect('review_trafo')


@method_decorator(decorator=login_required, name='dispatch')
class TrafoDelete(DeleteView):
    model = Trafo
    template_name = 'delete_trafo.html'
    success_url = reverse_lazy('review_trafo')
    success_message = "Item Deleted Successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(TrafoDelete, self).delete(request, *args, **kwargs)


@method_decorator(decorator=login_required, name='dispatch')
class AIOListView(ListView):
    model = AllInOne
    context_object_name = 'objects'
    template_name = "review_aio.html"

    def get_queryset(self):
        merk_query = self.request.GET.get('merk')
        phase_query = self.request.GET.get('phase')
        kva_value_query = self.request.GET.get('kva_value')
        search_query = self.request.GET.get('search')
        if search_query or merk_query or phase_query or kva_value_query:
            if search_query.isnumeric():
                if kva_value_query == '':
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query) | Q(kva=float(search_query))
                        | Q(phase__icontains=search_query)) & Q(merk__icontains=merk_query)
                        & Q(phase__icontains=phase_query)
                    )
                else:
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query) | Q(kva=float(search_query))
                        | Q(phase__icontains=search_query)) & Q(merk__icontains=merk_query)
                        & Q(phase__icontains=phase_query) & Q(kva_value=float(kva_value_query))
                    )
            else:
                if kva_value_query == '':
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query) | Q(phase__icontains=search_query)) 
                        & Q(merk__icontains=merk_query) & Q(phase__icontains=phase_query) 
                    )
                else:
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query) | Q(phase__icontains=search_query)) 
                        & Q(merk__icontains=merk_query) & Q(phase__icontains=phase_query)
                        & Q(kva=float(kva_value_query))
                    )
            return queryset
        else:
            queryset = self.model.objects.all()
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AIOSearchForm(initial={
            'merk': self.request.GET.get('merk', ''),
            'kva_value': self.request.GET.get('kva_value', ''),
            'phase': self.request.GET.get('phase', ''),
            'search': self.request.GET.get('search', '')
        })
        return context


@method_decorator(decorator=login_required, name='dispatch')
class AIOEdit(UpdateView):
    model = AllInOne
    form_class = AIOForm
    context_object_name = 'object'
    template_name = 'edit_aio.html'
    success_url = reverse_lazy('review_all_in_one')

    def form_valid(self, form):
        messages.success(self.request, 'Item Succesfully Edited!')
        aio = form.save(commit=False)
        aio.updated_at = timezone.now()
        aio.updated_by = self.request.user
        if aio.kurs == '$':
            aio.idr_value = round(cache.get_or_set('kurs_usd', get_idr_conversion_value('$'), 3600) * aio.value, 2)
        else:
            aio.idr_value = round(cache.get_or_set('kurs_eur', get_idr_conversion_value('E'), 3600) * aio.value, 2)
        aio.save()
        return redirect('review_all_in_one')


@method_decorator(decorator=login_required, name='dispatch')
class AIODelete(DeleteView):
    model = AllInOne
    template_name = 'delete_aio.html'
    success_url = reverse_lazy('review_aio')
    success_message = "Item Deleted Successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(AIODelete, self).delete(request, *args, **kwargs)


@method_decorator(decorator=login_required, name='dispatch')
class MountingListView(ListView):
    model = Mounting
    context_object_name = 'objects'
    template_name = "review_mounting.html"

    def get_queryset(self):
        merk_query = self.request.GET.get('merk')
        search_query = self.request.GET.get('search')
        kw_value_query = self.request.GET.get('kw_value')
        if search_query or merk_query or kw_value_query:
            if search_query.isnumeric():
                if kw_value_query == '':
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query) | Q(kw_value=float(search_query))) 
                        & Q(merk__icontains=merk_query)
                    )
                else:
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query) | Q(kw_value=float(search_query))) 
                        & Q(merk__icontains=merk_query) & Q(kw_value=float(kw_value_query))
                    )
            else:
                if kw_value_query == '':
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query)) & Q(merk__icontains=merk_query)
                    )
                else:
                    queryset = self.model.objects.filter(
                        (Q(merk__icontains=search_query) | Q(item__icontains=search_query)
                        | Q(tipe__icontains=search_query)) & Q(merk__icontains=merk_query)
                        & Q(kw_value=float(kw_value_query))
                    )
            return queryset
        else:
            queryset = self.model.objects.all()
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MountingSearchForm(initial={
            'merk': self.request.GET.get('merk', ''),
            'kw_value': self.request.GET.get('kw_value', ''),
            'search': self.request.GET.get('search', '')
        })
        return context


@method_decorator(decorator=login_required, name='dispatch')
class MountingEdit(UpdateView):
    model = Mounting
    form_class = MountingForm
    context_object_name = 'object'
    template_name = 'edit_mounting.html'
    success_url = reverse_lazy('review_mounting')

    def form_valid(self, form):
        messages.success(self.request, 'Item Succesfully Edited!')
        mounting = form.save(commit=False)
        mounting.updated_at = timezone.now()
        mounting.updated_by = self.request.user
        mounting.save()
        return redirect('review_mounting')


@method_decorator(decorator=login_required, name='dispatch')
class MountingDelete(DeleteView):
    model = Mounting
    template_name = 'delete_mounting.html'
    success_url = reverse_lazy('review_mounting')
    success_message = "Item Deleted Successfully!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MountingDelete, self).delete(request, *args, **kwargs)

