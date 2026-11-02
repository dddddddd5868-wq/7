from django.contrib import admin
from .models import CompanyInfo, Service


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'email')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ('title', 'price')
