import datetime

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class DetailPinjam(models.Model):
    peminjaman = models.ForeignKey('Peminjaman', on_delete=models.CASCADE)
    inventaris = models.ForeignKey('Inventaris', on_delete=models.CASCADE)
    jumlah = models.IntegerField()

    class Meta:
        db_table = 'detail_pinjam'


class Inventaris(models.Model):
    nama = models.CharField(max_length=100)
    kondisi = models.CharField(max_length=100)
    keterangan = models.TextField()
    jumlah = models.IntegerField()
    jenis = models.ForeignKey('Jenis', on_delete=models.CASCADE)
    tanggal_register = models.DateField()
    ruang = models.ForeignKey('Ruang', on_delete=models.CASCADE)
    kode_inventaris = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self):
        if self.id:
            self.updated_at = timezone.now()
        else:
            self.updated_at = timezone.now()
            self.created_at = timezone.now()
        super().save()

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'inventaris'


class Jenis(models.Model):
    nama_jenis = models.CharField(max_length=100)
    kode_jenis = models.CharField(max_length=100)
    keterangan = models.TextField()
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    def save(self):
        if self.id:
            self.updated_at = timezone.now()
        else:
            self.updated_at = timezone.now()
            self.created_at = timezone.now()
        super().save()

    def __str__(self):
        return self.nama_jenis

    class Meta:
        db_table = 'jenis'


class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    ipaddr = models.CharField(max_length=200)
    created_at = models.DateTimeField(
        default=datetime.datetime.now,
        blank=True)
    update_at = models.DateTimeField(blank=True, null=True)

    def save(self):
        if self.id:
            self.updated_at = timezone.now()
        else:
            self.updated_at = timezone.now()
            self.created_at = timezone.now()
        super().save()

    def __str__(self):
        return self.user.first_name

    class Meta:
        db_table = 'log'


class Pages(models.Model):
    page_name = models.CharField(max_length=200)
    page_route = models.CharField(max_length=200)
    is_parent = models.IntegerField(blank=True, null=True)
    children = models.IntegerField(blank=True, null=True)
    icon = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self):
        if self.id:
            self.updated_at = timezone.now()
        else:
            self.updated_at = timezone.now()
            self.created_at = timezone.now()
        super().save()

    def __str__(self):
        return self.page_name

    class Meta:
        db_table = 'pages'


class Pegawai(models.Model):
    nama_pegawai = models.CharField(max_length=100)
    nip = models.CharField(
        primary_key=True,
        max_length=20,
        validators=[RegexValidator(r'^\d{1,10}$')]
    )
    alamat = models.TextField()
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    def save(self):
        if Pegawai.objects.filter(nip=self.nip).exists():
            self.updated_at = timezone.now()
        else:
            self.updated_at = timezone.now()
            self.created_at = timezone.now()
        super().save()

    def __str__(self):
        return self.nama_pegawai

    class Meta:
        db_table = 'pegawai'


class Peminjaman(models.Model):
    STATUS = SHIRT_SIZES = (
        ('0', 'Dipinjam'),
        ('1', 'Dikembalikan'),
    )
    tanggal_pinjam = models.DateTimeField()
    tanggal_kembali = models.DateTimeField(blank=True, null=True)
    status_peminjaman = models.CharField(max_length=1, choices=STATUS)
    pegawai = models.ForeignKey(Pegawai, on_delete=models.CASCADE)
    inventaris = models.ManyToManyField(Inventaris, through=DetailPinjam)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.pegawai.nama_pegawai

    def save(self):
        if self.id:
            self.updated_at = timezone.now()
        else:
            self.updated_at = timezone.now()
            self.created_at = timezone.now()
        super().save()

    class Meta:
        db_table = 'peminjaman'


class Ruang(models.Model):
    nama_ruang = models.CharField(max_length=100)
    kode_ruang = models.CharField(max_length=100)
    keterangan = models.TextField()
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self):
        if self.id:
            self.updated_at = timezone.now()
        else:
            self.updated_at = timezone.now()
            self.created_at = timezone.now()
        super().save()

    def __str__(self):
        return self.nama_ruang

    class Meta:
        db_table = 'ruang'


class Settings(models.Model):
    id = models.IntegerField(primary_key=True)
    website_name = models.CharField(max_length=200)
    dashboard_text = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=100, blank=True, null=True)
    favicon = models.CharField(max_length=100, blank=True, null=True)
    automatic_code = models.IntegerField()
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.website_name

    def save(self):
        if self.id:
            self.updated_at = timezone.now()
        else:
            self.updated_at = timezone.now()
            self.created_at = timezone.now()
        super().save()

    class Meta:
        db_table = 'settings'
