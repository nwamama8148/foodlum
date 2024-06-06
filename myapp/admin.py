from django.contrib import admin
from . models import *

# Register your models here.

class ReservationAdmin(admin.ModelAdmin):
    '''Admin View for Reservation'''

    list_display = ('name','email','orders','special_request','nop',)


# class BreakfastFoodAdmin(admin.ModelAdmin):
#     '''Admin View for BreakfastFood'''

#     list_display = ['name', 'img','date_of_creation','desc','price','slug']
    
# class LunchFoodAdmin(admin.ModelAdmin):

#     list_display = ['name', 'img','date_of_creation','desc','price','slug']
 
    
class FoodProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'img','date_of_creation','desc','price','slug','is_breakfast',
'is_dinner','is_lunch','is_best',]
 
class TeamAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'designation','img']
    
    
admin.site.register(Reservation, ReservationAdmin)
# admin.site.register(BreakfastFood, BreakfastFoodAdmin)
# admin.site.register(LunchFood, LunchFoodAdmin)
admin.site.register(FoodProduct, FoodProductAdmin)
admin.site.register(Team, TeamAdmin)