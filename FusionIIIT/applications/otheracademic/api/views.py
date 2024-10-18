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
from django.contrib.auth.models import User
from applications.otheracademic.models import (LeaveFormTable, BonafideFormTableUpdated, GraduateSeminarFormTable, 
                                               AssistantshipClaimFormStatusUpd, LeavePG, NoDues)
from datetime import date
from applications.filetracking.models import File
from applications.filetracking.sdk.methods import create_file
from notification.views import otheracademic_notif
from applications.filetracking.models import *
from applications.filetracking.sdk.methods import *
from applications.globals.models import ExtraInfo, HoldsDesignation, Designation


class LeaveFormSubmitView(APIView):
    permission_classes = [IsAuthenticated] 

    def post(self, request):
      
        data = request.data
        file = request.FILES.get('related_document')  
        hodname = data.get('hod_credential')

      
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

        if serializer.is_valid():
            leave = serializer.save()

       
            leave_hod = User.objects.get(username=hodname)
            receiver_value = User.objects.get(username=request.user.username)
            receiver_value_designation = HoldsDesignation.objects.filter(user=receiver_value).first()
            obj = receiver_value_designation.designation

     
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

        
            return Response({"message": "You successfully submitted your form"}, status=status.HTTP_201_CREATED)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class BonafideFormSubmitView(APIView):
    """
    API view to handle Bonafide form submission
    """

    permission_classes = [IsAuthenticated]

    def post(self, request):

        data = request.data
        # file = request.FILES.get('related_document')

        bonafide_data = {
            'student_names': data.get('student_name'),
            'roll_nos': data.get('roll_no'),
            'branch_types': data.get('branch'),
            'semester_types': data.get('semester'),
            'purposes': data.get('purpose'),
            'date_of_applications': date.today(),
            'download_file': "not available",
        }


        serializer = BonafideFormSerializer(data=bonafide_data)

        if serializer.is_valid():

            bonafide = serializer.save()

            # if file:

            #     bonafide.download_file = "/" 
            #     bonafide.save()

         
            acad_admin_des_id = Designation.objects.get(name="acadadmin")
            user_ids = HoldsDesignation.objects.filter(designation_id=acad_admin_des_id.id).values_list('user_id', flat=True)
            bonafide_receiver = User.objects.get(id=user_ids[0])
            message = 'A Bonafide application has been received'
            otheracademic_notif(request.user, bonafide_receiver, 'bonafide', 1, 'student', message)

            return Response({'message': 'Form submitted successfully', 'bonafide_id': bonafide.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)