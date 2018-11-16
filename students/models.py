from django.db import models
from cuser.models import CUser
from OASys import settings
import datetime
from accounts.models import StudentProfile

# Create your models here.
class Subjects(models.Model):
 	subj_id = models.CharField(default='',primary_key=True,max_length=50)
 	name = models.CharField(default='',max_length=200)
 	sub_sem = models.CharField(
						max_length=10,
						choices=(
							('Sem-I','Semester One'),
							('Sem-II','Semester Two'),
							('Sem-III','Semester Three'),
							('Sem-IV','Semester Four'),
							('Sem-V','Semester Five'),
							('Sem-VI','Semester Six'),
						)
					)
 	course = models.CharField(
							max_length=3,
							choices=(
								('MCS','Masters in Computer Science'),
								('MCA', 'Masters in Comuter Applications'),
							)
						)
 	def __str__(self):
 		return self.subj_id

class Teaches(models.Model):
	cid = models.OneToOneField(Subjects, on_delete=models.CASCADE)
	teacher_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	class Meta:
		unique_together = (('cid','teacher_id'),)

	def __str__(self):
		return self.cid.name

class Assignment(models.Model):
	teacher_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default='')
	subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
	asmt_no = models.PositiveSmallIntegerField()
	announcement_date = models.DateField()
	due_datetime = models.DateTimeField()
	asmt_group = models.PositiveSmallIntegerField()
	asmt_file = models.FileField(upload_to='asmt/')
	
	class Meta:
		unique_together = (('subject','asmt_no',),)

	def __str__(self):
		return self.subject.subj_id + "_" + str(self.asmt_no) +"_"+ str(self.announcement_date.year)


class Mark(models.Model):
	asmt = models.ForeignKey(Assignment, on_delete=models.CASCADE)
	student_id = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
	marks = models.PositiveSmallIntegerField()

class Submission(models.Model):
	student_id = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
	asmt = models.ForeignKey(Assignment, on_delete=models.CASCADE)
	submission_datetime = models.DateTimeField()
	asmt_solution_file = models.FileField(upload_to='asmt_submission/')