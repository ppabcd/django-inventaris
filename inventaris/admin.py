from django.contrib import admin

# Register your models here.
from .models import Pegawai, Jenis, Ruang, Inventaris, Detail, Peminjaman

class DetailInline(admin.TabularInline):
	model = Peminjaman.inventaris.through
	extra = 1
	min_num = 1

class PeminjamanAdmin(admin.ModelAdmin):
	inlines = [DetailInline]
	exclude = ['created_at']

class InventarisAdmin(admin.ModelAdmin):
	fieldsets:[
		(None, {'fields':['nama','kondisi','keterangan','jumlah', 'kode']}),
	]
	exclude = ['created_at']
	list_display = ('nama','kondisi','keterangan','jumlah')
admin.site.register(Pegawai)
admin.site.register(Jenis)
admin.site.register(Ruang)
admin.site.register(Detail)
admin.site.register(Peminjaman, PeminjamanAdmin)
admin.site.register(Inventaris, InventarisAdmin)