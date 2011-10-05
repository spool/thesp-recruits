from recruits.forms import RecruitForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse

def recruit(request, form_class=RecruitForm, template_name="recruit.html", extra_context=None):
    recruit_form = form_class(request.POST or None)
    if recruit_form.is_valid():
        recruit_form.save()
        messages.success(request, 'Thanks very much!')
        return HttpResponseRedirect(reverse('home'))

    context = {'recruit_form': recruit_form}
    messages.success(request, None)
    
    if extra_context is not None:
        context.update(extra_context)

    return render_to_response(template_name, context, 
            context_instance=RequestContext(request))
