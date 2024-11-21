from django.urls import path
from . import  views 

urlpatterns = [
    path('leave-form-submit/', views.LeaveFormSubmitView.as_view(), name='leave-form-submit'), 
    path('leave-pg-submit/', views.LeavePGSubmitView.as_view(), name='leave-pg-submit'), 
    path('bonafide-form-submit/', views.BonafideFormSubmitView.as_view(), name='bonafide-form-submit'), 
    path('fetch-pending-leaves/', views.FetchPendingLeaveRequests.as_view(), name='fetch-pending-leaves'),
    path('update-leave-status/', views.UpdateLeaveStatus.as_view(), name='update-leave-status'),
    path('fetch-pending-leaves-ta/', views.FetchPendingLeaveRequestsTA.as_view(), name='fetch-pending-leaves-ta'),
    path('update-leave-status-ta/', views.UpdateLeaveStatusTA.as_view(), name='update-leave-status-ta'),
    path('fetch-pending-leaves-thesis/', views.FetchPendingLeaveRequestsThesis.as_view(), name='fetch-pending-leaves-tesis'),
    path('update-leave-status-thesis/', views.UpdateLeaveStatusThesis.as_view(), name='update-leave-status-thesis'),
    path('get-leave-requests/', views.GetLeaveRequests.as_view(), name='get-leave-requests'),
    path('get-pg-leave-requests/', views.GetPGLeaveRequests.as_view(), name='get-pg-leave-requests'),
]
