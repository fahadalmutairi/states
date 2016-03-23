from django.contrib import admin
from main.models import State, StateCapital, City

# Register your models here.

class StateCapitalAdmin(admin.ModelAdmin):
	list_display = ('name', 'population')
	search_fields = ('name', )

class CityAdmin(admin.ModelAdmin):
	list_display = ('name', 'county')
	search_fields = ('name', )

class CityInline(admin.TabularInline):
    model = City

class StateAdmin(admin.ModelAdmin):
	list_display = ('name', 'abbreviation')
	search_fields = ('name', )
	inlines = [CityInline]

admin.site.register(State, StateAdmin)
admin.site.register(City)	
admin.site.register(StateCapital)  	
