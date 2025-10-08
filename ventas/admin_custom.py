from django.contrib import admin
from django.contrib.admin.sites import AdminSite

class CustomAdminSite(AdminSite):
    class Media:
        css = {
            'all': ('css/admin_custom.css',)
        }

# O si no quieres reemplazar el AdminSite, puedes usar un hook global:
admin.site.site_header = "Administración de Django"
admin.site.site_title = "Panel de Administración"
admin.site.index_title = "Bienvenido al panel"

# Esto añade el CSS globalmente
def custom_admin_css():
    from django.contrib.staticfiles.storage import staticfiles_storage
    from django.conf import settings
    from django.utils.html import format_html

    return format_html('<link rel="stylesheet" type="text/css" href="{}">', staticfiles_storage.url('css/admin_custom.css'))

admin.site.each_context = lambda request: {**admin.site.each_context(request), 'custom_admin_css': custom_admin_css()}
