from django.db import models
# from django.contrib.auth.models import User
from django.db.models.signals import post_save
from OASys import settings
from cuser.models import CUser
# Create your models here.
class StudentProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	course = models.CharField(
							max_length=3,
							choices=(
								('MCS','Masters in Computer Science'),
								('MCA', 'Masters in Comuter Applications')
							)
						)
	rollno = models.IntegerField(default=0)
	semester = models.CharField(
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

	def __str__(self):
		return self.user.email

	def full_name(self):
		return self.user.first_name+' '+self.user.last_name


def create_profile(sender, **kwargs):
	if kwargs['created']:
		student_profile = StudentProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=CUser)

