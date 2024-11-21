# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Application(models.Model):
    application_id = models.CharField(primary_key=True, max_length=100)
    applied_flag = models.BooleanField()
    award = models.CharField(max_length=30)
    student_id = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Application'


class AssignedTeachingCredits(models.Model):
    assigned_course = models.CharField(max_length=100)
    roll_no = models.ForeignKey('TeachingCredits1', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Assigned_Teaching_credits'


class Assistantship(models.Model):
    file = models.CharField(max_length=100, blank=True, null=True)
    action = models.IntegerField()
    comments = models.CharField(max_length=150, blank=True, null=True)
    instructor_id = models.ForeignKey('CurriculumInstructor', models.DO_NOTHING)
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Assistantship'
        unique_together = (('student_id', 'instructor_id'),)


class Assistantshipclaimformstausupd(models.Model):
    student_name = models.CharField(max_length=100)
    discipline = models.CharField(max_length=100)
    datefrom = models.DateField(db_column='dateFrom')  # Field name made lowercase.
    dateto = models.DateField(db_column='dateTo')  # Field name made lowercase.
    bank_account = models.CharField(max_length=100)
    student_signature = models.CharField(max_length=100)
    dateapplied = models.DateField(db_column='dateApplied')  # Field name made lowercase.
    ta_supervisor = models.CharField(max_length=100)
    thesis_supervisor = models.CharField(max_length=100)
    hod = models.CharField(max_length=100)
    applicability = models.CharField(max_length=100)
    ta_approved = models.BooleanField(db_column='TA_approved')  # Field name made lowercase.
    ta_rejected = models.BooleanField(db_column='TA_rejected')  # Field name made lowercase.
    ths_approved = models.BooleanField(db_column='Ths_approved')  # Field name made lowercase.
    ths_rejected = models.BooleanField(db_column='Ths_rejected')  # Field name made lowercase.
    hod_approved = models.BooleanField(db_column='HOD_approved')  # Field name made lowercase.
    hod_rejected = models.BooleanField(db_column='HOD_rejected')  # Field name made lowercase.
    acad_approved = models.BooleanField(db_column='Acad_approved')  # Field name made lowercase.
    acad_rejected = models.BooleanField(db_column='Acad_rejected')  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    half_day_leave = models.IntegerField()
    full_day_leave = models.IntegerField()
    remark = models.TextField()
    roll_no = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'AssistantshipClaimFormStausUpd'


class AwardAndScholarship(models.Model):
    award_name = models.CharField(max_length=100)
    catalog = models.TextField()

    class Meta:
        managed = False
        db_table = 'Award_and_scholarship'


class Bonafide(models.Model):
    student_name = models.CharField(max_length=50)
    purpose = models.CharField(max_length=100)
    academic_year = models.CharField(max_length=15)
    enrolled_course = models.CharField(max_length=10)
    complaint_date = models.DateTimeField()
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Bonafide'


class Bonafideformtableupdated(models.Model):
    student_names = models.CharField(max_length=100)
    branch_types = models.CharField(max_length=50)
    semester_types = models.CharField(max_length=20)
    purposes = models.TextField()
    date_of_applications = models.DateField()
    download_file = models.CharField(max_length=20)
    roll_nos = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'BonafideFormTableUpdated'


class Cpda(models.Model):
    pf_no = models.CharField(db_column='PF_no', max_length=100)  # Field name made lowercase.
    purpose = models.CharField(max_length=100)
    amoutn = models.IntegerField()
    designation = models.ForeignKey('GlobalsDesignation', models.DO_NOTHING)
    name = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'CPDA'


class Calendar(models.Model):
    from_date = models.DateField()
    to_date = models.DateField()
    description = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'Calendar'


class ChangeOffice(models.Model):
    status = models.CharField(max_length=50)
    date_request = models.DateTimeField()
    date_approve = models.DateTimeField()
    remarks = models.CharField(max_length=256, blank=True, null=True)
    club = models.ForeignKey('ClubInfo', models.DO_NOTHING)
    co_coordinator = models.ForeignKey('AuthUser', models.DO_NOTHING)
    co_ordinator = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Change_office'


class ClubBudget(models.Model):
    budget_for = models.CharField(max_length=256)
    budget_amt = models.IntegerField()
    budget_file = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=50)
    remarks = models.CharField(max_length=256, blank=True, null=True)
    club = models.ForeignKey('ClubInfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Club_budget'


class ClubInfo(models.Model):
    club_name = models.CharField(primary_key=True, max_length=50)
    club_website = models.CharField(max_length=150, blank=True, null=True)
    category = models.CharField(max_length=50)
    club_file = models.CharField(max_length=100, blank=True, null=True)
    activity_calender = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    alloted_budget = models.IntegerField(blank=True, null=True)
    spent_budget = models.IntegerField(blank=True, null=True)
    avail_budget = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50)
    co_coordinator = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)
    co_ordinator = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)
    faculty_incharge = models.ForeignKey('GlobalsFaculty', models.DO_NOTHING)
    created_on = models.DateField(blank=True, null=True)
    head_changed_on = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Club_info'


class ClubMember(models.Model):
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50)
    remarks = models.CharField(max_length=256, blank=True, null=True)
    club = models.ForeignKey(ClubInfo, models.DO_NOTHING)
    member = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Club_member'


class ClubReport(models.Model):
    event_name = models.CharField(max_length=50)
    date = models.DateTimeField()
    event_details = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    club = models.ForeignKey(ClubInfo, models.DO_NOTHING)
    incharge = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Club_report'


class CoreTeam(models.Model):
    team = models.CharField(max_length=50)
    year = models.DateTimeField(blank=True, null=True)
    fest_name = models.CharField(max_length=256)
    pda = models.TextField()
    remarks = models.CharField(max_length=256, blank=True, null=True)
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Core_team'


class Course(models.Model):
    course_name = models.CharField(max_length=600)
    course_details = models.TextField()

    class Meta:
        managed = False
        db_table = 'Course'


class Courserequested(models.Model):
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'CourseRequested'


class CpdaApplication(models.Model):
    status = models.CharField(max_length=20, blank=True, null=True)
    pf_number = models.CharField(max_length=50, blank=True, null=True)
    purpose = models.CharField(max_length=500)
    requested_advance = models.IntegerField()
    request_timestamp = models.DateTimeField(blank=True, null=True)
    adjustment_amount = models.IntegerField(blank=True, null=True)
    bills_attached = models.IntegerField(blank=True, null=True)
    total_bills_amount = models.IntegerField(blank=True, null=True)
    ppa_register_page_no = models.IntegerField(blank=True, null=True)
    adjustment_timestamp = models.DateTimeField(blank=True, null=True)
    applicant = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Cpda Application'


class CpdaBills(models.Model):
    bill = models.CharField(max_length=100)
    application = models.ForeignKey(CpdaApplication, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cpda Bills'


class CpdaTracking(models.Model):
    application = models.OneToOneField(CpdaApplication, models.DO_NOTHING, primary_key=True)
    current_reviewer_id = models.IntegerField()
    remarks = models.CharField(max_length=250, blank=True, null=True)
    remarks_rev1 = models.CharField(max_length=250, blank=True, null=True)
    remarks_rev2 = models.CharField(max_length=250, blank=True, null=True)
    remarks_rev3 = models.CharField(max_length=250, blank=True, null=True)
    review_status = models.CharField(max_length=20, blank=True, null=True)
    bill = models.CharField(max_length=100, blank=True, null=True)
    reviewer_design = models.ForeignKey('GlobalsDesignation', models.DO_NOTHING, blank=True, null=True)
    reviewer_design2 = models.ForeignKey('GlobalsDesignation', models.DO_NOTHING, blank=True, null=True)
    reviewer_design3 = models.ForeignKey('GlobalsDesignation', models.DO_NOTHING, blank=True, null=True)
    reviewer_id = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    reviewer_id2 = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    reviewer_id3 = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cpda Tracking'


class Curriculum(models.Model):
    curriculum_id = models.AutoField(primary_key=True)
    course_code = models.CharField(max_length=20)
    credits = models.IntegerField()
    course_type = models.CharField(max_length=25)
    programme = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)
    batch = models.IntegerField()
    sem = models.IntegerField()
    optional = models.BooleanField()
    floated = models.BooleanField()
    course_id = models.ForeignKey(Course, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Curriculum'
        unique_together = (('course_code', 'batch', 'programme'),)


class CurriculumInstructor(models.Model):
    chief_inst = models.BooleanField()
    curriculum_id = models.ForeignKey(Curriculum, models.DO_NOTHING)
    instructor_id = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Curriculum_Instructor'
        unique_together = (('curriculum_id', 'instructor_id'),)


class DirectorGold(models.Model):
    status = models.CharField(max_length=10)
    relevant_document = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    academic_achievements = models.TextField(blank=True, null=True)
    science_inside = models.TextField(blank=True, null=True)
    science_outside = models.TextField(blank=True, null=True)
    games_inside = models.TextField(blank=True, null=True)
    games_outside = models.TextField(blank=True, null=True)
    cultural_inside = models.TextField(blank=True, null=True)
    cultural_outside = models.TextField(blank=True, null=True)
    social = models.TextField(blank=True, null=True)
    corporate = models.TextField(blank=True, null=True)
    hall_activities = models.TextField(blank=True, null=True)
    gymkhana_activities = models.TextField(blank=True, null=True)
    institute_activities = models.TextField(blank=True, null=True)
    counselling_activities = models.TextField(blank=True, null=True)
    other_activities = models.TextField(blank=True, null=True)
    justification = models.TextField(blank=True, null=True)
    correspondence_address = models.CharField(max_length=100, blank=True, null=True)
    financial_assistance = models.TextField(blank=True, null=True)
    grand_total = models.IntegerField(blank=True, null=True)
    nearest_policestation = models.CharField(max_length=25, blank=True, null=True)
    nearest_railwaystation = models.CharField(max_length=25, blank=True, null=True)
    award_id = models.ForeignKey(AwardAndScholarship, models.DO_NOTHING)
    student = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Director_gold'


class DirectorSilver(models.Model):
    nearest_policestation = models.TextField()
    nearest_railwaystation = models.TextField()
    correspondence_address = models.TextField(blank=True, null=True)
    award_type = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=10)
    relevant_document = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    financial_assistance = models.TextField(blank=True, null=True)
    grand_total = models.IntegerField(blank=True, null=True)
    inside_achievements = models.TextField(blank=True, null=True)
    justification = models.TextField(blank=True, null=True)
    outside_achievements = models.TextField(blank=True, null=True)
    award_id = models.ForeignKey(AwardAndScholarship, models.DO_NOTHING)
    student = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Director_silver'


class Dues(models.Model):
    mess_due = models.IntegerField()
    hostel_due = models.IntegerField()
    library_due = models.IntegerField()
    placement_cell_due = models.IntegerField()
    academic_due = models.IntegerField()
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Dues'


class EventInfo(models.Model):
    event_name = models.CharField(max_length=256)
    venue = models.CharField(max_length=50)
    incharge = models.CharField(max_length=256)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)
    event_poster = models.CharField(max_length=100)
    details = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50)
    club = models.ForeignKey(ClubInfo, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Event_info'


class ExamTimetable(models.Model):
    upload_date = models.DateField()
    exam_time_table = models.CharField(max_length=100)
    batch = models.IntegerField()
    programme = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Exam_Timetable'


class Feepayments(models.Model):
    mode = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=40)
    fee_receipt = models.CharField(max_length=100, blank=True, null=True)
    deposit_date = models.DateField()
    utr_number = models.CharField(max_length=40, blank=True, null=True)
    fee_paid = models.IntegerField()
    reason = models.CharField(max_length=20, blank=True, null=True)
    actual_fee = models.IntegerField()
    semester_id = models.ForeignKey('ProgrammeCurriculumSemester', models.DO_NOTHING)
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'FeePayments'


class FestBudget(models.Model):
    fest = models.CharField(max_length=50)
    budget_amt = models.IntegerField()
    budget_file = models.CharField(max_length=100)
    year = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField()
    status = models.CharField(max_length=50)
    remarks = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fest_budget'


class File(models.Model):
    subject = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    upload_date = models.DateTimeField()
    upload_file = models.CharField(max_length=100, blank=True, null=True)
    is_read = models.BooleanField()
    designation = models.ForeignKey('GlobalsDesignation', models.DO_NOTHING, blank=True, null=True)
    uploader = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)
    file_extra_json = models.JSONField(db_column='file_extra_JSON', blank=True, null=True)  # Field name made lowercase.
    src_module = models.CharField(max_length=100)
    src_object_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'File'


class Finalregistration(models.Model):
    verified = models.BooleanField()
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)
    course_slot_id = models.ForeignKey('ProgrammeCurriculumCourseslot', models.DO_NOTHING, blank=True, null=True)
    semester_id = models.ForeignKey('ProgrammeCurriculumSemester', models.DO_NOTHING)
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'FinalRegistration'


class Finalregistrations(models.Model):
    semester = models.IntegerField()
    batch = models.IntegerField()
    verified = models.BooleanField()
    curr_id = models.ForeignKey(Curriculum, models.DO_NOTHING)
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'FinalRegistrations'


class FormAvailable(models.Model):
    roll = models.CharField(primary_key=True, max_length=7)
    status = models.BooleanField()
    form_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'Form_available'


class Grades(models.Model):
    grade = models.CharField(max_length=4)
    verify = models.BooleanField()
    curriculum_id = models.ForeignKey(Curriculum, models.DO_NOTHING)
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Grades'


class Graduateseminarformtable(models.Model):
    roll_no = models.CharField(max_length=20)
    semester = models.CharField(max_length=100)
    date_of_seminar = models.DateField()

    class Meta:
        managed = False
        db_table = 'GraduateSeminarFormTable'


class Holiday(models.Model):
    holiday_date = models.DateField()
    holiday_name = models.CharField(max_length=40)
    holiday_type = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'Holiday'


class Indentfile(models.Model):
    file_info = models.OneToOneField(File, models.DO_NOTHING, primary_key=True)
    item_name = models.CharField(max_length=250)
    quantity = models.IntegerField()
    present_stock = models.IntegerField()
    estimated_cost = models.IntegerField(blank=True, null=True)
    purpose = models.CharField(max_length=250)
    specification = models.CharField(max_length=250)
    item_type = models.CharField(max_length=250)
    nature = models.BooleanField()
    indigenous = models.BooleanField()
    replaced = models.BooleanField()
    budgetary_head = models.CharField(max_length=250)
    expected_delivery = models.DateField()
    sources_of_supply = models.CharField(max_length=250)
    head_approval = models.BooleanField()
    director_approval = models.BooleanField()
    financial_approval = models.BooleanField()
    purchased = models.BooleanField()
    item_subtype = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'IndentFile'


class Initialregistration(models.Model):
    timestamp = models.DateTimeField()
    priority = models.IntegerField(blank=True, null=True)
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING, blank=True, null=True)
    course_slot_id = models.ForeignKey('ProgrammeCurriculumCourseslot', models.DO_NOTHING, blank=True, null=True)
    semester_id = models.ForeignKey('ProgrammeCurriculumSemester', models.DO_NOTHING, blank=True, null=True)
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'InitialRegistration'


class Initialregistrations(models.Model):
    timestamp = models.DateTimeField()
    priority = models.IntegerField(blank=True, null=True)
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING, blank=True, null=True)
    course_slot_id = models.ForeignKey('ProgrammeCurriculumCourseslot', models.DO_NOTHING, blank=True, null=True)
    semester_id = models.ForeignKey('ProgrammeCurriculumSemester', models.DO_NOTHING, blank=True, null=True)
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'InitialRegistrations'


class Inventory(models.Model):
    club_name = models.OneToOneField(ClubInfo, models.DO_NOTHING, primary_key=True)
    inventory = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'Inventory'


class Ltc(models.Model):
    date_request = models.DateField()
    travel_mode = models.CharField(max_length=10)
    advance = models.IntegerField()
    family_details = models.TextField()
    department = models.ForeignKey('GlobalsDepartmentinfo', models.DO_NOTHING)
    designation = models.ForeignKey('GlobalsDesignation', models.DO_NOTHING)
    leave = models.ForeignKey('LeaveLeave', models.DO_NOTHING)
    name = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'LTC'


class Lab(models.Model):
    lab = models.CharField(max_length=10)
    lab_instructor = models.CharField(max_length=30)
    day = models.CharField(max_length=10)
    s_time = models.CharField(max_length=6)
    e_time = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'Lab'


class Leaveformtable(models.Model):
    student_name = models.CharField(max_length=100)
    date_from = models.DateField()
    date_to = models.DateField()
    date_of_application = models.DateField()
    upload_file = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100)
    purpose = models.TextField()
    leave_type = models.CharField(max_length=20)
    hod = models.CharField(max_length=100)
    roll_no = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)
    status = models.CharField(max_length=20, blank=True, null=True)
    stud_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    parent_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    leave_mobile_no = models.CharField(max_length=20, blank=True, null=True)
    curr_sem = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LeaveFormTable'


class Leavepg(models.Model):
    student_name = models.CharField(max_length=100)
    curr_sem = models.CharField(max_length=100)
    date_from = models.DateField()
    date_to = models.DateField()
    date_of_application = models.DateField()
    upload_file = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    purpose = models.TextField()
    leave_type = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=100)
    parent_mobile_no = models.CharField(max_length=100)
    alt_mobile_no = models.CharField(max_length=100)
    roll_no = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)
    status = models.CharField(max_length=20, blank=True, null=True)
    hod = models.CharField(max_length=100, blank=True, null=True)
    ta_supervisor = models.CharField(max_length=100, blank=True, null=True)
    thesis_supervisor = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'LeavePG'


class Leavepgupdtable(models.Model):
    student_name = models.CharField(max_length=100)
    programme = models.CharField(max_length=100)
    discipline = models.CharField(max_length=100)
    semester = models.CharField(db_column='Semester', max_length=100)  # Field name made lowercase.
    date_from = models.DateField()
    date_to = models.DateField()
    date_of_application = models.DateField()
    upload_file = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    purpose = models.TextField()
    leave_type = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=100)
    parent_mobile_no = models.CharField(max_length=100)
    alt_mobile_no = models.CharField(max_length=100)
    ta_approved = models.BooleanField()
    ta_rejected = models.BooleanField()
    hod_approved = models.BooleanField()
    hod_rejected = models.BooleanField()
    ta_supervisor = models.CharField(max_length=100)
    hod = models.CharField(max_length=100)
    roll_no = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'LeavePGUpdTable'


class LtcApplication(models.Model):
    status = models.CharField(max_length=20, blank=True, null=True)
    pf_number = models.CharField(max_length=50)
    basic_pay = models.IntegerField()
    leave_start = models.DateField(blank=True, null=True)
    leave_end = models.DateField()
    family_departure_date = models.DateField()
    leave_nature = models.CharField(max_length=50)
    purpose = models.CharField(max_length=500)
    is_hometown_or_elsewhere = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    address_during_leave = models.CharField(max_length=500)
    travel_mode = models.CharField(max_length=50)
    ltc_availed = models.CharField(max_length=100)
    ltc_to_avail = models.CharField(max_length=200)
    dependents = models.CharField(max_length=500)
    requested_advance = models.IntegerField()
    request_timestamp = models.DateTimeField(blank=True, null=True)
    review_timestamp = models.DateTimeField(blank=True, null=True)
    applicant = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Ltc Application'


class LtcTracking(models.Model):
    application = models.OneToOneField(LtcApplication, models.DO_NOTHING, primary_key=True)
    designations = models.CharField(max_length=350, blank=True, null=True)
    remarks = models.CharField(max_length=350, blank=True, null=True)
    review_status = models.CharField(max_length=20, blank=True, null=True)
    admin_remarks = models.CharField(max_length=200, blank=True, null=True)
    reviewer_design = models.ForeignKey('GlobalsDesignation', models.DO_NOTHING, blank=True, null=True)
    reviewer_id = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ltc Tracking'


class Marksubmissioncheck(models.Model):
    verified = models.BooleanField()
    submitted = models.BooleanField()
    announced = models.BooleanField()
    curr_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'MarkSubmissionCheck'


class Mcm(models.Model):
    brother_name = models.CharField(max_length=30, blank=True, null=True)
    brother_occupation = models.TextField(blank=True, null=True)
    sister_name = models.CharField(max_length=30, blank=True, null=True)
    sister_occupation = models.TextField(blank=True, null=True)
    income_father = models.IntegerField()
    income_mother = models.IntegerField()
    income_other = models.IntegerField()
    father_occ = models.CharField(max_length=10)
    mother_occ = models.CharField(max_length=10)
    father_occ_desc = models.CharField(max_length=30, blank=True, null=True)
    mother_occ_desc = models.CharField(max_length=30, blank=True, null=True)
    four_wheeler = models.IntegerField(blank=True, null=True)
    four_wheeler_desc = models.CharField(max_length=30, blank=True, null=True)
    two_wheeler = models.IntegerField(blank=True, null=True)
    two_wheeler_desc = models.CharField(max_length=30, blank=True, null=True)
    house = models.CharField(max_length=10, blank=True, null=True)
    plot_area = models.IntegerField(blank=True, null=True)
    constructed_area = models.IntegerField(blank=True, null=True)
    school_fee = models.IntegerField(blank=True, null=True)
    school_name = models.CharField(max_length=30, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    loan_amount = models.IntegerField(blank=True, null=True)
    college_fee = models.IntegerField(blank=True, null=True)
    college_name = models.CharField(max_length=30, blank=True, null=True)
    income_certificate = models.CharField(max_length=100, blank=True, null=True)
    forms = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=10)
    annual_income = models.IntegerField()
    date = models.DateField()
    award_id = models.ForeignKey(AwardAndScholarship, models.DO_NOTHING)
    student = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Mcm'


class Meeting(models.Model):
    venue = models.CharField(max_length=50)
    date = models.DateField()
    time = models.CharField(max_length=20)
    agenda = models.TextField()
    minutes_file = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'Meeting'


class Member(models.Model):
    meeting_id = models.ForeignKey(Meeting, models.DO_NOTHING)
    member_id = models.ForeignKey('GlobalsFaculty', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Member'
        unique_together = (('member_id', 'meeting_id'),)


class Nodues(models.Model):
    name = models.CharField(max_length=100)
    library_clear = models.BooleanField()
    library_notclear = models.BooleanField()
    hostel_clear = models.BooleanField()
    hostel_notclear = models.BooleanField()
    mess_clear = models.BooleanField()
    mess_notclear = models.BooleanField()
    ece_clear = models.BooleanField()
    ece_notclear = models.BooleanField()
    physics_lab_clear = models.BooleanField()
    physics_lab_notclear = models.BooleanField()
    mechatronics_lab_clear = models.BooleanField()
    mechatronics_lab_notclear = models.BooleanField()
    cc_clear = models.BooleanField()
    cc_notclear = models.BooleanField()
    workshop_clear = models.BooleanField()
    workshop_notclear = models.BooleanField()
    signal_processing_lab_clear = models.BooleanField()
    signal_processing_lab_notclear = models.BooleanField()
    vlsi_clear = models.BooleanField()
    vlsi_notclear = models.BooleanField()
    design_studio_clear = models.BooleanField()
    design_studio_notclear = models.BooleanField()
    design_project_clear = models.BooleanField()
    design_project_notclear = models.BooleanField()
    bank_clear = models.BooleanField()
    bank_notclear = models.BooleanField()
    icard_dsa_clear = models.BooleanField()
    icard_dsa_notclear = models.BooleanField()
    account_clear = models.BooleanField()
    account_notclear = models.BooleanField()
    btp_supervisor_clear = models.BooleanField()
    btp_supervisor_notclear = models.BooleanField()
    discipline_office_clear = models.BooleanField()
    discipline_office_notclear = models.BooleanField()
    student_gymkhana_clear = models.BooleanField()
    student_gymkhana_notclear = models.BooleanField()
    alumni_clear = models.BooleanField()
    alumni_notclear = models.BooleanField()
    placement_cell_clear = models.BooleanField()
    placement_cell_notclear = models.BooleanField()
    hostel_credential = models.CharField(max_length=100)
    bank_credential = models.CharField(max_length=100)
    btp_credential = models.CharField(max_length=100)
    cse_credential = models.CharField(max_length=100)
    design_credential = models.CharField(max_length=100)
    acad_credential = models.CharField(max_length=100)
    ece_credential = models.CharField(max_length=100)
    library_credential = models.CharField(max_length=100)
    me_credential = models.CharField(max_length=100)
    mess_credential = models.CharField(max_length=100)
    physics_credential = models.CharField(max_length=100)
    discipline_credential = models.CharField(max_length=100)
    acad_admin_float = models.BooleanField()
    roll_no = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'NoDues'


class Notification(models.Model):
    notification_mcm_flag = models.BooleanField()
    notification_convocation_flag = models.BooleanField()
    invite_mcm_accept_flag = models.BooleanField()
    invite_convocation_accept_flag = models.BooleanField()
    release_id = models.ForeignKey('Release', models.DO_NOTHING)
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Notification'


class NotionalPrize(models.Model):
    spi = models.FloatField()
    cpi = models.FloatField()
    year = models.CharField(max_length=10)
    award_id = models.ForeignKey(AwardAndScholarship, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Notional_prize'


class OtherReport(models.Model):
    event_name = models.CharField(max_length=50)
    date = models.DateTimeField()
    event_details = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    incharge = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Other_report'


class PreviousWinner(models.Model):
    programme = models.CharField(max_length=10)
    year = models.IntegerField()
    award_id = models.ForeignKey(AwardAndScholarship, models.DO_NOTHING)
    student = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Previous_winner'


class ProficiencyDm(models.Model):
    relevant_document = models.CharField(max_length=100, blank=True, null=True)
    title_name = models.CharField(max_length=30, blank=True, null=True)
    award_type = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=10)
    no_of_students = models.IntegerField()
    date = models.DateField()
    roll_no1 = models.IntegerField()
    roll_no2 = models.IntegerField()
    roll_no3 = models.IntegerField()
    roll_no4 = models.IntegerField()
    roll_no5 = models.IntegerField()
    brief_description = models.TextField(blank=True, null=True)
    justification = models.TextField(blank=True, null=True)
    ece_topic = models.CharField(max_length=25, blank=True, null=True)
    cse_topic = models.CharField(max_length=25, blank=True, null=True)
    mech_topic = models.CharField(max_length=25, blank=True, null=True)
    design_topic = models.CharField(max_length=25, blank=True, null=True)
    ece_percentage = models.IntegerField(blank=True, null=True)
    cse_percentage = models.IntegerField(blank=True, null=True)
    mech_percentage = models.IntegerField(blank=True, null=True)
    design_percentage = models.IntegerField(blank=True, null=True)
    correspondence_address = models.CharField(max_length=100, blank=True, null=True)
    financial_assistance = models.TextField(blank=True, null=True)
    grand_total = models.IntegerField(blank=True, null=True)
    nearest_policestation = models.CharField(max_length=25, blank=True, null=True)
    nearest_railwaystation = models.CharField(max_length=25, blank=True, null=True)
    award_id = models.ForeignKey(AwardAndScholarship, models.DO_NOTHING)
    student = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Proficiency_dm'


class Register(models.Model):
    year = models.IntegerField()
    semester = models.IntegerField()
    curr_id = models.ForeignKey(Curriculum, models.DO_NOTHING)
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Register'
        unique_together = (('curr_id', 'student_id'),)


class RegistrarResponse(models.Model):
    remark = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    track_id = models.ForeignKey('Tracking', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Registrar_response'


class RegistrationForm(models.Model):
    roll = models.CharField(primary_key=True, max_length=8)
    user_name = models.CharField(max_length=40)
    branch = models.CharField(max_length=20)
    cpi = models.FloatField()
    programme = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'Registration_form'


class Release(models.Model):
    date_time = models.DateTimeField()
    programme = models.CharField(max_length=10)
    startdate = models.DateField()
    enddate = models.DateField()
    award = models.CharField(max_length=50)
    remarks = models.TextField()
    batch = models.TextField()
    notif_visible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Release'


class Semestermarks(models.Model):
    q1 = models.FloatField()
    mid_term = models.FloatField()
    q2 = models.FloatField()
    end_term = models.FloatField()
    other = models.FloatField()
    grade = models.CharField(max_length=5, blank=True, null=True)
    curr_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'SemesterMarks'


class SessionInfo(models.Model):
    venue = models.CharField(max_length=50)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    session_poster = models.CharField(max_length=100, blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50)
    club = models.ForeignKey(ClubInfo, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Session_info'


class Spi(models.Model):
    sem = models.IntegerField()
    spi = models.FloatField()
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Spi'
        unique_together = (('student_id', 'sem'),)


class Stockentry(models.Model):
    item_id = models.OneToOneField(Indentfile, models.DO_NOTHING, primary_key=True)
    vendor = models.CharField(max_length=250)
    current_stock = models.IntegerField()
    recieved_date = models.DateField()
    bill = models.CharField(max_length=100)
    dealing_assistant_id = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)
    location = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'StockEntry'


class Stockitem(models.Model):
    nomenclature = models.CharField(unique=True, max_length=100)
    inuse = models.BooleanField(db_column='inUse')  # Field name made lowercase.
    location = models.CharField(max_length=100)
    istransferred = models.BooleanField(db_column='isTransferred')  # Field name made lowercase.
    stockentryid = models.ForeignKey(Stockentry, models.DO_NOTHING, db_column='StockEntryId_id')  # Field name made lowercase.
    department = models.ForeignKey('GlobalsDepartmentinfo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'StockItem'


class Stocktransfer(models.Model):
    src_location = models.CharField(max_length=100)
    dest_location = models.CharField(max_length=100)
    datetime = models.DateTimeField(db_column='dateTime')  # Field name made lowercase.
    dest_dept = models.ForeignKey('GlobalsDepartmentinfo', models.DO_NOTHING, blank=True, null=True)
    indent_file = models.ForeignKey(Indentfile, models.DO_NOTHING)
    src_dept = models.ForeignKey('GlobalsDepartmentinfo', models.DO_NOTHING, blank=True, null=True)
    stockitem = models.ForeignKey(Stockitem, models.DO_NOTHING, db_column='stockItem_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StockTransfer'


class Studentregistrationcheck(models.Model):
    pre_registration_flag = models.BooleanField()
    final_registration_flag = models.BooleanField()
    semester = models.IntegerField()
    student = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'StudentRegistrationCheck'


class Studentregistrationchecks(models.Model):
    pre_registration_flag = models.BooleanField()
    final_registration_flag = models.BooleanField()
    semester_id = models.ForeignKey('ProgrammeCurriculumSemester', models.DO_NOTHING)
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'StudentRegistrationChecks'


class StudentAttendance(models.Model):
    date = models.DateField()
    present = models.BooleanField()
    instructor_id = models.ForeignKey(CurriculumInstructor, models.DO_NOTHING)
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Student_attendance'


class TaAssign(models.Model):
    balance = models.IntegerField()
    lab = models.ForeignKey(Lab, models.DO_NOTHING)
    roll_no = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'TA_assign'


class Teachingcreditregistration(models.Model):
    req_pending = models.BooleanField()
    course_completion = models.BooleanField()
    approved_course = models.ForeignKey(Curriculum, models.DO_NOTHING, blank=True, null=True)
    curr_1 = models.ForeignKey(Curriculum, models.DO_NOTHING)
    curr_2 = models.ForeignKey(Curriculum, models.DO_NOTHING)
    curr_3 = models.ForeignKey(Curriculum, models.DO_NOTHING)
    curr_4 = models.ForeignKey(Curriculum, models.DO_NOTHING)
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)
    supervisor_id = models.ForeignKey('GlobalsFaculty', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TeachingCreditRegistration'


class TeachingCredits1(models.Model):
    roll_no = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    programme = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    course1 = models.CharField(max_length=100)
    course2 = models.CharField(max_length=100)
    course3 = models.CharField(max_length=100)
    tag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Teaching_credits1'


class Thesis(models.Model):
    topic = models.CharField(max_length=1000)
    reg_id = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)
    supervisor_id = models.ForeignKey('GlobalsFaculty', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Thesis'


class Thesistopicprocess(models.Model):
    research_area = models.CharField(max_length=50)
    thesis_topic = models.CharField(max_length=1000)
    submission_by_student = models.BooleanField()
    pending_supervisor = models.BooleanField()
    approval_supervisor = models.BooleanField()
    forwarded_to_hod = models.BooleanField()
    pending_hod = models.BooleanField()
    approval_by_hod = models.BooleanField()
    date = models.DateField()
    co_supervisor_id = models.ForeignKey('GlobalsFaculty', models.DO_NOTHING, blank=True, null=True)
    curr_id = models.ForeignKey(Curriculum, models.DO_NOTHING, blank=True, null=True)
    member1 = models.ForeignKey('GlobalsFaculty', models.DO_NOTHING, blank=True, null=True)
    member2 = models.ForeignKey('GlobalsFaculty', models.DO_NOTHING, blank=True, null=True)
    member3 = models.ForeignKey('GlobalsFaculty', models.DO_NOTHING, blank=True, null=True)
    student_id = models.ForeignKey('AcademicInformationStudent', models.DO_NOTHING)
    supervisor_id = models.ForeignKey('GlobalsFaculty', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ThesisTopicProcess'


class Timetable(models.Model):
    upload_date = models.DateTimeField()
    time_table = models.CharField(max_length=100)
    batch = models.IntegerField()
    programme = models.CharField(max_length=10)
    branch = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Timetable'


class Tracking(models.Model):
    receive_date = models.DateTimeField()
    forward_date = models.DateTimeField()
    remarks = models.CharField(max_length=250, blank=True, null=True)
    upload_file = models.CharField(max_length=100)
    is_read = models.BooleanField()
    current_design = models.ForeignKey('GlobalsHoldsdesignation', models.DO_NOTHING, blank=True, null=True)
    current_id = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)
    file_id = models.ForeignKey(File, models.DO_NOTHING, blank=True, null=True)
    receive_design = models.ForeignKey('GlobalsDesignation', models.DO_NOTHING, blank=True, null=True)
    receiver_id = models.ForeignKey('AuthUser', models.DO_NOTHING, blank=True, null=True)
    tracking_extra_json = models.JSONField(db_column='tracking_extra_JSON', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tracking'


class AcademicInformationStudent(models.Model):
    id = models.OneToOneField('GlobalsExtrainfo', models.DO_NOTHING, primary_key=True)
    programme = models.CharField(max_length=10)
    batch = models.IntegerField()
    cpi = models.FloatField()
    category = models.CharField(max_length=10)
    father_name = models.CharField(max_length=40, blank=True, null=True)
    mother_name = models.CharField(max_length=40, blank=True, null=True)
    hall_no = models.IntegerField()
    room_no = models.CharField(max_length=10, blank=True, null=True)
    specialization = models.CharField(max_length=40, blank=True, null=True)
    curr_semester_no = models.IntegerField()
    batch_id = models.ForeignKey('ProgrammeCurriculumBatch', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academic_information_student'


class AcademicProceduresAssistantshipStatus(models.Model):
    student_status = models.BooleanField()
    hod_status = models.BooleanField()
    account_status = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'academic_procedures_assistantship_status'


class AcademicProceduresAssistantshipclaim(models.Model):
    date = models.DateTimeField()
    month = models.CharField(max_length=10)
    year = models.IntegerField()
    bank_account = models.CharField(max_length=11)
    applicability = models.CharField(max_length=5)
    ta_supervisor_remark = models.BooleanField()
    thesis_supervisor_remark = models.BooleanField()
    hod_approval = models.BooleanField()
    acad_approval = models.BooleanField()
    account_approval = models.BooleanField()
    stipend = models.IntegerField()
    student = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)
    ta_supervisor = models.ForeignKey('GlobalsFaculty', models.DO_NOTHING)
    thesis_supervisor = models.ForeignKey('GlobalsFaculty', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'academic_procedures_assistantshipclaim'


class AcademicProceduresBacklogCourse(models.Model):
    is_summer_course = models.BooleanField()
    course_id = models.ForeignKey(Course, models.DO_NOTHING)
    semester_id = models.ForeignKey('ProgrammeCurriculumSemester', models.DO_NOTHING)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'academic_procedures_backlog_course'


class AcademicProceduresBranchchange(models.Model):
    c_id = models.AutoField(primary_key=True)
    applied_date = models.DateField()
    branches = models.ForeignKey('GlobalsDepartmentinfo', models.DO_NOTHING)
    user = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'academic_procedures_branchchange'


class AcademicProceduresCoursesmtech(models.Model):
    specialization = models.CharField(max_length=40)
    c_id = models.ForeignKey(Course, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'academic_procedures_coursesmtech'


class AcademicProceduresFeepayment(models.Model):
    semester = models.IntegerField()
    batch = models.IntegerField()
    mode = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=40)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'academic_procedures_feepayment'


class AcademicProceduresMessdue(models.Model):
    month = models.CharField(max_length=10)
    year = models.IntegerField()
    description = models.CharField(max_length=15)
    amount = models.IntegerField()
    remaining_amount = models.IntegerField()
    student = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'academic_procedures_messdue'


class AcademicProceduresMinimumcredits(models.Model):
    semester = models.IntegerField()
    credits = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'academic_procedures_minimumcredits'


class AcademicProceduresMtechgraduateseminarreport(models.Model):
    theme_of_work = models.TextField()
    date = models.DateField()
    place = models.CharField(max_length=30)
    time = models.TimeField()
    work_done_till_previous_sem = models.TextField()
    specific_contri_in_cur_sem = models.TextField()
    future_plan = models.TextField()
    brief_report = models.CharField(max_length=100)
    publication_submitted = models.IntegerField()
    publication_accepted = models.IntegerField()
    paper_presented = models.IntegerField()
    papers_under_review = models.IntegerField()
    quality_of_work = models.CharField(max_length=20)
    quantity_of_work = models.CharField(max_length=15)
    overall_grade = models.CharField(db_column='Overall_grade', max_length=2)  # Field name made lowercase.
    panel_report = models.CharField(max_length=15)
    suggestion = models.TextField(blank=True, null=True)
    student = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'academic_procedures_mtechgraduateseminarreport'


class AcademicProceduresPhdprogressexamination(models.Model):
    theme = models.CharField(max_length=50)
    seminar_date_time = models.DateTimeField()
    place = models.CharField(max_length=30)
    work_done = models.TextField()
    specific_contri_curr_semester = models.TextField()
    future_plan = models.TextField()
    details = models.CharField(max_length=100)
    papers_published = models.IntegerField()
    presented_papers = models.IntegerField()
    papers_submitted = models.IntegerField()
    quality_of_work = models.CharField(max_length=20)
    quantity_of_work = models.CharField(max_length=15)
    overall_grade = models.CharField(db_column='Overall_grade', max_length=2)  # Field name made lowercase.
    completion_period = models.IntegerField(blank=True, null=True)
    panel_report = models.TextField(blank=True, null=True)
    continuation_enhancement_assistantship = models.CharField(max_length=20, blank=True, null=True)
    enhancement_assistantship = models.CharField(max_length=15, blank=True, null=True)
    annual_progress_seminar = models.CharField(max_length=20, blank=True, null=True)
    commments = models.TextField(blank=True, null=True)
    student = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'academic_procedures_phdprogressexamination'


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class ApplyForPurchase(models.Model):
    inspecting_authority = models.CharField(max_length=200)
    expected_purchase_date = models.DateField()
    order_date = models.DateField()
    purchase_status = models.IntegerField()
    amount = models.IntegerField()
    purchase_date = models.DateField()
    registrar_approve_tag = models.IntegerField()
    director_approve_tag = models.IntegerField()
    hod_approve_tag = models.IntegerField(db_column='HOD_approve_tag')  # Field name made lowercase.
    accounts_approve_tag = models.IntegerField()
    gem_tag = models.IntegerField()
    purchase_type = models.IntegerField()
    purpose = models.CharField(max_length=200)
    budgetary_head = models.CharField(max_length=200)
    invoice = models.CharField(max_length=100)
    nature_of_item1 = models.IntegerField()
    nature_of_item2 = models.IntegerField()
    item_name = models.CharField(max_length=100)
    expected_cost = models.IntegerField()
    quantity = models.IntegerField()
    indentor_name = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'apply_for_purchase'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class AutoFairClaim(models.Model):
    purpose = models.CharField(max_length=100)
    amount = models.IntegerField()
    auto_reg_no = models.CharField(max_length=50)
    auto_contact = models.IntegerField()
    bill = models.CharField(max_length=100)
    date = models.DateField()
    name = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auto_fair_claim'


class CentralMessDeregistrationRequest(models.Model):
    status = models.CharField(max_length=10)
    deregistration_remark = models.CharField(max_length=50)
    end_date = models.DateField(blank=True, null=True)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'central_mess_deregistration_request'


class CentralMessFeedback(models.Model):
    mess = models.CharField(max_length=10)
    mess_rating = models.SmallIntegerField()
    fdate = models.DateField()
    description = models.TextField()
    feedback_type = models.CharField(max_length=20)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)
    feedback_remark = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'central_mess_feedback'


class CentralMessMenu(models.Model):
    mess_option = models.CharField(max_length=20)
    meal_time = models.CharField(max_length=20)
    dish = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'central_mess_menu'


class CentralMessMenuChangeRequest(models.Model):
    reason = models.TextField()
    request = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    app_date = models.DateField()
    dish = models.ForeignKey(CentralMessMenu, models.DO_NOTHING)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'central_mess_menu_change_request'


class CentralMessMessMeeting(models.Model):
    meet_date = models.DateField()
    agenda = models.TextField()
    venue = models.TextField()
    meeting_time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'central_mess_mess_meeting'


class CentralMessMessMinutes(models.Model):
    mess_minutes = models.CharField(max_length=100)
    meeting_date = models.OneToOneField(CentralMessMessMeeting, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'central_mess_mess_minutes'


class CentralMessMessReg(models.Model):
    sem = models.IntegerField()
    start_reg = models.DateField()
    end_reg = models.DateField()

    class Meta:
        managed = False
        db_table = 'central_mess_mess_reg'


class CentralMessMessbillbase(models.Model):
    bill_amount = models.IntegerField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'central_mess_messbillbase'


class CentralMessMessinfo(models.Model):
    mess_option = models.CharField(max_length=20)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'central_mess_messinfo'
        unique_together = (('student_id', 'mess_option'),)


class CentralMessMonthlyBill(models.Model):
    month = models.CharField(max_length=20)
    year = models.IntegerField()
    amount = models.IntegerField()
    rebate_count = models.IntegerField()
    rebate_amount = models.IntegerField()
    total_bill = models.IntegerField()
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)
    paid = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'central_mess_monthly_bill'
        unique_together = (('student_id', 'month', 'year'),)


class CentralMessPayments(models.Model):
    payment_year = models.IntegerField()
    amount_paid = models.IntegerField()
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)
    payment_date = models.DateField()
    payment_month = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'central_mess_payments'


class CentralMessRebate(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    purpose = models.TextField()
    status = models.CharField(max_length=20)
    app_date = models.DateField()
    leave_type = models.CharField(max_length=20)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)
    rebate_remark = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'central_mess_rebate'


class CentralMessRegMain(models.Model):
    program = models.CharField(max_length=10)
    current_mess_status = models.CharField(max_length=20)
    balance = models.IntegerField()
    mess_option = models.CharField(max_length=20)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'central_mess_reg_main'


class CentralMessRegRecords(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'central_mess_reg_records'


class CentralMessRegistrationRequest(models.Model):
    txn_no = models.CharField(db_column='Txn_no', max_length=20)  # Field name made lowercase.
    img = models.CharField(max_length=100)
    amount = models.IntegerField()
    status = models.CharField(max_length=10)
    registration_remark = models.CharField(max_length=50)
    start_date = models.DateField(blank=True, null=True)
    payment_date = models.DateField(blank=True, null=True)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'central_mess_registration_request'


class CentralMessSemdates(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'central_mess_semdates'
        unique_together = (('start_date', 'end_date'),)


class CentralMessSpecialRequest(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    request = models.TextField()
    status = models.CharField(max_length=20)
    item1 = models.CharField(max_length=50)
    item2 = models.CharField(max_length=50)
    app_date = models.DateField()
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'central_mess_special_request'


class CentralMessUpdatePayment(models.Model):
    txn_no = models.CharField(db_column='Txn_no', max_length=20)  # Field name made lowercase.
    img = models.CharField(max_length=100)
    amount = models.IntegerField()
    status = models.CharField(max_length=10)
    update_remark = models.CharField(max_length=50)
    payment_date = models.DateField(blank=True, null=True)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'central_mess_update_payment'


class CentralMessVacationFood(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    purpose = models.TextField()
    status = models.CharField(max_length=20)
    app_date = models.DateField()
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'central_mess_vacation_food'


class ComplaintSystemCaretaker(models.Model):
    area = models.CharField(max_length=20)
    rating = models.IntegerField()
    myfeedback = models.CharField(max_length=400)
    staff_id = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'complaint_system_caretaker'


class ComplaintSystemSectionincharge(models.Model):
    work_type = models.CharField(max_length=20)
    staff_id = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'complaint_system_sectionincharge'


class ComplaintSystemStudentcomplain(models.Model):
    complaint_date = models.DateTimeField()
    complaint_finish = models.DateField(blank=True, null=True)
    complaint_type = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    specific_location = models.CharField(max_length=50)
    details = models.CharField(max_length=100)
    status = models.IntegerField()
    remarks = models.CharField(max_length=300)
    flag = models.IntegerField()
    reason = models.CharField(max_length=100)
    feedback = models.CharField(max_length=500)
    upload_complaint = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    complainer = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)
    worker_id = models.ForeignKey('ComplaintSystemWorkers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complaint_system_studentcomplain'


class ComplaintSystemSupervisor(models.Model):
    sup_id = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)
    type = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'complaint_system_supervisor'


class ComplaintSystemWorkers(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
    phone = models.BigIntegerField()
    worker_type = models.CharField(max_length=20)
    secincharge_id = models.ForeignKey(ComplaintSystemSectionincharge, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complaint_system_workers'


class CounsellingCellCounsellingfaq(models.Model):
    counselling_question = models.TextField()
    counselling_answer = models.TextField()
    counselling_category = models.ForeignKey('CounsellingCellCounsellingissuecategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'counselling_cell_counsellingfaq'


class CounsellingCellCounsellingissue(models.Model):
    issue_raised_date = models.DateTimeField()
    issue = models.TextField()
    issue_status = models.CharField(max_length=20)
    response_remark = models.TextField(blank=True, null=True)
    issue_category = models.ForeignKey('CounsellingCellCounsellingissuecategory', models.DO_NOTHING)
    resolved_by = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING, blank=True, null=True)
    student = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'counselling_cell_counsellingissue'


class CounsellingCellCounsellingissuecategory(models.Model):
    category_id = models.CharField(unique=True, max_length=40)
    category = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'counselling_cell_counsellingissuecategory'


class CounsellingCellCounsellingmeeting(models.Model):
    meeting_date = models.DateField()
    meeting_time = models.CharField(max_length=20)
    agenda = models.TextField()
    venue = models.CharField(max_length=20)
    student_invities = models.TextField()
    meeting_host = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'counselling_cell_counsellingmeeting'


class CounsellingCellCounsellingminutes(models.Model):
    counselling_minutes = models.CharField(max_length=100)
    counselling_meeting = models.ForeignKey(CounsellingCellCounsellingmeeting, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'counselling_cell_counsellingminutes'


class CounsellingCellFacultycounsellingteam(models.Model):
    faculty_position = models.CharField(max_length=50)
    faculty = models.ForeignKey('GlobalsFaculty', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'counselling_cell_facultycounsellingteam'
        unique_together = (('faculty', 'faculty_position'),)


class CounsellingCellStudentcounsellinginfo(models.Model):
    student = models.OneToOneField(AcademicInformationStudent, models.DO_NOTHING)
    student_guide = models.ForeignKey('CounsellingCellStudentcounsellingteam', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'counselling_cell_studentcounsellinginfo'


class CounsellingCellStudentcounsellingteam(models.Model):
    student_position = models.CharField(max_length=50)
    student = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'counselling_cell_studentcounsellingteam'
        unique_together = (('student', 'student_position'),)


class CounsellingCellStudentmeetingrequest(models.Model):
    requested_time = models.DateTimeField()
    description = models.TextField()
    requested_meeting_status = models.CharField(max_length=20)
    recipient_reply = models.TextField()
    requested_faculty_invitee = models.ForeignKey(CounsellingCellFacultycounsellingteam, models.DO_NOTHING, blank=True, null=True)
    requested_student_invitee = models.ForeignKey(CounsellingCellStudentcounsellingteam, models.DO_NOTHING, blank=True, null=True)
    student = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'counselling_cell_studentmeetingrequest'


class CourseRegistration(models.Model):
    working_year = models.IntegerField(blank=True, null=True)
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)
    course_slot_id = models.ForeignKey('ProgrammeCurriculumCourseslot', models.DO_NOTHING, blank=True, null=True)
    semester_id = models.ForeignKey('ProgrammeCurriculumSemester', models.DO_NOTHING)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'course_registration'


class DepartmentAnnouncements(models.Model):
    ann_date = models.DateTimeField()
    message = models.CharField(max_length=200)
    batch = models.CharField(max_length=40)
    department = models.CharField(max_length=40)
    programme = models.CharField(max_length=10)
    upload_announcement = models.CharField(max_length=100, blank=True, null=True)
    maker_id = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'department_announcements'


class DepartmentInformation(models.Model):
    phone_number = models.BigIntegerField()
    email = models.CharField(max_length=200)
    facilites = models.TextField()
    labs = models.TextField()
    department = models.OneToOneField('GlobalsDepartmentinfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'department_information'


class DepartmentSpecialrequest(models.Model):
    request_date = models.DateTimeField()
    brief = models.CharField(max_length=20)
    request_details = models.CharField(max_length=200)
    upload_request = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    remarks = models.CharField(max_length=300)
    request_receiver = models.CharField(max_length=30)
    request_maker = models.ForeignKey('GlobalsExtrainfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'department_specialrequest'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class EisEmpAchievement(models.Model):
    pf_no = models.CharField(max_length=20)
    a_type = models.CharField(max_length=180)
    details = models.TextField()
    a_day = models.IntegerField(blank=True, null=True)
    a_month = models.IntegerField(blank=True, null=True)
    a_year = models.IntegerField(blank=True, null=True)
    date_entry = models.DateField()
    achievment_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eis_emp_achievement'


class EisEmpConfrenceOrganised(models.Model):
    pf_no = models.CharField(max_length=20)
    name = models.CharField(max_length=500)
    venue = models.CharField(max_length=500)
    k_year = models.IntegerField(blank=True, null=True)
    a_month = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    date_entry = models.DateField(blank=True, null=True)
    role1 = models.CharField(max_length=200, blank=True, null=True)
    role2 = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eis_emp_confrence_organised'


class EisEmpConsultancyProjects(models.Model):
    pf_no = models.CharField(max_length=20)
    consultants = models.CharField(max_length=150)
    title = models.CharField(max_length=1000)
    client = models.CharField(max_length=1000)
    financial_outlay = models.IntegerField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=500, blank=True, null=True)
    date_entry = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    remarks = models.CharField(max_length=1000, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eis_emp_consultancy_projects'


class EisEmpEventOrganized(models.Model):
    pf_no = models.CharField(max_length=20)
    type = models.CharField(max_length=180)
    name = models.CharField(max_length=1000)
    sponsoring_agency = models.CharField(max_length=150)
    venue = models.CharField(max_length=100)
    role = models.CharField(max_length=11)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    date_entry = models.DateField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eis_emp_event_organized'


class EisEmpExpertLectures(models.Model):
    pf_no = models.CharField(max_length=20)
    l_type = models.CharField(max_length=14)
    title = models.CharField(max_length=1000)
    place = models.CharField(max_length=1000)
    l_date = models.DateField(blank=True, null=True)
    l_year = models.IntegerField(blank=True, null=True)
    a_month = models.IntegerField(blank=True, null=True)
    date_entry = models.DateField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eis_emp_expert_lectures'


class EisEmpKeynoteAddress(models.Model):
    pf_no = models.CharField(max_length=20)
    type = models.CharField(max_length=140)
    title = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    venue = models.CharField(max_length=1000)
    page_no = models.CharField(max_length=100)
    isbn_no = models.CharField(max_length=200)
    k_year = models.IntegerField(blank=True, null=True)
    a_month = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    date_entry = models.DateField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eis_emp_keynote_address'


class EisEmpMtechphdThesis(models.Model):
    pf_no = models.CharField(max_length=20)
    degree_type = models.IntegerField()
    title = models.CharField(max_length=250)
    supervisors = models.CharField(max_length=250)
    co_supervisors = models.CharField(max_length=250, blank=True, null=True)
    rollno = models.CharField(max_length=200)
    s_name = models.CharField(max_length=5000)
    s_year = models.IntegerField(blank=True, null=True)
    a_month = models.IntegerField(blank=True, null=True)
    date_entry = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eis_emp_mtechphd_thesis'


class EisEmpPatents(models.Model):
    pf_no = models.CharField(max_length=20)
    p_no = models.CharField(max_length=150)
    title = models.CharField(max_length=1500)
    earnings = models.IntegerField()
    status = models.CharField(max_length=15)
    p_year = models.IntegerField(blank=True, null=True)
    a_month = models.IntegerField(blank=True, null=True)
    date_entry = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eis_emp_patents'


class EisEmpPublishedBooks(models.Model):
    pf_no = models.CharField(max_length=20)
    p_type = models.CharField(max_length=16)
    title = models.CharField(max_length=2500)
    publisher = models.CharField(max_length=2500)
    pyear = models.IntegerField(blank=True, null=True)
    authors = models.CharField(max_length=250)
    date_entry = models.DateField(blank=True, null=True)
    publication_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eis_emp_published_books'


class EisEmpResearchPapers(models.Model):
    pf_no = models.CharField(max_length=20)
    rtype = models.CharField(max_length=500)
    authors = models.CharField(max_length=2500, blank=True, null=True)
    co_authors = models.CharField(max_length=2500, blank=True, null=True)
    title_paper = models.CharField(max_length=2500, blank=True, null=True)
    name = models.CharField(max_length=2500, blank=True, null=True)
    paper = models.CharField(max_length=1000, blank=True, null=True)
    venue = models.CharField(max_length=2500, blank=True, null=True)
    volume_no = models.CharField(max_length=500, blank=True, null=True)
    page_no = models.CharField(max_length=500, blank=True, null=True)
    is_sci = models.CharField(max_length=6, blank=True, null=True)
    isbn_no = models.CharField(max_length=250, blank=True, null=True)
    doi = models.CharField(max_length=1000, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    date_acceptance = models.DateField(blank=True, null=True)
    date_publication = models.DateField(blank=True, null=True)
    year = models.CharField(max_length=10, blank=True, null=True)
    a_month = models.CharField(max_length=500, blank=True, null=True)
    doc_id = models.CharField(max_length=50, blank=True, null=True)
    doc_description = models.CharField(max_length=1000, blank=True, null=True)
    date_entry = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)
    date_submission = models.DateTimeField(blank=True, null=True)
    reference_number = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eis_emp_research_papers'


class EisEmpResearchProjects(models.Model):
    pf_no = models.CharField(max_length=20)
    ptype = models.CharField(max_length=100)
    pi = models.CharField(max_length=1000)
    co_pi = models.CharField(max_length=1500)
    title = models.TextField()
    funding_agency = models.CharField(max_length=250, blank=True, null=True)
    financial_outlay = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=10)
    start_date = models.DateField(blank=True, null=True)
    finish_date = models.DateField(blank=True, null=True)
    date_submission = models.DateField(blank=True, null=True)
    date_entry = models.DateField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eis_emp_research_projects'


class EisEmpSessionChair(models.Model):
    pf_no = models.CharField(max_length=20)
    name = models.CharField(max_length=500)
    event = models.TextField()
    s_year = models.IntegerField(blank=True, null=True)
    a_month = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    date_entry = models.DateField(blank=True, null=True)
    remarks = models.CharField(max_length=1000)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eis_emp_session_chair'


class EisEmpTechtransfer(models.Model):
    pf_no = models.CharField(max_length=20)
    details = models.CharField(max_length=500)
    date_entry = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eis_emp_techtransfer'


class EisEmpVisits(models.Model):
    pf_no = models.CharField(max_length=20)
    v_type = models.IntegerField()
    country = models.CharField(max_length=500)
    place = models.CharField(max_length=500)
    purpose = models.CharField(max_length=500)
    v_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    entry_date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eis_emp_visits'


class EisFacultyAbout(models.Model):
    user = models.OneToOneField(AuthUser, models.DO_NOTHING, primary_key=True)
    about = models.TextField()
    doj = models.DateField()
    education = models.TextField()
    interest = models.TextField()
    contact = models.CharField(max_length=10, blank=True, null=True)
    github = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eis_faculty_about'


class EstablishmentAppraisal(models.Model):
    discipline = models.CharField(max_length=30, blank=True, null=True)
    knowledge_field = models.CharField(max_length=30, blank=True, null=True)
    research_interest = models.CharField(max_length=60, blank=True, null=True)
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(blank=True, null=True)
    other_research_element = models.CharField(max_length=200, blank=True, null=True)
    publications = models.CharField(max_length=200, blank=True, null=True)
    conferences_meeting_attended = models.CharField(max_length=200, blank=True, null=True)
    conferences_meeting_organized = models.CharField(max_length=200, blank=True, null=True)
    admin_assign = models.CharField(max_length=200, blank=True, null=True)
    sevice_to_ins = models.CharField(max_length=200, blank=True, null=True)
    extra_info = models.CharField(max_length=200, blank=True, null=True)
    faculty_comments = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    applicant = models.ForeignKey(AuthUser, models.DO_NOTHING)
    designation = models.ForeignKey('GlobalsDesignation', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'establishment_appraisal'


class EstablishmentAppraisaladministrators(models.Model):
    authority = models.ForeignKey('GlobalsDesignation', models.DO_NOTHING, blank=True, null=True)
    officer = models.ForeignKey('GlobalsDesignation', models.DO_NOTHING, blank=True, null=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'establishment_appraisaladministrators'


class EstablishmentAppraisalrequest(models.Model):
    remark_hod = models.CharField(max_length=50, blank=True, null=True)
    remark_director = models.CharField(max_length=50, blank=True, null=True)
    status_hod = models.CharField(max_length=20)
    status_director = models.CharField(max_length=20)
    permission = models.CharField(max_length=20, blank=True, null=True)
    request_timestamp = models.DateTimeField(blank=True, null=True)
    appraisal = models.ForeignKey(EstablishmentAppraisal, models.DO_NOTHING)
    director = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    hod = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'establishment_appraisalrequest'


class EstablishmentCoursesinstructed(models.Model):
    semester = models.IntegerField(blank=True, null=True)
    course_name = models.CharField(max_length=30)
    course_num = models.IntegerField(blank=True, null=True)
    lecture_hrs_wk = models.FloatField(blank=True, null=True)
    tutorial_hrs_wk = models.FloatField(blank=True, null=True)
    lab_hrs_wk = models.FloatField(blank=True, null=True)
    reg_students = models.IntegerField(blank=True, null=True)
    co_instructor = models.CharField(max_length=250, blank=True, null=True)
    appraisal = models.ForeignKey(EstablishmentAppraisal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'establishment_coursesinstructed'


class EstablishmentCpdabalance(models.Model):
    user = models.OneToOneField(AuthUser, models.DO_NOTHING, primary_key=True)
    cpda_balance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'establishment_cpdabalance'


class EstablishmentDependent(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(blank=True, null=True)
    depend = models.CharField(max_length=30)
    ltc = models.ForeignKey(LtcApplication, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'establishment_dependent'


class EstablishmentEstablishmentVariables(models.Model):
    est_admin = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'establishment_establishment_variables'


class EstablishmentLtcAvailed(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(blank=True, null=True)
    ltc = models.ForeignKey(LtcApplication, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'establishment_ltc_availed'


class EstablishmentLtcEligibleUser(models.Model):
    user = models.OneToOneField(AuthUser, models.DO_NOTHING, primary_key=True)
    date_of_joining = models.DateField()
    current_block_size = models.IntegerField()
    total_ltc_allowed = models.IntegerField()
    hometown_ltc_allowed = models.IntegerField()
    elsewhere_ltc_allowed = models.IntegerField()
    hometown_ltc_availed = models.IntegerField()
    elsewhere_ltc_availed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'establishment_ltc_eligible_user'


class EstablishmentLtcToAvail(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(blank=True, null=True)
    ltc = models.ForeignKey(LtcApplication, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'establishment_ltc_to_avail'


class EstablishmentNewcoursematerial(models.Model):
    course_name = models.CharField(max_length=30)
    course_num = models.IntegerField(blank=True, null=True)
    ug_or_pg = models.CharField(max_length=2, blank=True, null=True)
    activity_type = models.CharField(max_length=10, blank=True, null=True)
    availiability = models.CharField(max_length=10, blank=True, null=True)
    appraisal = models.ForeignKey(EstablishmentAppraisal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'establishment_newcoursematerial'


class EstablishmentNewcoursesoffered(models.Model):
    course_name = models.CharField(max_length=30)
    course_num = models.IntegerField(blank=True, null=True)
    ug_or_pg = models.CharField(max_length=2, blank=True, null=True)
    tutorial_hrs_wk = models.FloatField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    semester = models.IntegerField()
    appraisal = models.ForeignKey(EstablishmentAppraisal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'establishment_newcoursesoffered'


class EstablishmentSponsoredprojects(models.Model):
    project_title = models.CharField(max_length=30)
    sponsoring_agency = models.CharField(max_length=30)
    funding = models.IntegerField()
    duration = models.IntegerField()
    status = models.CharField(max_length=30)
    remarks = models.CharField(max_length=30)
    appraisal = models.ForeignKey(EstablishmentAppraisal, models.DO_NOTHING)
    co_investigators = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'establishment_sponsoredprojects'


class EstablishmentThesisresearchsupervision(models.Model):
    stud_name = models.CharField(max_length=30)
    thesis_title = models.CharField(max_length=30, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    semester = models.IntegerField()
    status = models.CharField(max_length=30)
    appraisal = models.ForeignKey(EstablishmentAppraisal, models.DO_NOTHING)
    co_supervisors = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'establishment_thesisresearchsupervision'


class EstateModuleBuilding(models.Model):
    name = models.CharField(max_length=100)
    dateissued = models.DateField(db_column='dateIssued')  # Field name made lowercase.
    dateconstructionstarted = models.DateField(db_column='dateConstructionStarted', blank=True, null=True)  # Field name made lowercase.
    dateconstructioncompleted = models.DateField(db_column='dateConstructionCompleted', blank=True, null=True)  # Field name made lowercase.
    dateoperational = models.DateField(db_column='dateOperational', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=2)
    area = models.IntegerField(blank=True, null=True)
    constructioncostestimated = models.IntegerField(db_column='constructionCostEstimated', blank=True, null=True)  # Field name made lowercase.
    constructioncostactual = models.IntegerField(db_column='constructionCostActual', blank=True, null=True)  # Field name made lowercase.
    numrooms = models.IntegerField(db_column='numRooms', blank=True, null=True)  # Field name made lowercase.
    numwashrooms = models.IntegerField(db_column='numWashrooms', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(blank=True, null=True)
    verified = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'estate_module_building'


class EstateModuleInventoryconsumable(models.Model):
    quantity = models.IntegerField()
    dateordered = models.DateField(db_column='dateOrdered')  # Field name made lowercase.
    datereceived = models.DateField(db_column='dateReceived', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(blank=True, null=True)
    presentquantity = models.IntegerField(db_column='presentQuantity')  # Field name made lowercase.
    building = models.ForeignKey(EstateModuleBuilding, models.DO_NOTHING, blank=True, null=True)
    inventorytype = models.ForeignKey('EstateModuleInventorytype', models.DO_NOTHING, db_column='inventoryType_id')  # Field name made lowercase.
    work = models.ForeignKey('EstateModuleWork', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estate_module_inventoryconsumable'


class EstateModuleInventorynonconsumable(models.Model):
    quantity = models.IntegerField()
    dateordered = models.DateField(db_column='dateOrdered')  # Field name made lowercase.
    datereceived = models.DateField(db_column='dateReceived', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(blank=True, null=True)
    serial_no = models.CharField(max_length=20)
    datelastverified = models.DateField(db_column='dateLastVerified')  # Field name made lowercase.
    building = models.ForeignKey(EstateModuleBuilding, models.DO_NOTHING, blank=True, null=True)
    inventorytype = models.ForeignKey('EstateModuleInventorytype', models.DO_NOTHING, db_column='inventoryType_id')  # Field name made lowercase.
    issued_to = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    work = models.ForeignKey('EstateModuleWork', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estate_module_inventorynonconsumable'


class EstateModuleInventorytype(models.Model):
    name = models.CharField(max_length=100)
    rate = models.IntegerField()
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estate_module_inventorytype'


class EstateModuleSubwork(models.Model):
    name = models.CharField(max_length=100)
    dateissued = models.DateField(db_column='dateIssued')  # Field name made lowercase.
    datestarted = models.DateField(db_column='dateStarted', blank=True, null=True)  # Field name made lowercase.
    datecompleted = models.DateField(db_column='dateCompleted', blank=True, null=True)  # Field name made lowercase.
    costestimated = models.IntegerField(db_column='costEstimated', blank=True, null=True)  # Field name made lowercase.
    costactual = models.IntegerField(db_column='costActual', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(blank=True, null=True)
    work = models.ForeignKey('EstateModuleWork', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'estate_module_subwork'


class EstateModuleWork(models.Model):
    name = models.CharField(max_length=100)
    worktype = models.CharField(db_column='workType', max_length=2)  # Field name made lowercase.
    contractorname = models.CharField(db_column='contractorName', max_length=100)  # Field name made lowercase.
    status = models.CharField(max_length=2)
    dateissued = models.DateField(db_column='dateIssued')  # Field name made lowercase.
    datestarted = models.DateField(db_column='dateStarted', blank=True, null=True)  # Field name made lowercase.
    datecompleted = models.DateField(db_column='dateCompleted', blank=True, null=True)  # Field name made lowercase.
    costestimated = models.IntegerField(db_column='costEstimated', blank=True, null=True)  # Field name made lowercase.
    costactual = models.IntegerField(db_column='costActual', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(blank=True, null=True)
    verified = models.BooleanField()
    building = models.ForeignKey(EstateModuleBuilding, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estate_module_work'


class ExaminationAuthentication(models.Model):
    authenticator_1 = models.BooleanField()
    authenticator_2 = models.BooleanField()
    authenticator_3 = models.BooleanField()
    year = models.DateField()
    course_year = models.IntegerField()
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'examination_authentication'


class ExaminationGrade(models.Model):
    student = models.CharField(max_length=20)
    curriculum = models.CharField(max_length=50)
    semester_id = models.CharField(max_length=10)
    grade = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'examination_grade'


class ExaminationHiddenGrades(models.Model):
    student_id = models.CharField(max_length=20)
    course_id = models.CharField(max_length=50)
    semester_id = models.CharField(max_length=10)
    grade = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'examination_hidden_grades'


class FeedsAlltags(models.Model):
    tag = models.CharField(max_length=100)
    subtag = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'feeds_alltags'


class FeedsAnsweraquestion(models.Model):
    content = models.TextField()
    uploaded_at = models.DateTimeField()
    is_liked = models.BooleanField()
    question = models.ForeignKey('FeedsAskaquestion', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_answeraquestion'


class FeedsAnsweraquestionAnswers(models.Model):
    answeraquestion = models.ForeignKey(FeedsAnsweraquestion, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_answeraquestion_answers'
        unique_together = (('answeraquestion', 'user'),)


class FeedsAnsweraquestionDislikes(models.Model):
    answeraquestion = models.ForeignKey(FeedsAnsweraquestion, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_answeraquestion_dislikes'
        unique_together = (('answeraquestion', 'user'),)


class FeedsAnsweraquestionLikes(models.Model):
    answeraquestion = models.ForeignKey(FeedsAnsweraquestion, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_answeraquestion_likes'
        unique_together = (('answeraquestion', 'user'),)


class FeedsAskaquestion(models.Model):
    can_delete = models.BooleanField()
    can_update = models.BooleanField()
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    file = models.CharField(max_length=100, blank=True, null=True)
    uploaded_at = models.DateTimeField()
    is_liked = models.BooleanField()
    is_requested = models.BooleanField()
    request = models.IntegerField()
    anonymous_ask = models.BooleanField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_askaquestion'


class FeedsAskaquestionDislikes(models.Model):
    askaquestion = models.ForeignKey(FeedsAskaquestion, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_askaquestion_dislikes'
        unique_together = (('askaquestion', 'user'),)


class FeedsAskaquestionLikes(models.Model):
    askaquestion = models.ForeignKey(FeedsAskaquestion, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_askaquestion_likes'
        unique_together = (('askaquestion', 'user'),)


class FeedsAskaquestionRequests(models.Model):
    askaquestion = models.ForeignKey(FeedsAskaquestion, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_askaquestion_requests'
        unique_together = (('askaquestion', 'user'),)


class FeedsAskaquestionSelectTag(models.Model):
    askaquestion = models.ForeignKey(FeedsAskaquestion, models.DO_NOTHING)
    alltags = models.ForeignKey(FeedsAlltags, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_askaquestion_select_tag'
        unique_together = (('askaquestion', 'alltags'),)


class FeedsComments(models.Model):
    comment_text = models.CharField(max_length=5000)
    commented_at = models.DateTimeField()
    is_liked = models.BooleanField()
    question = models.ForeignKey(FeedsAskaquestion, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_comments'


class FeedsCommentsLikesComment(models.Model):
    comments = models.ForeignKey(FeedsComments, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_comments_likes_comment'
        unique_together = (('comments', 'user'),)


class FeedsHidden(models.Model):
    question = models.ForeignKey(FeedsAskaquestion, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_hidden'
        unique_together = (('user', 'question'),)


class FeedsProfile(models.Model):
    bio = models.CharField(max_length=250)
    profile_picture = models.CharField(max_length=100, blank=True, null=True)
    profile_view = models.IntegerField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_profile'


class FeedsQuestionaccesscontrol(models.Model):
    canvote = models.BooleanField(db_column='canVote')  # Field name made lowercase.
    cananswer = models.BooleanField(db_column='canAnswer')  # Field name made lowercase.
    cancomment = models.BooleanField(db_column='canComment')  # Field name made lowercase.
    created_at = models.DateTimeField()
    posted_by = models.ForeignKey('FeedsRoles', models.DO_NOTHING)
    question = models.ForeignKey(FeedsAskaquestion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_questionaccesscontrol'


class FeedsReply(models.Model):
    msg = models.CharField(max_length=1000)
    content = models.CharField(max_length=5000)
    replied_at = models.DateTimeField()
    comment = models.ForeignKey(FeedsComments, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_reply'


class FeedsReplyReplies(models.Model):
    reply = models.ForeignKey(FeedsReply, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_reply_replies'
        unique_together = (('reply', 'user'),)


class FeedsReport(models.Model):
    report_msg = models.CharField(max_length=1000)
    question = models.ForeignKey(FeedsAskaquestion, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_report'


class FeedsRoles(models.Model):
    role = models.CharField(max_length=100)
    active = models.BooleanField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_roles'


class FeedsTags(models.Model):
    my_tag = models.CharField(max_length=100)
    my_subtag = models.ForeignKey(FeedsAlltags, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feeds_tags'
        unique_together = (('user', 'my_subtag'),)


class FinanceAccountsBank(models.Model):
    bank_id = models.AutoField(primary_key=True)
    account_no = models.IntegerField(db_column='Account_no', unique=True)  # Field name made lowercase.
    bank_name = models.CharField(db_column='Bank_Name', max_length=50)  # Field name made lowercase.
    ifsc_code = models.CharField(db_column='IFSC_Code', unique=True, max_length=20)  # Field name made lowercase.
    branch_name = models.CharField(db_column='Branch_Name', max_length=80)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'finance_accounts_bank'
        unique_together = (('bank_name', 'branch_name'),)


class FinanceAccountsCompany(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(db_column='Company_Name', unique=True, max_length=20)  # Field name made lowercase.
    start_date = models.DateField(db_column='Start_Date')  # Field name made lowercase.
    end_date = models.DateField(db_column='End_Date', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'finance_accounts_company'


class FinanceAccountsPayments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    transactionid = models.IntegerField(db_column='TransactionId', unique=True)  # Field name made lowercase.
    towhom = models.CharField(db_column='ToWhom', max_length=80)  # Field name made lowercase.
    fromwhom = models.CharField(db_column='FromWhom', max_length=80)  # Field name made lowercase.
    purpose = models.CharField(db_column='Purpose', max_length=20)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'finance_accounts_payments'


class FinanceAccountsPaymentscheme(models.Model):
    month = models.CharField(max_length=70, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    pf = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=70)
    designation = models.CharField(max_length=50)
    pay = models.IntegerField()
    gr_pay = models.IntegerField()
    da = models.IntegerField()
    ta = models.IntegerField()
    hra = models.IntegerField()
    fpa = models.IntegerField()
    special_allow = models.IntegerField()
    nps = models.IntegerField()
    gpf = models.IntegerField()
    income_tax = models.IntegerField()
    p_tax = models.IntegerField()
    gslis = models.IntegerField()
    gis = models.IntegerField()
    license_fee = models.IntegerField()
    electricity_charges = models.IntegerField()
    others = models.IntegerField()
    gr_reduction = models.IntegerField()
    net_payment = models.IntegerField()
    senior_verify = models.BooleanField()
    ass_registrar_verify = models.BooleanField()
    ass_registrar_aud_verify = models.BooleanField()
    registrar_director_verify = models.BooleanField()
    runpayroll = models.BooleanField()
    view = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'finance_accounts_paymentscheme'
        unique_together = (('month', 'year', 'pf'),)


class FinanceAccountsReceipts(models.Model):
    receipt_id = models.AutoField(primary_key=True)
    transactionid = models.IntegerField(db_column='TransactionId', unique=True)  # Field name made lowercase.
    towhom = models.CharField(db_column='ToWhom', max_length=80)  # Field name made lowercase.
    fromwhom = models.CharField(db_column='FromWhom', max_length=80)  # Field name made lowercase.
    purpose = models.CharField(db_column='Purpose', max_length=20)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'finance_accounts_receipts'


class GlobalsDepartmentinfo(models.Model):
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'globals_departmentinfo'


class GlobalsDesignation(models.Model):
    name = models.CharField(unique=True, max_length=50)
    full_name = models.CharField(max_length=100)
    type = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'globals_designation'


class GlobalsExtrainfo(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    title = models.CharField(max_length=20)
    sex = models.CharField(max_length=2)
    date_of_birth = models.DateField()
    user_status = models.CharField(max_length=50)
    address = models.TextField()
    phone_no = models.BigIntegerField(blank=True, null=True)
    user_type = models.CharField(max_length=20)
    profile_picture = models.CharField(max_length=100, blank=True, null=True)
    about_me = models.TextField()
    date_modified = models.DateTimeField(blank=True, null=True)
    department = models.ForeignKey(GlobalsDepartmentinfo, models.DO_NOTHING, blank=True, null=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)
    last_selected_role = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'globals_extrainfo'


class GlobalsFaculty(models.Model):
    id = models.OneToOneField(GlobalsExtrainfo, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'globals_faculty'


class GlobalsFeedback(models.Model):
    rating = models.IntegerField()
    feedback = models.TextField()
    timestamp = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'globals_feedback'


class GlobalsHoldsdesignation(models.Model):
    held_at = models.DateTimeField()
    designation = models.ForeignKey(GlobalsDesignation, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    working = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'globals_holdsdesignation'
        unique_together = (('user', 'designation'), ('working', 'designation'),)


class GlobalsIssue(models.Model):
    report_type = models.CharField(max_length=63)
    module = models.CharField(max_length=63)
    closed = models.BooleanField()
    text = models.TextField()
    title = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    added_on = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'globals_issue'


class GlobalsIssueImages(models.Model):
    issue = models.ForeignKey(GlobalsIssue, models.DO_NOTHING)
    issueimage = models.ForeignKey('GlobalsIssueimage', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'globals_issue_images'
        unique_together = (('issue', 'issueimage'),)


class GlobalsIssueSupport(models.Model):
    issue = models.ForeignKey(GlobalsIssue, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'globals_issue_support'
        unique_together = (('issue', 'user'),)


class GlobalsIssueimage(models.Model):
    image = models.CharField(max_length=100)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'globals_issueimage'


class GlobalsModuleaccess(models.Model):
    designation = models.CharField(max_length=155)
    program_and_curriculum = models.BooleanField()
    course_registration = models.BooleanField()
    course_management = models.BooleanField()
    other_academics = models.BooleanField()
    spacs = models.BooleanField()
    department = models.BooleanField()
    examinations = models.BooleanField()
    hr = models.BooleanField()
    iwd = models.BooleanField()
    complaint_management = models.BooleanField()
    fts = models.BooleanField()
    purchase_and_store = models.BooleanField()
    rspc = models.BooleanField()
    hostel_management = models.BooleanField()
    mess_management = models.BooleanField()
    gymkhana = models.BooleanField()
    placement_cell = models.BooleanField()
    visitor_hostel = models.BooleanField()
    phc = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'globals_moduleaccess'


class GlobalsStaff(models.Model):
    id = models.OneToOneField(GlobalsExtrainfo, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'globals_staff'


class GymkhanaVotingChoices(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    votes = models.IntegerField()
    poll_event = models.ForeignKey('GymkhanaVotingPolls', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gymkhana_voting_choices'


class GymkhanaVotingPolls(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    pub_date = models.DateTimeField()
    exp_date = models.DateTimeField()
    created_by = models.CharField(max_length=100, blank=True, null=True)
    groups = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'gymkhana_voting_polls'


class GymkhanaVotingVoters(models.Model):
    student_id = models.CharField(max_length=50)
    poll_event = models.ForeignKey(GymkhanaVotingPolls, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gymkhana_voting_voters'


class HealthCenterAllMedicine(models.Model):
    medicine_name = models.CharField(max_length=1000, blank=True, null=True)
    brand_name = models.CharField(max_length=1000, blank=True, null=True)
    constituents = models.TextField(blank=True, null=True)
    manufacturer_name = models.CharField(max_length=1000, blank=True, null=True)
    pack_size_label = models.CharField(max_length=1000, blank=True, null=True)
    threshold = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'health_center_all_medicine'


class HealthCenterAllPrescribedMedicine(models.Model):
    quantity = models.IntegerField()
    days = models.IntegerField()
    times = models.IntegerField()
    revoked = models.BooleanField()
    revoked_date = models.DateField(blank=True, null=True)
    medicine_id = models.ForeignKey(HealthCenterAllMedicine, models.DO_NOTHING)
    prescription_id = models.ForeignKey('HealthCenterAllPrescription', models.DO_NOTHING)
    stock = models.ForeignKey('HealthCenterPresentStock', models.DO_NOTHING, blank=True, null=True)
    prescription_followup_id = models.ForeignKey('HealthCenterPrescriptionFollowup', models.DO_NOTHING, blank=True, null=True)
    revoked_prescription = models.ForeignKey('HealthCenterPrescriptionFollowup', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'health_center_all_prescribed_medicine'


class HealthCenterAllPrescription(models.Model):
    user_id = models.CharField(max_length=15)
    details = models.TextField(blank=True, null=True)
    date = models.DateField()
    suggestions = models.TextField(blank=True, null=True)
    test = models.CharField(max_length=200, blank=True, null=True)
    file_id = models.IntegerField()
    is_dependent = models.BooleanField()
    dependent_name = models.CharField(max_length=30)
    dependent_relation = models.CharField(max_length=20)
    doctor_id = models.ForeignKey('HealthCenterDoctor', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'health_center_all_prescription'


class HealthCenterDoctor(models.Model):
    doctor_name = models.CharField(max_length=50)
    doctor_phone = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'health_center_doctor'


class HealthCenterDoctorsSchedule(models.Model):
    day = models.CharField(max_length=10)
    from_time = models.TimeField(blank=True, null=True)
    to_time = models.TimeField(blank=True, null=True)
    room = models.IntegerField()
    date = models.DateField()
    doctor_id = models.ForeignKey(HealthCenterDoctor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'health_center_doctors_schedule'


class HealthCenterFiles(models.Model):
    file_data = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'health_center_files'


class HealthCenterMedicalRelief(models.Model):
    description = models.CharField(max_length=200)
    file = models.CharField(max_length=100)
    file_id = models.IntegerField()
    compounder_forward_flag = models.BooleanField()
    acc_admin_forward_flag = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'health_center_medical_relief'


class HealthCenterMedicalprofile(models.Model):
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1)
    blood_type = models.CharField(max_length=3)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    user_id = models.ForeignKey(GlobalsExtrainfo, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'health_center_medicalprofile'


class HealthCenterPathologist(models.Model):
    pathologist_name = models.CharField(max_length=50)
    pathologist_phone = models.CharField(max_length=15)
    specialization = models.CharField(max_length=100)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'health_center_pathologist'


class HealthCenterPathologistSchedule(models.Model):
    day = models.CharField(max_length=10)
    from_time = models.TimeField(blank=True, null=True)
    to_time = models.TimeField(blank=True, null=True)
    room = models.IntegerField()
    date = models.DateField()
    pathologist_id = models.ForeignKey(HealthCenterPathologist, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'health_center_pathologist_schedule'


class HealthCenterPrescriptionFollowup(models.Model):
    details = models.TextField(blank=True, null=True)
    date = models.DateField()
    test = models.CharField(max_length=200, blank=True, null=True)
    suggestions = models.TextField(blank=True, null=True)
    file_id = models.IntegerField()
    doctor_id = models.ForeignKey(HealthCenterDoctor, models.DO_NOTHING, db_column='Doctor_id_id', blank=True, null=True)  # Field name made lowercase.
    prescription_id = models.ForeignKey(HealthCenterAllPrescription, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'health_center_prescription_followup'


class HealthCenterPresentStock(models.Model):
    quantity = models.IntegerField()
    stock_id = models.ForeignKey('HealthCenterStockEntry', models.DO_NOTHING)
    expiry_date = models.DateField(db_column='Expiry_date')  # Field name made lowercase.
    medicine_id = models.ForeignKey(HealthCenterAllMedicine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'health_center_present_stock'


class HealthCenterRequiredMedicine(models.Model):
    quantity = models.IntegerField()
    threshold = models.IntegerField()
    medicine_id = models.ForeignKey(HealthCenterAllMedicine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'health_center_required_medicine'


class HealthCenterRequiredTabelLastUpdated(models.Model):
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'health_center_required_tabel_last_updated'


class HealthCenterStockEntry(models.Model):
    quantity = models.IntegerField()
    supplier = models.CharField(max_length=50)
    expiry_date = models.DateField(db_column='Expiry_date')  # Field name made lowercase.
    date = models.DateField()
    medicine_id = models.ForeignKey(HealthCenterAllMedicine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'health_center_stock_entry'


class HostelAllotment(models.Model):
    program = models.CharField(max_length=30)
    year = models.IntegerField()
    gender = models.CharField(max_length=10)
    hall_no = models.CharField(max_length=15)
    number_students = models.IntegerField()
    remark = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'hostel_allotment'


class HostelCapacity(models.Model):
    name = models.CharField(max_length=15)
    current_capacity = models.IntegerField()
    total_capacity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hostel_capacity'


class HostelManagementGuestroom(models.Model):
    room = models.CharField(max_length=255)
    occupied_till = models.DateField(blank=True, null=True)
    vacant = models.BooleanField()
    room_type = models.CharField(max_length=10)
    hall = models.ForeignKey('HostelManagementHall', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hostel_management_guestroom'


class HostelManagementGuestroombooking(models.Model):
    guest_name = models.CharField(max_length=255)
    guest_phone = models.CharField(max_length=255)
    guest_email = models.CharField(max_length=255)
    guest_address = models.TextField()
    rooms_required = models.IntegerField(blank=True, null=True)
    total_guest = models.IntegerField()
    purpose = models.TextField()
    arrival_date = models.DateField()
    arrival_time = models.TimeField()
    departure_date = models.DateField()
    departure_time = models.TimeField()
    status = models.CharField(max_length=255)
    booking_date = models.DateField()
    nationality = models.CharField(max_length=255)
    hall = models.ForeignKey('HostelManagementHall', models.DO_NOTHING)
    intender = models.ForeignKey(AuthUser, models.DO_NOTHING)
    room_type = models.CharField(max_length=10)
    guest_room_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'hostel_management_guestroombooking'


class HostelManagementHall(models.Model):
    hall_id = models.CharField(max_length=10)
    hall_name = models.CharField(max_length=50)
    max_accomodation = models.IntegerField()
    number_students = models.IntegerField()
    assigned_batch = models.CharField(max_length=50, blank=True, null=True)
    type_of_seater = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'hostel_management_hall'


class HostelManagementHallcaretaker(models.Model):
    hall = models.ForeignKey(HostelManagementHall, models.DO_NOTHING)
    staff = models.ForeignKey(GlobalsStaff, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hostel_management_hallcaretaker'


class HostelManagementHallroom(models.Model):
    room_no = models.CharField(max_length=4)
    block_no = models.CharField(max_length=1)
    room_cap = models.IntegerField()
    room_occupied = models.IntegerField()
    hall = models.ForeignKey(HostelManagementHall, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hostel_management_hallroom'


class HostelManagementHallwarden(models.Model):
    faculty = models.ForeignKey(GlobalsFaculty, models.DO_NOTHING)
    hall = models.ForeignKey(HostelManagementHall, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hostel_management_hallwarden'


class HostelManagementHostelallotment(models.Model):
    assignedbatch = models.CharField(db_column='assignedBatch', max_length=50)  # Field name made lowercase.
    assignedcaretaker = models.ForeignKey(GlobalsStaff, models.DO_NOTHING, db_column='assignedCaretaker_id', blank=True, null=True)  # Field name made lowercase.
    assignedwarden = models.ForeignKey(GlobalsFaculty, models.DO_NOTHING, db_column='assignedWarden_id', blank=True, null=True)  # Field name made lowercase.
    hall = models.ForeignKey(HostelManagementHall, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hostel_management_hostelallotment'


class HostelManagementHostelcomplaint(models.Model):
    hall_name = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    description = models.TextField()
    contact_number = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'hostel_management_hostelcomplaint'


class HostelManagementHostelfine(models.Model):
    fine_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    reason = models.TextField()
    hall = models.ForeignKey(HostelManagementHall, models.DO_NOTHING)
    student = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hostel_management_hostelfine'


class HostelManagementHostelhistory(models.Model):
    timestamp = models.DateTimeField()
    batch = models.CharField(max_length=50, blank=True, null=True)
    caretaker = models.ForeignKey(GlobalsStaff, models.DO_NOTHING, blank=True, null=True)
    hall = models.ForeignKey(HostelManagementHall, models.DO_NOTHING)
    warden = models.ForeignKey(GlobalsFaculty, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hostel_management_hostelhistory'


class HostelManagementHostelinventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    inventory_name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    hall = models.ForeignKey(HostelManagementHall, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hostel_management_hostelinventory'


class HostelManagementHostelleave(models.Model):
    student_name = models.CharField(max_length=100)
    roll_num = models.CharField(max_length=20)
    reason = models.TextField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20)
    remark = models.TextField(blank=True, null=True)
    file_upload = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hostel_management_hostelleave'


class HostelManagementHostelnoticeboard(models.Model):
    head_line = models.CharField(max_length=100)
    content = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    hall = models.ForeignKey(HostelManagementHall, models.DO_NOTHING)
    posted_by = models.ForeignKey(GlobalsExtrainfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hostel_management_hostelnoticeboard'


class HostelManagementHostelstudentattendence(models.Model):
    date = models.DateField()
    present = models.BooleanField()
    hall = models.ForeignKey(HostelManagementHall, models.DO_NOTHING)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hostel_management_hostelstudentattendence'


class HostelManagementHosteltransactionhistory(models.Model):
    change_type = models.CharField(max_length=100)
    previous_value = models.CharField(max_length=255)
    new_value = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    hall = models.ForeignKey(HostelManagementHall, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hostel_management_hosteltransactionhistory'


class HostelManagementStaffschedule(models.Model):
    staff_type = models.CharField(max_length=100)
    day = models.CharField(max_length=15)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    hall = models.ForeignKey(HostelManagementHall, models.DO_NOTHING)
    staff_id = models.ForeignKey(GlobalsStaff, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hostel_management_staffschedule'


class HostelManagementStudentdetails(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    programme = models.CharField(max_length=100, blank=True, null=True)
    batch = models.CharField(max_length=100, blank=True, null=True)
    room_num = models.CharField(max_length=20, blank=True, null=True)
    hall_no = models.CharField(max_length=20, blank=True, null=True)
    hall_id = models.CharField(max_length=20, blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    parent_contact = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hostel_management_studentdetails'


class HostelManagementWorkerreport(models.Model):
    worker_id = models.CharField(max_length=10)
    worker_name = models.CharField(max_length=50)
    year = models.IntegerField()
    month = models.IntegerField()
    absent = models.IntegerField()
    total_day = models.IntegerField()
    remark = models.CharField(max_length=100)
    hall = models.ForeignKey(HostelManagementHall, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hostel_management_workerreport'


class Hr2Appraisalform(models.Model):
    employeeid = models.IntegerField(db_column='employeeId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=22)
    designation = models.CharField(max_length=50)
    disciplineinfo = models.CharField(db_column='disciplineInfo', max_length=22, blank=True, null=True)  # Field name made lowercase.
    specificfieldofknowledge = models.TextField(db_column='specificFieldOfKnowledge', blank=True, null=True)  # Field name made lowercase.
    currentresearchinterests = models.TextField(db_column='currentResearchInterests', blank=True, null=True)  # Field name made lowercase.
    coursestaught = models.JSONField(db_column='coursesTaught', blank=True, null=True)  # Field name made lowercase.
    newcoursesintroduced = models.JSONField(db_column='newCoursesIntroduced', blank=True, null=True)  # Field name made lowercase.
    newcoursesdeveloped = models.JSONField(db_column='newCoursesDeveloped', blank=True, null=True)  # Field name made lowercase.
    otherinstructionaltasks = models.TextField(db_column='otherInstructionalTasks', blank=True, null=True)  # Field name made lowercase.
    thesissupervision = models.JSONField(db_column='thesisSupervision', blank=True, null=True)  # Field name made lowercase.
    sponsoredreseachprojects = models.JSONField(db_column='sponsoredReseachProjects', blank=True, null=True)  # Field name made lowercase.
    otherresearchelement = models.TextField(db_column='otherResearchElement', blank=True, null=True)  # Field name made lowercase.
    publication = models.TextField(blank=True, null=True)
    referredconference = models.TextField(db_column='referredConference', blank=True, null=True)  # Field name made lowercase.
    conferenceorganised = models.TextField(db_column='conferenceOrganised', blank=True, null=True)  # Field name made lowercase.
    membership = models.TextField(blank=True, null=True)
    honours = models.TextField(blank=True, null=True)
    editorofpublications = models.TextField(db_column='editorOfPublications', blank=True, null=True)  # Field name made lowercase.
    expertlecturedelivered = models.TextField(db_column='expertLectureDelivered', blank=True, null=True)  # Field name made lowercase.
    membershipofbos = models.TextField(db_column='membershipOfBOS', blank=True, null=True)  # Field name made lowercase.
    otherextensiontasks = models.TextField(db_column='otherExtensionTasks', blank=True, null=True)  # Field name made lowercase.
    administrativeassignment = models.TextField(db_column='administrativeAssignment', blank=True, null=True)  # Field name made lowercase.
    servicetoinstitute = models.TextField(db_column='serviceToInstitute', blank=True, null=True)  # Field name made lowercase.
    othercontribution = models.TextField(db_column='otherContribution', blank=True, null=True)  # Field name made lowercase.
    performancecomments = models.TextField(db_column='performanceComments', blank=True, null=True)  # Field name made lowercase.
    submissiondate = models.DateField(db_column='submissionDate', blank=True, null=True)  # Field name made lowercase.
    approved = models.BooleanField(blank=True, null=True)
    approveddate = models.DateField(db_column='approvedDate', blank=True, null=True)  # Field name made lowercase.
    approved_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr2_appraisalform'


class Hr2Cpdaadvanceform(models.Model):
    employeeid = models.IntegerField(db_column='employeeId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=40, blank=True, null=True)
    designation = models.CharField(max_length=40, blank=True, null=True)
    pfno = models.IntegerField(db_column='pfNo', blank=True, null=True)  # Field name made lowercase.
    purpose = models.TextField(blank=True, null=True)
    amountrequired = models.IntegerField(db_column='amountRequired', blank=True, null=True)  # Field name made lowercase.
    advancedueadjustment = models.DecimalField(db_column='advanceDueAdjustment', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    submissiondate = models.DateField(db_column='submissionDate', blank=True, null=True)  # Field name made lowercase.
    balanceavailable = models.DecimalField(db_column='balanceAvailable', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    advanceamountpda = models.DecimalField(db_column='advanceAmountPDA', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amountcheckedinpda = models.DecimalField(db_column='amountCheckedInPDA', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    approved = models.BooleanField(blank=True, null=True)
    approveddate = models.DateField(db_column='approvedDate', blank=True, null=True)  # Field name made lowercase.
    approved_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr2_cpdaadvanceform'


class Hr2Cpdareimbursementform(models.Model):
    employeeid = models.IntegerField(db_column='employeeId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    pfno = models.IntegerField(db_column='pfNo')  # Field name made lowercase.
    advancetaken = models.IntegerField(db_column='advanceTaken')  # Field name made lowercase.
    purpose = models.TextField()
    adjustmentsubmitted = models.DecimalField(db_column='adjustmentSubmitted', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    balanceavailable = models.DecimalField(db_column='balanceAvailable', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    advancedueadjustment = models.DecimalField(db_column='advanceDueAdjustment', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    advanceamountpda = models.DecimalField(db_column='advanceAmountPDA', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    amountcheckedinpda = models.DecimalField(db_column='amountCheckedInPDA', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    submissiondate = models.DateField(db_column='submissionDate')  # Field name made lowercase.
    approved = models.BooleanField(blank=True, null=True)
    approveddate = models.DateField(db_column='approvedDate', blank=True, null=True)  # Field name made lowercase.
    approved_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr2_cpdareimbursementform'


class Hr2Empappraisalform(models.Model):
    year = models.DateField(blank=True, null=True)
    appraisal_form = models.CharField(max_length=100, blank=True, null=True)
    extra_info = models.ForeignKey(GlobalsExtrainfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr2_empappraisalform'


class Hr2Empconfidentialdetails(models.Model):
    aadhar_no = models.BigIntegerField()
    maritial_status = models.CharField(max_length=50)
    bank_account_no = models.IntegerField()
    salary = models.IntegerField()
    extra_info = models.OneToOneField(GlobalsExtrainfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr2_empconfidentialdetails'


class Hr2Empdependents(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    dob = models.DateField(blank=True, null=True)
    relationship = models.CharField(max_length=40)
    extra_info = models.OneToOneField(GlobalsExtrainfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr2_empdependents'


class Hr2Employee(models.Model):
    father_name = models.CharField(max_length=40)
    mother_name = models.CharField(max_length=40)
    religion = models.CharField(max_length=40)
    category = models.CharField(max_length=50)
    cast = models.CharField(max_length=40)
    home_state = models.CharField(max_length=40)
    home_district = models.CharField(max_length=40)
    date_of_joining = models.DateField(blank=True, null=True)
    designation = models.CharField(max_length=40)
    blood_group = models.CharField(max_length=50)
    extra_info = models.OneToOneField(GlobalsExtrainfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr2_employee'


class Hr2Foreignservice(models.Model):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    job_title = models.CharField(max_length=50)
    organisation = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    salary_source = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    extra_info = models.ForeignKey(GlobalsExtrainfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr2_foreignservice'


class Hr2Leavebalance(models.Model):
    casualleave = models.IntegerField(db_column='casualLeave')  # Field name made lowercase.
    specialcasualleave = models.IntegerField(db_column='specialCasualLeave')  # Field name made lowercase.
    earnedleave = models.IntegerField(db_column='earnedLeave')  # Field name made lowercase.
    commutedleave = models.IntegerField(db_column='commutedLeave')  # Field name made lowercase.
    restrictedholiday = models.IntegerField(db_column='restrictedHoliday')  # Field name made lowercase.
    stationleave = models.IntegerField(db_column='stationLeave')  # Field name made lowercase.
    vacationleave = models.IntegerField(db_column='vacationLeave')  # Field name made lowercase.
    employeeid = models.OneToOneField(GlobalsExtrainfo, models.DO_NOTHING, db_column='employeeId_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hr2_leavebalance'


class Hr2Leaveform(models.Model):
    employeeid = models.IntegerField(db_column='employeeId', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=40, blank=True, null=True)
    designation = models.CharField(max_length=40, blank=True, null=True)
    submissiondate = models.DateField(db_column='submissionDate', blank=True, null=True)  # Field name made lowercase.
    pfno = models.IntegerField(db_column='pfNo', blank=True, null=True)  # Field name made lowercase.
    departmentinfo = models.CharField(db_column='departmentInfo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    natureofleave = models.TextField(db_column='natureOfLeave', blank=True, null=True)  # Field name made lowercase.
    leavestartdate = models.DateField(db_column='leaveStartDate', blank=True, null=True)  # Field name made lowercase.
    leaveenddate = models.DateField(db_column='leaveEndDate', blank=True, null=True)  # Field name made lowercase.
    purposeofleave = models.TextField(db_column='purposeOfLeave', blank=True, null=True)  # Field name made lowercase.
    addressduringleave = models.TextField(db_column='addressDuringLeave', blank=True, null=True)  # Field name made lowercase.
    academicresponsibility = models.TextField(db_column='academicResponsibility', blank=True, null=True)  # Field name made lowercase.
    addministrativeresponsibiltyassigned = models.TextField(db_column='addministrativeResponsibiltyAssigned', blank=True, null=True)  # Field name made lowercase.
    approved = models.BooleanField(blank=True, null=True)
    approveddate = models.DateField(db_column='approvedDate', blank=True, null=True)  # Field name made lowercase.
    approved_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr2_leaveform'


class Hr2Ltcform(models.Model):
    employeeid = models.IntegerField(db_column='employeeId')  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    blockyear = models.TextField(db_column='blockYear')  # Field name made lowercase.
    pfno = models.IntegerField(db_column='pfNo')  # Field name made lowercase.
    basicpaysalary = models.IntegerField(db_column='basicPaySalary', blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(max_length=50)
    departmentinfo = models.CharField(db_column='departmentInfo', max_length=50)  # Field name made lowercase.
    leaverequired = models.BooleanField(db_column='leaveRequired', blank=True, null=True)  # Field name made lowercase.
    leavestartdate = models.DateField(db_column='leaveStartDate', blank=True, null=True)  # Field name made lowercase.
    leaveenddate = models.DateField(db_column='leaveEndDate', blank=True, null=True)  # Field name made lowercase.
    dateofdepartureforfamily = models.DateField(db_column='dateOfDepartureForFamily', blank=True, null=True)  # Field name made lowercase.
    natureofleave = models.TextField(db_column='natureOfLeave', blank=True, null=True)  # Field name made lowercase.
    purposeofleave = models.TextField(db_column='purposeOfLeave', blank=True, null=True)  # Field name made lowercase.
    hometownornot = models.BooleanField(db_column='hometownOrNot')  # Field name made lowercase.
    placeofvisit = models.TextField(db_column='placeOfVisit', blank=True, null=True)  # Field name made lowercase.
    addressduringleave = models.TextField(db_column='addressDuringLeave', blank=True, null=True)  # Field name made lowercase.
    modeoftravel = models.TextField(db_column='modeofTravel', blank=True, null=True)  # Field name made lowercase.
    detailsoffamilymembersalreadydone = models.JSONField(db_column='detailsOfFamilyMembersAlreadyDone', blank=True, null=True)  # Field name made lowercase.
    detailsoffamilymembersabouttoavail = models.JSONField(db_column='detailsOfFamilyMembersAboutToAvail', blank=True, null=True)  # Field name made lowercase.
    detailsofdependents = models.JSONField(db_column='detailsOfDependents', blank=True, null=True)  # Field name made lowercase.
    amountofadvancerequired = models.IntegerField(db_column='amountOfAdvanceRequired', blank=True, null=True)  # Field name made lowercase.
    certifiedthatfamilydependents = models.BooleanField(db_column='certifiedThatFamilyDependents', blank=True, null=True)  # Field name made lowercase.
    certifiedthatadvancetakenon = models.DateField(db_column='certifiedThatAdvanceTakenOn', blank=True, null=True)  # Field name made lowercase.
    adjustedmonth = models.TextField(db_column='adjustedMonth', blank=True, null=True)  # Field name made lowercase.
    submissiondate = models.DateField(db_column='submissionDate', blank=True, null=True)  # Field name made lowercase.
    phonenumberforcontact = models.BigIntegerField(db_column='phoneNumberForContact')  # Field name made lowercase.
    approved = models.BooleanField(blank=True, null=True)
    approveddate = models.DateField(db_column='approvedDate', blank=True, null=True)  # Field name made lowercase.
    approved_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr2_ltcform'


class Hr2Workassignemnt(models.Model):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    job_title = models.CharField(max_length=50)
    orders_copy = models.CharField(max_length=100, blank=True, null=True)
    extra_info = models.ForeignKey(GlobalsExtrainfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr2_workassignemnt'


class IncomeExpenditureBalancesheet(models.Model):
    balancesheet = models.CharField(db_column='balanceSheet', max_length=100)  # Field name made lowercase.
    date_added = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'income_expenditure_balancesheet'


class IncomeExpenditureExpenditure(models.Model):
    amount = models.IntegerField()
    date_added = models.DateField()
    remarks = models.CharField(max_length=100)
    expenditure_receipt = models.CharField(max_length=100)
    spent_on = models.ForeignKey('IncomeExpenditureExpendituretype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'income_expenditure_expenditure'


class IncomeExpenditureExpendituretype(models.Model):
    expenditure_type = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'income_expenditure_expendituretype'


class IncomeExpenditureFixedattributes(models.Model):
    attribute = models.CharField(max_length=100)
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'income_expenditure_fixedattributes'


class IncomeExpenditureIncome(models.Model):
    amount = models.IntegerField()
    date_added = models.DateField()
    remarks = models.CharField(max_length=100)
    receipt = models.CharField(max_length=100)
    source = models.ForeignKey('IncomeExpenditureIncomesource', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'income_expenditure_income'


class IncomeExpenditureIncomesource(models.Model):
    income_source = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'income_expenditure_incomesource'


class IncomeExpenditureOtherexpense(models.Model):
    spent_on = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    userid = models.CharField(max_length=10)
    amount = models.IntegerField()
    date_added = models.DateField()
    remarks = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'income_expenditure_otherexpense'


class Iwdmodulev2Addendum(models.Model):
    issuedate = models.DateField(db_column='issueDate')  # Field name made lowercase.
    nitniqno = models.IntegerField(db_column='nitNiqNo')  # Field name made lowercase.
    name = models.CharField(max_length=200)
    opendate = models.DateField(db_column='openDate')  # Field name made lowercase.
    opentime = models.TimeField(db_column='openTime')  # Field name made lowercase.
    key = models.OneToOneField('Iwdmodulev2Projects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_addendum'


class Iwdmodulev2Aesdetails(models.Model):
    sno = models.CharField(db_column='sNo', max_length=100)  # Field name made lowercase.
    descofitems = models.CharField(db_column='descOfItems', max_length=200)  # Field name made lowercase.
    unit = models.CharField(max_length=200)
    quantity = models.IntegerField()
    rate = models.IntegerField()
    amount = models.IntegerField()
    key = models.ForeignKey('Iwdmodulev2Projects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_aesdetails'


class Iwdmodulev2Agreement(models.Model):
    date = models.DateField()
    agencyname = models.CharField(db_column='agencyName', max_length=200)  # Field name made lowercase.
    workname = models.CharField(db_column='workName', max_length=200)  # Field name made lowercase.
    fdrsum = models.IntegerField(db_column='fdrSum')  # Field name made lowercase.
    key = models.OneToOneField('Iwdmodulev2Projects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_agreement'


class Iwdmodulev2Bills(models.Model):
    file = models.CharField(max_length=100)
    request_id = models.ForeignKey('Iwdmodulev2Requests', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_bills'


class Iwdmodulev2Budget(models.Model):
    name = models.CharField(max_length=200)
    budgetissued = models.IntegerField(db_column='budgetIssued')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_budget'


class Iwdmodulev2Corrigendumtable(models.Model):
    issuedate = models.DateField(db_column='issueDate')  # Field name made lowercase.
    nitno = models.IntegerField(db_column='nitNo')  # Field name made lowercase.
    name = models.CharField(max_length=200)
    lastdate = models.DateField(db_column='lastDate', blank=True, null=True)  # Field name made lowercase.
    lasttime = models.TimeField(db_column='lastTime')  # Field name made lowercase.
    env1bidopeningdate = models.DateField(db_column='env1BidOpeningDate')  # Field name made lowercase.
    env1bidopeningtime = models.TimeField(db_column='env1BidOpeningTime')  # Field name made lowercase.
    env2bidopeningdate = models.DateField(db_column='env2BidOpeningDate')  # Field name made lowercase.
    env2bidopeningtime = models.TimeField(db_column='env2BidOpeningTime')  # Field name made lowercase.
    key = models.OneToOneField('Iwdmodulev2Projects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_corrigendumtable'


class Iwdmodulev2Extensionoftimedetails(models.Model):
    sno = models.CharField(db_column='sNo', max_length=200)  # Field name made lowercase.
    hindrance = models.CharField(max_length=200)
    periodofhindrance = models.IntegerField(db_column='periodOfHindrance')  # Field name made lowercase.
    periodofextension = models.IntegerField(db_column='periodOfExtension')  # Field name made lowercase.
    key = models.ForeignKey('Iwdmodulev2Projects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_extensionoftimedetails'


class Iwdmodulev2Financialbiddetails(models.Model):
    sno = models.CharField(db_column='sNo', max_length=200)  # Field name made lowercase.
    description = models.CharField(max_length=200)
    key = models.OneToOneField('Iwdmodulev2Projects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_financialbiddetails'


class Iwdmodulev2Financialcontractordetails(models.Model):
    name = models.CharField(max_length=200)
    estimatedcost = models.IntegerField(db_column='estimatedCost')  # Field name made lowercase.
    percentagerelcost = models.IntegerField(db_column='percentageRelCost')  # Field name made lowercase.
    perfigures = models.IntegerField(db_column='perFigures')  # Field name made lowercase.
    totalcost = models.IntegerField(db_column='totalCost')  # Field name made lowercase.
    key = models.ForeignKey(Iwdmodulev2Financialbiddetails, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_financialcontractordetails'


class Iwdmodulev2Inventory(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    cost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_inventory'


class Iwdmodulev2Letterofintentdetails(models.Model):
    nitniqno = models.IntegerField(db_column='nitNiqNo')  # Field name made lowercase.
    dateofopening = models.DateField(db_column='dateOfOpening')  # Field name made lowercase.
    agency = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    tendervalue = models.IntegerField(db_column='tenderValue')  # Field name made lowercase.
    key = models.OneToOneField('Iwdmodulev2Projects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_letterofintentdetails'


class Iwdmodulev2Milestones(models.Model):
    sno = models.CharField(db_column='sNo', max_length=200)  # Field name made lowercase.
    description = models.CharField(max_length=200)
    timeallowed = models.IntegerField(db_column='timeAllowed')  # Field name made lowercase.
    amountwithheld = models.IntegerField(db_column='amountWithheld')  # Field name made lowercase.
    key = models.ForeignKey('Iwdmodulev2Projects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_milestones'


class Iwdmodulev2Nooftechnicalbidtimes(models.Model):
    number = models.IntegerField()
    key = models.OneToOneField('Iwdmodulev2Projects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_nooftechnicalbidtimes'


class Iwdmodulev2Pageonedetails(models.Model):
    aesfile = models.CharField(db_column='aESFile', max_length=100, blank=True, null=True)  # Field name made lowercase.
    dasa = models.DateField(db_column='dASA', blank=True, null=True)  # Field name made lowercase.
    nitniqno = models.IntegerField(db_column='nitNiqNo', blank=True, null=True)  # Field name made lowercase.
    proth = models.CharField(db_column='proTh', max_length=200, blank=True, null=True)  # Field name made lowercase.
    emddetails = models.CharField(db_column='emdDetails', max_length=200, blank=True, null=True)  # Field name made lowercase.
    prebiddate = models.DateField(db_column='preBidDate', blank=True, null=True)  # Field name made lowercase.
    technicalbiddate = models.DateField(db_column='technicalBidDate', blank=True, null=True)  # Field name made lowercase.
    financialbiddate = models.DateField(db_column='financialBidDate', blank=True, null=True)  # Field name made lowercase.
    page_id = models.OneToOneField('Iwdmodulev2Projects', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_pageonedetails'


class Iwdmodulev2Pagethreedetails(models.Model):
    extensionoftime = models.CharField(db_column='extensionOfTime', max_length=100)  # Field name made lowercase.
    actualcostofbuilding = models.IntegerField(db_column='actualCostOfBuilding')  # Field name made lowercase.
    page_id = models.OneToOneField('Iwdmodulev2Projects', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_pagethreedetails'


class Iwdmodulev2Pagetwodetails(models.Model):
    corrigendum = models.CharField(max_length=100, blank=True, null=True)
    addendum = models.CharField(max_length=100, blank=True, null=True)
    prebidmeetingdetails = models.CharField(db_column='preBidMeetingDetails', max_length=100, blank=True, null=True)  # Field name made lowercase.
    technicalbidmeetingdetails = models.CharField(db_column='technicalBidMeetingDetails', max_length=100, blank=True, null=True)  # Field name made lowercase.
    technicallyqualifiedagencies = models.CharField(db_column='technicallyQualifiedAgencies', max_length=200, blank=True, null=True)  # Field name made lowercase.
    financialbidmeetingdetails = models.CharField(db_column='financialBidMeetingDetails', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nameoflowestagency = models.CharField(db_column='nameOfLowestAgency', max_length=200, blank=True, null=True)  # Field name made lowercase.
    letterofintent = models.CharField(db_column='letterOfIntent', max_length=100, blank=True, null=True)  # Field name made lowercase.
    workorder = models.CharField(db_column='workOrder', max_length=100, blank=True, null=True)  # Field name made lowercase.
    agreementletter = models.CharField(db_column='agreementLetter', max_length=100, blank=True, null=True)  # Field name made lowercase.
    milestones = models.CharField(max_length=100, blank=True, null=True)
    page_id = models.OneToOneField('Iwdmodulev2Projects', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_pagetwodetails'


class Iwdmodulev2Prebiddetails(models.Model):
    sno = models.CharField(db_column='sNo', max_length=200)  # Field name made lowercase.
    nameofparticipants = models.CharField(db_column='nameOfParticipants', max_length=200)  # Field name made lowercase.
    issuesraised = models.CharField(db_column='issuesRaised', max_length=200)  # Field name made lowercase.
    responsedecision = models.CharField(db_column='responseDecision', max_length=200)  # Field name made lowercase.
    key = models.OneToOneField('Iwdmodulev2Projects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_prebiddetails'


class Iwdmodulev2Projects(models.Model):
    id = models.CharField(primary_key=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_projects'


class Iwdmodulev2Requests(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    area = models.CharField(max_length=200)
    requestcreatedby = models.CharField(db_column='requestCreatedBy', max_length=200)  # Field name made lowercase.
    engineerprocessed = models.IntegerField(db_column='engineerProcessed')  # Field name made lowercase.
    directorapproval = models.IntegerField(db_column='directorApproval')  # Field name made lowercase.
    deanprocessed = models.IntegerField(db_column='deanProcessed')  # Field name made lowercase.
    status = models.CharField(max_length=200)
    issuedworkorder = models.IntegerField(db_column='issuedWorkOrder')  # Field name made lowercase.
    workcompleted = models.IntegerField(db_column='workCompleted')  # Field name made lowercase.
    billgenerated = models.IntegerField(db_column='billGenerated')  # Field name made lowercase.
    billprocessed = models.IntegerField(db_column='billProcessed')  # Field name made lowercase.
    billsettled = models.IntegerField(db_column='billSettled')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_requests'


class Iwdmodulev2Technicalbidcontractordetails(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    key = models.ForeignKey('Iwdmodulev2Technicalbiddetails', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_technicalbidcontractordetails'


class Iwdmodulev2Technicalbiddetails(models.Model):
    sno = models.CharField(db_column='sNo', max_length=200)  # Field name made lowercase.
    requirements = models.CharField(max_length=200)
    key = models.OneToOneField(Iwdmodulev2Projects, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_technicalbiddetails'


class Iwdmodulev2Useditems(models.Model):
    itemname = models.CharField(db_column='itemName', max_length=200)  # Field name made lowercase.
    cost = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateField()
    request_id = models.ForeignKey(Iwdmodulev2Requests, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_useditems'


class Iwdmodulev2Workorder(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    agency = models.CharField(max_length=200)
    amount = models.IntegerField()
    deposit = models.IntegerField()
    alloted_time = models.CharField(max_length=200)
    start_date = models.DateField()
    completion_date = models.DateField()
    request_id = models.ForeignKey(Iwdmodulev2Requests, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_workorder'


class Iwdmodulev2Workorderform(models.Model):
    issuedate = models.DateField(db_column='issueDate')  # Field name made lowercase.
    nitniqno = models.IntegerField(db_column='nitNiqNo')  # Field name made lowercase.
    agency = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    amount = models.IntegerField()
    time = models.IntegerField()
    monthday = models.IntegerField(db_column='monthDay')  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate')  # Field name made lowercase.
    completiondate = models.DateField(db_column='completionDate')  # Field name made lowercase.
    deposit = models.IntegerField()
    contractday = models.IntegerField(db_column='contractDay')  # Field name made lowercase.
    key = models.OneToOneField(Iwdmodulev2Projects, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iwdModuleV2_workorderform'


class LeaveClosedholiday(models.Model):
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'leave_closedholiday'


class LeaveLeave(models.Model):
    purpose = models.CharField(max_length=500)
    status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(blank=True, null=True)
    extra_info = models.CharField(max_length=200, blank=True, null=True)
    applicant = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'leave_leave'


class LeaveLeaveadministrators(models.Model):
    authority = models.ForeignKey(GlobalsDesignation, models.DO_NOTHING, blank=True, null=True)
    officer = models.ForeignKey(GlobalsDesignation, models.DO_NOTHING, blank=True, null=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'leave_leaveadministrators'


class LeaveLeavemigration(models.Model):
    type_migration = models.CharField(max_length=10)
    on_date = models.DateField()
    replacement_type = models.CharField(max_length=20)
    leave = models.ForeignKey(LeaveLeave, models.DO_NOTHING)
    replacee = models.ForeignKey(AuthUser, models.DO_NOTHING)
    replacer = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'leave_leavemigration'


class LeaveLeaveoffline(models.Model):
    purpose = models.CharField(max_length=500)
    timestamp = models.DateTimeField(blank=True, null=True)
    application_date = models.DateField()
    applicant = models.ForeignKey(AuthUser, models.DO_NOTHING)
    leave_user_select = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leave_leaveoffline'


class LeaveLeaverequest(models.Model):
    remark = models.CharField(max_length=50, blank=True, null=True)
    permission = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    leave = models.ForeignKey(LeaveLeave, models.DO_NOTHING)
    requested_from = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'leave_leaverequest'


class LeaveLeavescount(models.Model):
    year = models.IntegerField()
    remaining_leaves = models.FloatField()
    leave_type = models.ForeignKey('LeaveLeavetype', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'leave_leavescount'


class LeaveLeavesegment(models.Model):
    document = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    start_half = models.BooleanField()
    end_date = models.DateField()
    end_half = models.BooleanField()
    address = models.CharField(max_length=500, blank=True, null=True)
    leave = models.ForeignKey(LeaveLeave, models.DO_NOTHING)
    leave_type = models.ForeignKey('LeaveLeavetype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leave_leavesegment'


class LeaveLeavesegmentoffline(models.Model):
    document = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    start_half = models.BooleanField()
    end_date = models.DateField()
    end_half = models.BooleanField()
    address = models.CharField(max_length=500, blank=True, null=True)
    leave = models.ForeignKey(LeaveLeaveoffline, models.DO_NOTHING)
    leave_type = models.ForeignKey('LeaveLeavetype', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'leave_leavesegmentoffline'


class LeaveLeavetype(models.Model):
    name = models.CharField(max_length=40)
    max_in_year = models.IntegerField()
    requires_proof = models.BooleanField()
    authority_forwardable = models.BooleanField()
    for_faculty = models.BooleanField()
    for_staff = models.BooleanField()
    for_student = models.BooleanField()
    requires_address = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'leave_leavetype'


class LeaveReplacementsegment(models.Model):
    replacement_type = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20)
    remark = models.CharField(max_length=50, blank=True, null=True)
    leave = models.ForeignKey(LeaveLeave, models.DO_NOTHING)
    replacer = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'leave_replacementsegment'


class LeaveReplacementsegmentoffline(models.Model):
    replacement_type = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    leave = models.ForeignKey(LeaveLeaveoffline, models.DO_NOTHING)
    replacer = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'leave_replacementsegmentoffline'


class LeaveRestrictedholiday(models.Model):
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'leave_restrictedholiday'


class LeaveVacationholiday(models.Model):
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'leave_vacationholiday'


class NotificationsNotification(models.Model):
    level = models.CharField(max_length=20)
    unread = models.BooleanField()
    actor_object_id = models.CharField(max_length=255)
    verb = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    target_object_id = models.CharField(max_length=255, blank=True, null=True)
    action_object_object_id = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField()
    public = models.BooleanField()
    action_object_content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    actor_content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    recipient = models.ForeignKey(AuthUser, models.DO_NOTHING)
    target_content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    deleted = models.BooleanField()
    emailed = models.BooleanField()
    data = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notifications_notification'


class OfficeModuleBudget(models.Model):
    budget_type = models.CharField(max_length=20)
    club_type = models.CharField(max_length=20)
    budget_allocated = models.IntegerField()
    budget_expenditure = models.IntegerField()
    budget_available = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'office_module_budget'


class OfficeModuleDeansApproveCommittes(models.Model):
    date_approved = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=200)
    convener = models.ForeignKey(GlobalsExtrainfo, models.DO_NOTHING)
    faculty_incharge = models.ForeignKey(GlobalsExtrainfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'office_module_deans_approve_committes'


class OfficeModuleFilemovement(models.Model):
    date = models.DateTimeField()
    remarks = models.CharField(max_length=200, blank=True, null=True)
    actionby_receiver = models.CharField(max_length=50)
    receivedby = models.ForeignKey(GlobalsHoldsdesignation, models.DO_NOTHING)
    rid = models.ForeignKey('OfficeModuleRequisitions', models.DO_NOTHING)
    sentby = models.ForeignKey(GlobalsHoldsdesignation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'office_module_filemovement'


class OfficeModuleHostelGuestroomApproval(models.Model):
    hall_no = models.CharField(max_length=16)
    arrival_date = models.DateField()
    departure_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20)
    intender = models.ForeignKey(GlobalsExtrainfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'office_module_hostel_guestroom_approval'


class OfficeModuleProjectClosure(models.Model):
    completion_date = models.DateField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    expenses_dues = models.CharField(max_length=20)
    expenses_dues_description = models.CharField(max_length=200, blank=True, null=True)
    payment_dues = models.CharField(max_length=20)
    payment_dues_description = models.CharField(max_length=200, blank=True, null=True)
    salary_dues = models.CharField(max_length=20)
    salary_dues_description = models.CharField(max_length=200, blank=True, null=True)
    advances_dues = models.CharField(max_length=20)
    advances_description = models.CharField(max_length=200, blank=True, null=True)
    others_dues = models.CharField(max_length=20)
    other_dues_description = models.CharField(max_length=200, blank=True, null=True)
    overhead_deducted = models.CharField(max_length=20)
    overhead_description = models.CharField(max_length=200, blank=True, null=True)
    hod_response = models.CharField(db_column='HOD_response', max_length=10)  # Field name made lowercase.
    drspc_response = models.CharField(db_column='DRSPC_response', max_length=10)  # Field name made lowercase.
    remarks = models.CharField(max_length=300, blank=True, null=True)
    extended_duration = models.CharField(max_length=100, blank=True, null=True)
    project_id = models.ForeignKey('OfficeModuleProjectRegistration', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'office_module_project_closure'


class OfficeModuleProjectExtension(models.Model):
    date = models.DateField(blank=True, null=True)
    extended_duration = models.IntegerField()
    extension_details = models.CharField(max_length=300)
    hod_response = models.CharField(db_column='HOD_response', max_length=10)  # Field name made lowercase.
    drspc_response = models.CharField(db_column='DRSPC_response', max_length=10)  # Field name made lowercase.
    file = models.CharField(max_length=100, blank=True, null=True)
    project_id = models.ForeignKey('OfficeModuleProjectRegistration', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'office_module_project_extension'


class OfficeModuleProjectReallocation(models.Model):
    date = models.DateField(blank=True, null=True)
    previous_budget_head = models.CharField(max_length=300)
    previous_amount = models.IntegerField()
    pf_no = models.CharField(max_length=100, blank=True, null=True)
    new_budget_head = models.CharField(max_length=300)
    new_amount = models.IntegerField()
    transfer_reason = models.CharField(max_length=300)
    hod_response = models.CharField(db_column='HOD_response', max_length=10)  # Field name made lowercase.
    drspc_response = models.CharField(db_column='DRSPC_response', max_length=10)  # Field name made lowercase.
    project_id = models.ForeignKey('OfficeModuleProjectRegistration', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'office_module_project_reallocation'


class OfficeModuleProjectRegistration(models.Model):
    project_title = models.CharField(max_length=200)
    sponsored_agency = models.CharField(max_length=100)
    co_pi = models.CharField(db_column='CO_PI', max_length=100, blank=True, null=True)  # Field name made lowercase.
    start_date = models.DateField(blank=True, null=True)
    duration = models.IntegerField()
    agreement = models.CharField(max_length=20)
    amount_sanctioned = models.IntegerField()
    project_type = models.CharField(max_length=25)
    project_operated = models.CharField(max_length=50)
    remarks = models.CharField(max_length=200)
    fund_recieved_date = models.DateField(blank=True, null=True)
    hod_response = models.CharField(db_column='HOD_response', max_length=10)  # Field name made lowercase.
    drspc_response = models.CharField(db_column='DRSPC_response', max_length=10)  # Field name made lowercase.
    applied_date = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    file = models.CharField(max_length=100, blank=True, null=True)
    pi_id = models.ForeignKey(GlobalsExtrainfo, models.DO_NOTHING, db_column='PI_id_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'office_module_project_registration'


class OfficeModuleRegistrar(models.Model):
    file_name = models.CharField(max_length=50)
    date = models.DateField()
    purpose = models.CharField(max_length=100)
    status = models.CharField(max_length=1)
    file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'office_module_registrar'


class OfficeModuleRegistrarCreateDoc(models.Model):
    file_name = models.CharField(max_length=50)
    purpose = models.CharField(max_length=100)
    description = models.CharField(db_column='Description', max_length=200)  # Field name made lowercase.
    file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'office_module_registrar_create_doc'


class OfficeModuleRegistrarDirectorSection(models.Model):
    file_name = models.CharField(max_length=50)
    date = models.DateField()
    purpose = models.CharField(max_length=100)
    status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'office_module_registrar_director_section'


class OfficeModuleRegistrarEstablishmentSection(models.Model):
    person_name = models.CharField(max_length=50)
    person_mail_id = models.CharField(max_length=50)
    date = models.DateField()
    duration = models.IntegerField()
    post = models.CharField(max_length=100)
    file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'office_module_registrar_establishment_section'


class OfficeModuleRegistrarFile(models.Model):
    status = models.IntegerField()
    approval = models.IntegerField()
    section_name = models.CharField(max_length=50)
    section_type = models.CharField(max_length=20)
    file_id = models.ForeignKey(Tracking, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'office_module_registrar_file'


class OfficeModuleRegistrarFinanceSection(models.Model):
    file_name = models.CharField(max_length=50)
    date = models.DateField()
    purpose = models.CharField(max_length=100)
    status = models.IntegerField()
    file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'office_module_registrar_finance_section'


class OfficeModuleRegistrarGeneralSection(models.Model):
    file_name = models.CharField(max_length=50)
    date = models.DateField()
    amount = models.IntegerField()
    status = models.IntegerField()
    file = models.ForeignKey(OfficeModuleRegistrarCreateDoc, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'office_module_registrar_general_section'


class OfficeModuleRegistrarPurchaseSalesSection(models.Model):
    file_name = models.CharField(max_length=50)
    member1 = models.CharField(max_length=50)
    member2 = models.CharField(max_length=50)
    member3 = models.CharField(max_length=50)
    date = models.DateField()
    purpose = models.CharField(max_length=100)
    status = models.IntegerField()
    file = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'office_module_registrar_purchase_sales_section'


class OfficeModuleRequisitions(models.Model):
    req_date = models.DateTimeField()
    title = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    building = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    tag = models.IntegerField()
    assign_file = models.ForeignKey(File, models.DO_NOTHING, blank=True, null=True)
    userid = models.ForeignKey(GlobalsExtrainfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'office_module_requisitions'


class OnlineCmsAssignment(models.Model):
    upload_time = models.DateTimeField()
    submit_date = models.DateTimeField()
    assignment_name = models.CharField(max_length=100)
    assignment_url = models.CharField(max_length=100, blank=True, null=True)
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_assignment'


class OnlineCmsAttendance(models.Model):
    date = models.DateField()
    present = models.IntegerField()
    instructor_id = models.ForeignKey('ProgrammeCurriculumCourseinstructor', models.DO_NOTHING)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)
    no_of_attendance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'online_cms_attendance'


class OnlineCmsAttendancefiles(models.Model):
    upload_time = models.DateTimeField()
    file_name = models.CharField(max_length=40)
    file_url = models.CharField(max_length=100, blank=True, null=True)
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_attendancefiles'


class OnlineCmsCoursedocuments(models.Model):
    upload_time = models.DateTimeField()
    description = models.CharField(max_length=100)
    document_name = models.CharField(max_length=40)
    document_url = models.CharField(max_length=100, blank=True, null=True)
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)
    module_id = models.ForeignKey('OnlineCmsModules', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_coursedocuments'


class OnlineCmsCoursevideo(models.Model):
    upload_time = models.DateTimeField()
    description = models.CharField(max_length=100)
    video_name = models.CharField(max_length=40)
    video_url = models.CharField(max_length=100, blank=True, null=True)
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_coursevideo'


class OnlineCmsForum(models.Model):
    comment_time = models.DateTimeField()
    comment = models.TextField()
    commenter_id = models.ForeignKey(GlobalsExtrainfo, models.DO_NOTHING)
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_forum'


class OnlineCmsForumreply(models.Model):
    forum_ques = models.ForeignKey(OnlineCmsForum, models.DO_NOTHING)
    forum_reply = models.ForeignKey(OnlineCmsForum, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_forumreply'


class OnlineCmsGradingscheme(models.Model):
    type_of_evaluation = models.CharField(max_length=100)
    weightage = models.DecimalField(max_digits=10, decimal_places=2)
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_gradingscheme'


class OnlineCmsGradingschemeGrades(models.Model):
    o_lower = models.DecimalField(db_column='O_Lower', max_digits=10, decimal_places=2)  # Field name made lowercase.
    o_upper = models.DecimalField(db_column='O_Upper', max_digits=10, decimal_places=2)  # Field name made lowercase.
    a_plus_lower = models.DecimalField(db_column='A_plus_Lower', max_digits=10, decimal_places=2)  # Field name made lowercase.
    a_plus_upper = models.DecimalField(db_column='A_plus_Upper', max_digits=10, decimal_places=2)  # Field name made lowercase.
    a_lower = models.DecimalField(db_column='A_Lower', max_digits=10, decimal_places=2)  # Field name made lowercase.
    a_upper = models.DecimalField(db_column='A_Upper', max_digits=10, decimal_places=2)  # Field name made lowercase.
    b_plus_lower = models.DecimalField(db_column='B_plus_Lower', max_digits=10, decimal_places=2)  # Field name made lowercase.
    b_plus_upper = models.DecimalField(db_column='B_plus_Upper', max_digits=10, decimal_places=2)  # Field name made lowercase.
    b_lower = models.DecimalField(db_column='B_Lower', max_digits=10, decimal_places=2)  # Field name made lowercase.
    b_upper = models.DecimalField(db_column='B_Upper', max_digits=10, decimal_places=2)  # Field name made lowercase.
    c_plus_lower = models.DecimalField(db_column='C_plus_Lower', max_digits=10, decimal_places=2)  # Field name made lowercase.
    c_plus_upper = models.DecimalField(db_column='C_plus_Upper', max_digits=10, decimal_places=2)  # Field name made lowercase.
    c_lower = models.DecimalField(db_column='C_Lower', max_digits=10, decimal_places=2)  # Field name made lowercase.
    c_upper = models.DecimalField(db_column='C_Upper', max_digits=10, decimal_places=2)  # Field name made lowercase.
    d_plus_lower = models.DecimalField(db_column='D_plus_Lower', max_digits=10, decimal_places=2)  # Field name made lowercase.
    d_plus_upper = models.DecimalField(db_column='D_plus_Upper', max_digits=10, decimal_places=2)  # Field name made lowercase.
    d_lower = models.DecimalField(db_column='D_Lower', max_digits=10, decimal_places=2)  # Field name made lowercase.
    d_upper = models.DecimalField(db_column='D_Upper', max_digits=10, decimal_places=2)  # Field name made lowercase.
    f_lower = models.DecimalField(db_column='F_Lower', max_digits=10, decimal_places=2)  # Field name made lowercase.
    f_upper = models.DecimalField(db_column='F_Upper', max_digits=10, decimal_places=2)  # Field name made lowercase.
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_gradingscheme_grades'


class OnlineCmsModules(models.Model):
    module_name = models.CharField(max_length=50)
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_modules'


class OnlineCmsPractice(models.Model):
    prac_quiz_name = models.CharField(max_length=20)
    negative_marks = models.FloatField()
    number_of_question = models.IntegerField()
    description = models.TextField()
    total_score = models.IntegerField()
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_practice'


class OnlineCmsPracticequestion(models.Model):
    question = models.TextField()
    options1 = models.CharField(max_length=100, blank=True, null=True)
    options2 = models.CharField(max_length=100, blank=True, null=True)
    options3 = models.CharField(max_length=100, blank=True, null=True)
    options4 = models.CharField(max_length=100, blank=True, null=True)
    options5 = models.CharField(max_length=100, blank=True, null=True)
    answer = models.IntegerField()
    image = models.TextField(blank=True, null=True)
    prac_quiz_id = models.ForeignKey(OnlineCmsPractice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_practicequestion'


class OnlineCmsQuestion(models.Model):
    question = models.TextField()
    options1 = models.CharField(max_length=100, blank=True, null=True)
    options2 = models.CharField(max_length=100, blank=True, null=True)
    options3 = models.CharField(max_length=100, blank=True, null=True)
    options4 = models.CharField(max_length=100, blank=True, null=True)
    options5 = models.CharField(max_length=100, blank=True, null=True)
    answer = models.IntegerField()
    image = models.TextField(blank=True, null=True)
    marks = models.IntegerField()
    question_bank = models.ForeignKey('OnlineCmsQuestionbank', models.DO_NOTHING)
    topic = models.ForeignKey('OnlineCmsTopics', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_question'


class OnlineCmsQuestionbank(models.Model):
    name = models.CharField(max_length=100)
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)
    instructor_id = models.ForeignKey(GlobalsExtrainfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_questionbank'


class OnlineCmsQuiz(models.Model):
    quiz_name = models.CharField(max_length=20)
    end_time = models.DateTimeField()
    start_time = models.DateTimeField()
    d_day = models.CharField(max_length=2)
    d_hour = models.CharField(max_length=2)
    d_minute = models.CharField(max_length=2)
    negative_marks = models.FloatField()
    number_of_question = models.IntegerField()
    description = models.TextField()
    rules = models.TextField()
    total_score = models.IntegerField()
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_quiz'


class OnlineCmsQuizquestion(models.Model):
    question = models.ForeignKey(OnlineCmsQuestion, models.DO_NOTHING)
    quiz_id = models.ForeignKey(OnlineCmsQuiz, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_quizquestion'


class OnlineCmsQuizresult(models.Model):
    score = models.IntegerField()
    finished = models.BooleanField()
    quiz_id = models.ForeignKey(OnlineCmsQuiz, models.DO_NOTHING)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_quizresult'


class OnlineCmsStudentGrades(models.Model):
    semester = models.IntegerField()
    year = models.IntegerField()
    roll_no = models.TextField()
    total_marks = models.DecimalField(max_digits=10, decimal_places=2)
    grade = models.TextField()
    batch = models.IntegerField()
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_student_grades'


class OnlineCmsStudentanswer(models.Model):
    choice = models.IntegerField()
    question_id = models.ForeignKey(OnlineCmsQuizquestion, models.DO_NOTHING)
    quiz_id = models.ForeignKey(OnlineCmsQuiz, models.DO_NOTHING)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_studentanswer'


class OnlineCmsStudentassignment(models.Model):
    upload_time = models.DateTimeField()
    upload_url = models.TextField()
    score = models.IntegerField(blank=True, null=True)
    feedback = models.CharField(max_length=100, blank=True, null=True)
    assign_name = models.CharField(max_length=100)
    assignment_id = models.ForeignKey(OnlineCmsAssignment, models.DO_NOTHING)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_studentassignment'


class OnlineCmsStudentevaluation(models.Model):
    marks = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_marks = models.DecimalField(max_digits=10, decimal_places=2)
    evaluation_id = models.ForeignKey(OnlineCmsGradingscheme, models.DO_NOTHING)
    student_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_studentevaluation'


class OnlineCmsTopics(models.Model):
    topic_name = models.TextField()
    course_id = models.ForeignKey('ProgrammeCurriculumCourse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'online_cms_topics'


class PlacementCellAchievement(models.Model):
    achievement = models.CharField(max_length=100)
    achievement_type = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    issuer = models.CharField(max_length=200)
    date_earned = models.DateField()
    unique_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'placement_cell_achievement'


class PlacementCellChairmanvisit(models.Model):
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    visiting_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'placement_cell_chairmanvisit'


class PlacementCellCoauthor(models.Model):
    coauthor_name = models.CharField(max_length=100)
    publication_id = models.ForeignKey('PlacementCellPublication', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'placement_cell_coauthor'


class PlacementCellCoinventor(models.Model):
    coinventor_name = models.CharField(max_length=100)
    patent_id = models.ForeignKey('PlacementCellPatent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'placement_cell_coinventor'


class PlacementCellCompanydetails(models.Model):
    company_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'placement_cell_companydetails'


class PlacementCellConference(models.Model):
    conference_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    sdate = models.DateField()
    edate = models.DateField(blank=True, null=True)
    unique_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'placement_cell_conference'


class PlacementCellCourse(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    license_no = models.CharField(max_length=100, blank=True, null=True)
    sdate = models.DateField()
    edate = models.DateField(blank=True, null=True)
    unique_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'placement_cell_course'


class PlacementCellEducation(models.Model):
    degree = models.CharField(max_length=40)
    grade = models.CharField(max_length=10)
    institute = models.TextField()
    stream = models.CharField(max_length=150, blank=True, null=True)
    sdate = models.DateField()
    edate = models.DateField(blank=True, null=True)
    unique_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'placement_cell_education'


class PlacementCellExperience(models.Model):
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    sdate = models.DateField()
    edate = models.DateField(blank=True, null=True)
    unique_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'placement_cell_experience'


class PlacementCellExtracurricular(models.Model):
    event_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    name_of_position = models.CharField(max_length=200)
    date_earned = models.DateField()
    unique_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'placement_cell_extracurricular'


class PlacementCellHas(models.Model):
    skill_rating = models.IntegerField()
    skill_id = models.ForeignKey('PlacementCellSkill', models.DO_NOTHING)
    unique_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'placement_cell_has'
        unique_together = (('skill_id', 'unique_id'),)


class PlacementCellInterest(models.Model):
    interest = models.CharField(max_length=100)
    unique_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'placement_cell_interest'


class PlacementCellMessageofficer(models.Model):
    message = models.CharField(max_length=100)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'placement_cell_messageofficer'


class PlacementCellNotifystudent(models.Model):
    placement_type = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    ctc = models.DecimalField(max_digits=10, decimal_places=4)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'placement_cell_notifystudent'


class PlacementCellPatent(models.Model):
    patent_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    patent_office = models.TextField()
    patent_date = models.DateField()
    unique_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'placement_cell_patent'


class PlacementCellPlacementrecord(models.Model):
    placement_type = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    ctc = models.DecimalField(max_digits=5, decimal_places=2)
    year = models.IntegerField()
    test_score = models.IntegerField(blank=True, null=True)
    test_type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'placement_cell_placementrecord'


class PlacementCellPlacementschedule(models.Model):
    title = models.CharField(max_length=100)
    placement_date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    time = models.TimeField()
    attached_file = models.CharField(max_length=100, blank=True, null=True)
    schedule_at = models.DateTimeField(blank=True, null=True)
    notify_id = models.ForeignKey(PlacementCellNotifystudent, models.DO_NOTHING)
    role = models.ForeignKey('PlacementCellRole', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'placement_cell_placementschedule'


class PlacementCellPlacementstatus(models.Model):
    invitation = models.CharField(max_length=20)
    placed = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    no_of_days = models.IntegerField(blank=True, null=True)
    notify_id = models.ForeignKey(PlacementCellNotifystudent, models.DO_NOTHING)
    unique_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'placement_cell_placementstatus'
        unique_together = (('notify_id', 'unique_id'),)


class PlacementCellProject(models.Model):
    project_name = models.CharField(max_length=50)
    project_status = models.CharField(max_length=20)
    summary = models.TextField(blank=True, null=True)
    project_link = models.CharField(max_length=200, blank=True, null=True)
    sdate = models.DateField()
    edate = models.DateField(blank=True, null=True)
    unique_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'placement_cell_project'


class PlacementCellPublication(models.Model):
    publication_title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    publisher = models.TextField()
    publication_date = models.DateField()
    unique_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'placement_cell_publication'


class PlacementCellReference(models.Model):
    reference_name = models.CharField(max_length=100)
    post = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    unique_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'placement_cell_reference'


class PlacementCellRole(models.Model):
    role = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'placement_cell_role'


class PlacementCellSkill(models.Model):
    skill = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'placement_cell_skill'


class PlacementCellStudentplacement(models.Model):
    unique_id = models.OneToOneField(AcademicInformationStudent, models.DO_NOTHING, primary_key=True)
    debar = models.CharField(max_length=20)
    future_aspect = models.CharField(max_length=20)
    placed_type = models.CharField(max_length=20)
    placement_date = models.DateField(blank=True, null=True)
    package = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'placement_cell_studentplacement'


class PlacementCellStudentrecord(models.Model):
    record_id = models.ForeignKey(PlacementCellPlacementrecord, models.DO_NOTHING)
    unique_id = models.ForeignKey(AcademicInformationStudent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'placement_cell_studentrecord'
        unique_together = (('record_id', 'unique_id'),)


class ProgrammeCurriculumBatch(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()
    running_batch = models.BooleanField()
    curriculum = models.ForeignKey('ProgrammeCurriculumCurriculum', models.DO_NOTHING, blank=True, null=True)
    discipline = models.ForeignKey('ProgrammeCurriculumDiscipline', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'programme_curriculum_batch'
        unique_together = (('name', 'discipline', 'year'),)


class ProgrammeCurriculumCourse(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    credit = models.IntegerField()
    lecture_hours = models.IntegerField(blank=True, null=True)
    tutorial_hours = models.IntegerField(blank=True, null=True)
    pratical_hours = models.IntegerField(blank=True, null=True)
    discussion_hours = models.IntegerField(blank=True, null=True)
    project_hours = models.IntegerField(blank=True, null=True)
    pre_requisits = models.TextField(blank=True, null=True)
    syllabus = models.TextField()
    percent_quiz_1 = models.IntegerField()
    percent_midsem = models.IntegerField()
    percent_quiz_2 = models.IntegerField()
    percent_endsem = models.IntegerField()
    percent_project = models.IntegerField()
    percent_lab_evaluation = models.IntegerField()
    percent_course_attendance = models.IntegerField()
    ref_books = models.TextField()
    working_course = models.BooleanField()
    latest_version = models.BooleanField()
    version = models.DecimalField(max_digits=5, decimal_places=1)

    class Meta:
        managed = False
        db_table = 'programme_curriculum_course'
        unique_together = (('code', 'version'),)


class ProgrammeCurriculumCourseDisciplines(models.Model):
    course = models.ForeignKey(ProgrammeCurriculumCourse, models.DO_NOTHING)
    discipline = models.ForeignKey('ProgrammeCurriculumDiscipline', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'programme_curriculum_course_disciplines'
        unique_together = (('course', 'discipline'),)


class ProgrammeCurriculumCoursePreRequisitCourses(models.Model):
    from_course = models.ForeignKey(ProgrammeCurriculumCourse, models.DO_NOTHING)
    to_course = models.ForeignKey(ProgrammeCurriculumCourse, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'programme_curriculum_course_pre_requisit_courses'
        unique_together = (('from_course', 'to_course'),)


class ProgrammeCurriculumCourseinstructor(models.Model):
    batch_id = models.ForeignKey(ProgrammeCurriculumBatch, models.DO_NOTHING)
    course_id = models.ForeignKey(ProgrammeCurriculumCourse, models.DO_NOTHING)
    instructor_id = models.ForeignKey(GlobalsExtrainfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'programme_curriculum_courseinstructor'
        unique_together = (('course_id', 'instructor_id', 'batch_id'),)


class ProgrammeCurriculumCourseslot(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=70)
    course_slot_info = models.TextField(blank=True, null=True)
    duration = models.IntegerField()
    min_registration_limit = models.IntegerField()
    max_registration_limit = models.IntegerField()
    semester = models.ForeignKey('ProgrammeCurriculumSemester', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'programme_curriculum_courseslot'
        unique_together = (('semester', 'name', 'type'),)


class ProgrammeCurriculumCourseslotCourses(models.Model):
    courseslot = models.ForeignKey(ProgrammeCurriculumCourseslot, models.DO_NOTHING)
    course = models.ForeignKey(ProgrammeCurriculumCourse, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'programme_curriculum_courseslot_courses'
        unique_together = (('courseslot', 'course'),)


class ProgrammeCurriculumCurriculum(models.Model):
    name = models.CharField(max_length=100)
    version = models.DecimalField(max_digits=5, decimal_places=1)
    working_curriculum = models.BooleanField()
    no_of_semester = models.IntegerField()
    min_credit = models.IntegerField()
    programme = models.ForeignKey('ProgrammeCurriculumProgramme', models.DO_NOTHING)
    latest_version = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'programme_curriculum_curriculum'
        unique_together = (('name', 'version'),)


class ProgrammeCurriculumDiscipline(models.Model):
    name = models.CharField(unique=True, max_length=100)
    acronym = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'programme_curriculum_discipline'


class ProgrammeCurriculumDisciplineProgrammes(models.Model):
    discipline = models.ForeignKey(ProgrammeCurriculumDiscipline, models.DO_NOTHING)
    programme = models.ForeignKey('ProgrammeCurriculumProgramme', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'programme_curriculum_discipline_programmes'
        unique_together = (('discipline', 'programme'),)


class ProgrammeCurriculumNewproposalfile(models.Model):
    uploader = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    credit = models.IntegerField()
    lecture_hours = models.IntegerField(blank=True, null=True)
    tutorial_hours = models.IntegerField(blank=True, null=True)
    pratical_hours = models.IntegerField(blank=True, null=True)
    discussion_hours = models.IntegerField(blank=True, null=True)
    project_hours = models.IntegerField(blank=True, null=True)
    pre_requisits = models.TextField(blank=True, null=True)
    syllabus = models.TextField()
    percent_quiz_1 = models.IntegerField()
    percent_midsem = models.IntegerField()
    percent_quiz_2 = models.IntegerField()
    percent_endsem = models.IntegerField()
    percent_project = models.IntegerField()
    percent_lab_evaluation = models.IntegerField()
    percent_course_attendance = models.IntegerField()
    ref_books = models.TextField()
    subject = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=400, blank=True, null=True)
    upload_date = models.DateTimeField()
    is_read = models.BooleanField()
    is_update = models.BooleanField()
    is_archive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'programme_curriculum_newproposalfile'
        unique_together = (('code', 'uploader', 'name'),)


class ProgrammeCurriculumNewproposalfilePreRequisitCourses(models.Model):
    newproposalfile = models.ForeignKey(ProgrammeCurriculumNewproposalfile, models.DO_NOTHING)
    course = models.ForeignKey(ProgrammeCurriculumCourse, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'programme_curriculum_newproposalfile_pre_requisit_courses'
        unique_together = (('newproposalfile', 'course'),)


class ProgrammeCurriculumProgramme(models.Model):
    category = models.CharField(max_length=3)
    name = models.CharField(unique=True, max_length=70)
    programme_begin_year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'programme_curriculum_programme'


class ProgrammeCurriculumProposalTracking(models.Model):
    file_id = models.CharField(max_length=100)
    current_id = models.CharField(max_length=100)
    current_design = models.CharField(max_length=100)
    receive_date = models.DateTimeField()
    forward_date = models.DateTimeField()
    remarks = models.CharField(max_length=250, blank=True, null=True)
    is_added = models.BooleanField()
    is_submitted = models.BooleanField()
    is_rejected = models.BooleanField()
    disciplines = models.ForeignKey(ProgrammeCurriculumDiscipline, models.DO_NOTHING)
    receive_design = models.ForeignKey(GlobalsDesignation, models.DO_NOTHING)
    receive_id = models.ForeignKey(AuthUser, models.DO_NOTHING)
    receiver_archive = models.BooleanField()
    sender_archive = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'programme_curriculum_proposal_tracking'
        unique_together = (('file_id', 'current_id', 'current_design', 'disciplines'),)


class ProgrammeCurriculumSemester(models.Model):
    semester_no = models.IntegerField()
    instigate_semester = models.BooleanField(blank=True, null=True)
    start_semester = models.DateField(blank=True, null=True)
    end_semester = models.DateField(blank=True, null=True)
    semester_info = models.TextField(blank=True, null=True)
    curriculum = models.ForeignKey(ProgrammeCurriculumCurriculum, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'programme_curriculum_semester'
        unique_together = (('curriculum', 'semester_no'),)


class PurchaseCommitee(models.Model):
    approve_mem1 = models.IntegerField()
    approve_mem2 = models.IntegerField()
    approve_mem3 = models.IntegerField()
    local_comm_mem1 = models.ForeignKey(GlobalsExtrainfo, models.DO_NOTHING)
    local_comm_mem2 = models.ForeignKey(GlobalsExtrainfo, models.DO_NOTHING)
    local_comm_mem3 = models.ForeignKey(GlobalsExtrainfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'purchase_commitee'


class Quotations(models.Model):
    quotation1 = models.CharField(max_length=100)
    quotation2 = models.CharField(max_length=100)
    quotation3 = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'quotations'


class RecruitmentAcademicdetails(models.Model):
    area_of_specialization = models.TextField()
    current_area_of_research = models.TextField()
    date_of_enrollment_in_phd = models.DateField()
    date_of_phd_defence = models.DateField()
    date_of_award_of_phd = models.DateField()
    xiith = models.OneToOneField('RecruitmentEducationaldetails', models.DO_NOTHING, db_column='XIIth_id')  # Field name made lowercase.
    xth = models.OneToOneField('RecruitmentEducationaldetails', models.DO_NOTHING, db_column='Xth_id')  # Field name made lowercase.
    graduation = models.OneToOneField('RecruitmentEducationaldetails', models.DO_NOTHING)
    phd = models.OneToOneField('RecruitmentEducationaldetails', models.DO_NOTHING)
    post_graduation = models.OneToOneField('RecruitmentEducationaldetails', models.DO_NOTHING)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_academicdetails'


class RecruitmentAdministrativeexperience(models.Model):
    period = models.IntegerField(blank=True, null=True)
    organization = models.CharField(max_length=200, blank=True, null=True)
    title_of_post = models.CharField(max_length=200, blank=True, null=True)
    nature_of_work = models.TextField(blank=True, null=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_administrativeexperience'


class RecruitmentApplied(models.Model):
    date = models.DateField()
    advertisement_number = models.ForeignKey('RecruitmentVacancy', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_applied'


class RecruitmentBankdetails(models.Model):
    payment_reference_number = models.CharField(max_length=20)
    payment_date = models.DateField()
    bank_name = models.CharField(max_length=100)
    bank_branch = models.CharField(max_length=200)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_bankdetails'


class RecruitmentBooks(models.Model):
    name_of_book = models.CharField(max_length=100)
    year = models.IntegerField()
    published = models.BooleanField()
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    co_author = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_books'


class RecruitmentConsultancy(models.Model):
    period = models.CharField(max_length=10)
    sponsoring_organisation = models.CharField(max_length=200)
    title_of_project = models.CharField(max_length=200)
    grant_amount = models.IntegerField(blank=True, null=True)
    co_investigators = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_consultancy'


class RecruitmentCoursestaught(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=20, blank=True, null=True)
    number_of_times = models.IntegerField(blank=True, null=True)
    developed_by_you = models.BooleanField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_coursestaught'


class RecruitmentEducationaldetails(models.Model):
    university = models.CharField(max_length=200)
    board = models.CharField(max_length=200)
    year_of_passing = models.IntegerField()
    division = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'recruitment_educationaldetails'


class RecruitmentExperience(models.Model):
    duration = models.IntegerField(blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recruitment_experience'


class RecruitmentExperiencedetails(models.Model):
    total_experience_months = models.IntegerField(blank=True, null=True)
    member_of_professional_body = models.CharField(max_length=200, blank=True, null=True)
    employer = models.CharField(max_length=100, blank=True, null=True)
    position_held = models.CharField(max_length=100, blank=True, null=True)
    date_of_joining = models.DateField(blank=True, null=True)
    date_of_leaving = models.DateField(blank=True, null=True)
    pay_in_payband = models.CharField(max_length=20, blank=True, null=True)
    payband = models.CharField(max_length=20, blank=True, null=True)
    agp = models.CharField(db_column='AGP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reasons_for_leaving = models.TextField(blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_experiencedetails'


class RecruitmentIndustrialexperience(models.Model):
    period = models.IntegerField(blank=True, null=True)
    organization = models.CharField(max_length=200, blank=True, null=True)
    title_of_post = models.CharField(max_length=200, blank=True, null=True)
    nature_of_work = models.TextField(blank=True, null=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_industrialexperience'


class RecruitmentInternationalconference(models.Model):
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    title = models.CharField(max_length=100)
    name_and_place_of_conference = models.CharField(max_length=200)
    presented = models.BooleanField()
    published = models.BooleanField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_internationalconference'


class RecruitmentNationalconference(models.Model):
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    title = models.CharField(max_length=100)
    name_and_place_of_conference = models.CharField(max_length=200)
    presented = models.BooleanField()
    published = models.BooleanField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_nationalconference'


class RecruitmentPapersinreferredjournal(models.Model):
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    published = models.BooleanField()
    accepted = models.BooleanField()
    title = models.CharField(max_length=100)
    reference_of_journal = models.CharField(max_length=100)
    impact_factor = models.CharField(max_length=100)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_papersinreferredjournal'


class RecruitmentPatent(models.Model):
    filed_national = models.CharField(max_length=200, blank=True, null=True)
    filed_international = models.CharField(max_length=200, blank=True, null=True)
    award_national = models.CharField(max_length=200, blank=True, null=True)
    award_international = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_patent'


class RecruitmentPersonaldetails(models.Model):
    title = models.CharField(max_length=20)
    sex = models.CharField(max_length=2)
    profile_picture = models.CharField(max_length=100, blank=True, null=True)
    marital_status = models.CharField(max_length=10)
    discipline = models.CharField(max_length=50)
    specialization = models.CharField(max_length=10)
    category = models.CharField(max_length=20)
    father_name = models.CharField(max_length=40)
    address_correspondence = models.TextField()
    address_permanent = models.TextField()
    email_alternate = models.CharField(max_length=50, blank=True, null=True)
    phone_no = models.BigIntegerField(blank=True, null=True)
    mobile_no_first = models.BigIntegerField()
    mobile_no_second = models.BigIntegerField(blank=True, null=True)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=30)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_personaldetails'


class RecruitmentPublications(models.Model):
    referred_journal = models.CharField(max_length=100)
    sci_index_journal = models.CharField(max_length=100)
    international_conferences = models.CharField(max_length=100, blank=True, null=True)
    national_conferences = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_publications'


class RecruitmentQualifiedexams(models.Model):
    net = models.BooleanField()
    gate = models.BooleanField()
    jrf = models.BooleanField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_qualifiedexams'


class RecruitmentReferences(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=254)
    mobile_number = models.BigIntegerField()
    department = models.CharField(max_length=50)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_references'


class RecruitmentResearchexperience(models.Model):
    research_experience = models.ForeignKey(RecruitmentExperience, models.DO_NOTHING)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_researchexperience'


class RecruitmentSponsoredprojects(models.Model):
    period = models.CharField(max_length=10)
    sponsoring_organisation = models.CharField(max_length=200)
    title_of_project = models.CharField(max_length=200)
    grant_amount = models.IntegerField(blank=True, null=True)
    co_investigators = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_sponsoredprojects'


class RecruitmentTeachingexperience(models.Model):
    teaching_experience = models.ForeignKey(RecruitmentExperience, models.DO_NOTHING)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_teachingexperience'


class RecruitmentThesissupervision(models.Model):
    name_of_student = models.CharField(max_length=200)
    masters_or_phd = models.CharField(max_length=20)
    year_of_completion = models.IntegerField()
    title_of_thesis = models.CharField(max_length=100)
    co_guides = models.CharField(max_length=200, blank=True, null=True)
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'recruitment_thesissupervision'


class RecruitmentVacancy(models.Model):
    advertisement_number = models.IntegerField()
    job_description = models.TextField()
    job_notification = models.CharField(max_length=100)
    number_of_vacancy = models.IntegerField()
    job_type = models.CharField(max_length=15)
    last_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'recruitment_vacancy'


class ResearchProceduresCategory(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=500)
    sub_category_name = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'research_procedures_category'


class ResearchProceduresCoPis(models.Model):
    co_pi = models.ForeignKey(AuthUser, models.DO_NOTHING)
    project_id = models.ForeignKey('ResearchProceduresProjects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'research_procedures_co_pis'


class ResearchProceduresCoProjectInvestigator(models.Model):
    co_pi_id = models.ForeignKey(AuthUser, models.DO_NOTHING)
    project_id = models.ForeignKey('ResearchProceduresProjects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'research_procedures_co_project_investigator'


class ResearchProceduresFinancialOutlay(models.Model):
    financial_outlay_id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=500)
    sub_category = models.CharField(max_length=500)
    amount = models.IntegerField()
    year = models.IntegerField()
    status = models.IntegerField()
    staff_limit = models.IntegerField()
    utilized_amount = models.IntegerField(blank=True, null=True)
    project_id = models.ForeignKey('ResearchProceduresProjects', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'research_procedures_financial_outlay'


class ResearchProceduresProjects(models.Model):
    project_id = models.IntegerField(primary_key=True)
    project_name = models.CharField(max_length=600)
    project_type = models.CharField(max_length=500)
    sponsored_agency = models.CharField(max_length=500)
    start_date = models.DateField()
    submission_date = models.DateField()
    finish_date = models.DateField()
    years = models.IntegerField()
    status = models.IntegerField()
    project_info_file = models.CharField(max_length=100, blank=True, null=True)
    financial_outlay_status = models.IntegerField()
    co_project_investigator_id = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    project_investigator_id = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'research_procedures_projects'


class ResearchProceduresRequests(models.Model):
    request_id = models.IntegerField(primary_key=True)
    request_type = models.CharField(max_length=500)
    approval_status = models.IntegerField()
    project_id = models.ForeignKey(ResearchProceduresProjects, models.DO_NOTHING)
    project_investigator_id = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'research_procedures_requests'


class ResearchProceduresStaffAllocations(models.Model):
    staff_allocation_id = models.IntegerField(primary_key=True)
    staff_name = models.CharField(max_length=500)
    qualification = models.CharField(max_length=500)
    year = models.IntegerField()
    stipend = models.IntegerField()
    staff_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    project_id = models.ForeignKey(ResearchProceduresProjects, models.DO_NOTHING)
    staff_id = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'research_procedures_staff_allocations'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class Stock(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    item_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock'


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=100)
    vendor_address = models.CharField(max_length=200)
    vendor_item = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'vendor'


class VisitorHostelBill(models.Model):
    meal_bill = models.IntegerField()
    room_bill = models.IntegerField()
    payment_status = models.BooleanField()
    booking = models.OneToOneField('VisitorHostelBookingdetail', models.DO_NOTHING)
    caretaker = models.ForeignKey(AuthUser, models.DO_NOTHING)
    bill_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'visitor_hostel_bill'


class VisitorHostelBillRoom(models.Model):
    bill = models.ForeignKey(VisitorHostelBill, models.DO_NOTHING)
    roomdetail = models.ForeignKey('VisitorHostelRoomdetail', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'visitor_hostel_bill_room'
        unique_together = (('bill', 'roomdetail'),)


class VisitorHostelBookingdetail(models.Model):
    visitor_category = models.CharField(max_length=1)
    modified_visitor_category = models.CharField(max_length=1)
    person_count = models.IntegerField()
    purpose = models.TextField()
    booking_from = models.DateField()
    booking_to = models.DateField()
    arrival_time = models.TextField(blank=True, null=True)
    departure_time = models.TextField(blank=True, null=True)
    forwarded_date = models.DateField(blank=True, null=True)
    confirmed_date = models.DateField(blank=True, null=True)
    check_in = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)
    check_in_time = models.TimeField(blank=True, null=True)
    check_out_time = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=15)
    remark = models.CharField(max_length=40, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)
    number_of_rooms = models.IntegerField(blank=True, null=True)
    number_of_rooms_alloted = models.IntegerField(blank=True, null=True)
    booking_date = models.DateField()
    bill_to_be_settled_by = models.CharField(max_length=15)
    caretaker = models.ForeignKey(AuthUser, models.DO_NOTHING)
    intender = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'visitor_hostel_bookingdetail'


class VisitorHostelBookingdetailRooms(models.Model):
    bookingdetail = models.ForeignKey(VisitorHostelBookingdetail, models.DO_NOTHING)
    roomdetail = models.ForeignKey('VisitorHostelRoomdetail', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'visitor_hostel_bookingdetail_rooms'
        unique_together = (('bookingdetail', 'roomdetail'),)


class VisitorHostelBookingdetailVisitor(models.Model):
    bookingdetail = models.ForeignKey(VisitorHostelBookingdetail, models.DO_NOTHING)
    visitordetail = models.ForeignKey('VisitorHostelVisitordetail', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'visitor_hostel_bookingdetail_visitor'
        unique_together = (('bookingdetail', 'visitordetail'),)


class VisitorHostelInventory(models.Model):
    item_name = models.CharField(max_length=20)
    quantity = models.IntegerField()
    consumable = models.BooleanField()
    opening_stock = models.IntegerField()
    addition_stock = models.IntegerField()
    total_stock = models.IntegerField()
    serviceable = models.IntegerField()
    non_serviceable = models.IntegerField()
    inuse = models.IntegerField()
    total_usable = models.IntegerField()
    remark = models.TextField()

    class Meta:
        managed = False
        db_table = 'visitor_hostel_inventory'


class VisitorHostelInventorybill(models.Model):
    bill_number = models.CharField(max_length=40)
    cost = models.IntegerField()
    item_name = models.ForeignKey(VisitorHostelInventory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'visitor_hostel_inventorybill'


class VisitorHostelMealrecord(models.Model):
    meal_date = models.DateField()
    morning_tea = models.IntegerField()
    eve_tea = models.IntegerField()
    breakfast = models.IntegerField()
    lunch = models.IntegerField()
    dinner = models.IntegerField()
    persons = models.IntegerField()
    booking = models.ForeignKey(VisitorHostelBookingdetail, models.DO_NOTHING)
    visitor = models.ForeignKey('VisitorHostelVisitordetail', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'visitor_hostel_mealrecord'


class VisitorHostelRoomdetail(models.Model):
    room_number = models.CharField(unique=True, max_length=4)
    room_type = models.CharField(max_length=12)
    room_floor = models.CharField(max_length=12)
    room_status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'visitor_hostel_roomdetail'


class VisitorHostelRoomdetailVisitor(models.Model):
    roomdetail = models.ForeignKey(VisitorHostelRoomdetail, models.DO_NOTHING)
    visitordetail = models.ForeignKey('VisitorHostelVisitordetail', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'visitor_hostel_roomdetail_visitor'
        unique_together = (('roomdetail', 'visitordetail'),)


class VisitorHostelVisitordetail(models.Model):
    visitor_phone = models.CharField(max_length=15)
    visitor_name = models.CharField(max_length=40)
    visitor_email = models.CharField(max_length=40)
    visitor_organization = models.CharField(max_length=100)
    visitor_address = models.TextField()
    nationality = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'visitor_hostel_visitordetail'
