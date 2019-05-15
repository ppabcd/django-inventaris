import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators  import RegexValidator

# Create your models here.
class Pegawai(models.Model):
    nama_pegawai = models.CharField(max_length=200)
    nip = models.CharField(primary_key=True, max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    alamat = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return self.nama_pegawai

class Jenis(models.Model):
    nama = models.CharField(max_length=200)
    kode = models.CharField(max_length=10)
    keterangan = models.TextField()
    
    created_at = models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return self.nama

class Ruang(models.Model):
    nama = models.CharField(max_length=200)
    kode = models.CharField(max_length=16)
    keterangan = models.TextField()

    created_at = models.DateTimeField(default=datetime.datetime.now, blank=True)
    def __str__(self):
        return self.nama

class Inventaris(models.Model):
    nama = models.CharField(max_length=200)
    kondisi = models.CharField(max_length=200)
    keterangan = models.TextField()

    jumlah = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,10}$')])
    jenis = models.ForeignKey(Jenis, on_delete=models.CASCADE)
    ruang = models.ForeignKey(Ruang, on_delete=models.CASCADE)
    kode = models.CharField(max_length=16)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return self.nama

class Detail(models.Model):
    peminjaman = models.ForeignKey('Peminjaman', on_delete=models.CASCADE)
    inventaris = models.ForeignKey('Inventaris', on_delete=models.CASCADE)
    jumlah_item = models.CharField(max_length=11, validators=[RegexValidator(r'^\d{1,10}$')])

class Peminjaman(models.Model):
    STATUS =  SHIRT_SIZES = (
        ('0', 'Dipinjam'),
        ('1', 'Dikembalikan'),
    )
    tanggal_pinjam = models.DateTimeField('Tanggal Peminjaman')
    tanggal_kembali = models.DateTimeField(blank=True,null=True)
    # status_peminjaman = models.CharField(max_length=1, validators=[RegexValidator(r'^\d{1,10}$')])
    status_peminjaman = models.CharField(max_length=1, choices=STATUS)
    pegawai = models.ForeignKey(Pegawai, on_delete=models.CASCADE)
    inventaris = models.ManyToManyField(Inventaris, through=Detail)
    created_at = models.DateTimeField(default=datetime.datetime.now, blank=True)

    def __str__(self):
        return self.pegawai.nama_pegawai

    def status(self):
        if(self.status_peminjaman == 1):
            return 'Dikembalikan'
        else:
            return 'Dipinjam'