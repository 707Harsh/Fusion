from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LeaveFormSerializer  ,BonafideFormSerializer 
from datetime import date
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect,render
from rest_framework.permissions import IsAuthenticated  
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from applications.otheracademic.models import (LeaveFormTable, BonafideFormTableUpdated, GraduateSeminarFormTable,AssistantshipClaimFormStatusUpd, LeavePG, NoDues)
from datetime import date
from applications.filetracking.models import File
from applications.filetracking.sdk.methods import create_file
from notification.views import otheracademic_notif
from applications.filetracking.models import *
from applications.filetracking.sdk.methods import *
from applications.globals.models import ExtraInfo, HoldsDesignation, Designation
from django.http import JsonResponse

class LeaveFormSubmitView(APIView):
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        # Extract data from the request
        data = request.POST
        file = request.FILES.get('related_document')
        hodname = data.get('hod_credential')

        print(data.get('mobile_number'),data.get('parents_mobile'),"hello ab")
        
        # Create a new LeaveFormTable instance and save it to the database
        leave = LeaveFormTable.objects.create(
            student_name=request.user.first_name+request.user.last_name,
            roll_no=request.user.extrainfo,
            date_from=data.get('date_from'),
            date_to=data.get('date_to'),
            leave_type=data.get('leave_type'),
            upload_file=file,
            address=data.get('address'),
            purpose=data.get('purpose'),
            date_of_application=date.today(),
            # approved=False,  # Initially not approved
            # rejected=False,  # Initially not rejected
            stud_mobile_no=data.get('mobile_number'),
            parent_mobile_no=data.get('parents_mobile'),
            leave_mobile_no=data.get('mobile_during_leave'),
            curr_sem=int(data.get('semester')),
            hod=data.get('hod_credential')
        )
        print(data.get('mobile_number'),data.get('parents_mobile'))
        
        leave_hod = User.objects.get(username=hodname)
        receiver_value = User.objects.get(username=request.user.username)
        receiver_value_designation = HoldsDesignation.objects.filter(user=receiver_value)
        lis = list(receiver_value_designation)
        obj = lis[0].designation

        file_id = create_file(
            uploader=request.user.username,
            uploader_designation=obj,
            receiver=leave_hod,
            receiver_designation="student",
            src_module="otheracademic",
            src_object_id=leave.id,
            file_extra_JSON={"value": 2},
            attached_file=None,
            subject='ug_leave'
        )

        
      
        serializer = LeaveFormSerializer(data={
            'student_name': data.get('student_name'),
            'roll_no': data.get('roll_no'), 
            'date_from': data.get('date_from'),
            'date_to': data.get('date_to'),
            'leave_type': data.get('leave_type'),
            'upload_file': file,
            'address': data.get('address'),
            'purpose': data.get('purpose'),
            'date_of_application': date.today(),
            'approved': False, 
            'rejected': False,
            'hod': hodname
        })

        # new_tracking = Tracking.objects.create(
        #     file_id=file_id,  # The newly created file object
        #     uploader=request.user.username,
        #     uploader_designation=obj,
        #     receiver=leave_hod,
        #     receive_design=receiver_designation_obj,  # Receiver's designation object
        #     tracking_extra_JSON=file_extra_JSON,  # Additional metadata in JSON format
        #     remarks=f"File with id:{file_id} created by {uploader} and sent to {receiver}"  # Remarks for this tracking event
        # )

        message = "A new leave application"
        otheracademic_notif(request.user, leave_hod, 'ug_leave_hod', leave.id, 'student', message)
    
        return Response({"message": "You successfully submitted your form"}, status=status.HTTP_201_CREATED)
    



# class FetchPendingLeaveRequests(APIView):
#     print("here")
#     permission_classes = [IsAuthenticated]

#     def get(self):
#         # Query the LeaveFormTable for entries with status = "Pending"
#         pending_leaves = LeaveFormTable.objects.filter(status="Pending")
        
#         # Format the data as an array of JSON objects
#         data = []
#         for leave in pending_leaves:
#             data.append({
#                 "rollNo": leave.roll_no,  # Assuming roll_no field in ExtraInfo has roll_no property
#                 "name": leave.student_name,
#                 "form": leave.upload_file.url if leave.upload_file else None,
#                 "details": {
#                     "dateFrom": leave.date_from.strftime("%Y-%m-%d"),
#                     "dateTo": leave.date_to.strftime("%Y-%m-%d"),
#                     "leaveType": leave.leave_type,
#                     "address": leave.address,
#                     "purpose": leave.purpose,
#                     "hodCredential": leave.hod,
#                     "mobileNumber": leave.stud_mobile_no,
#                     "parentsMobile": leave.parent_mobile_no,
#                     "mobileDuringLeave": leave.leave_mobile_no,
#                     "semester": str(leave.curr_sem),
#                     "academicYear": f"{leave.date_from.year}-{leave.date_to.year}",
#                     "dateOfApplication": leave.date_of_application.strftime("%Y-%m-%d"),
#                 }
#             })

#         # Return the data as a JSON response
#         return JsonResponse(data, safe=False)


class FetchPendingLeaveRequests(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):  # Add request as a parameter
        # Filter for pending leave requests
        pending_leaves = LeaveFormTable.objects.filter(status="Pending")
        # Serialize the data
        data = [
            {
                "id": leave.id,
                "rollNo": leave.roll_no.id,  # Assuming roll_number is the field in ExtraInfo
                "name": leave.student_name,
                "form": leave.upload_file.url if leave.upload_file else None,
                "details": {
                    "dateFrom": leave.date_from,
                    "dateTo": leave.date_to,
                    "leaveType": leave.leave_type,
                    "address": leave.address,
                    "purpose": leave.purpose,
                    "hodCredential": leave.hod,
                    "mobileNumber": leave.stud_mobile_no,
                    "parentsMobile": leave.parent_mobile_no,
                    "mobileDuringLeave": leave.leave_mobile_no,
                    "semester": leave.curr_sem,
                    "academicYear": leave.date_of_application.year,
                    "dateOfApplication": leave.date_of_application,
                },
            }
            for leave in pending_leaves
        ]
        return Response(data)
    
class UpdateLeaveStatus(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Get the list of approved and rejected leave ids from the request
        approved_leaves_ids = request.data.get('approvedLeaves', [])
        rejected_leaves_ids = request.data.get('rejectedLeaves', [])

        # Update the status of approved leaves
        approved_leaves = LeaveFormTable.objects.filter(id__in=approved_leaves_ids)
        approved_leaves.update(status="Approved")

        # Update the status of rejected leaves
        rejected_leaves = LeaveFormTable.objects.filter(id__in=rejected_leaves_ids)
        rejected_leaves.update(status="Rejected")

        return Response({"message": "Leave statuses updated successfully."})
    

class GetLeaveRequests(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Get roll_no and username from query params
        
        roll_no_id = request.query_params.get('roll_no')
        username = request.query_params.get('username')
        print(roll_no_id,username)
        
        # print(f"Received roll_no: {roll_no_id}, username: {username}")


        # # Filter the leave requests based on roll_no and student_name (username)
        leave_requests = LeaveFormTable.objects.filter(
            roll_no=roll_no_id
        )

        # Serialize the data (assuming the serializer is defined for LeaveFormTable)
        data = [
            {
                "rollNo": roll_no_id,  # Assuming roll_number is the field in ExtraInfo
                "name": leave.student_name,
                "dateFrom": leave.date_from,
                "dateTo": leave.date_to,
                "leaveType": leave.leave_type,
                "attachment": leave.upload_file.url if leave.upload_file else None,
                "purpose": leave.purpose,
                "address": leave.address,
                "action": leave.status,
            }
            for leave in leave_requests
        ]
        print(data) 

        return Response(data, status=status.HTTP_200_OK)



class BonafideFormSubmitView(APIView):
    """
    API view to handle Bonafide form submission.
    """

    permission_classes = [IsAuthenticated] 

    def post(self, request):
        # Extract data from the request
        data = request.POST
        file = request.FILES.get('related_document')  # Handle the file if uploaded

        try:
            # Create a new BonafideFormTableUpdated instance and save it to the database
            bonafide_form = BonafideFormTableUpdated.objects.create(
                student_names=f"{request.user.first_name} {request.user.last_name}",
                roll_nos=request.user.extrainfo,  # Assuming `extrainfo` is the user's ExtraInfo instance
                branch_types=data.get('branch'),
                semester_types=data.get('semester'),
                purposes=data.get('purpose'),
                date_of_applications=date.today(),
                download_file=file.name if file else "unavailable",
                approve=False,  # Default value
                reject=False,  # Default value
            )

            # Notify the academic admin about the new bonafide application
            acad_admin_des_id = Designation.objects.get(name="acadadmin")
            user_ids = HoldsDesignation.objects.filter(designation_id=acad_admin_des_id.id).values_list('user_id', flat=True)

            if user_ids.exists():
                bonafide_receiver = User.objects.get(id=user_ids[0])
                message = "A new Bonafide application has been submitted."
                otheracademic_notif(
                    request.user, 
                    bonafide_receiver, 
                    'bonafide', 
                    bonafide_form.id, 
                    'student', 
                    message
                )

            return Response(
                {"message": "Your bonafide form has been successfully submitted."},
                status=status.HTTP_201_CREATED
            )

        except Exception as e:
            return Response(
                {"error": f"An error occurred: {str(e)}"},
                status=status.HTTP_400_BAD_REQUEST
            )
        


 

 

class FetchPendingBonafideRequests(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Fetch Bonafide requests where both approve and reject are False (unseen requests)
        pending_bonafides = BonafideFormTableUpdated.objects.filter(approve=False, reject=False)
        
        # Prepare response data
        data = [
            {
                "id": bonafide.id,
                "rollNo": bonafide.roll_nos_id,  # Assuming roll_no is a field in ExtraInfo
                "name": bonafide.student_names,
                "details": {
                    "purpose": bonafide.purposes,
                    "dateOfApplication": bonafide.date_of_applications,
                    "semester": bonafide.semester_types,
                },
            }
            for bonafide in pending_bonafides
        ]
        
        return Response(data)



 

 

class UpdateBonafideStatus(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Get the lists of approved and rejected bonafide request IDs from the request body
        approved_bonafides_ids = request.data.get('approvedBonafides', [])
        rejected_bonafides_ids = request.data.get('rejectedBonafides', [])

        # Update the approve/reject status based on the provided lists
        if approved_bonafides_ids:
           BonafideFormTableUpdated.objects.filter(id__in=approved_bonafides_ids).update(approve=True, reject=False)

        if rejected_bonafides_ids:
            BonafideFormTableUpdated.objects.filter(id__in=rejected_bonafides_ids).update(approve=False, reject=True)

        return Response({"message": "Bonafide statuses updated successfully."})



class GetBonafideStatus(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Get roll number and username from the request
        roll_no = request.data.get("roll_no")
        username = request.data.get("username")

        # Check if roll number and username are provided
        if not roll_no or not username:
            return Response(
                {"error": "Roll number and username are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            # Query bonafide forms for the given roll number
            bonafide_requests = BonafideFormTableUpdated.objects.filter(roll_nos_id=roll_no)
            
            # Manually format the response data
            response_data = [
                {
                    "rollNo": bonafide.roll_nos_id,
                    "name": bonafide.student_names,
                    "branch": bonafide.branch_types,
                    "semester": bonafide.semester_types,
                    "purpose": bonafide.purposes,
                    "dateApplied": bonafide.date_of_applications.strftime("%Y-%m-%d") if bonafide.date_of_applications else None,
                    "status": (
                        "Approved" if bonafide.approve else "Rejected" if bonafide.reject else "Pending"
                    ),
                }
                for bonafide in bonafide_requests
            ]

            return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": "An error occurred while fetching bonafide status.", "details": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


            return Response({'message': 'Form submitted successfully', 'bonafide_id': bonafide.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt  # Exempt CSRF verification for this view
@login_required
def leave_form_submit(request):
    """
    View function for submitting a leave form.

    Description:
        This function handles form submission for leave requests, processes the data, and saves it to the database.
        It also notifies the relevant authority about the new leave application.
    """
    if request.method == 'POST':
        # Extract data from the request
        data = request.POST
        file = request.FILES.get('related_document')
        hodname = data.get('hod_credential')
        
        # Create a new LeaveFormTable instance and save it to the database
        leave = LeaveFormTable.objects.create(
            student_name=request.user.first_name+request.user.last_name,
            roll_no=request.user.extrainfo,
            date_from=data.get('date_from'),
            date_to=data.get('date_to'),
            leave_type=data.get('leave_type'),
            upload_file=file,
            address=data.get('address'),
            purpose=data.get('purpose'),
            date_of_application=date.today(),
            hod=data.get('hod_credential')
        )
        
        leave_hod = User.objects.get(username=hodname)
        receiver_value = User.objects.get(username=request.user.username)
        receiver_value_designation = HoldsDesignation.objects.filter(user=receiver_value)
        lis = list(receiver_value_designation)
        obj = lis[0].designation

        file_id = create_file(
            uploader=request.user.username,
            uploader_designation=obj,
            receiver=leave_hod,
            receiver_designation="student",
            src_module="otheracademic",
            src_object_id=leave.id,
            file_extra_JSON={"value": 2},
            attached_file=None,
            subject='ug_leave'
        )


        message = "A new leave application"
        otheracademic_notif(request.user, leave_hod, 'ug_leave_hod', leave.id, 'student', message)
        if leave:
            messages.success(request, "You successfully submitted your form")
            
        # return HttpResponseRedirect('/otheracademic/leaveform')

