# Generated by Django 4.2.5 on 2023-09-06 10:21

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('team_leader', 'Team Leader'), ('normal_user', 'Normal User')], max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile_pic', models.FileField(default='', upload_to='uploads/')),
                ('transaction_number', models.CharField(default='', max_length=50, null=True)),
                ('user_enabled', models.CharField(default='', max_length=1, null=True)),
                ('user_title', models.CharField(default='', max_length=20, null=True)),
                ('user_fname', models.CharField(default='', max_length=100, null=True)),
                ('user_mname', models.CharField(default='', max_length=100, null=True)),
                ('user_lname', models.CharField(default='', max_length=100, null=True)),
                ('user_full_name', models.CharField(default='', max_length=150, null=True)),
                ('user_address1', models.TextField(default='', null=True)),
                ('user_address2', models.TextField(default='', null=True)),
                ('user_address3', models.TextField(default='', null=True)),
                ('user_city_code', models.CharField(default='', max_length=100, null=True)),
                ('user_zip_code', models.CharField(default='', max_length=100, null=True)),
                ('user_state_code', models.CharField(default='', max_length=100, null=True)),
                ('user_country_code', models.CharField(default='', max_length=100, null=True)),
                ('user_birthday', models.DateField(default=None, null=True)),
                ('user_anniversary', models.DateField(default=None, null=True)),
                ('user_team_id', models.IntegerField(default=None, null=True)),
                ('user_seniority', models.CharField(default='', max_length=100, null=True)),
                ('user_profession', models.CharField(default='', max_length=100, null=True)),
                ('user_manager', models.CharField(default='', max_length=100, null=True)),
                ('user_extension', models.BigIntegerField(default=None, null=True)),
                ('created_DateField', models.DateField(default=None, null=True)),
                ('modified_DateField', models.DateField(default=None, null=True)),
                ('last_activity_DateField', models.DateField(default=None, null=True)),
                ('user_timezone_id', models.IntegerField(default=None, null=True)),
                ('user_timezone_timespan', models.IntegerField(default=None, null=True)),
                ('user_login_id', models.CharField(default='', max_length=100, null=True)),
                ('user_password', models.CharField(default='', max_length=100, null=True)),
                ('user_current_theme', models.CharField(default='', max_length=100, null=True)),
                ('user_phone', models.CharField(default='', max_length=100, null=True)),
                ('user_emailid', models.CharField(default='', max_length=100, null=True)),
                ('user_role', models.CharField(default='', max_length=100, null=True)),
                ('cust_reportingtocolumn', models.CharField(default='', max_length=100, null=True)),
                ('user_joingDateField', models.DateField(default=None, null=True)),
                ('user_LastworkingDateField', models.DateField(default=None, null=True)),
                ('user_contractstartDateField', models.DateField(default=None, null=True)),
                ('user_contractendDateField', models.DateField(default=None, null=True)),
                ('user_materialstatus', models.CharField(default='', max_length=100, null=True)),
                ('user_gender', models.CharField(default='', max_length=100, null=True)),
                ('user_emergencydetails', models.CharField(default='', max_length=100, null=True)),
                ('user_project', models.CharField(default='', max_length=100, null=True)),
                ('user_usersType', models.CharField(default='', max_length=100, null=True)),
                ('user_educationalStatus', models.CharField(default='', max_length=100, null=True)),
                ('user_bloodGrp', models.CharField(default='', max_length=100, null=True)),
                ('user_NRCNo', models.CharField(default='', max_length=100, null=True)),
                ('user_nationality', models.CharField(default='', max_length=100, null=True)),
                ('user_Region', models.CharField(default='', max_length=100, null=True)),
                ('user_basicSalary', models.CharField(default='', max_length=100, null=True)),
                ('user_PersonalPay', models.CharField(default='', max_length=100, null=True)),
                ('user_GrossSalary', models.CharField(default='', max_length=100, null=True)),
                ('user_expect', models.CharField(default='', max_length=100, null=True)),
                ('user_contractTerms', models.CharField(default='', max_length=100, null=True)),
                ('user_personalemailid', models.CharField(default='', max_length=100, null=True)),
                ('user_personalphone', models.CharField(default='', max_length=100, null=True)),
                ('user_bankname', models.CharField(default='', max_length=100, null=True)),
                ('user_bankAccountNo', models.CharField(default='', max_length=100, null=True)),
                ('user_EmployeeSSB', models.CharField(default='', max_length=100, null=True)),
                ('user_EmployerSSB', models.CharField(default='', max_length=100, null=True)),
                ('user_ssnnumber', models.CharField(default='', max_length=100, null=True)),
                ('user_taxslab', models.CharField(default='', max_length=100, null=True)),
                ('user_educationdetails', models.CharField(default='', max_length=100, null=True)),
                ('user_Parents', models.CharField(default='', max_length=100, null=True)),
                ('user_Children', models.CharField(default='', max_length=100, null=True)),
                ('user_code', models.CharField(default='', max_length=50, null=True)),
                ('user_dob', models.DateField(default=None, null=True)),
                ('user_InActiveStatus', models.CharField(default='', max_length=100, null=True)),
                ('user_TerminationRemarks', models.CharField(default='', max_length=1000, null=True)),
                ('user_mothername', models.CharField(default='', max_length=100, null=True)),
                ('user_wifename', models.CharField(default='', max_length=100, null=True)),
                ('user_wifejob', models.CharField(default='', max_length=100, null=True)),
                ('user_childname', models.CharField(default='', max_length=100, null=True)),
                ('user_parentPhone', models.CharField(default='', max_length=100, null=True)),
                ('user_ProbationstartDateField', models.DateField(default=None, null=True)),
                ('user_ProbationEndDateField', models.DateField(default=None, null=True)),
                ('user_project_lob', models.CharField(default='', max_length=100, null=True)),
                ('user_PAN', models.CharField(default='', max_length=100, null=True)),
                ('user_hra', models.CharField(default='', max_length=100, null=True)),
                ('user_eduqualification', models.CharField(default='', max_length=100, null=True)),
                ('user_Place', models.CharField(default='', max_length=100, null=True)),
                ('user_WFH_WFO', models.CharField(default='', max_length=100, null=True)),
                ('user_TrainingStart', models.DateField(default=None, null=True)),
                ('user_TrainingEnd', models.DateField(default=None, null=True)),
                ('user_ifsccode', models.CharField(default='', max_length=100, null=True)),
                ('user_Category', models.CharField(default='', max_length=100, null=True)),
                ('user_FloorStatus', models.CharField(default='', max_length=100, null=True)),
                ('user_Tenure', models.CharField(default='', max_length=100, null=True)),
                ('user_TenureBucket', models.CharField(default='', max_length=100, null=True)),
                ('user_BroadbandSystem', models.CharField(default='', max_length=100, null=True)),
                ('user_FT_PT', models.CharField(default='', max_length=100, null=True)),
                ('user_Age', models.CharField(default='', max_length=100, null=True)),
                ('user_AgeGroup', models.CharField(default='', max_length=100, null=True)),
                ('user_FatherHusbandName', models.CharField(default='', max_length=100, null=True)),
                ('user_GuardianName', models.CharField(default='', max_length=100, null=True)),
                ('user_GuardianNo', models.CharField(default='', max_length=100, null=True)),
                ('user_Referance1', models.CharField(default='', max_length=100, null=True)),
                ('user_Referance2', models.CharField(default='', max_length=100, null=True)),
                ('user_Referance1_No', models.CharField(default='', max_length=100, null=True)),
                ('user_Referance2_No', models.CharField(default='', max_length=100, null=True)),
                ('user_EmergencyuserNo', models.CharField(default='', max_length=100, null=True)),
                ('user_EduCategory', models.CharField(default='', max_length=100, null=True)),
                ('user_University', models.CharField(default='', max_length=100, null=True)),
                ('user_CompletionYear', models.CharField(default='', max_length=100, null=True)),
                ('user_Religion', models.CharField(default='', max_length=100, null=True)),
                ('user_BloodGroup', models.CharField(default='', max_length=100, null=True)),
                ('user_Fresher', models.CharField(default='', max_length=100, null=True)),
                ('user_PreviosuOrg', models.CharField(default='', max_length=100, null=True)),
                ('user_TotalExp', models.CharField(default='', max_length=100, null=True)),
                ('user_SourceType', models.CharField(default='', max_length=100, null=True)),
                ('user_SourceName', models.CharField(default='', max_length=100, null=True)),
                ('user_LanguageKnows', models.CharField(default='', max_length=100, null=True)),
                ('user_UANApplicability', models.CharField(default='', max_length=100, null=True)),
                ('user_ESIApplicability', models.CharField(default='', max_length=100, null=True)),
                ('user_UANNo', models.CharField(default='', max_length=100, null=True)),
                ('user_ESINo', models.CharField(default='', max_length=100, null=True)),
                ('user_Incentive', models.CharField(default='', max_length=100, null=True)),
                ('user_Bonus', models.CharField(default='', max_length=100, null=True)),
                ('user_SubTotal', models.CharField(default='', max_length=100, null=True)),
                ('user_PFCompany', models.CharField(default='', max_length=100, null=True)),
                ('user_ESICompany', models.CharField(default='', max_length=100, null=True)),
                ('user_PFEmployee', models.CharField(default='', max_length=100, null=True)),
                ('user_ESIEmployee', models.CharField(default='', max_length=100, null=True)),
                ('user_Gratuity', models.CharField(default='', max_length=100, null=True)),
                ('user_Variable', models.CharField(default='', max_length=100, null=True)),
                ('user_PT', models.CharField(default='', max_length=100, null=True)),
                ('user_CTC', models.CharField(default='', max_length=100, null=True)),
                ('user_Inhand', models.CharField(default='', max_length=100, null=True)),
                ('user_InactiveBucket', models.CharField(default='', max_length=100, null=True)),
                ('user_AttritionBucket', models.CharField(default='', max_length=100, null=True)),
                ('user_SeparationRemark', models.CharField(default='', max_length=100, null=True)),
                ('user_RehireStatus', models.CharField(default='', max_length=100, null=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='mordified_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('user_dept_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='department', to='users.department')),
                ('user_desig_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='designation', to='users.designation')),
            ],
        ),
    ]
