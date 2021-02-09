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
        self.fields['usd_value'].label = 'Price in US$'

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
        self.fields['usd_value'].label = 'Price in US$'

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
        self.fields['usd_value'].label = 'Price in US$'

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
            'merk', 'item', 'tipe', 'kw_value', 'kurs',
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
        self.fields['usd_value'].label = 'Price in US$'

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
        self.fields['usd_value'].label = 'Price in US$'

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
        self.fields['price'].label = 'Price in IDR'

    class Meta:
        model = models.Trafo
        fields = [
            'merk', 'item', 'tipe', 'kva_value',
            'price', 'year', 'distributor'
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
        self.fields['kurs'].label = 'Kurs'
        self.fields['wp_price'].label = 'Price per Wp'

    class Meta:
        model = models.Mounting
        fields = [
            'merk', 'item', 'tipe', 'kw_value', 'kurs',
            'wp_price', 'contact', 'period'
        ]


class InverterSearchForm(forms.Form):
    PHASE_CHOISES = [
        ('', '-------'),
        ('Single Phase', "Single Phase"),
        ('Triple Phase', "Triple Phase"),
    ]

    APPLICATION_CHOISES = [
        ('', '-------'),
        ('On', 'On-Grid'),
        ('Off', 'Off-Grid'),
        ('Hybrid', 'Hybrid')
    ]

    merk = forms.ChoiceField(choices=[])
    phase = forms.ChoiceField(choices=PHASE_CHOISES, label='Inverter Phases')
    application = forms.ChoiceField(choices=APPLICATION_CHOISES, label='Inverter Application')
    search = forms.CharField(max_length=100, label='Search')
    
    def __init__(self, *args, **kwargs):
        super(InverterSearchForm, self).__init__(*args, **kwargs)

        all_objects = models.Inverter.objects.all()
        merk_choices = [
            ('', '-------'),
        ]
        try:
            for object in all_objects:
                if (object.merk, object.merk) in merk_choices:
                    continue
                else:
                    merk_choices.append((object.merk, object.merk))
        except OperationalError:
            pass

        self.fields['merk'] = forms.ChoiceField(choices=merk_choices, label='Brand')


class MonitoringSearchForm(forms.Form):
    merk = forms.ChoiceField(choices=[])
    search = forms.CharField(max_length=100, label='Search')

    def __init__(self, *args, **kwargs):
        super(MonitoringSearchForm, self).__init__(*args, **kwargs)

        all_objects = models.Monitoring.objects.all()
        merk_choices = [
            ('', '-------'),
        ]
        try:
            for object in all_objects:
                if (object.merk, object.merk) in merk_choices:
                    continue
                else:
                    merk_choices.append((object.merk, object.merk))
        except OperationalError:
            pass

        self.fields['merk'] = forms.ChoiceField(choices=merk_choices, label='Brand')


class WSSearchForm(forms.Form):
    merk = forms.ChoiceField(choices=[])
    search = forms.CharField(max_length=100, label='Search')

    def __init__(self, *args, **kwargs):
        super(WSSearchForm, self).__init__(*args, **kwargs)

        all_objects = models.WeatherStation.objects.all()
        merk_choices = [
            ('', '-------'),
        ]
        try:
            for object in all_objects:
                if (object.merk, object.merk) in merk_choices:
                    continue
                else:
                    merk_choices.append((object.merk, object.merk))
        except OperationalError:
            pass

        self.fields['merk'] = forms.ChoiceField(choices=merk_choices, label='Brand')


class SensorSearchForm(forms.Form):
    merk = forms.ChoiceField(choices=[])
    search = forms.CharField(max_length=100, label='Search')

    def __init__(self, *args, **kwargs):
        super(SensorSearchForm, self).__init__(*args, **kwargs)

        all_objects = models.Sensor.objects.all()
        merk_choices = [
            ('', '-------'),
        ]
        try:
            for object in all_objects:
                if (object.merk, object.merk) in merk_choices:
                    continue
                else:
                    merk_choices.append((object.merk, object.merk))
        except OperationalError:
            pass

        self.fields['merk'] = forms.ChoiceField(choices=merk_choices, label='Brand')


class SolarCCSearchForm(forms.Form):
    merk = forms.ChoiceField(choices=[])
    search = forms.CharField(max_length=100, label='Search')

    def __init__(self, *args, **kwargs):
        super(SolarCCSearchForm, self).__init__(*args, **kwargs)

        all_objects = models.SolarCC.objects.all()
        merk_choices = [
            ('', '-------'),
        ]
        try:
            for object in all_objects:
                if (object.merk, object.merk) in merk_choices:
                    continue
                else:
                    merk_choices.append((object.merk, object.merk))
        except OperationalError:
            pass

        self.fields['merk'] = forms.ChoiceField(choices=merk_choices, label='Brand')


class PVModuleSearchForm(forms.Form):
    merk = forms.ChoiceField(choices=[])
    kw_value = forms.ChoiceField(choices=[])
    search = forms.CharField(max_length=100, label='Search')

    def __init__(self, *args, **kwargs):
        super(PVModuleSearchForm, self).__init__(*args, **kwargs)

        all_objects = models.PVModule.objects.all()
        merk_choices = [
            ('', '-------'),
        ]
        kw_value_choices = [
            ('', '-------'),
        ]
        try:
            for object in all_objects:
                if (object.merk, object.merk) in merk_choices:
                    pass
                else:
                    merk_choices.append((object.merk, object.merk))

                if (object.kw_value, str(object.kw_value) + ' Wp') in kw_value_choices:
                    continue
                else:
                    kw_value_choices.append((object.kw_value, str(object.kw_value) + ' Wp'))
        except OperationalError:
            pass
            
        self.fields['merk'] = forms.ChoiceField(choices=merk_choices, label='Brand')
        self.fields['kw_value'] = forms.ChoiceField(choices=kw_value_choices, label='Module Capacity')


class BatterySearchForm(forms.Form):
    merk = forms.ChoiceField(choices=[])
    v_per_cell = forms.ChoiceField(choices=[])
    tipe = forms.ChoiceField(choices=[])
    search = forms.CharField(max_length=100, label='Search')

    def __init__(self, *args, **kwargs):
        super(BatterySearchForm, self).__init__(*args, **kwargs)

        all_objects = models.Battery.objects.all()
        merk_choices = [
            ('', '-------'),
        ]
        tipe_choices = [
            ('', '-------'),
        ]
        v_per_cell_choices = [
            ('', '-------'),
        ]
        try:
            for object in all_objects:
                if (object.merk, object.merk) in merk_choices:
                    pass
                else:
                    merk_choices.append((object.merk, object.merk))

                if (object.tipe, object.tipe) in tipe_choices:
                    pass
                else:
                    tipe_choices.append((object.tipe, object.tipe))

                if (object.v_per_cell, str(object.v_per_cell) + ' V') in v_per_cell_choices:
                    continue
                else:
                    v_per_cell_choices.append((object.v_per_cell, str(object.v_per_cell) + ' V'))
        except OperationalError:
            pass
            
        self.fields['merk'] = forms.ChoiceField(choices=merk_choices, label='Brand')
        self.fields['v_per_cell'] = forms.ChoiceField(choices=v_per_cell_choices, label='Cell Voltage')
        self.fields['tipe'] = forms.ChoiceField(choices=tipe_choices, label='Battery Type')

    
class LVPanelSearchForm(forms.Form):
    merk = forms.ChoiceField(choices=[])
    search = forms.CharField(max_length=100, label='Search')

    def __init__(self, *args, **kwargs):
        super(LVPanelSearchForm, self).__init__(*args, **kwargs)

        all_objects = models.LVPanel.objects.all()
        merk_choices = [
            ('', '-------'),
        ]
        try:
            for object in all_objects:
                if (object.merk, object.merk) in merk_choices:
                    continue
                else:
                    merk_choices.append((object.merk, object.merk))
        except OperationalError:
            pass

        self.fields['merk'] = forms.ChoiceField(choices=merk_choices, label='Brand')


class MVPanelSearchForm(forms.Form):
    merk = forms.ChoiceField(choices=[])
    search = forms.CharField(max_length=100, label='Search')

    def __init__(self, *args, **kwargs):
        super(MVPanelSearchForm, self).__init__(*args, **kwargs)

        all_objects = models.MVPanel.objects.all()
        merk_choices = [
            ('', '-------'),
        ]
        try:
            for object in all_objects:
                if (object.merk, object.merk) in merk_choices:
                    continue
                else:
                    merk_choices.append((object.merk, object.merk))
        except OperationalError:
            pass

        self.fields['merk'] = forms.ChoiceField(choices=merk_choices, label='Brand')


class TrafoSearchForm(forms.Form):
    merk = forms.ChoiceField(choices=[])
    year = forms.ChoiceField(choices=[])
    kva_value = forms.ChoiceField(choices=[])
    search = forms.CharField(max_length=100, label='Search')

    def __init__(self, *args, **kwargs):
        super(TrafoSearchForm, self).__init__(*args, **kwargs)

        all_objects = models.Trafo.objects.all()
        merk_choices = [
            ('', '-------'),
        ]
        year_choices = [
            ('', '-------'),
        ]
        kva_choices = [
            ('', '-------'),
        ]
        try:
            for object in all_objects:
                if (object.merk, object.merk) in merk_choices:
                    pass
                else:
                    merk_choices.append((object.merk, object.merk))

                if (object.year, object.year) in year_choices:
                    pass
                else:
                    year_choices.append((object.year, object.year))

                if (object.kva_value, str(object.kva_value) + ' KVA') in kva_choices:
                    continue
                else:
                    kva_choices.append((object.kva_value, str(object.kva_value) + ' KVA'))
        except OperationalError:
            pass

            
        self.fields['merk'] = forms.ChoiceField(choices=merk_choices, label='Brand')
        self.fields['year'] = forms.ChoiceField(choices=year_choices, label='Year')
        self.fields['kva_value'] = forms.ChoiceField(choices=kva_choices, label='Trafo Capacity')


class AIOSearchForm(forms.Form):
    PHASE_CHOISES = [
        ('', '-------'),
        ('Single Phase', "Single Phase"),
        ('Triple Phase', "Triple Phase"),
    ]

    merk = forms.ChoiceField(choices=[])
    phase = forms.ChoiceField(choices=PHASE_CHOISES, label='AIO Phases')
    kva_value = forms.ChoiceField(choices=[])
    search = forms.CharField(max_length=100, label='Search')

    def __init__(self, *args, **kwargs):
        super(AIOSearchForm, self).__init__(*args, **kwargs)

        all_objects = models.AllInOne.objects.all()
        merk_choices = [
            ('', '-------'),
        ]
        kva_choices = [
            ('', '-------'),
        ]
        try:
            for object in all_objects:
                if (object.merk, object.merk) in merk_choices:
                    pass
                else:
                    merk_choices.append((object.merk, object.merk))

                if (object.kva, str(object.kva) + ' KVA') in kva_choices:
                    continue
                else:
                    kva_choices.append((object.kva, str(object.kva) + ' KVA'))
        except OperationalError:
            pass

            
        self.fields['merk'] = forms.ChoiceField(choices=merk_choices, label='Brand')
        self.fields['kva_value'] = forms.ChoiceField(choices=kva_choices, label='AIO Capacity')


class MountingSearchForm(forms.Form):
    merk = forms.ChoiceField(choices=[])
    kw_value = forms.ChoiceField(choices=[])
    search = forms.CharField(max_length=100, label='Search')

    def __init__(self, *args, **kwargs):
        super(MountingSearchForm, self).__init__(*args, **kwargs)

        all_objects = models.Mounting.objects.all()
        merk_choices = [
            ('', '-------'),
        ]
        kw_value_choices = [
            ('', '-------'),
        ]
        try:
            for object in all_objects:
                if (object.merk, object.merk) in merk_choices:
                    pass
                else:
                    merk_choices.append((object.merk, object.merk))

                if (object.kw_value, str(object.kw_value) + ' Wp') in kw_value_choices:
                    continue
                else:
                    kw_value_choices.append((object.kw_value, str(object.kw_value) + ' Wp'))
        except OperationalError:
            pass
            
        self.fields['merk'] = forms.ChoiceField(choices=merk_choices, label='Brand')
        self.fields['kw_value'] = forms.ChoiceField(choices=kw_value_choices, label='Module Capacity')
