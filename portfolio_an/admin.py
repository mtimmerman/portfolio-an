from django.contrib import admin
from portfolio_an.models import PortfolioUser, Contact

admin.site.register(PortfolioUser)

class ContactAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "date",)
    date_hierarchy = "date"
    search_fields = ("email", "first_name", "last_name",)

admin.site.register(Contact, ContactAdmin)
