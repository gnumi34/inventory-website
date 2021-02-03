from django.db import models
from django.contrib.auth.models import User


class Inverter(models.Model):
    APPLICATIONS = [
        ('On-Grid', 'On-Grid'),
        ('Off-Grid', 'Off-Grid'),
        ('Hybrid', 'Hybrid')
    ]

    PHASE_CHOISES = [
        ('Single Phase', "Single Phase"),
        ('Triple Phase', "Triple Phase"),
    ]

    KURS_UANG = [
        ('$', 'USD'),
        ('Euro', 'Euro'),
    ]

    merk = models.CharField(max_length=30, unique=False)
    tipe = models.CharField(max_length=50, unique=False)
    jenis = models.CharField(max_length=50, unique=False)
    aplikasi = models.CharField(max_length=50, unique=False, choices=APPLICATIONS)
    phase = models.CharField(max_length=15, choices=PHASE_CHOISES)
    kva = models.FloatField(help_text="Please enter the number in kVA")
    kurs = models.CharField(max_length=5, choices=KURS_UANG)
    value = models.FloatField(help_text="Please insert the price in chosen foreign currency")
    idr_value = models.FloatField()
    contact = models.CharField(max_length=25)
    period = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    entry_by = models.ForeignKey(User, related_name='inverters', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (self.merk + ' ' + self.tipe)


class Monitoring(models.Model):
    merk = models.CharField(max_length=30, unique=False)
    item = models.CharField(max_length=100, unique=False)
    tipe = models.CharField(max_length=50, unique=False)
    usd_value = models.FloatField()
    contact = models.CharField(max_length=25)
    period = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    entry_by = models.ForeignKey(User, related_name='monitors', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (self.merk + ' ' + self.tipe)


class WeatherStation(models.Model):
    merk = models.CharField(max_length=30, unique=False)
    item = models.CharField(max_length=100, unique=False)
    tipe = models.CharField(max_length=50, unique=False)
    usd_value = models.FloatField()
    contact = models.CharField(max_length=25)
    period = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    entry_by = models.ForeignKey(User, related_name='wstations', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (self.merk + ' ' + self.tipe)


class Sensor(models.Model):
    merk = models.CharField(max_length=30, unique=False)
    item = models.CharField(max_length=100, unique=False)
    tipe = models.CharField(max_length=50, unique=False)
    usd_value = models.FloatField()
    contact = models.CharField(max_length=25)
    period = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    entry_by = models.ForeignKey(User, related_name='sensors', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (self.merk + ' ' + self.tipe)


class SolarCC(models.Model):
    KURS_UANG = [
        ('$', 'USD'),
        ('Euro', 'Euro'),
    ]

    merk = models.CharField(max_length=30, unique=False)
    item = models.CharField(max_length=100, unique=False)
    tipe = models.CharField(max_length=50, unique=False)
    vbat = models.FloatField(help_text="Please insert the value in Volt.")
    amperage = models.FloatField(help_text="Please insert the value in Ampere.")
    wattmax = models.FloatField(help_text="Please insert the value in Watt.")
    kurs = models.CharField(max_length=5, choices=KURS_UANG)
    value = models.FloatField(help_text="Please insert the price in chosen foreign currency.")
    idr_value = models.FloatField()
    contact = models.CharField(max_length=25)
    period = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    entry_by = models.ForeignKey(User, related_name='solarccs', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (self.merk + ' ' + self.tipe)


class PVModule(models.Model):
    KURS_UANG = [
        ('$', 'USD'),
        ('E', 'Euro'),
    ]

    merk = models.CharField(max_length=30, unique=False)
    item = models.CharField(max_length=100, unique=False)
    tipe = models.CharField(max_length=50, unique=False)
    kw_value = models.FloatField(help_text="Please insert the value in Wp.")
    kurs = models.CharField(max_length=5, choices=KURS_UANG)
    wp_price = models.FloatField(help_text="Please insert the price per Wp.")
    contact = models.CharField(max_length=25)
    period = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    entry_by = models.ForeignKey(User, related_name='pv_modules', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (self.merk + ' ' + self.tipe)


class Battery(models.Model):
    KURS_UANG = [
        ('$', 'USD'),
        ('Euro', 'Euro'),
    ]

    merk = models.CharField(max_length=30, unique=False)
    item = models.CharField(max_length=100, unique=False)
    tipe = models.CharField(max_length=50, unique=False)
    keterangan = models.CharField(max_length=100, unique=False)
    v_per_cell = models.FloatField(help_text="Please insert the value in Volt per Cell.")
    capacity = models.FloatField(help_text="Please insert the value in Ah.")
    kwh = models.FloatField(help_text="Please insert the value in KWh.")
    kurs = models.CharField(max_length=5, choices=KURS_UANG)
    value = models.FloatField(help_text="Please insert the price in chosen foreign currency.")
    idr_value = models.FloatField()
    contact = models.CharField(max_length=25)
    period = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    entry_by = models.ForeignKey(User, related_name='batteries', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (self.merk + ' ' + self.tipe)


class LVPanel(models.Model):
    merk = models.CharField(max_length=30, unique=False)
    item = models.CharField(max_length=100, unique=False)
    tipe = models.CharField(max_length=50, unique=False)
    usd_value = models.FloatField()
    contact = models.CharField(max_length=25)
    period = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    entry_by = models.ForeignKey(User, related_name='lv_panels', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (self.merk + ' ' + self.tipe)


class MVPanel(models.Model):
    merk = models.CharField(max_length=30, unique=False)
    item = models.CharField(max_length=100, unique=False)
    tipe = models.CharField(max_length=50, unique=False)
    usd_value = models.FloatField()
    contact = models.CharField(max_length=25)
    period = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    entry_by = models.ForeignKey(User, related_name='mv_panels', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (self.merk + ' ' + self.tipe)


class Trafo(models.Model):
    YEAR = [
        ('2010', '2010'),
        ('2011', '2011'),
        ('2012', '2012'),
        ('2013', '2013'),
        ('2014', '2014'),
        ('2015', '2015'),
        ('2016', '2016'),
        ('2017', '2017'),
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
        ('2022', '2022'),
        ('2023', '2023')
    ]

    merk = models.CharField(max_length=30, unique=False)
    item = models.CharField(max_length=100, unique=False)
    tipe = models.CharField(max_length=50, unique=False)
    kva_value = models.FloatField(help_text="Please insert the value in kVA.")
    price = models.FloatField()
    year = models.CharField(max_length=4, choices=YEAR)
    distributor = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    entry_by = models.ForeignKey(User, related_name='transformers', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)


class AllInOne(models.Model):
    PHASE_CHOISES = [
        ('Single Phase', "Single Phase"),
        ('Triple Phase', "Triple Phase"),
    ]

    KURS_UANG = [
        ('$', 'USD'),
        ('Euro', 'Euro'),
    ]

    merk = models.CharField(max_length=30, unique=False)
    item = models.CharField(max_length=100, unique=False)
    tipe = models.CharField(max_length=50, unique=False)
    phase = models.CharField(max_length=15, choices=PHASE_CHOISES)
    kva = models.FloatField(help_text="Please enter the number in kVA")
    kurs = models.CharField(max_length=5, choices=KURS_UANG)
    value = models.FloatField(help_text="Please insert the price in chosen foreign currency")
    idr_value = models.FloatField()
    contact = models.CharField(max_length=25)
    period = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    entry_by = models.ForeignKey(User, related_name='aios', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (self.merk + ' ' + self.tipe)


class Mounting(models.Model):
    KURS_UANG = [
        ('$', 'USD'),
        ('E', 'Euro'),
    ]

    merk = models.CharField(max_length=30, unique=False)
    item = models.CharField(max_length=100, unique=False)
    tipe = models.CharField(max_length=50, unique=False)
    kw_value = models.FloatField(help_text="Please insert the value in Wp.")
    kurs = models.CharField(max_length=5, choices=KURS_UANG)
    wp_price = models.FloatField(help_text="Please insert the price per Wp in USD.")
    contact = models.CharField(max_length=25)
    period = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    entry_by = models.ForeignKey(User, related_name='mountings', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (self.merk + ' ' + self.tipe)