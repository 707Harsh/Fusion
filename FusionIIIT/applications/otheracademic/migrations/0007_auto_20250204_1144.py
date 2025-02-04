# Generated by Django 3.1.5 on 2025-02-04 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otheracademic', '0006_leaveformtable_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bonafideformtableupdated',
            name='status',
        ),
        migrations.RemoveField(
            model_name='leavepg',
            name='Semester',
        ),
        migrations.RemoveField(
            model_name='leavepg',
            name='alt_mobile_no',
        ),
        migrations.RemoveField(
            model_name='leavepg',
            name='discipline',
        ),
        migrations.RemoveField(
            model_name='leavepg',
            name='hod_approved',
        ),
        migrations.RemoveField(
            model_name='leavepg',
            name='hod_rejected',
        ),
        migrations.RemoveField(
            model_name='leavepg',
            name='mobile_no',
        ),
        migrations.RemoveField(
            model_name='leavepg',
            name='programme',
        ),
        migrations.RemoveField(
            model_name='leavepg',
            name='ta_approved',
        ),
        migrations.RemoveField(
            model_name='leavepg',
            name='ta_rejected',
        ),
        migrations.RemoveField(
            model_name='leavepg',
            name='thesis_approved',
        ),
        migrations.RemoveField(
            model_name='leavepg',
            name='thesis_rejected',
        ),
        migrations.AddField(
            model_name='bonafideformtableupdated',
            name='approve',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bonafideformtableupdated',
            name='reject',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='leaveformtable',
            name='curr_sem',
            field=models.IntegerField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='leaveformtable',
            name='leave_mobile_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='leaveformtable',
            name='parent_mobile_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='leaveformtable',
            name='stud_mobile_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='leavepg',
            name='curr_sem',
            field=models.IntegerField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='leavepg',
            name='leave_mobile_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='leavepg',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=20),
        ),
        migrations.AddField(
            model_name='leavepg',
            name='stud_mobile_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='assistantshipclaimformstatusupd',
            name='student_signature',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='leavepg',
            name='parent_mobile_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='leavepg',
            name='upload_file',
            field=models.FileField(blank=True, null=True, upload_to='leave_documents/'),
        ),
    ]
