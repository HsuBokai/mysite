from django.shortcuts import render
from django.http import HttpResponse
from formtools.wizard.views import SessionWizardView

# Create your views here.

def home(request):
    return HttpResponse('<h1>ABC</h1>')

class ContactWizard(SessionWizardView):
    template_name = 'blog/contact_form.html'

    def done(self, form_list, **kwards):
        return HttpResponse('<h1>ABC</h1>')
