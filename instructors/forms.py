from django import forms
from OASys import settings
from django.forms import ModelForm
from students.models import Teaches, Assignment
from django.contrib.admin import widgets

class AddSubjectForm(ModelForm):
	class Meta:
		model = Teaches
		fields = ['cid',]

class GiveAssignmentForm(ModelForm):
	class Meta:
		model = Assignment
		fields = ['teacher_id', 'subject', 'asmt_name' ,'asmt_no', 'announcement_date','due_date','asmt_group','asmt_file']
		# exclude = ('teacher_id',)
	def __init__(self, *args, **kwargs):
		super(GiveAssignmentForm, self).__init__(*args, **kwargs)
		self.fields['announcement_date'].widget = widgets.AdminDateWidget()