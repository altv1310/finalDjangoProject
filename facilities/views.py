from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Facilities
from .forms import FacilityCreateForm, FacilityUpdateForm


class FacilityList(ListView):
    model = Facilities


class FacilityCreate(CreateView):
    model = Facilities
    template_name = 'facilities/facilities_create_form.html'
    form_class = FacilityCreateForm


class FacilityUpdate(UpdateView):
    model = Facilities
    template_name = 'facilities/facilities_update_form.html'
    form_class = FacilityUpdateForm


class FacilityDelete(DeleteView):
    model = Facilities
    template_name = 'facilities/facilities_delete_form.html'
    success_url = '/facilitieslist'
