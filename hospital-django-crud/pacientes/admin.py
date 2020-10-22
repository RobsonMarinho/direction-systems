from django.contrib import admin
from .models import Paciente
from django.utils.html import format_html


class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'email', 'dtNascimento', 'status_colored', 'endereco']

    def status_colored(self, obj):
        color = 'cyan'
        if obj.status == 'Closed':
            color = 'red'
        return format_html(
                '<b style="background:{};">{}</b>',
                color,
                obj.status
            )
        status_colored.admin_order_field = 'new'

admin.site.register(Paciente, PacienteAdmin)
