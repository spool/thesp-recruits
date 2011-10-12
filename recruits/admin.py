from recruits.models import Recruit
from django.contrib import admin
class RecruitAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'institution', 'college', 'acting',
                        "production", "tech", "musician", "tickets",)

admin.site.register(Recruit, RecruitAdmin)

