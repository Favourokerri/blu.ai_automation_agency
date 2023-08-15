from django.contrib import admin
from base_app.models import Hero_section
from base_app.models import About_us
from base_app.models import Services
from base_app.models import MainServices
from base_app.models import Team
from base_app.models import Questions
from base_app.models import Details
from base_app.models import Contact_Us
from base_app.models import Accounts

# Register your models here.

admin.site.site_header ="balablu"
class CustomAdminSite(admin.AdminSite):
    site_title = 'Your Custom Admin Title'

class TeamAdmin(admin.ModelAdmin):
    list_display=("name", "position", "about")

class ServiceAdmin(admin.ModelAdmin):
    list_display=("name_of_service", "date_posted")

class QuestionAdmin(admin.ModelAdmin):
    list_display=("question", "answer")

class DetailsAdmin(admin.ModelAdmin):
    list_display=("location", "email", "phone_number")

admin.site.register(Hero_section)
admin.site.register(About_us)
admin.site.register(MainServices)
admin.site.register(Services, ServiceAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Questions, QuestionAdmin)
admin.site.register(Details, DetailsAdmin)
admin.site.register(Contact_Us)
admin.site.register(Accounts)