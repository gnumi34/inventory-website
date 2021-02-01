from django import forms
from django.db.utils import OperationalError
from . import models

class InverterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InverterForm, self).__init__(*args, **kwargs)
        self.fields['merk'].label = 'Brand'
        self.fields['tipe'].label = 'Model Name'
        self.fields['jenis'].label = 'Type'
        self.fields['aplikasi'].label = 'Application'
        self.fields['kva'].label = 'kVA Value'
        self.fields['value'].label = 'Price'

    class Meta:
        model = models.Inverter
        fields = [
            'merk', 'tipe', 'jenis', 'aplikasi', 'phase',
            'kva', 'kurs', 'value', 'contact', 'period'
        ]


class MonitoringForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MonitoringForm, self).__init__(*args, **kwargs)
        self.fields['merk'].label = 'Brand'
        self.fields['item'].label = 'Model Name'
        self.fields['tipe'].label = 'Type'
        self.fields['usd_value'].label = 'Price in USD'

    class Meta:
        model = models.Monitoring
        fields = [
            'merk', 'item', 'tipe', 'usd_value',
            'contact', 'period'
        ]


class WSForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WSForm, self).__init__(*args, **kwargs)
        self.fields['merk'].label = 'Brand'
        self.fields['item'].label = 'Model Name'
        self.fields['tipe'].label = 'Type'
        self.fields['usd_value'].label = 'Price in USD'

    class Meta:
        model = models.WeatherStation
        fields = [
            'merk', 'item', 'tipe', 'usd_value',
            'contact', 'period'
        ]


class SensorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SensorForm, self).__init__(*args, **kwargs)
        self.fields['merk'].label = 'Brand'
        self.fields['item'].label = 'Model Name'
        self.fields['tipe'].label = 'Type'
        self.fields['usd_value'].label = 'Price in USD'

    class Meta:
        model = models.Sensor
        fields = [
            'merk', 'item', 'tipe', 'usd_value',
            'contact', 'period'
        ]


class SCCForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SCCForm, self).__init__(*args, **kwargs)
        self.fields['merk'].label = 'Brand'
        self.fields['item'].label = 'Model Name'
        self.fields['tipe'].label = 'Type'
        self.fields['vbat'].label = 'Battery Charge Voltage'
        self.fields['amperage'].label = 'Maximum Charge Current'
        self.fields['wattmax'].label = 'Maximum Charge Power'
        self.fields['value'].label = 'Price'

    class Meta:
        model = models.SolarCC
        fields = [
            'merk', 'item', 'tipe', 'vbat',
            'amperage', 'wattmax', 'kurs',
            'value', 'contact', 'period'
        ]


class PVModuleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PVModuleForm, self).__init__(*args, **kwargs)
        self.fields['merk'].label = 'Brand'
        self.fields['item'].label = 'Model Name'
        self.fields['tipe'].label = 'Type'
        self.fields['kw_value'].label = 'Power Capacity'
        self.fields['wp_price'].label = 'Price per Wp'

    class Meta:
        model = models.PVModule
        fields = [
            'merk', 'item', 'tipe', 'kw_value',
            'wp_price', 'contact', 'period'
        ]


class BatteryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BatteryForm, self).__init__(*args, **kwargs)
        self.fields['merk'].label = 'Brand'
        self.fields['item'].label = 'Model Name'
        self.fields['tipe'].label = 'Type'
        self.fields['keterangan'].label = 'Additional Information'
        self.fields['v_per_cell'].label = 'Voltage per Cell'
        self.fields['capacity'].label = 'Battery Capacity'
        self.fields['kwh'].label = 'Battery Power Capacity'
        self.fields['value'].label = 'Price'

    class Meta:
        model = models.Battery
        fields = [
            'merk', 'item', 'tipe', 'keterangan',
            'v_per_cell', 'capacity', 'kwh',
            'kurs', 'value', 'contact', 'period'
        ]


class LVPanelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LVPanelForm, self).__init__(*args, **kwargs)
        self.fields['merk'].label = 'Brand'
        self.fields['item'].label = 'Model Name'
        self.fields['tipe'].label = 'Type'
        self.fields['usd_value'].label = 'Price in USD'

    class Meta:
        model = models.LVPanel
        fields = [
            'merk', 'item', 'tipe', 'usd_value',
            'contact', 'period'
        ]


class MVPanelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MVPanelForm, self).__init__(*args, **kwargs)
        self.fields['merk'].label = 'Brand'
        self.fields['item'].label = 'Model Name'
        self.fields['tipe'].label = 'Type'
        self.fields['usd_value'].label = 'Price in USD'

    class Meta:
        model = models.MVPanel
        fields = [
            'merk', 'item', 'tipe', 'usd_value',
            'contact', 'period'
        ]


class TrafoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrafoForm, self).__init__(*args, **kwargs)
        self.fields['merk'].label = 'Brand'
        self.fields['item'].label = 'Model Name'
        self.fields['tipe'].label = 'Type'
        self.fields['kva_value'].label = 'Transformer Capacity'
        self.fields['usd_value'].label = 'Price in USD'

    class Meta:
        model = models.Trafo
        fields = [
            'merk', 'item', 'tipe', 'kva_value',
            'usd_value', 'year', 'distributor'
        ]


class AIOForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AIOForm, self).__init__(*args, **kwargs)
        self.fields['merk'].label = 'Brand'
        self.fields['item'].label = 'Model Name'
        self.fields['tipe'].label = 'Type'
        self.fields['kva'].label = 'Power Capacity'
        self.fields['value'].label = 'Price'

    class Meta:
        model = models.AllInOne
        fields = [
            'merk', 'item', 'tipe', 'phase',
            'kva', 'kurs', 'value', 'contact',
            'period'
        ]


class MountingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MountingForm, self).__init__(*args, **kwargs)
        self.fields['merk'].label = 'Brand'
        self.fields['item'].label = 'Model Name'
        self.fields['tipe'].label = 'Type'
        self.fields['kw_value'].label = 'Power Capacity'
        self.fields['wp_price'].label = 'Price per Wp'

    class Meta:
        model = models.Mounting
        fields = [
            'merk', 'item', 'tipe', 'kw_value',
            'wp_price', 'contact', 'period'
        ]


class InverterSearchForm(forms.Form):
    all_inverter = models.Inverter.objects.all()
    merk_choices = [
        ('', '-------'),
    ]
    try:
    	for object in all_inverter:
            if (object.merk, object.merk) in merk_choices:
                continue
            else:
            	merk_choices.append((object.merk, object.merk))
    except OperationalError:
    	pass

    PHASE_CHOISES = [
        ('', '-------'),
        ('Single Phase', "Single Phase"),
        ('Triple Phase', "Triple Phase"),
    ]

    APPLICATION_CHOISES = [
        ('', '-------'),
        ('On', 'On-Grid'),
        ('Off', 'Off-Grid')
    ]

    merk = forms.ChoiceField(choices=merk_choices, label='Brand')
    phase = forms.ChoiceField(choices=PHASE_CHOISES, label='Inverter Phases')
    application = forms.ChoiceField(choices=APPLICATION_CHOISES, label='Inverter Application')
    search = forms.CharField(max_length=100, label='Search')