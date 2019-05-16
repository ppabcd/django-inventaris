from django.contrib import admin

from .models import DetailPinjam, Inventaris, Jenis, Pegawai, Peminjaman, Ruang


# Inline
class DetailInline(admin.TabularInline):
    model = Peminjaman.inventaris.through
    extra = 1
    min_num = 1


class PegawaiAdmin(admin.ModelAdmin):
    exclude = ['created_at', 'updated_at', 'deleted_at']


class JenisAdmin(admin.ModelAdmin):
    exclude = ['created_at', 'updated_at', 'deleted_at']


class RuangAdmin(admin.ModelAdmin):
    exclude = ['created_at', 'updated_at', 'deleted_at']


class PeminjamanAdmin(admin.ModelAdmin):
    inlines = [DetailInline]
    exclude = ['created_at', 'updated_at', 'deleted_at']
    list_display = [
        'tanggal_pinjam',
        'pegawai',
        'status_peminjaman',
        'created_at',
        'updated_at'
    ]


class InventarisAdmin(admin.ModelAdmin):
    fieldsets: [
        (None, {'fields': [
            'nama',
            'kondisi',
            'keterangan',
            'jumlah',
            'kode'
        ]}),
    ]
    exclude = ['created_at', 'updated_at']
    list_display = (
        'nama',
        'jumlah',
        'kondisi',
        'ruang',
        'jenis',
        'keterangan'
    )
    list_filter = ['kondisi']
    search_fields = ['nama', 'keterangan']


class DetailPinjamAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


admin.site.register(Pegawai, PegawaiAdmin)
admin.site.register(Jenis, JenisAdmin)
admin.site.register(Ruang, RuangAdmin)
admin.site.register(DetailPinjam, DetailPinjamAdmin)
admin.site.register(Peminjaman, PeminjamanAdmin)
admin.site.register(Inventaris, InventarisAdmin)
# admin.site.register(Peminjaman)
# admin.site.register(Inventaris)
