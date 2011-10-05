from form_utils.forms import BetterModelForm
from recruits.models import Recruit

class RecruitForm(BetterModelForm):
    error_css_class = "error"
    required_css_class = "required"

    class Meta:
        model = Recruit
        fieldsets = [
            ('contact',
                {'fields': ['first_name',
                            'last_name',
                            'email',
                            'institution',
                            'college', ],
                 'legend': '',
                 'description': 'Contact Details',
                 'classes': ['recruit', 'details'],}),
            ('interests',
                {'fields': ['acting',
                            'production',
                            'tech',
                            'musician',
                            'tickets',],
                 'legend': ''})
            ]
