from django.urls import path
from . import  views 

urlpatterns = [
    path('leave-form-submit/', views.LeaveFormSubmitView.as_view(), name='leave-form-submit'), 
    path('bonafide-form-submit/', views.BonafideFormSubmitView.as_view(), name='bonafide-form-submit'), 

]
