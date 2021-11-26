from django.urls import path

from . import views

urlpatterns = [
    path('', views.FacilityList.as_view(), name='facilities_list'),
    path('facilitieslist', views.FacilityList.as_view(), name='facilities_list'),
    path('facilitiescreate', views.FacilityCreate.as_view(), name='facilities_create'),
    path('facilitiesupdate/<pk>', views.FacilityUpdate.as_view(), name='facilities_update'),
    path('facilitiesdelete/<pk>', views.FacilityDelete.as_view(), name='facilities_delete'),
]
