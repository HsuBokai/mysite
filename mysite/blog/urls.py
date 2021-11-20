from django.conf.urls import url
from . import views
from . import forms

urlpatterns = [
    url(r'^contact/$', views.ContactWizard.as_view([forms.ContactForm1, forms.ContactForm2]), name='blog-contact'),
    url(r'', views.home, name='blog-home'),
]
